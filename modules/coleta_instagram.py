"""
coleta_instagram.py
Versão revisada e robusta do coletor de posts públicos do Instagram usando Instaloader.

Melhorias incluídas:
- Logging consistente
- Tratamento de sessão mais robusto
- Validações de parâmetros
- Conversão e normalização de campos para DataFrame
- Função auxiliar para salvar em SQLite
- Função simulada para testes

Autor: Leonardo França
Data: 24/11/2025
"""

from __future__ import annotations

import os
import logging
from typing import Optional, List, Dict
import instaloader
import pandas as pd
from dotenv import load_dotenv

# Carrega .env
load_dotenv()

# Logger
logger = logging.getLogger(__name__)
if not logger.handlers:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s - %(message)s")

# Configurações via .env
LOGGING_INSTAGRAM = os.getenv("LOGGING_INSTAGRAM", "false").lower() == "true"
INSTAGRAM_USER = os.getenv("INSTAGRAM_USER")
INSTAGRAM_PASS = os.getenv("INSTAGRAM_PASS")

SESSION_FILE = os.getenv("SESSION_FILE", "data/session-instagram.session")
SQLITE_DB = os.getenv("SQLITE_DB", "data/instagram_posts.db")


# -----------------------------------------------------------------------------
# Helpers
# -----------------------------------------------------------------------------
def _ensure_data_dirs(*paths: str) -> None:
    """Cria diretórios necessários para arquivos."""
    for p in paths:
        d = os.path.dirname(p) or "."
        os.makedirs(d, exist_ok=True)


# -----------------------------------------------------------------------------
# Autenticação
# -----------------------------------------------------------------------------
def autenticar_instagram() -> instaloader.Instaloader:
    """Autentica no Instagram ou retorna modo anônimo."""
    _ensure_data_dirs(SESSION_FILE)

    L = instaloader.Instaloader(
        download_pictures=False,
        download_videos=False,
        download_comments=False,
        save_metadata=False,
        compress_json=False,
    )

    # Carregar sessão se existir
    if os.path.exists(SESSION_FILE):
        try:
            L.load_session_from_file(INSTAGRAM_USER, SESSION_FILE)
            logger.info("Sessão do Instagram carregada com sucesso.")
            return L
        except Exception as e:
            logger.warning(f"Falha ao carregar sessão: {e}")

    # Login desativado
    if not LOGGING_INSTAGRAM:
        logger.info("Modo anônimo selecionado.")
        return L

    # Verificar credenciais
    if not INSTAGRAM_USER or not INSTAGRAM_PASS:
        raise RuntimeError("LOGIN_INSTAGRAM ativo, mas credenciais ausentes no .env")

    # Tentativa de login
    try:
        L.login(INSTAGRAM_USER, INSTAGRAM_PASS)
        L.save_session_to_file(SESSION_FILE)
        logger.info("Login realizado com sucesso.")
        return L
    except Exception as exc:
        logger.error(f"Falha ao autenticar no Instagram: {exc}")
        raise


# -----------------------------------------------------------------------------
# Normalização de posts
# -----------------------------------------------------------------------------
def _normalize_post_to_row(post) -> Dict:
    """Converte objeto Post do Instaloader em dicionário limpo."""

    media_id = getattr(post, "mediaid", None) or getattr(post, "id", None)
    shortcode = getattr(post, "shortcode", None)
    caption = getattr(post, "caption", "") or ""
    dt = getattr(post, "date_utc", None)
    likes = getattr(post, "likes", None)
    comments = getattr(post, "comments", None)
    is_video = getattr(post, "is_video", False)

    return {
        "post_id": int(media_id) if media_id else None,
        "shortcode": shortcode,
        "url": f"https://www.instagram.com/p/{shortcode}/" if shortcode else None,
        "caption": caption,
        "datetime": pd.to_datetime(dt) if dt else pd.NaT,
        "likes": int(likes) if likes is not None else None,
        "comments": int(comments) if comments is not None else None,
        "is_video": bool(is_video),
    }


