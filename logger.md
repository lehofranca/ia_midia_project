LOGGER DO PROJETO: ia_midia_project

1️⃣ Propósito:

**O logger do projeto utiliza a biblioteca loguru para registrar informações importantes, warnings e erros durante a execução do sistema.**

Ele substitui os print() comuns, fornecendo:

- Formatação de logs colorida no console

- Armazenamento de logs em arquivo (logs/app.log)

- Diferenciação entre níveis: INFO, WARNING, ERROR



2️⃣ Instalação da biblioteca:

Certifique-se de que o loguru está instalado no seu ambiente:
pip install loguru

3️⃣ Como usar:

No código, basta importar e inicializar o logger:

from modules.utils.logger import get_logger

logger = get_logger()


**Substituindo print() por logger:**
logger.info("Mensagem informativa")
logger.warning("Aviso importante")
logger.error("Erro crítico")


**Exemplo de uso no main.py:**
df = carregar_dados(CAMINHO_CSV)
logger.info(f"Dados carregados com sucesso! ({len(df)} registros)")


4️⃣ Configuração do Logger:

O arquivo modules/utils/logger.py define:

Nível de log padrão: INFO

Arquivo de log: logs/app.log

Formato da mensagem: timestamp, nível, arquivo e mensagem

**Exemplo de saída no console:**
2025-10-20 10:15:32 | INFO     | main.py:25 - Dados carregados com sucesso! (5 registros)
2025-10-20 10:15:35 | WARNING  | main.py:33 - R² negativo indica que o modelo precisa de ajustes
2025-10-20 10:15:36 | ERROR    | main.py:40 - Erro inesperado: arquivo não encontrado

5️⃣ Benefícios:

Consolida todas as mensagens importantes do sistema

Facilita debugging e monitoramento

Mantém histórico de execução, útil para auditoria ou análise posterior

6️⃣ **Estrutura de Pastas:**

ia_midia_project/
├─ modules/
│  ├─ utils/
│  │  └─ logger.py
├─ logs/
│  └─ app.log
├─ main.py
├─ data/
│  └─ posts_exemplo.csv
└─ README.md
