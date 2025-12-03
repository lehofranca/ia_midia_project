import sys
from pathlib import Path

# Caminho absoluto da psta onde o pytest está sendo executado:
ROOT_DIR = Path(__file__).resolve().parent

# Garante que a pasta raiz do projeto está no sys.path:

if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

# Também garante o acesso direto à pasta 'modules'
MODULES_PATH = ROOT_DIR / "modules"
if MODULES_PATH.exists() and str(MODULES_PATH) not in sys.path:
    sys.path.insert(0, str(MODULES_PATH))

print(f"[DEBUG] sys.path configurado: {ROOT_DIR}")
