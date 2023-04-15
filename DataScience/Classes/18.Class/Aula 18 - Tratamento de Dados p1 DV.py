#!/usr/bin/env python
# coding: utf-8

# ## Tratamento de Dados

# Created on Fri Apr 12 11:07:43 2023

# @author: AM

# #### Importando bibliotecas úteis

import pandas as pd
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


# ### Dados Problemáticos
# Para resolver esses problemas, notamos ter 2 soluções principais:
# - Remover dados/amostras
# - Imputar valores

# ### Removendo Valores
# Utilizaremos técnicas estatísticas para identificar valores anormais (i.e. raros ou errados); 
# esses dados poderão ser removidos ou selecionados para correção (veremos imputação mais adiante)

# #### IQR (interquartil-range)

# Podemos usar as medidas de dispersão e distribuição para avaliar e encontrar amostras 
# que estão muito distantes do esperado. Uma dar formas é o intervalo interquartil
# <br>$IQR = (Q3 - Q1)$
# <br>
# O interquartil separa metade dos dados que estão na parte central, i.e. de 25% à 75%. 
# Podemos pensar que valores que se afastam em uma proporção dessa amplitude são raros ou ruído

# LEITURA DO DATASET
# valores ? indicam valores faltantes na nossa base
vendas = pd.read_csv("vendasRuido.csv", header=None) 
vendas.columns=['hora','prod1','prod2']
print("\n VENDAS: \n",vendas)
vendas[['prod1','prod2']].describe()

plt.plot(vendas["prod1"],color="green") 
plt.title("tempo x prod1")
plt.xlabel("tempo [H]")
plt.ylabel("VENDAS")     
plt.show()


plt.plot(vendas["prod2"],color="green") 
plt.title("tempo x prod2")
plt.xlabel("tempo [H]")
plt.ylabel("VENDAS")     
plt.show()

input ("DIGITE ALGO PARA CONTINUAR: ")


# Por exemplo, vemos que para o produto 1, temos entre 10 e 80 vendas por hora; 
# mas em 50% das horas amostradas, temos entre 22 e 28 vendas. 
# É intuitivo pensar que se na metade das horas as vendas oscilam em 6 pontos (nosso IQR), 
# valores que se distanciem em 6 pontos do Q1 e do Q3 sejam bem mais raros. 
# Em aplicações reais tendemos a ser ainda mais permissivos na nossa margem, 
# **multiplicamos o IQR por 1.5** e adicionamos ou subtraímos de Q3 e Q1 (respectivamente) 
# para definir a nossa região de dados 'comuns'. 
# Esse valor é tão usado que é pradrão em um plot estatístico, o **boxplot**

vendas.boxplot()
plt.show()

input ("DIGITE ALGO PARA CONTINUAR BOX PLOT: ")

# O DESVIO PADRÃO E A VARIÂNCIA DEPENDEM FORTEMENTE DO VALOR DA MÉDIA, 
# QUE SÃO INFLUENCIADOS POR VALORES DISCREPANTES. 
# UMA SOLUÇÃO É UTILIZAR A MEDIANA PARA CONTORNAR O PROBLEMA 
# Calculando IQR (INTERVALO ENTRE QUARTIS) e margem 'válida'
IQR = vendas[['prod1','prod2']].quantile(0.75) - vendas[['prod1','prod2']].quantile(0.25)
margemMin = vendas[['prod1','prod2']].quantile(0.25) - IQR*1.5
margemMax = vendas[['prod1','prod2']].quantile(0.75) + IQR*1.5

# Filtrando valores anormais/outliers de acordo com IQR
idx=[]
for col in ['prod1','prod2']:
    filtered = vendas[col][(vendas[col] < margemMin[col]) | (vendas[col] > margemMax[col])]
    idx.extend(filtered.index)
vendas.iloc[idx]

# vendas.info() #nossa base original possui 216 amostras
# dessas 216, 11 possuem algum tipo de anormalidade ~ 5%
vendas.iloc[idx].info() 


# #### Alta distância para a média em termos de desvios padrões
# Ainda sob essa perspectiva de usar alguma medida de amplitude para medir valores anormais. 
# Podemos utilizar o desvio padrão. 
# Sabemos que em amostras simétricas temos 68% das amostras dentro de 1 desvio padrão da média, 
# e quando aumentamos essa margem para 3 desvios padrões temos cerca de 99.7%. 
# Iremos filtrar fora todas as amostras que estão a 3 desvios padrões da média, 
# para mais ou para menos


