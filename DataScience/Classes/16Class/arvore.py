import os
import subprocess
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt #para gráficos
from sklearn import tree #Tem uma estrutura de árvore que será usada
from sklearn.tree import DecisionTreeClassifier #Classificador que gera uma árvore de regras

#  Lendo os dados
db = pd.read_csv("C:\\Users\\bcaboclo\\Desktop\\Tecprogramspace\\Classes\\16Class\\DATA SET EXEMPLO 001DD REDUZIDO.csv")
print(db)

campos = list(db)

for campo in campos:
    print(f'\nCAMPO: {campo}')
    print([campo])

input ("DIGITE ALGO 0:")


# SEPARANDO DADOS DE PETALAS
EstadoCivil = db['ECIVIL'].copy() 
Idade = db['IDADE'].copy() 
Peso = db['PESO'].copy()
Altura= db['ALTURA'].copy()

# SEPARAR DADOS COMPRIMENTO e LARGURA PETALA
EstadoCivil0=[]
Idade0=[]
Peso0=[]
Altura0=[]
EstadoCivil1=[]
Idade1=[]
Peso1=[]
Altura1=[]
EstadoCivil2=[]
Idade2=[]
Peso2=[]
Altura2=[]
EstadoCivil3=[]
Idade3=[]
Peso3=[]
Altura3=[]

for i in range(len(Idade)):
    if EstadoCivil[i]==0:
        EstadoCivil0.append(EstadoCivil[i])
        Idade0.append(Idade[i])
        Peso0.append(Peso[i])
        Altura0.append(Altura[i])
    if EstadoCivil[i]==1:
        EstadoCivil1.append(EstadoCivil[i])
        Idade1.append(Idade[i])
        Peso1.append(Peso[i])
        Altura1.append(Altura[i])
    if EstadoCivil[i]==2:
        EstadoCivil2.append(EstadoCivil[i])
        Idade2.append(Idade[i])    
        Peso2.append(Peso[i])
        Altura2.append(Altura[i])        
    else:
        EstadoCivil3.append(EstadoCivil[i])
        Idade3.append(Idade[i])  
        Peso3.append(Peso[i])
        Altura3.append(Altura[i])        
        
plt.scatter(EstadoCivil0,Idade0,color="green") 
plt.scatter(EstadoCivil1,Idade1,color="blue")
plt.scatter(EstadoCivil2,Idade2,color="yellow")
plt.scatter(EstadoCivil3,Idade3,color="black")
plt.title("SOLTEIRO(verde)  CASADO(azul)  DIVORCIO(amarelo)  VIUVO(preto)")
plt.xlabel("ESTADO CIVIL")
plt.ylabel("IDADE")     
plt.show()
  
plt.scatter(EstadoCivil0,Peso0,color="green") 
plt.scatter(EstadoCivil1,Peso1,color="blue")
plt.scatter(EstadoCivil2,Peso2,color="yellow")
plt.scatter(EstadoCivil3,Peso3,color="black")
plt.title("SOLTEIRO(verde)  CASADO(azul)  DIVORCIO(amarelo)  VIUVO(preto)")
plt.xlabel("ESTADO CIVIL")
plt.ylabel("PESO")     
plt.show()     
        
plt.scatter(EstadoCivil0,Altura0,color="green") 
plt.scatter(EstadoCivil1,Altura1,color="blue")
plt.scatter(EstadoCivil2,Altura2,color="yellow")
plt.scatter(EstadoCivil3,Altura3,color="black")
plt.title("SOLTEIRO(verde)  CASADO(azul)  DIVORCIO(amarelo)  VIUVO(preto)")
plt.xlabel("ESTADO CIVIL")
plt.ylabel("ALTURA")     
plt.show()

input ("DIGITE ALGO PLOT DADOS:")

# CONTAR O NÚMERO DE OCORRÊNCIAS
Cidade=db.value_counts("IDADE") 
print("CONTAR IDADES: \n",Cidade)

hd=db.head()
print("\nDB HEAD:\n",hd)

input ("DIGITE ALGO HEADS :")


# #### Criando classificador de árvore de decisão
# 
# A árvore de decisão procura cortes/intervalos 
# nos atributos de forma a dividir as classes o melhor possível; 
# gerando uma árvore de regras de decisão e nos informando 
# o quão separadas estão as classes em função dessa regra

# entropia é uma medida de caoticidade/'bagunça',
# utilizada para medir a mistura das classes dentro de uma regra,
# veremos ela logo
clf = DecisionTreeClassifier(criterion="entropy") 

