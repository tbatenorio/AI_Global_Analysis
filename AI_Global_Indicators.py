# 1 --- Importing necessary libraries
import pandas as pd
import streamlit as st
from PIL import Image
from st_pages import Page, show_pages

# 2 - Importing Images and Data Set
cs_img = Image.open("Assets/marca_cesar_school.png")
ai_img = Image.open("Assets/AI_Image.jpg")
dataset = pd.read_csv("Assets/AI_index_db.csv")

# Pages
st.set_page_config(page_title="Projeto Análise e Visualização de Dados")
show_pages(
    [
        Page("pages/Exploratory_Analysis.py", "Exploratory Analysis"),
        Page("pages/Map.py", "Indicators Around The World"),
    ]
)

dados_aluno = """
- Thiago Brito de Andrade Tenório
- Turma Dados 2023.1
- Disciplina Análise e Visualização de Dados
"""

introducao = """
- DataSet: [Link to Data Set](https://www.kaggle.com/datasets/katerynameleshenko/ai-index?select=AI_index_db.csv)

The Dataset "AI Global index" includes The Global AI Index itself and seven indicators affecting the Index on 62 countries, as well as general information about the countries 
(region, cluster, income group and political regime).

The Global AI Index is the first index to benchmark nations on their level of investment, innovation and implementation of artificial intelligence.

Talent, Infrastructure and Operating Environment are the factors of AI Implementation group of indicators, which represents the application of artificial intelligence 
by professionals in various sectors, such as businesses, governments, and communities.

- Talent indicator focuses on the availability of skilled practitioners for the provision of artificial intelligence solutions.
- Infrastructure indicator focuses on the reliability and scale of access infrastructure, from electricity and internet, to super computing capabilities.
- Operating Environment indicator focuses on the regulatory context, and public opinion surrounding artificial intelligence.

Research and Development are the factors of Innovation group of indicators, which reflects the progress made in technology and methodology, 
which signify the potential for artificial intelligence to evolve and improve.

- Research indicator focuses on the extent of specialist research and researchers; investigating the amount of publications and citations in credible academic journals.
- Development indicator focuses on the development of fundamental platforms and algorithms upon which innovative artificial intelligence projects rely.

Government Strategy and Commercial are the factors of Investment group of indicators, which reflects financial and procedural commitments to artificial intelligence.

- Government Strategy indicator focuses on the depth of commitment from national government to artificial intelligence; investigating spending commitments and national strategies.
- Commercial indicator focuses on the level of startup activity, investment and business initiatives based on artificial intelligence.

All these seven indicators were calculated by Tortoise Media via weighting and summarizing 143 other indicators.
"""


# 3 - Main Page
sidebar = st.sidebar
header = st.container()
box = st.container()

with sidebar:
    st.title("Projeto Final - CESAR School")
    st.markdown(dados_aluno)
    st.image(cs_img)

with header:
    st.image(ai_img)
    st.title("AI Global Indicators")
    

with box:
    st.title("About our DataSet")
    st.markdown(introducao)
    st.dataframe(dataset)