#Calculando IQR e margem 'válida'
deviation = vendas[['prod1','prod2']].std()
margemMin = vendas[['prod1','prod2']].mean() - 3*deviation
margemMax = vendas[['prod1','prod2']].mean() + 3*deviation

#Filtrando valores anormais/outliers
idx=[]
for col in ['prod1','prod2']:
    filtered = vendas[col][(vendas[col] < margemMin[col]) | (vendas[col] > margemMax[col])]
    idx.extend(filtered.index)
vendas.iloc[idx]

# vendas.info() #nossa base original possui 216 amostras
#dessas 216, 8 estão muito fora da média ~ 3,7%
vendas.iloc[idx].info() 


# **Dicussões e reflexões:**
# - Notamos que cada abordagem se comporta de uma maneira diferente. 
# - A IQR se preocupa com a amplitude, independente de assimetria ou desvio padrão; 
#   enquanto que a baseada em 3 desvios padrões tem uma interpretação muito boa 
#   para distribuições normais.
# - Sempre serão usados esse limiares (i.e. 3 desvios e 1.5 vezes o IQR)?

print("\n***************************************")
print("\nIMPUTANDO VALORES:")
# ### Imputando valores
# Podemos imputar valores tanto para corrigir valores anômalos, 
# quanto para imputar valores que não estavam presentes na base original

#valores ? indicam valores faltantes na nossa base
vendas = pd.read_csv("vendasMissing.csv", header=None, na_values='?') 
vendas.columns=['hora','prod1','prod2']

#Pandas marcou valores faltantes como NaN, especificamente pd.NA
print("\nDADOS FALTANDO: ")
print(vendas[12:36]) 


# Encontrando os índices onde tempos valores faltantes
indiceFaltandoValor=vendas[vendas['prod1'].isnull() | vendas['prod2'].isnull()].index 
print("\nINDICES COM VALORES FALTANDO:\n",indiceFaltandoValor)


# Como temos uma série, é plausível assumir que o valor não irá mudar muito 
# em relação à valores próximos; vimos que uma abordagem possível é imputar a **média** 
# dos valores anterior e posterior

# Mas e se não tivermos uma sequência de amostras, em cenários onde cada amostra 
# representa algo indepentente, e.g. população, Iris, não é viável escolher a amostra anterior 
# e posterior, muitas vezes não haverá relação direta entre amostras em sequência

input("DIGITE ALGO  FALORES FALTANDO - COMO TRATAR ? :")

# Dito isso, podemos usar a população de amostras a nosso favor
# Entendendo nossos dados e imputando valores centrais
#valores ? indicam valores faltantes na nossa base
print("\n\nLENDO O ARQUIVO:  pessoasMissing.csv")
pessoas = pd.read_csv('pessoasMissing.csv',na_values='?') 
print("DADOS:\n",pessoas)

# PLOTANDO GRÁFICOS
plt.plot(pessoas["alt"],c='g')
plt.title("DATASET ALTURA")
plt.ylabel("ALTURA")
plt.xlabel("AMOSTRA")
plt.show()

plt.plot(pessoas["peso"],c='b')
plt.title("DATASET PESO")
plt.ylabel("PESO")
plt.xlabel("AMOSTRA")
plt.show()

# PLOTANDO O HISTOGRAMA DAS DUAS VARIÁVEIS
pessoas.hist()
plt.show()


input("DIGITE ALGO    OBSERVE QUE ESTÃO FALTANDO DADOS: ")

# Outra forma de ver eventuais caldas,
# uma vez que já notamos que temos apenas um 'pico'
print("\n\nDADOS ESTATÍSTICOS:")
print(pessoas.describe())
print("\nOBSERVE OS VALORES DE MÉDIA E MEDIANA:")
print(pessoas.describe().loc[['mean','50%']])
  
input("DIGITE ALGO    OBSERVE VALORES DE MEDIA E MEDIANA: ")

# Nossa base de dados é bem simétrica, 
# podemos substituir os valores faltantes pela média da coluna, 
# sem muito risco de imputar um valor extraordinário
pessoasCompleto = pessoas.fillna(pessoas.mean())
print("DATASET COMPLETO SUBSTITUINDO OS VALORES FALTANDO PELA MÉDIA:\n",pessoasCompleto)

