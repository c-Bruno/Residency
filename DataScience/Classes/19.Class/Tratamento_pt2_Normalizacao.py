#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec


# ### Corrigindo para diferentes escalas
# OBSERVE QUE A ALTURA VARIA ENTRE 0 e 2, MAS O PESO ENTRE 0 e 52
# ESTA DIFERENÇA PROVOCA DISTORÇÃO NOS CÁLCULOS
df = pd.DataFrame({'Altura':[1.6,2.0,1.6,1.8],'Peso':[50,50,52,60],'Cor':['b','r','g','y']})

print("\nDATASET:\n",df)


# Qual amostra/indivíduo é o mais distante, ou diferente? 
# Nossa intuição diz que é o indivíduo número 1 (vermelho), 
# que é muito mais alto que os outros, e todos os outros tem quase o mesmo peso
# Quando geramos um gráfico, eles podem aprecer equi-distantes e nos induzir ao erro
df.plot.scatter('Altura','Peso',color=df['Cor'])
plt.show()

input("DIGITE ALGO PARA CONTINUAR:")

# Se consideramos que cada ponto é uma amostra ou ponto nessa imagem, 
# podemos medir a similaridade ou diferenças em função da distância entre os pontos

# Podemos medir essa distância como o tamanho da linha reta 
# que separa os dois pontos (i.e. distância euclidiana), 
# que é medida da seguinte forma (considerando vários atributos {X, Y, ... N}:
# d(a,b) = sqrt{(X_a - X_b)^2 + (Y_a - Y_b)^2 + ... + (N_a - N_b)^2} 
# 
# Em duas dimensões já conhecemos essa fórmula, ela vem do teorema de Pitágoras, 
# só foi extendida para aceitar mais que 2 dimensões

fig, ax = plt.subplots(nrows=1,ncols=1)
img = np.asarray(Image.open('Euclidiana.png'))
ax.tick_params(which = 'both', size = 0, labelsize = 0)
ax.imshow(img)
plt.show()
print('')

input("DIGITE ALGO PARA CONTINUAR:")


# Vamos gerar esse gráfico em escala para poder medir as distâncias entre os pontos, 
# e verificar qual ponto é o outlier
print("\nDATASET:\n",df)

d = []
for i in [0,1,2,3]:
    d.append([])
    for j in [0,1,2,3]:
        distAlt = (df.loc[i]['Altura'] - df.loc[j]['Altura'])**2
        distPeso = (df.loc[i]['Peso'] - df.loc[j]['Peso'])**2
        distij = np.sqrt(distAlt + distPeso)
        d[i].append(distij)
distDF = pd.DataFrame(d, index=df['Cor'].head(4), columns=df['Cor'].head(4))

# Notamos que Vermelho e Azul são bem próximos na verdade 
# e o diferentão é o Verde, por que isso acontece? 
# A imagem abaixo coloca esses pontos no espaço, 
# deixando os dois eixos na mesma escala (3 pontos de diferença)

print("\nDISTÂNCIA ENTRE OS PONTOS:\n",distDF)

input("DIGITE ALGO PARA CONTINUAR - DISTÂNCIA ENTRE OS PONTOS:")

df.head(4).plot.scatter('Altura','Peso',color=df.head(4)['Cor'],ylim=(49.5,60.5),xlim=(-0.5,2.5))
plt.show()

input("DIGITE ALGO PARA CONTINUAR - PLOTANDO OS PONTOS (ESCALA DEFINIDA) :")

# Para que a distância entre as amostras siga a nossa intuição, 
# precisamos reduzir a escala da altura, de modo que uma pequena mudança 
# na **altura** seja comparável com uma pequena mudança no **peso**

# Utilizaremos as outras amostras para gerar uma escala de 0 a 1, 
# 0 indica a menor amostra naquele atributo, e 1 a maior; 
# Notem que com essa transformação, deixamos de comparar pessoas de tal altura com tal altura 
# e começamos a comparar pessoas mais altas ou mais baixas, 
# com pessoas mais altas ou mais baixas, nossa medida fica relativa à nossa amostra

# Faremos isso por meio da normalização MinMax, ela recebe esse nome, 
# pois os valores mínimos serão atribuídos ao valor 0 e os valores máximos ao valor 1. 
# Considerando que cada atributo X é um conjunto de valores Xi, 
# normalizamos esse atributo com o seguinte cálculo:
# Xi_novo = ( x_i - min{X} ) / ( max{X} - min{X} )

# Para exemplificar vamos supor X = {1,2,4}
# min{X} = 1
# max{X} = 4
# Nossos Xi novos são:
# $\frac{1 - 1}{4 - 1} = \frac{0}{3} = 0$<br><br>
# $\frac{2 - 1}{4 - 1} = \frac{1}{3} = 0.33$<br><br>
# $\frac{4 - 1}{4 - 1} = \frac{3}{3} = 1$<br><br>
# Xnovo = {0, 0.33, 1}

