# 📲 IA Mídia Project
Automação inteligente para coleta, análise e otimização de conteúdo digital.

Este projeto combina **coleta automatizada de dados**, **análise de tendências**,
**modelos de previsão de engajamento** e **geração assistida de insights** para redes sociais.

---

## 📂 Estrutura do Projeto

ia_midia_project/
│
├── modules/
│ ├── coleta_instagram.py # Coleta posts públicos via Instaloader
│ ├── analise_tendencias.py # Análise estatística e visualização
│ ├── geracao_conteudo.py # Geração de resumos e insights
│ ├── otimizacao_engajamento.py # Modelo RandomForest para prever engajamento
│
├── utils/
│ ├── logger.py # Configuração profissional de logs (Loguru)
│
├── data/
│ ├── posts_exemplo.csv # Exemplo de dataset (ignorado no Git)
│
├── logs/ # Logs automáticos (ignorado no Git)
│
├── main.py # Orquestra o pipeline completo
├── requirements.txt # Dependências do projeto
└── README.md # Documento atual


---

## 🚀 Funcionalidades Principais

### ✅ 1. **Coleta automática de posts públicos do Instagram**
- Usa **Instaloader**
- Extrai:
  - Data e hora
  - Legenda
  - Hashtags
  - Likes
  - Comentários
  - Tipo de mídia
  - URL e shortcode
- Salva tudo em **CSV**

---

### ✅ 2. **Análise de tendências**
Inclui:
- Frequência de posts por período
- Identificação de hashtags comuns
- Correlações
- Visualizações gráficas opcionais

---

### ✅ 3. **Geração automática de conteúdo**
- Resumos estratégicos
- Insights de performance
- Sugestões de melhorias para engajamento

---

### ✅ 4. **Previsão de engajamento**
- Modelo **RandomForestRegressor**
- Entrada: likes, comentários, hashtags, tamanho da legenda, etc.
- Saída: probabilidade de engajamento
- Gráfico opcional via `matplotlib`

---

# 🛠️ Instalação

### 1️⃣ Criar ambiente virtual
```bash
python -m venv venv

2️⃣ Ativar ambiente

Windows

venv\Scripts\activate


Linux/macOS

source venv/bin/activate

3️⃣ Instalar dependências
pip install -r requirements.txt

▶️ Execução
🔹 Rodar o pipeline completo
python main.py

🔹 Rodar apenas o coletor do Instagram
python modules/coleta_instagram.py

🔹 Rodar apenas previsão de engajamento
python modules/otimizacao_engajamento.py

⚠️ Observações Importantes

O projeto ignora automaticamente:

venv/

logs/

.env

.vscode/

arquivos .csv e .xlsx

O dataset de exemplo não acompanha o repositório

O modelo RandomForest pode gerar R² negativo com datasets muito pequenos (comportamento normal)

🧭 Roadmap do Projeto

 Coletor Instagram funcional

 Estrutura modular organizada

 Logger centralizado

 Previsão de engajamento

 Criação de dashboard em Streamlit

 Exportação de relatórios automáticos

 Geração de legendas com IA

 Comparação entre perfis concorrentes

👨‍💻 Autor

Leonardo Mendes de França
Desenvolvedor • QA Automatizado • Criador de soluções de IA aplicada.
