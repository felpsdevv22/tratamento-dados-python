import re


def email_valido(email):

    padrao = r'^[\w\.-]+@[\w\.-]+\.(com|com\.br)$'

    return bool(re.match(padrao, str(email)))


def limpar_dados(df):

    antes = len(df)

    df = df.drop_duplicates()

    
    if 'email' in df.columns:

        df = df[df['email'].apply(email_valido)]

    depois = len(df)

    print(f"Registros originais: {antes}")
    print(f"Registros finais: {depois}")

    return df