# modules/analise_tendencias.py

import tweepy
from textblob import TextBlob
import pandas as pd

def analisar_tendencias(termo, max_tweets=10, bearer_token="SUA_CHAVE_AQUI"):
    """
    Busca tweets com um termo específico e calcula o sentimento de cada tweet.
    Retorna um DataFrame com o texto e o sentimento.
    """
    client = tweepy.Client(bearer_token=bearer_token)
    tweets = client.search_recent_tweets(query=termo, max_results=max_tweets)
    
    data = []
    for tweet in tweets.data:
        sentimento = TextBlop(tweet.text).sentiment.polarity
        data.append({"texto": tweet.text, "sentimento": sentimento})
        
    df = pd.DataFrame(data)
    return df


# Example usage:

if __name__ == "__main__":
    df_tweets = analisar_tendencias("tecnologia")
    print (df_tweets)    
    
    