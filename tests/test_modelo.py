import sys
import os
import pytest
import pandas as pd

# -- Resolução dinâmica do caminho raiz do projeto --
# Este bloco garante que o Python sempre encontre a pasta "modules"


CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(CURRENT_DIR, os.pardir))
MODULES_DIR = os.path.join(PROJECT_ROOT, "modules")

for path in [PROJECT_ROOT, MODULES_DIR]:
    if path not in sys.path:
        sys.path.insert(0, path)

from modelo import criar_dataframe_posts


@pytest.fixture
def sample_data():
    """
    Simula dados brutos retornados da coleta
    """
    return [
        {
            "shortcode": "abc123",
            "post_date": "2025-11-04",
            "likes": 100,
            "comments": 10,
        },
        {
            "shortcode": "xyz789",
            "post_date": "2025-11-03",
            "likes": 230,
            "comments": 22,
        },
    ]


# --- TESTES ---


def test_criacao_dataframe(sample_data):
    """
    Verifica se o DataFrame é criado corretamente a partir de dados válidos.
    """
    df = criar_dataframe_posts(sample_data)

    assert isinstance(df, pd.DataFrame)
    assert not df.empty
    assert list(df.columns) == ["shortcode", "post_date", "likes", "comments"]


def test_tipos_de_dados(sample_data):
    """
    Verifica se os tipos de dados do DataFrame estão corretos.
    """
    df = criar_dataframe_posts(sample_data)

    assert df["shortcode"].dtype == object
    assert pd.api.types.is_numeric_dtype(df["likes"])
    assert pd.api.types.is_numeric_dtype(df["comments"])


def test_tratamento_dados_invalidos():
    """
    Garante que o modelo lida com dados inválidos sem quebrar.
    """

    data_invalida = [{"shortcode": None, "likes": "cem"}]
    df = criar_dataframe_posts(data_invalida)

    assert isinstance(df, pd.DataFrame)
    assert "shortcode" in df.columns
    assert len(df) == 1
