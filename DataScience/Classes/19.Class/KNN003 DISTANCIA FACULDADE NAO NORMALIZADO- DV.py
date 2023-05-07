# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 00:13:47 2023

@author: AM
"""
import math
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn import metrics
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neighbors import NearestCentroid
import numpy as np
import pandas as pd
import operator
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.colors import ListedColormap
from sklearn import neighbors, datasets
import turtle


def distancia(p1,p2):
    p1x=p1[0]
    p1y=p1[1]
    p2x=p2[0]
    p2y=p2[1]    
    dist=math.sqrt( math.pow(p1x-p2x,2)+math.pow(p1y-p2y,2))
    return dist

from sklearn.neighbors import NearestNeighbors
import numpy as np

# LEITURA DADOS
dados=pd.read_csv("D:\\PUC-CAMPINAS\\APLICACAO MACHINE LEARNING\\AULAS\\AULA004 KNN\\dadosAlunos.csv")

# TRANSFORMAR OS VALORES LIDOS EM UM ARRAY
X=np.array(dados)

print("\nDATASET: \n",X)

input("DIGITE ALGO    DATASET: ")

# DETERMINAR OS VIZINHOS
nbrs = NearestNeighbors(n_neighbors=2, algorithm='kd_tree').fit(X)
distances, indices = nbrs.kneighbors(X)
#INDICE DE VIZINHOS MAIS PROXIMOS
print("\nVIZINHOS MAIS PROXIMOS")
for i in range(0,len(indices)):  
  tp=indices[i]  
  print(tp,"\t ",X[tp[0]]," - ",X[tp[1]],"\t  ",distances[i][1],"\t  ",distancia(X[tp[0]],X[tp[1]]))

           
# CALCULO ALTERNATIVO PARA A DISTANCIA II
indices=[]
distances=[]
clusters=[]
fatordistancia=input("DIGITE O FATOR DE DISTANCIA MÁXIMA: ")
fatordistancia=float(fatordistancia)

for i in range(0,len(X)):
    for j in range(0,len(X)):
        dist=distancia(X[i],X[j])
        if (i!=j) and dist<fatordistancia:
            indices.append([i,j])
            distances.append([0,dist])


#INDICE DE VIZINHOS MAIS PROXIMOS
print("\n\nVIZINHOS MAIS PROXIMOS ALTERNATIVO")
for i in range(0,len(indices)):  
  tp=indices[i]  
  print(tp,"\t ",X[tp[0]]," - ",X[tp[1]],"\t  ",distances[i][1],"\t  ",distancia(X[tp[0]],X[tp[1]]))

   
# DISTANCIAS
print("\nDISTANCIA ENTRE OS VIZINHOS")
print(distances)


x=[]
y=[]
for i in range(0,len(X)):
    x.append(float(X[i][0]))
    y.append(float(X[i][1]))
plt.scatter(x,y,color="yellow")
plt.show()


# MATRIZ DE CONEXÃO
matriz=nbrs.kneighbors_graph(X).toarray()
print("\nMATRIZ DE VIZINHOS")
print(matriz)


# MONTAR CLUSTERS
clusters=[]
for i in range(0,len(indices)):
    p0=indices[i][0]
    p1=indices[i][1]
    posP0=-1
    posP1=-1
    chaveP0=False
    for j in range(0,len(clusters)):
      if (p0 in clusters[j]):
          chaveP0=True
          posP0=j

    #clusters.append([p0]) 
    
    chaveP1=False
    for k in range(0,len(clusters)):
      if (p1 in clusters[k]):
          chaveP1=True
          posP1=k
          
    # VERIFICAR SE p0 e P1 NAO ESTAO CADASTRADOS 
    if (chaveP0==False) and (chaveP1==False):
        clusters.append([p0,p1])

    # VERIFICAR SE p0 CADASTRADO e P1 NAO ESTA CADASTRADO 
    if (chaveP0==True) and (chaveP1==False):
        clusters[posP0]+=[p1]    
    
    # VERIFICAR SE p0 CADASTRADO e P1 NAO ESTA CADASTRADO 
    if (chaveP0==False) and (chaveP1==True):
        clusters[posP1]+=[p0]          



# LISTAR DOS CLUSTERS
print("\nMONTAGEM DOS CLUSTERS")
for i in range(0,len(clusters)): 
   print(i,"  ",clusters[i]) 

# CORES
ck=['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w','b', 'g', 'r', 'c', 'm', 'y', 'k', 'w','b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']   
ck2=["red","green","blue", "yellow","darkblue","darkgreen"]
#PLOTAR PONTOS DOS CLUSTERS
for i in range(0,len(clusters)):
    # MONTAR OS CLASTERS
    xx=[]
    yy=[]
    for j in range(0,len(clusters[i])):
        xx.append(x[clusters[i][j]])
        yy.append(y[clusters[i][j]])    
               
    plt.scatter(xx, yy, s=10, c=ck[i])

plt.show()

