import sqlite3

def salvar_no_banco(df):
    conn = sqlite3.connect("dados.db")
    df.to_sql("clientes", conn, if_exists="replace", index=False)
    conn.close()
    print("💾 Dados salvos no banco com sucesso")