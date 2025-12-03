import markdown2
import pdfkit
import os

# Caminho para o executável do wkhtmltopdf
config = pdfkit.configuration(
    wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"
)

# Seu conteúdo em Markdown:
md_text = """
# IA Mídia Project
Projeto de demonstração de análise de tendências, geração de resumos e otimização de engajamento de posts 
em redes sociais utilizando Inteligência Artificial.
"""

# Converter Markdown para HTML
html_text = markdown2.markdown(md_text)
html_text = f'<meta charset= "UTF-8"> {html_text}'

# Gerar PDF
pdfkit.from_string(html_text, "IA_Mídia_Project.pdf", configuration=config)
print("PDF gerado com sucesso!")
