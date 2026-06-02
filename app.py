import streamlit as st
import pandas as pd

from cleaner import limpar_dados
from io import BytesIO

st.title("Sistema de tratamento de dados")

arquivo = st.file_uploader(
    "Envie um arquivo Excel ou CSV"
)

if arquivo:

    st.success("Arquivo enviado com sucesso!")

    
    if arquivo.name.endswith(".csv"):
        df = pd.read_csv(arquivo)

    else:
        df = pd.read_excel(arquivo)

    
    st.write("dados originais:")
    st.dataframe(df)

    total_original = len(df)
 
    df_limpo = limpar_dados(df)

    
    st.write("dados tratados:")
    st.dataframe(df_limpo)

    total_limpo = len(df_limpo)
    duplicados_removidos = total_original - total_limpo
    
    st.write(f"Total original de linhas: {total_original}")
    st.write(f"Total após limpeza: {total_limpo}")
    st.write(f"Duplicados removidos: {duplicados_removidos}")
    output = BytesIO()

    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df_limpo.to_excel(writer, index=False)

    output.seek(0)

    dados_excel = output.read()

   
    st.download_button(
        label="Baixar arquivo tratado",
        data=dados_excel,
        file_name="dados_tratados.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )