import streamlit as st
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns


# Carregar os dados do arquivo CSV
df = pd.read_csv('C:\\Users\\Usuario\\Downloads\\true_car_listings.csv')

# Adicionar um título ao aplicativo
st.title('Agrupamento de Carros')

# Adicionar uma breve descrição
st.write('Este aplicativo realiza o agrupamento de carros usando o algoritmo K-Means.')

# Mostrar as primeiras linhas do DataFrame
st.write('Primeiras linhas do DataFrame:')
st.write(df.head())

# Selecionar características numéricas para o agrupamento
caracteristicas_numericas = df[['Price', 'Year', 'Mileage']]

# Padronizar os dados para ter média zero e desvio padrão um
scaler = StandardScaler()
caracteristicas_numericas_padronizadas = scaler.fit_transform(caracteristicas_numericas)

# Escolher o número de clusters (usando o Método do Cotovelo)
# Aqui, você pode experimentar diferentes valores para num_clusters
num_clusters = st.slider('Escolha o número de clusters:', min_value=2, max_value=10, value=3)

# Aplicar o algoritmo k-means com definição explícita de n_init
kmeans = KMeans(n_clusters=num_clusters, random_state=42, n_init=10)
df['Cluster'] = kmeans.fit_predict(caracteristicas_numericas_padronizadas)

# Visualizar a distribuição dos clusters nos dados
st.write('Distribuição dos Clusters:')
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Year', y='Mileage', hue='Cluster', data=df, palette='viridis', s=100)
plt.title('Agrupamento K-Means de Carros')
plt.xlabel('Ano')
plt.ylabel('Quilometragem')
st.pyplot()

# Exibir estatísticas descritivas para cada cluster
estatisticas_clusters = df.groupby('Cluster')[['Price', 'Year', 'Mileage']].describe().transpose()
st.write('Estatísticas Descritivas para Cada Cluster:')
st.write(estatisticas_clusters)

# Visualizar os centros dos clusters nos dados originais
centros_clusters = scaler.inverse_transform(kmeans.cluster_centers_)
centros_clusters_df = pd.DataFrame(centros_clusters, columns=['Price', 'Year', 'Mileage'])
st.write('Centros dos Clusters:')
st.write(centros_clusters_df)

# Salvar o DataFrame com os clusters atribuídos para referência futura
df.to_csv('dados_carros_com_clusters.csv', index=False)