# Vamos aplicar a fórmula em todas as colunas do nossos dados. 
# Considerando que a altura varia de 0.5 a 2.3 e o peso de 30 a 110Kg

# AJUSTANDO A ESCALA
mins = pd.Series([0.5,30],index=['Altura','Peso'])
maxs = pd.Series([2.3,110],index=['Altura','Peso'])
dfNorm = (df[['Altura','Peso']] - mins)/(maxs - mins)
dfNorm = pd.concat([dfNorm,df['Cor']],axis=1) #colocando a coluna de cores de volta para podermos plotar
print("\nPONTOS NORMALIZADOS:\n",dfNorm)

distNorm = []
for i in [0,1,2,3]:
    distNorm.append([])
    for j in [0,1,2,3]:
        distAlt = (dfNorm.loc[i]['Altura'] - dfNorm.loc[j]['Altura'])**2
        distPeso = (dfNorm.loc[i]['Peso'] - dfNorm.loc[j]['Peso'])**2
        distij = np.sqrt(distAlt + distPeso)
        distNorm[i].append(distij)
distDFNorm = pd.DataFrame(distNorm, index=df['Cor'].head(4), columns=df['Cor'].head(4))

print("\nDISTÂNCIA ENTRE OS PONTOS:\n",distDFNorm)

input("DIGITE ALGO PARA CONTINUAR - PONTOS NORMALIZADOS :")

# Vamos plotar os 3 pontos novamente para mostrar que agora as distâncias 
# seguem nossa intuição de que o ponto vermelho é o mais distinto entre 
# os pontos vermelho, verde e azul

dfNorm.plot.scatter('Altura','Peso',color=dfNorm.head(4)['Cor'],xlim=(-0.1,1.1),ylim=(-0.1,1.1))
plt.show()

input("DIGITE ALGO PARA CONTINUAR - PONTOS NORMALIZADOS :")

# Nem sempre teremos um intervalo claro para decidir os limiares de mínimo e máximo; 
# mesmo no nosso exemplo utilizamos pontos arbitrários, afinal existem pessoas com menos de meio metro 
# ou mais de 110Kg. 
# Na maioria das vezes utilizamos os máximos e mínimos da própria amostra. 
# Vamos ver outro exemplo, adicionamos novos pontos, que serão coloridos de preto


# NOVO DATASET
print("\n*****************************************************")
print("NOVO DATASET")
df2 = pd.DataFrame({'Altura':[1.6, 2.0, 1.6, 1.5, 1.6, 1.8, 1.7],'Peso':[50,50,52,50,55,65,63],'Cor':['b','r','g','k','k','k','k']})
print("\nNOVO DATASET:\n",df2)


#Plotando automáticamente, o plotter já ajusta as escalar para o gráfico ficar visualmente agradável
df2.plot.scatter('Altura','Peso',color=df2['Cor'])
plt.show()
input("DIGITE ALGO PARA CONTINUAR - PLOTANDO OS PONTOS (SEM ESCALA DEFINIDA) :")

#Plotando em escala
df2.plot.scatter('Altura','Peso',color=df2['Cor'],xlim=(0,70), ylim=(0,70))
plt.show()
input("DIGITE ALGO PARA CONTINUAR - PLOTANDO OS PONTOS (EM ESCALA) :")



# APLICANDO A NORMALIZAÇÃO
df2Norm = ( df2[ ['Altura','Peso'] ] - df2[ ['Altura','Peso'] ].min() ) / ( df2[ ['Altura','Peso'] ].max()-df2[ ['Altura','Peso'] ].min() )
df2Norm = pd.concat([df2Norm,df2['Cor']],axis=1)
df2Norm.plot.scatter('Altura','Peso',color=df2Norm['Cor'])
plt.show()
input("DIGITE ALGO PARA CONTINUAR - PLOTANDO OS PONTOS (NORMALIZADO1) :")

# Olhando com todos os pontos, o antes e depois
plt.figure(figsize=(12, 5))
G = gridspec.GridSpec(1, 2)

# Plotando antes de transformar os dados, eixos na mesma escala (9 pontos)
axOriginal = plt.subplot(G[0])
df2.plot.scatter('Altura','Peso', color=df2['Cor'],ylim=(48,67),xlim=(0,9), ax = axOriginal)
axOriginal.set_title('Dados Originais')

# Plotando depois da normalização
axNorm = plt.subplot(G[1])
df2Norm.plot.scatter('Altura','Peso', color=df2Norm['Cor'], ax = axNorm)
axNorm.set_title('Dados Normalizados')
plt.show()

input("DIGITE ALGO PARA CONTINUAR - PLOTANDO OS PONTOS (NORMALIZADO2) :")