input("DIGITE ALGO   DATASET COMPLETO SUBSTITUINDO OS VALORES FALTANDO PELA MÉDIA:")
# PLOTANDO GRÁFICOS
plt.plot(pessoasCompleto["alt"],c='g')
plt.title("DATASET ALTURA DADOS COMPLETOS - SUBSTITUIDOS POR MEDIA")
plt.ylabel("ALTURA")
plt.xlabel("AMOSTRA")
plt.show()

plt.plot(pessoasCompleto["peso"],c='b')
plt.title("DATASET PESO   DADOS COMPLETOS - SUBSTITUIDOS POR MEDIA")
plt.ylabel("PESO")
plt.xlabel("AMOSTRA")
plt.show()

# PLOTANDO O HISTOGRAMA DAS DUAS VARIÁVEIS
pessoasCompleto.hist()
plt.show()

print("\n\nDADOS ESTATÍSTICOS - COMPLETO:")
print(pessoasCompleto.describe())
print("\nOBSERVE OS VALORES DE MÉDIA E MEDIANA DATASET COMPLETO:")
print(pessoasCompleto.describe().loc[['mean','50%']])

input("DIGITE ALGO    COMPARE OS GRAFICOS e ESTATÍSTICA: ")

print("\n\n*******************************")
print("\nSITUAÇÃO DIFERENTE: ")
print("\nEFETUANDO A LEITURA DO ARQUIVO: pessoas2Missing.csv  ")
# Mas podemos ter situações diferentes
pessoas2 = pd.read_csv('pessoas2Missing.csv', na_values='?')
pessoas2.head(10)

# PLOTANDO GRÁFICOS
plt.plot(pessoas2["alt"],c='g')
plt.title("DATASET ALTURA DADOS INCOMPLETOS-pessoas2")
plt.ylabel("ALTURA")
plt.xlabel("AMOSTRA")
plt.show()

plt.plot(pessoas2["peso"],c='b')
plt.title("DATASET PESO   DADOS INCOMPLETOS-pessoas2")
plt.ylabel("PESO")
plt.xlabel("AMOSTRA")
plt.show()

# PLOTANDO O HISTOGRAMA DAS DUAS VARIÁVEIS
pessoas2.hist()
plt.show()

input("DIGITE ALGO    OBSERVE OS GRAFICOS-pessoas2: ")

#a média ainda é próxima da mediana, indicando uma pequena calda ou simetria,
#mas notem que ambas são péssimas medidas de centralidade das amostras nesse caso
print("\n\nDADOS ESTATÍSTICOS-pessoas2:")
print(pessoas2.describe())
print("\nOBSERVE OS VALORES DE MÉDIA E MEDIANA-pessoas2:")
print(pessoas2.describe().loc[['mean','50%']])

input("DIGITE ALGO    OBSERVE VALORES DE MEDIA E MEDIANA-pessoas2: ")

# Não temos mais algo simétrico, com um centro bem definido; 
# imputaremos o peso como 70, ou como 20? 
# A média de 50 não possui nenhuma evidência...
# A solução é imputar valores diferentes para amostras diferentes

# Para o PESO notamos dois grupos óbvios, com mais ou menos de 50Kg, 
# poderíamos usar essa separação para imputar na média ou mediana

# SEPARANDO AS DUAS PARTES
# sabemos que não há peso igual a 50, é um limiar bem amplo
pessoas2_50mais = pessoas2[pessoas2['peso'] > 50] 
# sabemos que não há peso igual a 50, é um limiar bem amplo
pessoas2_50menos = pessoas2[pessoas2['peso'] < 50] 

pessoas2_50mais.hist()
pessoas2_50menos.hist()

input("DIGITE ALGO    HISTOGRAMA RECORTE <50 e >50 -pessoas2: ")

# SEPARANDO AS CALDAS
aux=pessoas2[pessoas2['peso'] > 50]['peso'].fillna(pessoas2[pessoas2['peso'] > 50]['peso'].mean())
pessoas2_50maisCompleto=pd.DataFrame( aux,columns=['peso'])

aux=pessoas2[pessoas2['peso'] < 50]['peso'].fillna(pessoas2[pessoas2['peso'] < 50]['peso'].mean())
pessoas2_50menosCompleto=pd.DataFrame( aux ,columns=['peso'])

pessoas2Completo = pd.concat([pessoas2_50maisCompleto,pessoas2_50menosCompleto],axis=0)
pessoas2Completo['peso'].hist()

