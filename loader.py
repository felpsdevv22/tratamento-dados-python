import pandas as pd

def carregar_dados(): 
    try: 
        return pd.read_csv("dados.csv")
    except Exception as e:
        print("Erro ao carregar arquivo: ", e)
        return None