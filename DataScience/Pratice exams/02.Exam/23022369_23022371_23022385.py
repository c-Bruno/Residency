import os
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import tree
import matplotlib.pyplot as plt


'''
=== Legenda colunas ========================
    species => Especies
    island => Ilha
    bill_length_mm => Comprimento do bico
    bill_depth_mm => Profundidade do bico
    flipper_length_mm => Comprimento da nadadeira
    body_mass_g => Massa corporal
    sex => Sexo
============================================
'''

# Lendo os dados do arquivo externo 
print('\033[33m\nImportando arquivo...\033[m')
current_directory = os.path.dirname(os.path.abspath(__file__)) # Define o diretorio atual como o diretorio do arquivo
fileName = os.path.join(current_directory, 'penguins.csv') # Partindo do diretorio, procuramos pelo nome do arquivo
dataframe_penguins = pd.read_csv(fileName)

print(dataframe_penguins)

print('\033[33mRemovendo ruido do dataset...\n\033[m')
dataframe_penguins = dataframe_penguins.dropna(subset='sex') # Remove todos os NaN da coluna sex
sexcolumn = dataframe_penguins['sex']

data = dataframe_penguins[[
    'bill_length_mm', 
    'bill_depth_mm', 
    'flipper_length_mm', 
    'body_mass_g',
]] = dataframe_penguins.groupby('species')[[
    'bill_length_mm', 
    'bill_depth_mm', 
    'flipper_length_mm', 
    'body_mass_g'
]].transform(lambda x: x.fillna((x.mean()))).applymap('{:.3f}'.format)

dataframe_penguins = pd.DataFrame(data)
dataframe_penguins['sex'] = sexcolumn
dataframe_penguins

print(dataframe_penguins) # Print do dataset já padronizado


# carregar conjunto de dados
print('\033[33m\nCarregando conjunto de dados...\033[m')
x = dataframe_penguins.drop(columns=['sex']) # entrada
y = dataframe_penguins['sex'] # saida
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2) # alocando 20% dos dados pra teste
# as primeiras vareaveis são a saida de treinamento, e as outras duas são a saida de test

# criar modelo de árvore de decisão
print('\033[33mCriando modelo da árvore de decisão...\033[m')
model = DecisionTreeClassifier()
model.fit(x_train, y_train)


# Imprimindo as regras geradas
fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(20,20))
tree.plot_tree(model, feature_names=dataframe_penguins.columns, 
               class_names={0:"Especies",
                            1:"Ilha",
                            2:"Comprimento do bico",
                            3:"Profundidade do bico",
                            4:"Comprimento da nadadeira",
                            5:"Massa corporal",
                            6:"Sexo"},filled=False) # o primeiro atributo pode ser a vareavel Arvore, é uma copia de clf
plt.show()

# SEPARANDO DADOS DOS penguins
# species = dataframe_penguins['species'].copy() 
# island = dataframe_penguins['island'].copy() 
# bill_length_mm = dataframe_penguins['bill_length_mm'].copy()
# bill_depth_mm = dataframe_penguins['bill_depth_mm'].copy()
# flipper_length_mm= dataframe_penguins['flipper_length_mm'].copy()
# body_mass_g= dataframe_penguins['body_mass_g'].copy()



# dataframe_penguins.shape # (n records, n columns)

# dataframe_penguins.describe()
# as colunas que não aparece provavelmente tem valores "incorretos"
# std = standart deviation, que é a variação entre os valores

# dataframe_penguins.values

# penguins = dataframe_penguins.fillna(dataframe_penguins.median())
# print(penguins)
