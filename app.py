import streamlit as st
from streamlit_option_menu import option_menu
#import numpy as np
#import pandas as pd
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
      
