"""
Módulo: modelo.py
Funções responsáveis por transformar os dados brutos coletados (por exemplo, do Instagram)
em DataFrames prontos para análise e visualização.

Autor: Leonardo França.
Data: 2025-11-09
"""

import pandas as pd


def criar_dataframe_posts(dados_brutos):
    """
    Cria um DataFrame do pandas a partir de uma lista de dicionários com informações de posts.

    Parâmetros:
    -----------
    dados_brutos: list[dict]
        Lista contendo dicionários com informações dos posts.
        {
            "shortcode": str,
            "post_date": str (YYYY-MM-DD),
            "likes": int,
            "comments": int
        }

    Retorno:
    --------
    pd.DataFrame
        DataFrame contendo as colunas:
        ['shortcode', 'post_date', 'likes', 'comments']

    Tratamentos:
    ------------
    - Remove linhas totalmente vazias.
    - Substitui valores inválidos ou ausentes por None.
    - Converte colunas numéricas corretamente.
    """

    # --- Validação inicial ---
    if not dados_brutos or not isinstance(dados_brutos, list):
        print("[AVISO] Nenhum dado válido recebido.")
        return pd.DataFrame(columns=["shortcode", "post_date", "likes", "comments"])

    # --- Criação inicial do DataFrame ---
    df = pd.DataFrame(dados_brutos)

    # --- Normaliza as colunas esperadas ---
    colunas_esperadas = ["shortcode", "post_date", "likes", "comments"]
    for col in colunas_esperadas:
        if col not in df.columns:
            df[col] = None  # Cria colunas faltantes

    # --- Converte tipos de dados ---
    df["likes"] = pd.to_numeric(df["likes"], errors="coerce")
    df["comments"] = pd.to_numeric(df["comments"], errors="coerce")

    # --- Remove linhas totalmente vazias ---
    df = df.dropna(how="all")

    # --- Garante ordem correta das colunas ---
    df = df[colunas_esperadas]

    return df


# ---------------------------------------------------
# Execução isolada (para testes manuais no terminal)
# ---------------------------------------------------
if __name__ == "__main__":
    dados_exemplo = [
        {
            "shortcode": "abc123",
            "post_date": "2025-11-10",
            "likes": 10524,
            "comments": 100,
        },
        {
            "shortcode": "leho934",
            "post_date": "2025-11-03",
            "likes": 230,
            "comments": 52,
        },
        {"shortcode": None, "likes": "cem", "comments": "dez"},
    ]

    df = criar_dataframe_posts(dados_exemplo)
    print("\n[DEBUG] DataFrame gerado:")
    print(df)