input("DIGITE ALGO    HISTOGRAMA COMPLETO <50 e >50 - pessoas2: ")

pessoas2['peso'].hist()
pessoas2.hist()
input("DIGITE ALGO    HISTOGRAMA - pessoas2 ORIGINAL: ")


# Comparando os 2 histogramas (antes e depois da imputação) não vemos grandes alterações no formato, 
# isso é um bom sinal

# Quanto à altura não conseguimos encontrar um corte evidente, 
# precisamos de uma forma mais objetiva para imputar valores; 
# será que podemos utilizar a decrição nas outras variáveis para imputar valores? 
# e.g. amostras com pesos parecidos devem ter alturas parecidas; 
# veremos o conceito de imputação por vizinhança



print("\n\n*****************************************")
print("IMPUTANDO PELA VIZINHANÇA")
# #### Imputando por vizinhança
# Quando imputamos por vizinhança, nossa suposição é que amostras similares 
# têm características similares
# Caso nossa base seja rotulada, definir essas vizinhanças pode ser bem simples

pessoas2b = pd.read_csv('pessoas2bMissing.csv', na_values='?')
print("\nDATASET pesoas2Missing.csv\n",pessoas2b)
print("\nESTATÍSTICAS DATASET TOTAL:\n",pessoas2b.describe())
print("\nESTATÍSTICAS DATASET ADULTO:\n",pessoas2b[pessoas2b['Faixa Etária']=='Adulto'].describe())
print("\nESTATÍSTICAS DATASET CRIANÇA:\n",pessoas2b[pessoas2b['Faixa Etária']=='Criança'].describe())
input("DIGITE ALGO    DATASET - pessoas2Missing ORIGINAL: ")

# Nesse caso sabemos que a base possui adultos e crianças, 
# o que justifica a mudança súbita em peso e a distribuição anormal de altura
# SEPARANDO CRIANÇAS
Criancas=pessoas2b[pessoas2b['Faixa Etária']=='Criança'][['alt','peso','Faixa Etária']]
print("\nCRIANÇAS:\n",Criancas)
pessoas2b[pessoas2b['Faixa Etária']=='Criança'][['alt','peso']].hist()

input("DIGITE ALGO    HISTOGRAMA - pessoas2Missing CRIANÇAS: ")


# SEPARANDO ADULTOS
Adultos=pessoas2b[pessoas2b['Faixa Etária']=='Adulto'][['alt','peso','Faixa Etária']]
print("\nADULTOS:\n",Adultos)
pessoas2b[pessoas2b['Faixa Etária']=='Adulto'][['alt','peso']].hist()

input("DIGITE ALGO    HISTOGRAMA - pessoas2Missing ADULTOS: ")

# SEPARANDO CRIANÇAS
Criancas=pessoas2b[pessoas2b['Faixa Etária']=='Crianças'][['alt','peso','Faixa Etária']]
print("\nADULTOS:\n",Criancas)
pessoas2b[pessoas2b['Faixa Etária']=='Crianças'][['alt','peso']].hist()

input("DIGITE ALGO    HISTOGRAMA - pessoas2Missing CRIANÇAS: ")

# Vemos que podemos imputar a média da classe ao invés da média global
print("IMPUTANDO A média NOS PONTOS FALTANTES .....")
pessoas2bAdultosM = pessoas2b[pessoas2b['Faixa Etária']=='Adulto'][['alt','peso']].mean()
pessoas2bCriancaM = pessoas2b[pessoas2b['Faixa Etária']=='Criança'][['alt','peso']].mean()
pessoas2bCompleto = pessoas2b.copy()
pessoas2bCompleto[pessoas2bCompleto['Faixa Etária']=='Adulto'] = pessoas2bCompleto[pessoas2bCompleto['Faixa Etária']=='Adulto'].fillna(pessoas2bAdultosM)
pessoas2bCompleto[pessoas2bCompleto['Faixa Etária']=='Criança'] = pessoas2bCompleto[pessoas2bCompleto['Faixa Etária']=='Criança'].fillna(pessoas2bCriancaM)
#O for abaixo faz o mesmo procedimento acima
# pessoas2bCompleto = pessoas2b.copy()
# for fe in ['Adulto','Criança']:
#     media = pessoas2bAdultosM = pessoas2b[pessoas2b['Faixa Etária']==fe][['alt','peso']].mean()
#     pessoas2bCompleto[pessoas2bCompleto['Faixa Etária']==fe] = pessoas2bCompleto[pessoas2bCompleto['Faixa Etária']==fe].fillna(media)
print("HISTOGRAMS APÓS SUBSTITUIÇÃO POR média:")
pessoas2bCompleto.hist()
pessoas2bCompleto[pessoas2b['Faixa Etária']=='Adulto'].hist()
pessoas2bCompleto[pessoas2b['Faixa Etária']=='Criança'].hist()

