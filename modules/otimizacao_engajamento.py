import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
import seaborn as sns
import os


def prever_engajamento(df, plot=False):
    """
    Recebe um Dataframe com colunas:
    hora_postagem, dia_semana, hastag_tendencia, curtidas 
    e retorna um modelo treinado e a acurácia (R²) sobre os dados de teste.
    
    Argumentos:
        df: pd.DataFrame - dados de entrada
        plot: bool - se True, exibe gráfico de previsão
    Retorna:
        modelo: RandomForestRegressor treinado
        r2 float - R² do modelo nos dados de teste
    """
    
    # Verifica se todas as colunas necessárias estão presentes:
    colunas_necessarias = ["hora_postagem", "dia_semana", "hashtag_tendencia", "curtidas"]
    for col in colunas_necessarias:
        if col not in df.columns:
            raise ValueError(f"Coluna '{col}' não encontrada no DataFrame")
    
    #Features e Target:
    
    X = df[["hora_postagem", "dia_semana", "hashtag_tendencia"]]
    y = df["curtidas"]
    
    # Separação Treino/ Teste:
    X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.3, random_state=42)
    
    # Treinamento do Modelo:
    modelo = RandomForestRegressor(random_state=42)
    modelo.fit(X_train, y_train)
    
    # Previão:
    y_pred = modelo.predict(X_test)
    
    # Cálculo do R² :
    r2 = r2_score(y_test, y_pred)
    
    # Plotagem Opcional ( exibição do gráfico se = True)/ Gráfico moderno para visualização:
    if plot:
        sns.set(style="whitegrid", context="talk", palette="rocket")
        plt.figure(figsize=(8,6))
        plt.scatter(y_test, y_pred, s=100, color="#FF6F61", alpha=0.8, edgecolors="black",
        label="Previsões")
        plt.plot([min(y_test), max(y_test)],[min(y_test), max(y_test)], 'lime', linestyle='--', linewidth=2, label="Linha Ideal")
        plt.title(f"Previsão de Engajamento - R² = {r2:.2f}", fontsize=16, weight='bold')
        plt.xlabel("Curtidas Reais", fontsize=12)
        plt.ylabel("Curtidas Previstas", fontsize=12)
        plt.legend()
        plt.grid(True, linestyle='--', alpha=0.6)
        plt.tight_layout()
        plt.show()
    
    return modelo, r2


if __name__ == "__main__":
    # Caminho para o arquivo dados:
    caminho_csv = os.path.join("data", "posts_exemplo.csv")
    
    if os.path.exists(caminho_csv):
        try:
            # Tentativa com UTF-8. Se falhar, tenta Latin-1
            try:
                df = pd.read_csv(caminho_csv, encoding='utf-8')
            except UnicodeDecodeError:
                df = pd.read_csv(caminho_csv, encoding='latin1')
            
            
            print("Dados carregados com sucesso!")
            modelo, r2 = prever_engajamento(df)
            print("Acurácia R²:", round(r2, 3))
            
        except Exception as e:
             print(f"Erro ao processar o arquivo: {e}")
             
    else:
        print("Arquivo 'data/posts_exemplo.csv' não encontrado. Verifique o caminho")