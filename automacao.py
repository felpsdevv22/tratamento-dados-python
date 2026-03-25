import pandas as pd
df = pd.read_csv("dados.csv")

antes = len(df)
df =df.drop_duplicates()
depois = len(df)

df = df[df['email'].str.contains('@')]
df.to_excel("dados_tratados.xlsx", index=False)

print("✅ Processo concluido")
print(f"Registros originais: {antes}")
print(f"Registros finais: {depois}")