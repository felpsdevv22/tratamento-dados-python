import pandas as pd

def carregar_dados(): 
    try: 
        return pd.read_csv("dados.csv")
    except Exception as e:
       print("Erro ao carregar arquivo: ", e)
       return None

df = carregar_dados()

if df is not None:
    print("Dados carregados com sucesso")    

antes = len(df)

df =df.drop_duplicates()

df = df[df['email'].str.contains('@')]

depois = len(df)

df.to_excel("dados_tratados.xlsx", index=False)

print("✅ Processo concluido")
print(f"Registros originais: {antes}")
print(f"Registros finais: {depois}")

