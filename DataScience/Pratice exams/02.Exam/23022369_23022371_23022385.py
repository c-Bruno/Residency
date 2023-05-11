import os
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import tree
import matplotlib.pyplot as plt
import seaborn as sns


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
# Define o diretorio atual como o diretorio do arquivo
current_directory = os.path.dirname(os.path.abspath(__file__))
# Partindo do diretorio, procuramos pelo nome do arquivo
fileName = os.path.join(current_directory, 'penguins.csv')
dataframe_penguins = pd.read_csv(fileName)

# dataframe_penguins.shape # (n records, n columns)

# dataframe_penguins.describe()
# dataframe_penguins.values
# as colunas que não aparece provavelmente tem valores "incorretos"
# std = standart deviation, que é a variação entre os valores

print('\033[33mRemovendo ruido do dataset...\n\033[m')
# Remover todos os 'NaN' das colunas 
dataframe_penguins = dataframe_penguins.dropna(subset=['species', 'island', 'sex']) 

# Codificando cada valor único em um inteiro diferente.
dataframe_penguins['species'] = dataframe_penguins['species'].factorize()[0]
dataframe_penguins['island'] = dataframe_penguins['island'].factorize()[0]

# Agrupar por espécies e preencher NaN com a média de cada grupo
cols = ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g']
dataframe_penguins[cols] = dataframe_penguins.groupby(
    'species')[cols].transform(lambda x: x.fillna(x.mean()))

# Formatar as colunas numéricas com 3 casas decimais
dataframe_penguins[cols] = dataframe_penguins[cols].applymap('{:.3f}'.format)

# Resetar o índice e manter a coluna 'sex' no final
dataframe_penguins = dataframe_penguins.reset_index(drop=True)[
    ['species', 'island', 'bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g', 'sex']]

# pd.set_option('display.max_columns', None)
# pd.set_option('display.max_rows', None)
print(dataframe_penguins.head(20))


print('\033[33m\nCriando modelo da árvore de decisão...\033[m')
model = DecisionTreeClassifier()


print('\033[33mPlotando os graficos...\033[m')
#Correlação 'bill_length_mm', 'bill_depth_mm', 'flipper_length_mm' e 'body_mass_g' com o sexo das espécies.
sns.scatterplot(data=dataframe_penguins, x='bill_length_mm', y='bill_depth_mm', hue='sex')
plt.show()

sns.scatterplot(data=dataframe_penguins, x='flipper_length_mm', y='body_mass_g', hue='sex')
plt.show()

# Gráfico de dispersão do comprimento do bico e massa corporal
plt.scatter(dataframe_penguins['bill_length_mm'], dataframe_penguins['body_mass_g'])
plt.xlabel('Comprimento do bico (mm)')
plt.ylabel('Massa corporal (g)')
plt.title('Relação entre comprimento do bico e massa corporal')
plt.show()

# Gráfico de barras da distribuição das espécies
species_counts = dataframe_penguins['species'].value_counts()
species_names = ['Adelie', 'Chinstrap', 'Gentoo']
plt.bar(species_names, species_counts)
plt.xlabel('Espécies')
plt.ylabel('Número de amostras')
plt.title('Distribuição das espécies')
plt.show()

sns.countplot(data=dataframe_penguins, x='species', hue='sex')
plt.title('Distribuição das espécies por sexo')
plt.xlabel('Espécies')
plt.ylabel('Contagem')
plt.show()


print('\033[33mTreinando...\033[m')
x = dataframe_penguins.drop(columns=['sex']) # entrada
y = dataframe_penguins['sex'] # saida
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2) # alocando 20% dos dados pra teste
# as primeiras vareaveis são a saida de treinamento, e as outras duas são a saida de test

model.fit(x_train, y_train)


print('\033[33mPlotando arvore de decisão...\033[m')
names = ["Especies", "Ilha", "Comprimento do bico","Profundidade do bico","Comprimento da nadadeira","Massa corporal","Sexo"]
# The class names are stored in decision_tree_classifier.classes_, i.e. the classes_ attribute of your DecisionTreeClassifier instance. 
# And the feature names should be the columns of your input dataframe. For your case you will have
feature_names = list(dataframe_penguins.columns)
class_names = model.classes_

# print(tree.export_text(model))
# the good is small size, and big DPI
plt.figure(figsize=(70,30))
tree.plot_tree(model, 
                   feature_names=names,  
                   class_names=class_names,
                   fontsize=15,
                   filled=True)
# plt.savefig('tree_high_dpi', dpi=200)
plt.show()


print('\033[33mAcuracia...\n\033[m')
predictions = model.predict(x_test)
score = accuracy_score(y_test, predictions)
print(score)