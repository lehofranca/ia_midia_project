# modules/geracao_conteudo.py

from transformers import pipeline

def gerar_resumo(texto, max_lenght=60, min_lenght=20):
    """
    Gera resumo automático de um texto usando modelo BART da Hugging Face.
    """
    
    resumidor = pipeline("summarization", model = "facebook/bart-large-cnn")
    resumo = resumidor(texto, max_lenght=max_lenght, min_length=min_lenght, do_sample=False)
    return resumo[0]['summary_text']

# Example Usage:

if __name__ == "__main__":
    texto = """
    A empresa X anunciou hoke o lançamento de seu novo smartphone, 
    que promete revolucionar o mercado com sua tecnologia avançada e design inovador.
    
    O dispositivo conta com uma câmera de alta resolução, bateria de longa duração e 
    um processador ultrarrápido, ideal para jogos e multitarefas.
    
    Além disso, o smartphone é compatível com redes 5G, garantindo uma conexão mais rápida e estável.
    A empresa espera que o novo lançamento atraia um grande número de consumidores e 
    fortaleça sua posição no mercado global de tecnologia.
    """
        
    print("Resumo:", gerar_resumo(texto))     
    