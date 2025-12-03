import pytest
import pandas as pd
from modules.coleta_instagram import coletar_posts_publicos
import sys
import os

sys.path.insert(0,os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def test_coleta_publica_pequena():
    """
    Testa a coleta de poucos posts públicos e valida estrutura do DataFrame retornado.
    """
    df = coletar_posts_publicos("instagram", max_posts=5, save_csv=False)

    # Testa se dataframe foi retornardo.

    assert df is not None
    assert isinstance(df, pd.DataFrame)

    # Testa tamanho do DataFrame:
    assert len(df) <=5

    #Testa se colunas essenciais existem:

    for col in ["shortcode", "post_date", "likes"]:
        assert col in df.columns


    # Testa tipos de dados:
    assert pd.api.types.is_object_dtype(df["shortcode"])
    assert pd.api.types.is_integer_dtype(df["likes"])


    # Testa se não há duplicatas
    assert df["shortcode"].is_unique, "Existem shortcodes duplicados no DataFrame!"

