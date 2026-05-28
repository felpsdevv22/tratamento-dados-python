import re


def limpar_dados(df):
    antes = len(df)

    df = df.drop_duplicates()

    if 'email' in df.columns:
        df = df[df['email'].str.contains('@', na=False)]

    depois = len(df)

    print(f"Registros originais: {antes}") 
    print(f"Registros finais: {depois}")

    return df  