# **Discussões e Reflexões:**
# 
# - Sempre que precisarmos medir distâncias, direta ou indiretamente, 
#   essa diferença em escala será relevante; devemos sempre pensar 
#   se nossa base de dados precisa ser normalizada
# - O que acontecerá caso uma nova amostra seja inserida nessa base? 
#   Se o novo ponto for maior que os outros, terá valores maiores do que 1, 
#   ainda assim a base segue normalizada; desde que as novas amostras sejam 
#   da mesma natureza das colhidas anteriormente
# - Mudamos a interpretação dos atributos ao normalizar, 
#   mas podemos reverter a base para seu estado original, 
#   desde que guardemos os máximos e mínimos utilizados para normalização, 
#   basta aplicar a função inversa à normalização; 
#   outra alternativa é usar o próprio dataframe original, 
#   com a informação obtida no normalizado
# 

# ### Usando distâncias para encontrar grupos e outliers
# ALTERANDO A VISUALIZAÇÃO DAS DISTÂNCIAS
df2['Cor']=['b','r','g','c','m', 'y', 'k']
df2Norm['Cor'] = ['b','r','g','c','m', 'y', 'k']
print("\nDADOS ORIGINAIS:\n",df2)

print("\n\nDADOS NORMALIZADOS:\n",df2Norm)
# Plotanto com cor única omitimos as cores deliberadamente
df2Norm.plot.scatter('Altura','Peso')
plt.show()

input("DIGITE ALGO PARA CONTINUAR - PLOTANDO OS PONTOS (NORMALIZADOS - COR ÚNICA) :")

# Utilizaremos um algoritmo chamado Single-Linkage. 
# Ele gera hierarquias de grupos de amostras usando as distâncias entre elas. 
# Vamos ver a hierarquia, irá facilitar o entendimento

plt.figure(figsize=(12, 5))
G = gridspec.GridSpec(1, 2)

#Plotando dados normalizados
axPontos = plt.subplot(G[0])
# Plot com cor única - omitindo as cores
df2Norm.plot.scatter('Altura','Peso', ax = axPontos)
axPontos.set_title('Dados como pontos')

#df2Norm.plot.scatter('Altura','Peso', color=df2Norm['Cor'],ax = axPontos) #Colorindo para verificar nossas conclusões

#Plotando hierarquia gerada pelo algoritmo
from scipy.cluster.hierarchy import dendrogram, linkage
Z = linkage(df2Norm[['Altura','Peso']], 'single', 'euclidean')

axHierarquia = plt.subplot(G[1])
dn = dendrogram(Z, labels=list(df2Norm['Cor']),ax=axHierarquia)
# INDICANDO AS LINHAS PONTILHADAS  [0.1325,0.2,0.2415,0.570,0.8]
axHierarquia.hlines([0.1325,0.2,0.2415,0.570,0.8],xmin=0,xmax=75, linestyles='dotted', colors=['orange','orange','green','blue','blue'])
axHierarquia.set_title('Dados na hierarquia')
axHierarquia.set_xlabel('Amostras')
axHierarquia.set_ylabel('Distância para união')

plt.show()

input("DIGITE ALGO PARA CONTINUAR - PLOTANDO DENDROGRAM (NORMALIZADOS) :")

# Utilizamos a distãncia euclidiana como havíamos antes para juntar pontos. 
# Notem que o pontos b(lue) e g(reen) se juntam em um nível/distância de aprox. 0.1325 (linha pontilhada laranja), 
# isso indica que a distância entre eles é de 0.1325; 
# logo depois vimos que c(yan), m(agenta) se unem com {b,g} num nível de 0.2 (linha pontilhada amarela superior), 
# o que indica que algum dos pontos c ou m, está a uma distância de 0.2 para b ou g

# Outra coisa que é notável é que r(ed) só se mistura com algum grupo no nível 0.8 (linha pontilhada azul superior), 
# indicando que precisa de tal distância para se juntar a **qualquer outra amostra**, 
# essa hierarquia nos permite ver outliers facilmente, sob uma ótima diferente da que vimos anteriormente

# Conseguimos ter uma ideia geral de qual ponto é qual? Usando essa hierarquia? 
# (descomentando a linha, podemos revelar as cores)<br>**#df2Norm.plot.scatter('Altura','Peso', color=df2Norm['Cor']) 
# Colorindo para verificar nossas conclusões)**



# #### SEM NORMALIZAR
# Sem normalizar essas distâncias estão todas distorcidas, 
# e é preciso uma mudança muito drástica na altura para compensar pequenas diferenças no peso

plt.figure(figsize=(12, 5))
G = gridspec.GridSpec(1, 2)

