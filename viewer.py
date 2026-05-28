import pandas as pd
import sqlite3

def visualizar_dados():
    conn = sqlite3.connect("dados.db")
    df = pd.read_sql("SELECT * FROM clientes", conn)
    conn.close()
    print(df.head())