# -----------------------------------------------------------------------------
# Função principal de coleta
# -----------------------------------------------------------------------------
def coletar_posts_publicos(
    username: str,
    max_posts: Optional[int] = 50,
    save_csv: bool = True,
    csv_path: str = "data/instagram_posts.csv",
    download_media: bool = False,
    media_dir: str = "data/instagram_media",
    use_session: Optional[bool] = None,
) -> pd.DataFrame:

    if not username:
        raise ValueError("username é obrigatório.")

    if use_session is None:
        use_session = LOGGING_INSTAGRAM

    _ensure_data_dirs(csv_path, SESSION_FILE)

    if download_media:
        os.makedirs(media_dir, exist_ok=True)

    # Instância do Instaloader
    try:
        L = (
            autenticar_instagram()
            if use_session
            else instaloader.Instaloader(
                download_pictures=False,
                download_videos=False,
                download_comments=False,
                save_metadata=False,
                compress_json=False,
            )
        )
    except Exception as e:
        logger.error(f"Erro ao preparar Instaloader: {e}")
        raise

    # Obter perfil
    try:
        profile = instaloader.Profile.from_username(L.context, username)
    except Exception as e:
        logger.error(f"Erro ao obter perfil '{username}': {e}")
        raise

    rows = []
    count = 0

    for post in profile.get_posts():
        if max_posts and count >= max_posts:
            break

        try:
            row = _normalize_post_to_row(post)
            rows.append(row)
            count += 1

            if download_media:
                try:
                    L.download_post(post, target=media_dir)
                except Exception as e:
                    logger.warning(f"Falha ao baixar mídia {row.get('shortcode')}: {e}")

        except Exception as e:
            logger.warning(f"Erro processando post: {e}")

    df = pd.DataFrame(rows)

    if not df.empty:
        if not pd.api.types.is_datetime64_any_dtype(df.get("datetime")):
            df["datetime"] = pd.to_datetime(df["datetime"])

        df["date"] = df["datetime"].dt.date
        df["hour"] = df["datetime"].dt.hour

    # Salvar CSV
    if save_csv:
        try:
            os.makedirs(os.path.dirname(csv_path) or ".", exist_ok=True)
            df.to_csv(csv_path, index=False, encoding="utf-8")
            logger.info(f"✅ {len(df)} posts salvos em {csv_path}")
        except Exception as e:
            logger.warning(f"Erro ao salvar CSV ({csv_path}): {e}")

    logger.info(f"Coleta concluída. Total: {len(df)} posts.")
    return df


# -----------------------------------------------------------------------------
# Dados simulados
# -----------------------------------------------------------------------------
def coletar_simulado(n: int = 5) -> pd.DataFrame:
    """Gera DataFrame simulado para testes."""
    import datetime

    data = []
    for i in range(n):
        ts = datetime.datetime.utcnow() - pd.Timedelta(days=i)
        data.append(
            {
                "post_id": 1000 + i,
                "shortcode": f"POST_{i}",
                "url": f"https://www.instagram.com/p/POST_{i}/",
                "caption": f"Legenda teste {i}",
                "datetime": ts,
                "likes": (i + 1) * 10,
                "comments": (i + 1) * 2,
                "is_video": False,
            }
        )

    df = pd.DataFrame(data)
    df["date"] = df["datetime"].dt.date
    df["hour"] = df["datetime"].dt.hour
    return df


# -----------------------------------------------------------------------------
# Persistência em SQLite
# -----------------------------------------------------------------------------
def save_posts_to_sqlite(
    df: pd.DataFrame, db_path: str = SQLITE_DB, table: str = "posts"
) -> None:
    if df is None or df.empty:
        logger.info("Nenhum dado para salvar no banco.")
        return

    _ensure_data_dirs(db_path)

    try:
        import sqlalchemy as sa

        engine = sa.create_engine(f"sqlite:///{db_path}")
        df.to_sql(table, con=engine, if_exists="append", index=False)
        logger.info(f"✅ {len(df)} posts gravados em {db_path}:{table}")
    except Exception as e:
        logger.warning(f"Erro ao salvar no SQLite: {e}")


# -----------------------------------------------------------------------------
if __name__ == "__main__":
    df_test = coletar_simulado(5)
    print(df_test.head())
