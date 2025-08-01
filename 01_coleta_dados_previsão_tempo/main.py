import requests
import pandas as pd
import os
from dotenv import load_dotenv

# Carrega chave da API
load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")
CITY = "Sorocaba"
UNITS = "metric"
URL = f"https://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units={UNITS}&lang=pt_br"

def coletar_dados():
    response = requests.get(URL)
    if response.status_code != 200:
        raise Exception(f"Erro na requisição: {response.status_code}")
    return response.json()

def processar_dados(json_data):
    previsoes = []
    for item in json_data["list"]:
        previsoes.append({
            "data": item["dt_txt"],
            "temperatura": item["main"]["temp"],
            "umidade": item["main"]["humidity"],
            "descricao": item["weather"][0]["description"]
        })
    return pd.DataFrame(previsoes)

def salvar_csv(df):
    df.to_csv("previsao_tempo.csv", index=False)
    print("Arquivo CSV salvo com sucesso.")

if __name__ == "__main__":
    print("🔄 Coletando dados da API...")
    dados = coletar_dados()
    print("✅ Dados recebidos. Processando...")
    df = processar_dados(dados)
    salvar_csv(df)
