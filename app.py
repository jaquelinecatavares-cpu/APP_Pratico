import streamlit as st
from streamlit_option_menu import option_menu
#import numpy as np
#import pandas as pd
#import matplotlib.pyplot

st.header( "introduzindo os elementos do streamlit")
menu = option_menu (menu_title="Menu",
                    options=["Início", "Gráficos Estatísticos", "Gráficos Dinâmicos", "Widgest", "Formulário"],
                    icons=["house", "bar-chart", "bar-chart-line", "tooggles", "bar-chart"],
                    menu_icon="cast",
                    default_index=0,
                    orientation="horizontal")
                    
