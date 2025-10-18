# main.py

from modules.analise_tendencias import analisar_tendencias
from modules.geracao_conteudo import gerar_resumo
from modules.otimizacao_engajamento import prever_engajamento
import panda as pd
import os

def main():
    # 1 - Análise de Tendências:
    print("=== Análise de Tendências ===")
    df_tweets = analisar_tendencias("tecnologia")
    print(df_tweets)
    
    # 2 - Geração de Resumo:
    print("\n=== Geração de Resumo ===")
    texto = "Empresa X anunciou hoje o lançamento de seu novo smartphone, com recursos inovadores..."
    resumo = gerar_resumo(texto)
    print(resumo)
    
    # 3 - Otimização de Engajamento:
    print("\n=== Otimização de Engajamento ===")
    
    caminho_csv = os.path.join("data", "posts_exemplo.csv")
   
    # Verifica se o arquivo CSV existe:   
    if os.path.exists(caminho_csv):
        try:
            df = pd.read_csv(caminho_csv, encoding= 'latin1')
            print ("✅ Dados carregados com sucesso!")
            
            
            # Conversão das colunas numéricas (tratando erros silenciosamente):
            colunas_numericas = ["hora_postagem", "dia_semana", "hashtag_tendencia", "curtidas"]
            for col in colunas_numericas:
                df[col] = pd.to_numeric(df[col], errors="coerce")
            
            # Remove linhas com valores nulos nessas colunas:        
            df = df.dropna(subset=colunas_numericas)
            print(f"📊 Linhas válidas para o modelo: {len(df)}")
            
            # Executa previsão de engajamento (sem gráfico para rodar mais rápido)        
            modelo, r2 = prever_engajamento(df, plot=True)
            print("🎯 Acurácia R²:", round(r2, 3))
                    
        except Exception as e:
            print("❌ Erro ao processar o arquivo: {e}")
    else:
        # Caso o CSV não exista, cria um dataset manual de exemplo:
        print("Arquivo 'data/posts_exemplo.csv' não encontrado. Usando dados de exemplo...")  
        dados = {
            "hora_postagem": [10,12,15,18,20],
            "dia_semana": [1,3,5,6,7],
            "hashtag_tendencia": [1,0,1,1,0],
            "curtidas": [150, 80, 200, 300, 90]
        }
        df = pd.DataFrame(dados)
    
        modelo, r2 = prever_engajamento (df, plot=True)
        print(f"🎯 Acurácia do Modelo (dados de exemplo): {round(r2, 3)}")
    
     
if __name__ == "__main__":
    main()