#Plotando dados originais
axPontos = plt.subplot(G[0])
df2.plot.scatter('Altura','Peso', ax = axPontos,xlim=(0,70),ylim=(0,70)) #omitindo cores
df2.plot.scatter('Altura','Peso', ax = axPontos,xlim=(0,70),ylim=(0,70), color=df2['Cor']) #mostrando as cores
axPontos.set_title('Dados como pontos')

#Plotando hierarquia gerada pelo algoritmo
from scipy.cluster.hierarchy import dendrogram, linkage
Z = linkage(df2[['Altura','Peso']], 'single', 'euclidean')

axHierarquia = plt.subplot(G[1])
dn = dendrogram(Z, labels=list(df2Norm['Cor']),ax=axHierarquia)
axHierarquia.hlines([2,0.1,3,0.400,8],xmin=0,xmax=75, linestyles='dotted', colors=['orange','blue','green','black','red'])
axHierarquia.set_title('Dados na hierarquia')
axHierarquia.set_xlabel('Amostras')
axHierarquia.set_ylabel('Distância para união')

plt.show()

input("DIGITE ALGO PARA CONTINUAR - PLOTANDO DENDROGRAM (NÃO NORMALIZADOS) :")

# **Discussões e reflexões**
# - A hierarquia nos permite verificar em 2 dimensões a distribuição geral das amostras
# - Normalizar é essencial quando temos diferenças muito grandes de escala, 
#   pois um atributo irá ter um impacto muito maior (mais significativo) que o outro no cálculo da distância
# - Notem a diferença na hierarquia ao não normalizar, o outlier r(ed) se tornou um ponto bem próximo aos outros
# - Com a hirarquia gerada, podemos notar se temos grupos de amostras?

# ************************************
# #### UTILIZANDO DADOS REAIS - IRIS
# Vamos ver como ficaria a base Iris (4D) usando esse mesmo algoritmo para visualização

print("\n********************************")
print("UTILIZANDO DADOS REAIS - IRIS")

irisdb = pd.read_csv("IrisColored.csv")

#irisdb
print("\nDADOS ITIRS - NÃO NORMALIZADOS\n:",irisdb)

# Ainda que as escalas na base de dados iris sejam similares entre os atributos, 
# vamos normalizar por garantia
irisdbNorm = irisdb.drop('Subespécie',axis=1)
irisdbNorm = (irisdbNorm - irisdbNorm.min())/(irisdbNorm.max() - irisdbNorm.min())
irisdbNorm = pd.concat([irisdbNorm, irisdb['Subespécie']],axis=1)

#irisdbNorm
print("\nDADOS ITIRS - NORMALIZADOS\n:",irisdbNorm)

input("DIGITE ALGO PARA CONTINUAR - DADOS IRIS :")


#Plotando hierarquia gerada pelo algoritmo
from scipy.cluster.hierarchy import dendrogram, linkage

# Base não normalizada
Z = linkage(irisdb.drop('Subespécie',axis=1), 'single', 'euclidean') 

plt.figure(figsize=(20, 5))
G = gridspec.GridSpec(1, 1)
ax = plt.subplot(G[0])

# Com rótulos, como as bases estão com índices na mesma ordem não é problema deixar irisdb['Subespécie'], 
# mesmo usando a normalizada, os valores serão idênticos
dn = dendrogram(Z, labels=list(irisdb['Subespécie']),ax=ax, leaf_font_size=12, leaf_rotation=0) 
ax.set_title('Dados na hierarquia')
ax.set_xlabel('Rótulo da amostra')
ax.set_ylabel('Distância para união')
#plt.savefig('Iris.png')
plt.show()

input("DIGITE ALGO PARA CONTINUAR - DENDROGRAM - DADOS IRIS NÃO NORMALIZADOS :")

# Base Normalizada
Z = linkage(irisdbNorm.drop('Subespécie',axis=1), 'single', 'euclidean') 

plt.figure(figsize=(20, 5))
G = gridspec.GridSpec(1, 1)
ax = plt.subplot(G[0])

dn = dendrogram(Z,ax=ax, leaf_font_size=6, leaf_rotation=60) #Sem rótulos
ax.set_title('Dados na hierarquia')
ax.set_xlabel('Rótulo da amostra')
ax.set_ylabel('Distância para união')
#plt.savefig('Iris.png')
plt.show()


input("DIGITE ALGO PARA CONTINUAR - DENDROGRAM - DADOS IRIS  NORMALIZADOS :")

# **Discussões e reflexões:**
# - Não conseguimos plotar a nuvem de pontos das 4 dimensões, 
#   mas pela hierarquia conseguimos ter uma noção geral da distribuição das amostras, 
#   mesmo sem poder visualizar no espaço original
# - Ainda nesse curso, aprenderemos um método de projeção para permitir projetar muitas dimensões 
#   em um espaço de 2 ou 3 dimensões que seja similar ao original; perderemos um pouco de informação, 
#   mas vai nos ajudar a visualizar também