# Os classificadores na biblioteca sklearn e scipy 
# esperam os dados (X) separados das metas/rótulos/classe (Y) 
# Vamos separar a coluna do rótulo

# drop (REMOVER) UMA COLUNA
dbAtributos = db.drop("ESCOLAR", axis=1, inplace=False)
print("\nDB ATRIBUTOS: \n",dbAtributos)


# SEPARA/COPIA O CAMPO "ESCOLAR"
#Em muitos casos o copy() não é necessário, mas é uma boa prática utilizá-lo
dbRotulos = db["ESCOLAR"].copy() 
print("\nDB RÓTULOS: \n",dbRotulos)

input ("DIGITE ALGO 3:")


Arvore=clf.fit(dbAtributos, dbRotulos)
print("ARVORE: \n",Arvore)
input ("DIGITE ALGO ATRIBUTOS FIT 4: ")


# Imprimindo as regras geradas
fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(20,20))
tree.plot_tree(clf, feature_names=dbAtributos.columns, class_names={0:"PRIMARIO",1:"ENSINO MEDIO",2:"SUPERIOR"},filled=False)
plt.show()
input ("DIGITE ALGO ÁRVORE:")

# ### Interpretando a árvore de decisão
# 
# Lê-se um conjunto de regras pelo caminho entre raiz e as folhas da árvore. 
# cada nível inferior, novas regras são adicionadas, 
# filtrando amostras em grupos potencialmente menores, 
# mas mais homogêneos em relação à distribuição de classes, 
# essa homogeneidade pode ser medida de várias maneiras escolhemos a entropia.
# 
# Cada nó na árvore apresenta algumas informações:
# - Regra no formato atributo maior|menor|(igual) valor
# - Valor da medida de homogeineidade
# - Quantidade de amostras filtradas pelo conjunto de regras
# - Distribuição das classes na forma: [$qtdC_1, qtdC_2, ... qtdC_n$]
# - Classe majoritária filtrada pela regra (em caso de empate uma das duas é escolhida)
# - Cada regra possui um filho (outra regra ou separação) à esquerda (valores menores que a regra) e à direita

# ##### Entendendo entropia [1]
# 
# É uma medida de informação introduzida por Claude Shannon, 
# inclusive sendo chamada de entropia de Shannon. 
# Podemos interpretá-la como a quantidade de bits necessária para descrever um conjunto de dados, 
# dados homogêneos não carregam informação portanto consomem 0 bits, 
# já dois eventos com probabilidade igual de acontecer precisam de 1 bit. 
# e.g. Uma moeda que sempre dá cara não possui informação, 
# mas quando a moeda tem a chance de dar cara ou coroa temos uma situação mais complicada 
# com mais informação, notem que não podemos prever uma face ou outra; 
# agora imaginem um meio termo, a moeda tem uma chance muito grande de dar cara e uma menor de dar coroa, 
# ainda temos incerteza/informação, mas ainda conseguimos 'apostar' 
# com uma certa confiança que ela irá dar cara, portanto ela tem um pouco menos de informação/caoticidade 
# em relação à moeda equilibrada, a entropia será maior que 0, mas menor do que 1. 
# Quanto mais possibilidades diferentes (no nosso exemplo cara ou coroa), 
# maior o potencial de informação e maior é o valor máximo de entropia, 
# e.g. com 4 possíveis saídas a entropia máxima é 2 bits. 
# Abaixo veremos como a curva de entropia para dois valores: 


# #Considerando que dois eventos distintos podem acontecer
# pi = np.arange(0.01,1,0.01)
# plt.plot(pi,-(pi*np.log2(pi) + (1-pi)*np.log2(1-pi)))
# plt.xlabel("Probabilidade de coroa")
# plt.ylabel("Entropia")
# plt.show()


# REGR DO TOPO
baseFiltro1 = db[db["ECIVIL"] <= 1.5] 
print("baseFiltro1: \n",baseFiltro1)

bfHD=baseFiltro1.head()
print("\nFILTRO ECIVIL <=1.5  : \n",bfHD)

input ("DIGITE ALGO ECIVIL <=1.5:")


baseFiltro1['IDADE'].value_counts()

# SEPARANDO DADOS DE OUTRA REGRA
baseFiltro2 = db[(db["ECIVIL"] >=1.5) & (db["IDADE"] <=50.5)] 
baseFiltro2['IDADE'].value_counts()
print("\nbaseFiltro2: \n",baseFiltro2)

input ("DIGITE ALGO REGRA   ECIVIL >=1.5 e IDADE <=50.5 :")

