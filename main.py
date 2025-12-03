# main.py
# ------------------------------------
# Arquivo principal do projeto ia_midia_project
# Orquestra os módulos, carrega dados, transforma, gera gráficos
# e executa previsão de engajamento.

import os
import pandas as pd
from dotenv import load_dotenv

# --- Módulos Internos ---
from utils.logger import configurar_logger
from modules.coleta_instagram import coletar_posts_publicos
from modules.dados_sinteticos import gerar_dados_sinteticos
from modules.modelo import criar_dataframe_posts
from modules.graficos import grafico_pizza, grafico_barras, grafico_piramide

load_dotenv()

# Caminho do CSV
CAMINHO_CSV = os.path.join("data", "posts_exemplo.csv")

# Cria pasta de saída para gráficos:
OUTPUT_DIR = "output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Logger Central:
logger = configurar_logger("execucao.log", nivel="INFO")


def coletar_dados_instagram():
    perfil = os.getenv("PERFIL_EXEMPLO")
    print(f"📸 Coletando posts do perfil: {perfil}")

    try:
        df_instagram = coletar_posts_publicos(
            username=perfil,
            max_posts=20,
            save_csv=True,
            csv_path=CAMINHO_CSV,
            download_media=False,
        )
        logger.info(f"Posts coletados: {len(df_instagram)}")
        return df_instagram

    except Exception as e:
        logger.warning(f"Falha ao coletar dados do Instagram: {e}")
        return None


def carregar_dados(caminho: str) -> pd.DataFrame:
    if not os.path.exists(caminho):
        raise FileNotFoundError(f"Arquivo não encontrado: {caminho}")

    try:
        df = pd.read_csv(caminho, encoding="utf-8")

    except UnicodeDecodeError:
        df = pd.read_csv(caminho, encoding="latin-1")

    logger.info(f"📊 Dados carregados: {len(df)} registros")
    return df


def gerar_graficos(df: pd.DataFrame):
    """
    Gera gráficos tecnológicos a partir dos dados.
    """

    logger.info("⚡Gerando gráficos tecnológicos...")

    # GRÁFICO DE PIZZA: distribuição de likes
    grafico_pizza(
        df, coluna="likes", output_path=os.path.join(OUTPUT_DIR, "pizza_likes.png")
    )

    # GRÁFICO DE BARRAS: likes por shortcode
    grafico_barras(
        df,
        x="shortcode",
        y="likes",
        output_path=os.path.join(OUTPUT_DIR, "barras_likes.png"),
    )

    # GRÁFICO PIRÂMIDE INVERTIDA: likes vs comments
    grafico_piramide(
        df,
        col_esq="likes",
        col_dir="comments",
        output_path=os.path.join(OUTPUT_DIR, "piramide_engajamento.png"),
    )

    logger.info("📁 Gráficos salvos na pasta / output")


def main():
    try:
        coletar_dados_instagram()

        df_raw = carregar_dados(CAMINHO_CSV)

        # ---  🔵 NOVO: normalização de dados pelo modelo.py ---
        df = criar_dataframe_posts(df_raw)

        logger.info("🔧 DataFrame tratado e pronto para visualização.")

        # ---  🔵 NOVO: gerar dashboards tecnológicos ---
        gerar_graficos(df)

        logger.info("🚀 Pipeline concluído com sucesso!")
    except Exception as e:
        logger.exception(f"Erro inesperado: {e}")


if __name__ == "__main__":
    main()
