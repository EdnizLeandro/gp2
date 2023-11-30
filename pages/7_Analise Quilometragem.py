import streamlit as st
import pandas as pd
import plotly.express as px
from build import build_header
from charts import boxplot, scatter, treemap, hist, bar, select_chart

# Corrigir caminho do arquivo de dados
data = pd.read_parquet('data/price_cars10k.parquet')

build_header(
    title='Análise Quilometragem',
    hdr='# Análise quilometragem',
    p='''
        <p> Primeiras análises no dataset de quilometragem</p>
    '''
)

# Gráfico de caixa (boxplot)
km_preco = data[['preco', 'quilometragem']]
boxplot(
    km_preco,
    x='quilometragem',
    title='BOXPLOT DOS QUILOMETRAGEM',
    p='Aqui vemos a distribuição dos preços dos veículos'
)

# Gráfico de dispersão (scatter plot)
scatter(
    data=data,
    x='quilometragem',
    y='preco',
    xlabel='Quilometragem',
    ylabel='Preço'
)

scatter(
    data=data,
    x='quilometragem',
    y='ano',
    xlabel='Quilometragem',
    ylabel='Ano'
)

# Treemap
treemap(
    data=km_preco,
    options=data.columns.to_list(),
    default=data.columns.to_list()[:2],
)

# Gráfico de barras
km_modelo = data.groupby("modelo", as_index=True)[['quilometragem']].mean()
km_modelo.sort_values('quilometragem', ascending=False, inplace=True)
km_modelo = km_modelo.head(10)
bar(
    title='GRAFICO DE BARRAS, MODELO X QUILOMETRAGEM',
    data=km_modelo,
    x='quilometragem',
    xlabel='Quilometragem Média',
    ylabel='Modelo'
)

# Ordenação redundante removida
data.sort_values('quilometragem', ascending=True, inplace=True)

# Selecione o gráfico com a função genérica
select_chart(
    data,
    x='quilometragem',
    options=data.columns,
    type_graph=px.bar,
    type_txt='GRAFICO DE BARRAS',
    xlabel='Quilometragem',
    ylabel='Outra Variável'
)
