import streamlit as st
st.header( "introduzindo os elementos do streamlit")
menu = option_menu (menu_title="Menu",
                    options=[Início", "Gráficos Estatísticos", "Gráficos Dinâmicos", "Widgest", "Formulário"],
                    icons=["house", "bar-chart", "bar-chart-line", "tooggles", "bar-chart"],
                    menu_icon="cast",
                    default_index=0,
                    orientation="horizontal"
                    
