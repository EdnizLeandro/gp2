import streamlit as st
import pandas as pd
from utils.build import build_header, breakrows, top_categories
import plotly.express as px
from utils.charts import boxplot, scatter, treemap

build_header(
    title='Análise de preço',
    hdr='# Análise de preço dos Veículos',
    p='''
        <p> Nessa análise, buscamos entender a influência do ano do veículo e quais regiões têm a maior concentração de veículos e marcas. </p>
    '''
)

# Corrigir barra invertida para barra normal no caminho do arquivo
data = pd.read_parquet('data/price_cars10k.parquet')

data_preco = data.groupby(['preco', 'marca', 'ano', 'modelo', 'estado', 'cidade']).size().reset_index(name='Total')
data_preco.sort_values('Total', ascending=True, inplace=True)
data_cars = data[['ano', 'preco', 'marca', 'modelo']]

with st.expander("VISUALIZAR OS DADOS DESTA SEÇÃO"):
    _, c2, _ = st.columns((1, 7, 1))
    c2.write(data_cars)

breakrows()

data_filtered = top_categories(
    data=data,
    top=10,
    label='modelo'
)
breakrows()

boxplot(
    data=data_filtered,
    title='BoxPlot do Modelo por Preço',
    x='modelo',
    y='preco',
    p='''<p style='text-align:justify;'>  </p>'''
)

boxplot(
    data_preco,
    x='preco',
    title='BOXPLOT DOS PREÇOS',
    p='''Nesse boxplot, vemos a distribuição dos preços dos veículos. 
    Temos uma concentração maior de veículos entre 13 mil e 26 mil reais.'''
)

breakrows()

scatter(
    data=data_filtered,
    x='preco',
    title='Scatter do Preço pela Quilometragem',
    y='quilometragem',
    p='''Vemos a relação entre o preço e a quilometragem rodada do veículo. 
    Os veículos com maior quilometragem tendem a ter um valor menor. 
    Podemos considerar uma correlação negativa entre essas variáveis, 
    mas é necessário levar em conta outras variáveis, pois a correlação não implica causalidade. 
    O ano e o modelo são determinantes na precificação final.'''
)

treemap(
    data=data_preco,
    options=data.columns.to_list(),
    default=data.columns.to_list()[:2],
)
