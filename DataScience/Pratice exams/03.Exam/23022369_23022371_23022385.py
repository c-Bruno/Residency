import os
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

#Carregar a base de dados Iris-2-1.csv
# Lendo os dados do arquivo externo
print('\033[33m\nImportando arquivo...\033[m')
# Define o diretorio atual como o diretorio do arquivo
current_directory = os.path.dirname(os.path.abspath(__file__))
# Partindo do diretorio, procuramos pelo nome do arquivo
fileName = os.path.join(current_directory, 'Iris-2-1.csv')

df = pd.read_csv(fileName)
# df = pd.read_csv('Iris-2-1.csv')

X = df.drop('Subespécie', axis=1)
y = df['Subespécie']


#Aplicar PCA para visualização (2 ou 3 dimensões)
pca_visualization = PCA(n_components=3)
X_visualization = pca_visualization.fit_transform(X)

# Plotar gráfico  em 2 dimensões com os componentes principais
plt.scatter(X_visualization[:, 0], X_visualization[:, 1], c=y)
plt.xlabel('Componente Principal 1')
plt.ylabel('Componente Principal 2')
plt.title('Visualização com PCA')
plt.show()

#Aplicar PCA para seleção de atributos (2 atributos)
pca_selection = PCA(n_components=2)
X_selection = pca_selection.fit_transform(X)

#Plotar gráfico com os atributos selecionados
plt.scatter(X_selection[:, 0], X_selection[:, 1], c=y)
plt.xlabel('Atributo Selecionado 1')
plt.ylabel('Atributo Selecionado 2')
plt.title('Seleção de Atributos com PCA')
plt.show()