input("DIGITE ALGO    HISTOGRAMA - pessoas2Missing GERAL ADULTOS CRIANÇAS: ")



print("\n\nAPLICANDO IMPUTAÇÃO PARA DATASETs SEM ATRIBUTOS:")
# Caso não tenhamos as classes, ainda assim podemos utilizar o(s) atributo(s) 
# disponíveis para medir essas distâncias
# Faremos um exemplo simples em uma base com apenas 2 atributos
pessoas2 = pd.read_csv('pessoas2Missing.csv', na_values='?')
print("DATASET pessoas2Missing.csv :\n",pessoas2.head(15))

# Encontrando valores faltantes
Faltantes=pessoas2[(pd.isna(pessoas2['alt'])) | (pd.isna(pessoas2['peso'])) ]
print("\nAMOSTRAS FALTANTES: \n",Faltantes)
amostrasFaltantes = pessoas2[(pd.isna(pessoas2['alt'])) | (pd.isna(pessoas2['peso'])) ].index
# AmostrasFaltantes
print("\nOUTRA FORMA - AMOSTRAS FALTANTES: \n",pessoas2.iloc[amostrasFaltantes])

input("DIGITE ALGO    AMOSTRAS FALTANTES - pessoas2Missing: ")

# Vamos encontrar as amostras vizinhas da amostra 7. 
# Não podemos usar a informação da altura, já que ela é indefinida para a amostra 7. 
# Iremos ver a disposição das amostras em relação ao peso 
# e vamos tentar encontrar as amostras mais parecidas/próximas da amostra 7 (em vermelho)
print("\nPLOTANDO O GRÁFICO PARA VERIFICAR O PONTO MAIS PRÓXIMO DA POSIÇÃO 7.")
print("PESSOAS2:\n",pessoas2)
#usaremos a cor azul para todos exceto o 7 (vermelho)
cores=['b' if x != 7 else 'r' for x in pessoas2.index] 
pessoas2.plot.scatter('peso','peso', color=cores)
plt.show()
#usaremos a cor azul para todos exceto o 7 (vermelho)
cores=['b' if x != 8 else 'r' for x in pessoas2.index] 
pessoas2.plot.scatter('alt','alt', color=cores)
plt.show()

input("DIGITE ALGO    PLOT AMOSTRAS FALTANTES - pessoas2Missing: ")

print("******************************************************")
print("\n\nCÁLCULO DA DISTÂNCIA A PARTIR DE UM CONJUNTO DE VALORES\n")
#CÁLCULO DA DISTÂNCIA A PARTIR DE UM CONJUNTO DE VALORES
from scipy.spatial.distance import pdist
from scipy.spatial.distance import squareform
#  pdist(X[, métrica, fora])  Distâncias pareadas entre observações no espaço n-dimensional.
Y = pdist([[x] for x in pessoas2['peso'].values], 'euclidean')
dist_matrix = squareform(Y)
print("\nMATRIZ DIST:\n",dist_matrix)
# TRANSFORMAR A METRIZ EM DATAFRAME
dm = pd.DataFrame(dist_matrix)
# PEGAR A MATRIZ NO PONTO 7
p7=dm[7].sort_values()
print("\nMATRIZ NO PONTO 7:\n",p7)
#dm[7].sort_values().index[1]
#pessoas2.iloc[1]['peso']

input("DIGITE ALGO    CÁLCULO DISTÂNCIA: ")

# Calcularemos a média da ALTURA dos vizinhos de 7 e imputaremos como a altura dele
# mude essa variável para usar a vizinhança, o gráfico e o valor imputado 
# serão alterados de acordo

qtdVizinhos = 5 
alt = 0
vizinhos=[]
print("\nPESSOAS2 - ORIGINAL:\n",pessoas2)
for i in range(1,qtdVizinhos+1):
    # SEPARAR INDEX DO VIZINHO
    idxVizinho = dm[7].sort_values().index[i]
    # SALVAR VIZINHO
    vizinhos.append(idxVizinho)
    # ALTURA DO VIZINHO
    altVizinho = pessoas2.iloc[idxVizinho]['alt']
    print("VIZINHO: ",idxVizinho,"   ALTURA: ",altVizinho)
    # SOMAR AS ALTURA
    alt = alt+altVizinho
# MÉDIA DA ALTURA DOS VIZINHOS    
alt = alt/qtdVizinhos
print("\nMÉDIA DOS ",qtdVizinhos,"VIZINHOS = ",alt)

# ALTERANDO O VALOR DA ALTURA PARA A POSIÇÃO 7 DA ALTURA
pessoas2.loc[7]['alt'] = alt

print("\nPESSOAS2 - CORRIGIDA A POSIÇÃO 7:\n",pessoas2)

input("DIGITE ALGO    SUBSTITUIÇÃO DO VALOR DA DISTÂNCIA NO PONTO 7: ")

# VISUALIZANDO OS PONTOS NO GRÁFICO
# MONTAGEM DAS CORES
cores=[]
for idx in pessoas2.index:
    if idx == 7: 
        #alvo cor=amarelo
        cores.append('y')
         #vizinhos cor=preto
    elif vizinhos.__contains__(idx): 
        cores.append('k')
    else: #outros cor=azul
        cores.append('b') 
        
pessoas2.plot.scatter('alt','peso', color=cores)
plt.show()

input("DIGITE ALGO    VISUALIZAÇÃO DOS VIZINHOS NO PONTO 7: ")



# Rodando com apenas 2 vizinhos notamos algo inusitado
# Calcularemos a média da ALTURA dos vizinhos de 7 e 
# imputaremos como a altura dele
qtdVizinhos = 2  

alt = 0
vizinhos=[]
for i in range(1,qtdVizinhos+1):
    idxVizinho = dm[7].sort_values().index[i]
    vizinhos.append(idxVizinho)
    altVizinho = pessoas2.iloc[idxVizinho]['alt']
    print(altVizinho)
    alt = alt+altVizinho
alt = alt/qtdVizinhos
pessoas2.loc[7]['alt'] = alt

#Visualizando
cores=[]
for idx in pessoas2.index:
    if idx == 7: 
        #alvo cor=amarelo
        cores.append('y')
    elif vizinhos.__contains__(idx): 
        #vizinhos cor=preto
        cores.append('k')
    else: 
        #outros cor=azul
        cores.append('b') 
        
pessoas2.plot.scatter('alt','peso', color=cores)
plt.title("DATASET CORREÇÃO DO PONTO 7 - SEM ESCALA")
plt.ylabel("VALORES")
plt.show()

input("DIGITE ALGO    VISUALIZAÇÃO DOS 2 VIZINHOS NO PONTO 7: ")


# O ponto azul (1.5,70) parece mais próximo que o vizinho da esquerda (1.45,75). 
# Por que isso acontece? O nosso gráfico está distorcido a altura varia entre 0.8 e 2.2 
# enquanto que o peso varia entre 10 e 90. Um gráfico em escala seria:
pessoas2.plot.scatter('alt','peso', color=cores,xlim=(0,90),ylim=(0,90))
plt.title("DATASET CORREÇÃO DO PONTO 7 - COM ESCALA")
plt.ylabel("VALORES")
plt.show()


# Agora fica evidente que a distância na vertical (cerca de 8 pontos/kg) 
# era maior que na horizontal (cerca de 0.2 pontos/m)
# Alguns algoritmos e abordagens serão sensíveis a essa diferença de escala, 
# iremos aprender a corrigir isso na próxima aula!

# **Discussões:**
# - Podemos utilizar o conceito de agrupamento visto na aula anterior 
#   para medir essas similaridades?
# - Medimos distâncias para encontrar os vizinhos das nossas amostras, 
#   o processo seria o mesmo caso tivéssemos mais atributos?

# **Preocupações:**
# - Os dados imputados não são um chute, devem ser uma aproximação do valor esperado
# - Elas devem alterar a distribuição dos dados o mínimo possível, evitando 'novidades'
# - Dados imputados têm menos embasamento na realidade, afinal os dados originais 
#   foram coletados do 'mundo real', são evidência; 
#   já os dados imputados foram colocados artificialmente; 
#   dito isso, ambos serão tratados da mesma forma pelos nossos algoritmos.

