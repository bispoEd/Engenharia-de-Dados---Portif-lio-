import pandas as pd
import os

# Carregar dados
df = pd.read_csv("dados/vendas_brutas.csv")

# Limpeza
df = df.dropna(subset=["Produto"])                 # Remove produtos vazios
df["Quantidade"] = df["Quantidade"].fillna(1)      # Preenche quantidades vazias
df["Total"] = df["Quantidade"] * df["Preço Unitário"]  # Nova coluna

# Conversão de data
df["Data"] = pd.to_datetime(df["Data"])

# Salvar dados tratados
os.makedirs("saida", exist_ok=True)
df.to_csv("saida/vendas_tratadas.csv", index=False)
print("✅ ETL finalizado. Arquivo salvo em saida/vendas_tratadas.csv")

