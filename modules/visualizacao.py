"""
Módulo: visualizacao.py
Responsável por gerar gráficos tecnológicos e modernos
a partir dos Dataframes tratados pelo módulo modelo.py

Autor: Leonardo França
Data: 11-11-2025
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Define um estilo dark tecnológico com grade suave e cores neon
plt.style.use("dark_background")

# Paleta personalizada com tons de neon / AI

PALETA_NEON = ["#00FFFF", "#FF00FF", "#00FF7F", "#FFD700", "#1E90FF"]


def plotar_graficos_posts(df: pd.DataFrame):
    """
    Gera e exibe gráficos com aparência tecnológica baseados no DataFrame de posts.

    Parâmetros:
    ----------
    df.pd.DataFrame
        DataFrame com as colunas ['shortcode', 'post_date', 'likes', 'comments']

    """

    if df.empty:
        print("[AVISO] DataFrame vazio - nenhum gráfico será gerado.")
        return

    # --- Configuração visual global ---
    sns.set(
        style="whitegrid",
        rc={"axes.facecolor": "H0D1117", "figure.facecolor": "H0D1117"},
    )
    sns.set_palette(PALETA_NEON)

    # -- 1. Gráfico de Barras (Likes e Comentários por Post) --

    plt.figure(figsize=(10, 6))
    df_plot = df.melt(
        id_vars=["shortcode"],
        value_vars=["likes", "comments"],
        var_name="Métrica",
        value_name="Quantidade",
    )

    sns.barplot(data=df_plot, x="shortcode", y="Quantidade", hue="Métrica", dodge=True)

    plt.title(
        "📊 Interações por Post - IA Vision Mode", fontsize=16, color="#00FFFF", pad=20
    )
    plt.xlabel("Código do Post", color="#FFFFFF")
    plt.ylabel("Quantidade", color="#FFFFFF")
    plt.legend(
        title="Métrica", loc="upper right", facecolor="0D1117", edgecolor="#00FFFF"
    )

    plt.grid(alpha=0.2, color="#00FFFF")
    plt.tight_layout()
    plt.show()

    # --- 2.Gráfico de Linha (Evolução de Likes) ---
    if "post_date" in df.columns:
        plt.figure(figsize=(10, 6))
        df_sorted = df.sort_values("post_date")
        sns.lineplot(
            data=df_sorted,
            x="post_date",
            y="likes",
            marker="o",
            linewidth=2.5,
            color="#00FFFF",
        )

        plt.title(
            "📈 Evolução dos Likes - Neural Pulse", fontsize=16, color="#00FFFF", pad=20
        )
        plt.xlabel("Data do Port", color="#FFFFFF")
        plt.ylabel("Likes", color="#FFFFFF")
        plt.grid(alpha=0.2, color="#FFFFFF")
        plt.tight_layout()
        plt.show()

    # --- 3. Gráfico de Dispersão (Correlação Likes x Comentários) ---
    plt.figure(figsize=(8, 6))
    sns.scatterplot(
        data=df,
        x="likes",
        y="comments",
        s=120,
        alpha=0.8,
        color="#FF00FF",
        edgecolor="#00FFFF",
    )

    plt.title(
        "⚙️ Correlação entre Likes e Comentários - AI Data Flow",
        fontsize=15,
        color="#00FFFF",
        pad=20,
    )
    plt.xlabel("Likes", color="FFFFFF")
    plt.ylabel("Comentários", color="FFFFFF")
    plt.grid(alpha=0.2, color="#00FFFFF")
    plt.tight_layout()
    plt.show()
