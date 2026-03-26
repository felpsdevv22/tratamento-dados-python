import sqlite3
import pandas as pd

def carregar_dados(): 
    try: 
        return pd.read_csv("dados.csv")
    except Exception as e:
        print("Erro ao carregar arquivo: ", e)
        return None

def limpar_dados(df):
    antes = len(df)

    df = df.drop_duplicates()

    if 'email' in df.columns:
        df = df[df['email'].str.contains('@', na=False)]

    depois = len(df)

    print(f"Registros originais: {antes}") 
    print(f"Registros finais: {depois}")

    return df  

def salvar_no_banco(df):
    conn = sqlite3.connect("dados.db")
    df.to_sql("clientes", conn, if_exists="replace", index=False)
    conn.close()
    print("💾 Dados salvos no banco com sucesso")

def visualizar_dados():
    conn = sqlite3.connect("dados.db")
    df = pd.read_sql("SELECT * FROM clientes", conn)
    conn.close()
    print(df.head())

def menu():
    global df
    df = None

    while True:
        print("\n=== MENU ===")
        print("1 - Carregar e tratar dados")
        print("2 - Salvar no banco")
        print("3 - Visualizar dados")
        print("4 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            df = carregar_dados()
            if df is not None:
                df = limpar_dados(df)

        elif opcao == "2":
            if df is not None:
                salvar_no_banco(df)
            else:
                print("⚠️ Nenhum dado carregado")

        elif opcao == "3":
            visualizar_dados()

        elif opcao == "4":
            print("Saindo...")
            break

        else:
            print("Opção inválida")

menu()