import pandas as pd
import matplotlib.pyplot as plt

dataframe = pd.read_csv("c:/Users/muril/Documentos/datasets/vinhos/vinhos.csv", delimiter=";")


#gráfico de barras com a quantidade total de vinhos por país
dataframe.replace()
plt.figure(figsize=(10, 6))
dataframe['pais'].value_counts().plot(kind='bar')
plt.xlabel('País')
plt.ylabel('Quantidade de Vinhos')
plt.title('Quantidade de Vinhos por País')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#gráfico de barras com a quantidade de vinhos por pontuação
plt.figure(figsize=(10, 6))
dataframe['pontos'].value_counts().sort_index().plot(kind='bar')
plt.xlabel('Pontuação')
plt.ylabel('Quantidade de Vinhos')
plt.title('Quantidade de Vinhos por Pontuação')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#histograma com as distribuições dos preços
num_bins=int(1+3.322* (len(dataframe['preco'].dropna()) **0.5))
plt.figure(figsize=(10, 6))
plt.hist(dataframe['preco'].dropna(), bins=num_bins, edgecolor='black')
plt.xlabel('Preço')
plt.ylabel('Frequência')
plt.title('Distribuição dos Preços dos Vinhos')
plt.tight_layout()
plt.show()