# SEPARANDO DADOS DE OUTRA REGRA
baseFiltro3 = db[(db["ECIVIL"] >=1.5) & (db["IDADE"] > 50.5)] 
baseFiltro3['IDADE'].value_counts()
print("\nbaseFiltro3: \n",baseFiltro3)

input ("DIGITE ALGO REGRA   ECIVIL >=1.5 e IDADE > 50.5 :")


# SEPARANDO DADOS DE OUTRA REGRA
baseFiltro4 = db[(db["ECIVIL"] <= 1.5) & (db["IDADE"] <11.) ]
print("baseFiltro3: \n",baseFiltro4)

#baseFiltro3['Subespécie'].value_counts()
input ("DIGITE ALGO IDADE COM ECIVIL <= 1.5 e IDADE<11:")


# ESTATISTICA
print("\n********************************")
print("ESTATÍSTICAS DA ARVORE:")
dbLabel=list(db.columns)
print("ROTULOS: ",dbLabel)
for pos,i in enumerate(dbLabel):
    print(pos," ",i)
# NÚMERO DE NÓS
n_nodes = clf.tree_.node_count
print("NÚMERO DE NÓS=",n_nodes)
children_left = clf.tree_.children_left
print("NÚMERO DE NÓS ESQUERDA=",children_left)
children_right = clf.tree_.children_right
print("NÚMERO DE NÓS DIREITA=",children_right)
feature = clf.tree_.feature
print("NÚMERO DE feature=",feature)
threshold = clf.tree_.threshold
print("NÚMERO DE threshold=",threshold)

input("STATUS DA ÁRVORE: ")

# MONTANDO AS REGRAS DE PERCURSO
node_depth = np.zeros(shape=n_nodes, dtype=np.int64)
is_leaves = np.zeros(shape=n_nodes, dtype=bool)

stack = [(0, 0)] 
# ENCONTRAR OS PONTOS TERMINAIS
while len(stack) > 0:
    # `pop` ensures each node is only visited once
    node_id, depth = stack.pop()
    node_depth[node_id] = depth

    # If the left and right child of a node is not the same we have a split
    # node
    is_split_node = children_left[node_id] != children_right[node_id]
    # If a split node, append left and right children and depth to `stack`
    # so we can loop through them
    if is_split_node:
        stack.append((children_left[node_id], depth + 1))
        stack.append((children_right[node_id], depth + 1))
    else:
        is_leaves[node_id] = True
        
print("A ÁRVORE TEM {n} NÓS - ESTRUTURA:\n".format(n=n_nodes))
    
for i in range(n_nodes):
    if is_leaves[i]:
        print(
            "{space}node={node} is a leaf node.".format(
                space=node_depth[i] * "\t", node=i
            )
        )
    else:
        print(
            "{space}node={node} is a split node: "
            "go to node {left} if X[:, {feature}] <= {threshold} "
            "else to node {right}.".format(
                space=node_depth[i] * "\t",
                node=i,
                left=children_left[i],
                feature=feature[i],
                threshold=threshold[i],
                right=children_right[i],
            )
        )
        
print("\n*******************************************************")        
for i in range(n_nodes):
     if is_leaves[i]:
         print(
             "{space}node={node} É UM NÓ FOLHA - TERMINAL.".format(space=node_depth[i] * "\t", node=i)
              )
     else:
         print(
             "{space}node={node} É UM NÓ COM DIVISÃO: "
             "VÁ PARA O NÓ {left} SE X[:, {feature}] <= {threshold} "
             "CASO CONTRÁRIO VÁ PARA O NÓ {right}.".format(
                 space=node_depth[i] * "\t",
                 node=i,
                 left=children_left[i],
                 feature=campos[feature[i]],
                 threshold=threshold[i],
                 right=children_right[i],
             )
         )       

# CAMINHOS DE DECISAO 
from sklearn.model_selection import train_test_split
# X_train, X_test, y_train, y_test = clf.train_test_split(dbAtributos, dbRotulos, random_state=0)
X_train, X_test, y_train, y_test = train_test_split(dbAtributos, dbRotulos, test_size=0.33, random_state=26) 


node_indicator = clf.decision_path(X_test)
# Return the index of the leaf that each sample is predicted as.
leaf_id = clf.apply(X_test)

# RETORNA A CLASSIFICACAO ESCOLAR PREVISTA
X_test["ECIVIL"][8]=1
print(X_test)
previsao=clf.predict(X_test)
print("X_test: \n",X_test)
print("\nPREVISÃO:",previsao)

input("DIGITE ALGO  previsão:")    
