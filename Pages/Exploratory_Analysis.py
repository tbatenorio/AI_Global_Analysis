# 1 --- Importe as bibliotecas necessárias
import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image
import numpy as np
import plotly.graph_objects as go


st.set_page_config(page_title="Exploratory Analysis")
dataset = pd.read_csv("Assets/AI_index_db.csv")
list_indicators = ['Total score','Talent','Infrastructure','Operating Environment','Research','Development','Government Strategy','Commercial']
list_regions = list(dataset.Region.unique())
bHeader = st.container()
bSidebar = st.sidebar
bBox1 = st.container()
bBox2 = st.container()


with bHeader:
    # elemento de titulo
    st.title("Exploratory Analysis")  


with bSidebar:
    # editar a sidebar
    option_indicator = st.selectbox('Select the Indicador:', list_indicators)
    st.title(" ")
    option_region = st.multiselect('Regions', list_regions, default= list_regions)
    st.title(" ")
    st.image(Image.open(f"Assets/{option_indicator}.jpg"), caption= f"{option_indicator} Indicator")
    
with bBox1:
    # Calcular a matriz de correlação entre os Indicadores
    indicators = dataset.copy()
    indicators.drop(['Total score','Country','Region','Cluster','Income group','Political regime'], axis=1, inplace=True)
    correlation_matrix = indicators.corr()
    correlation_matrix = correlation_matrix.apply(lambda x: round(x, 2))

    fig = px.imshow(correlation_matrix, text_auto=True, color_continuous_scale='Blues', title='Correlation about the Diferents Indicators')
    fig.update_layout(width=700, height=700)
    st.plotly_chart(fig, use_container_width=True) 
 

with bBox2: 
    #Graph 1
    st.header(f"TOP 10 Countries for: {option_indicator}")
    
    if(option_region != []):
        dff = dataset[dataset['Region'].isin(option_region)]
        dff = dff.sort_values(by= option_indicator, ascending=False).head(10)
    else:
        dff = dataset.sort_values(by= option_indicator, ascending=False).head(10)
    fig1 = px.bar(dff, x= dff[option_indicator], y= dff.Country, orientation='h')
    st.plotly_chart(fig1, use_container_width=True) 

    #Graph 2
    st.subheader('Political Regime Distribution')
    regimes = dff['Political regime'].value_counts(normalize = True)

    # Obtém o índice do valor máximo
    indice_maximo = np.argmax(regimes)

    # Cria a lista de valores pull
    pull_values = [0] * len(regimes.values)
    pull_values[indice_maximo] = 0.2

    fig2 = go.Figure(data=[go.Pie(labels= regimes.index, values= regimes.values, pull= pull_values)])
    st.plotly_chart(fig2, use_container_width=True)










