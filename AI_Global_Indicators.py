# 1 --- Importing necessary libraries
import streamlit as st
from st_pages import Page, show_pages



# Pages
st.set_page_config(page_title="Projeto Análise e Visualização de Dados")
show_pages(
    [   
        Page("pages/Home.py", "Introduction"),
        Page("pages/Exploratory_Analysis.py", "Exploratory Analysis"),
        Page("pages/Map.py", "Indicators Around The World"),
    ]
)
