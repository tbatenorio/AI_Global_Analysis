
import pandas as pd
import streamlit as st
import geopandas as gpd
import folium
from streamlit_folium import st_folium

st.set_page_config(page_title="AI World Map")
dataset = pd.read_csv("Assets/AI_index_db.csv")
dataset.rename(columns={'Country': 'country'}, inplace=True)
list_indicators = ['Total score','Talent','Infrastructure','Operating Environment','Research','Development','Government Strategy','Commercial']
shapefile = 'Assets/ne_110m_admin_0_countries.shp'
#Read shapefile using Geopandas
gdf = gpd.read_file(shapefile)[['ADMIN', 'ADM0_A3', 'geometry']]
#Rename columns.
gdf.columns = ['country', 'country_code', 'geometry']

bHeader = st.container()
bSidebar = st.sidebar
bBox1 = st.container()

insith_04 = """
**United States and China are the top 2 nations according to 'Total Score' in the 
AI ​​sector. These are followed by Canada and some European countries. The rest of 
the countries have little representation in the sector.**.
"""

with bHeader:
    # elemento de titulo
    st.title("AI World Map Indicators")  


with bSidebar:
    st.header('Indicator Options')
    # editar a sidebar
    option_indicator = st.selectbox('Select the Indicador:', list_indicators)


with bBox1:
    #Drop row corresponding to 'Antarctica'
    gdf = gdf.drop(gdf.index[159])

    merged = gdf.merge(dataset, left_on = 'country', right_on = 'country', how = 'left')
    merged.fillna(0, inplace = True)

   # Convert to GeoJSON
    merged.to_file('Assets/world_map.geojson', driver='GeoJSON')

    # Create a folium map object centered on the desired location
    map = folium.Map(location=[51.5074, -0.1278], zoom_start=2, min_zoom=1,max_zoom=3)

    # Create a choropleth map layer using the DataFrame
    choropleth = folium.Choropleth(
            geo_data= 'Assets/world_map.geojson',
            name='choropleth',
            data= merged,
            columns= ['country',f"{option_indicator}"],
            key_on='feature.properties.country',
            fill_color= 'YlGnBu',
            fill_opacity=0.7,
            line_opacity=0.2,
            legend_name='Indicator Score',
            highlight=True,
    ).add_to(map)

    choropleth.geojson.add_to(map)

    st_map = st_folium(map, width=700, height=700)

    #Insight
    st.markdown(insith_04)

    
    


