"""
Módulo: dados_sinteticos.py
Função: Gerar dados artificais de posts para sinmuar interações reais
(likes, comentários, hashtags, etc.)
"""

import pandas as pd
import numpy as numpy
from datetime import datetime, timedelta
import random

def gerar_dados_sinteticos(n=50, salvar_csv=True):
    """
    Gera um conjunto de dados sintético para simular posts do Instagram.
    Esses dados serão usados para testar o modelo de otimização e engajamento.
    """

    # Criar uma lista de datas recentes:
    hoje = datetime.now()
    datas = [hoje - timedelta(days=i) for i in range(n)]

    # Geração de dados aleatório coerentes com posts reais
    dados = {
        "data_postagem": datas, # quantidade de curtidas
        "likes": np.random.randint(0, 400, n), # número de comentários
        "hashtags": [random.randint(0,10) for _ in range (n)] # número de hashtags
        "hora_postagem": [random.randit(0,23) for _ in range (n)] # hora do post
        "legenda_tamanho": np.random.randint(50,500,n), # tamanho da legenda
        "tipo_post": np.random.choice(["foto", "video", "carrosesel"], n) # tipo de post
        
    }

    # Converter para DataFrame
    df = pd.DataFrame(dados)

    # Criar coluna de engajamento simulado (likes + comentários com peso)
    df["engajamento"] = df["likes"] * 0.7 + df["comentarios"] * 1.3

    # Converter para DataFrame
    df = pd.DataFrame(dados)

    # Criar coluna de engajamaento simulado (likes + comentários com peso)
    df["engajamento"] = df["likes"] * 0.7 + df["comentarios"] * 1.3

    # Salvar localmente caso solicitado
    if salvar_scv:
        df.to_csv("dados_sinteticos.csv", index=False)
        print ("✅ Dataset sintético salvo em 'dados_sinteticos.csv'.")

    return df

    if __name__ == "__main__":
        # Teste rápido de geração
        df_teste = gerar_dados_sinteticos(30)
        print(df_teste.head())
