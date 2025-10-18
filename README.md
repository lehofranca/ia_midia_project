# IA Mídia Project

Projeto de demonstração de análise de tendências, geração de resumos e otimização de engajamento de posts em redes sociais.

## Estrutura

- `modules/analise_tendencias.py` → captura e analisa tendências
- `modules/geracao_conteudo.py` → gera resumos automáticos
- `modules/otimizacao_engajamento.py` → previsão de engajamento com RandomForest
- `main.py` → script principal que orquestra todas as funções
- `data/posts_exemplo.csv` → exemplo de dados de posts

## Como usar

1. Ativar ambiente virtual:
```bash
python -m venv venv
source venv/Scripts/activate   # Windows
source venv/bin/activate       # Linux/macOS


1 - Instalar dependências:

pip install pandas scikit-learn matplotlib seaborn


2 - Rodar o script principal:

python main.py


3 - Rodar apenas a previsão de engajamento com gráfico:

python modules/otimizacao_engajamento.py

Observações

O gráfico de previsão é opcional e pode ser ativado passando plot=True na função prever_engajamento.

R² negativo indica que os dados são muito pequenos para o modelo RandomForest aprender padrões significativos.


---

### 3️⃣ Fluxo de publicação no GitHub

No terminal do seu projeto:

