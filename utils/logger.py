# modules/utils/logger.py

# -----------------------------------------------------
# Gerenciamento centralizado de logs para o projeto.
# Usa Ioguru para criar logs coloridos e rotativos.
# -----------------------------------------------------

from loguru import logger
import os
from datetime import datetime

def configurar_logger(nome_arquivo: str = "app.log", nivel: str = "INFO"):
    """
    Configura o logger para exibir e amarzenar logs com formato padronizado.
    
    
    Args:
        nome_arquivo (str): Nome do arquivo de log a ser criado em /logs.
        nível (str): Nível mínimo de log. Ex: "DEBUG", "INFO", "WARNING", "ERROR".
    
    """
    # Garante que a pasta de logs exista:
    os.makedirs("logs", exist_ok=True)
    
    # Caminho completo do log:
    caminho_log = os.path.join("logs", nome_arquivo)
    
    # Remove configurações padrão do Ioguru (evita logs duplicados):
    logger.remove()
    
    # Formato para o terminal (colorido e compacto):
    formato_terminal = (
        "<green>{time: YYYY-MM-DD HH:mm:ss}</green> | "
        "<level> {level: <8} </level> | "
        "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - "
        "<level>{message}</level>"
    )
    
    # Formato para o arquivo (completo e limpo):
    formato_arquivo = (
        "{time: YYYY-MM-DD HH:mm:ss} | {level: <8} | {name}: {function}:{line} - {message}"
    )
    
    # Configuração do log no terminal
    logger.add(
        sink=lambda msg: print(msg, end=""),
        level=nivel,
        format=formato_terminal,
        colorize=True,
        
        )
    
    # Configuração do log em arquivo
    logger.add(
        caminho_log,
        rotation = "5 MB",
        retention = "10 days",
        encoding="utf-8",
        format=formato_arquivo,
        enqueue=True
        
    )
    
    logger.info(f"Logger configurado em nível {nivel}. Arquivo: {caminho_log}")
    return logger
    
    