import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
#import numpy as np
#import matplotlib.pyplot

st.header( "introduzindo os elementos do streamlit")
menu = option_menu (menu_title="Menu",
                    options=["Início", "Gráficos Estatísticos", "Gráficos Dinâmicos", "Widgest", "Formulário"],
                    icons=["house-fill", "bar-chart", "bar-chart-line", "toggles", "bar-chart"],
                    menu_icon="cast",
                    default_index=0,
                    orientation="horizontal")

with st.sidebar: 
  st.success("**upload de dados**")
  dados = st.file_uploader(
    "Carregue...",
    type=["xlsx", "xls"]
  )
if dados:
  def carregar_dados (dados):
    try:
      df = pd.read_excel(dados)
      return df
    except FileNotFoundError:
      return pd.DataFrame()

      df = carregar_dados (dados)
      st.table(df)
else:
  st.info("Carregue um ficheiro Excel para começar")

if menu == "Início":
  with st.expander("**Sobre o Instituto Nacional de Estatística**"):
    st.write("Acesse o site www.ine.cv")
    st.image("INE.png")


if menu == "Widgets":
  bt = st.button("Dê um clique!")

  if bt:
    st.info("Clicaste num botão acima!")

  sd = st.slider("Mova o ponto so slider!", min_value=25, \
              max_value=35, value=30, step=1
              )

  texto = f"Eu tenho {sd} anos!"
  st.success(texto)
  
