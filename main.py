# main.py
# ------------------------------------

# Arquivo principal do projeto ia_midia_project
# Responsável por orquestar os módulos internos,
# carregar dados, treinar modelo e exibir resultados.

import os # Manipula caminhos de arquivos
import pandas as pd # Leitura e manipulação de dados
from modules.otimizacao_engajamento import prever_engajamento # Função de Modelo
from utils.logger import configurar_logger # Logger centralizado

# Instancia o logger global (gera logs no terminal e no arquivo/logs/execucao.log)
logger = configurar_logger("execucao.log", nivel="INFO")


# Caminho padrão para o CSV dentro da pasta /data
CAMINHO_CSV = os.path.join("data", "posts_exemplo.csv")


def carregar_dados(caminho: str) -> pd.DataFrame:
    """
    Lê um arquivo CSV e retorna um DataFrame pandas.
    Tenta automaticamente UTF-8 e Latin-1.
    """
    if not os.path.exists(caminho):
        raise FileNotFoundError(f"Arquivo não encontrado: {caminho}")
    
    try:
        df = pd.read_csv(caminho, encoding="utf-8")
    except UnicodeDecodeError:
        df = pd.read_csv(caminho, encoding="latin-1")
        
    logger.info(f" Dados carregados com sucesso! ({len(df)} registros)")
    return df
    
def executar_otimizacao(df: pd.DataFrame):
        """
        Chama o modelo de previsão e exibe métricas.
        """
        logger.info("🚀 Iniciando processo de otimização e engajamento...\n")
        
        modelo, r2 = prever_engajamento(df, plot=True)
        logger.info(f"Acurácia R² do modelo: {r2:.3f}")
        
        if r2 < 0:
            logger.warning("Resultado negativo indica que o modelo ainda precisa de ajustes.")
        else:
            logger.success(" Modelo performou bem nos dados de teste!")
            
def main():
        """
        Função principal que orquestra o fluxo do projeto.
        """
        
        try: 
            # Carrega os dados do CSV:
            df = carregar_dados(CAMINHO_CSV)
            # Executa a otimização e previsão do engajamento:
            executar_otimizacao(df)
            
            
        except FileNotFoundError as e:
            logger.error(f"Erro: {e}") 
        except Exception as e:
            logger.exception(f"Erro inesperado: {e}")
            
if __name__ == "__main__":
    main()                  