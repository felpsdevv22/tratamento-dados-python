import sqlite3
import pandas as pd
from loader import carregar_dados
from cleaner import limpar_dados
from db_manager import salvar_no_banco
from viewer import visualizar_dados
 
def menu():

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