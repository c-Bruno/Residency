import statistics
import math
from scipy import stats
import numpy
from collections import Counter

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv

path = "C:\\Users\\bcaboclo\\Downloads\\DATASETEXEMPLO001B.csv"
with open(path,'r',newline='') as ARQUIVO:
# Efetuar a leitura dos dados no arquivo
    d = csv.reader(ARQUIVO)
    dados = list(d)
    # print(dados)

    print("LEITURA DOS DADOS DO ARQUIVO - EFETUADO")
    idade = []
    altura = []
    peso = []
    estado_civil = []
    escolaridade = []

    for i in dados:
        idade.append(float(i[0]))
        altura.append(float(i[1]))
        peso.append(float(i[2]))
        estado_civil.append(i[3])
        escolaridade.append(i[4])
    
    auxDF=[]
    auxDF+=[(idade[j],altura[j],peso[j],estado_civil[j],escolaridade[j]) for j in range(0,len(dados))]
    DFdados = pd.DataFrame(auxDF, columns=['IDADE','ALTURA','PESO','ESTADO_CIVIL','ESCOLARIDADE'])
    # print(DFdados)

    #  Media
    VMidade = DFdados["IDADE"].mean()
    print("\nIDADE MÉDIA = ", VMidade, "ANOS")

    # MEDIANA
    VMDidade = DFdados["IDADE"].median()
    print("MEDIANA = ", VMDidade, "ANOS")

    # MODA
    VMODAidade = DFdados["IDADE"].mode()
    print("\nMODA = ", VMODAidade)

    VMODAidade = DFdados["PESO"].mode()
    print("\nMODA = ", VMODAidade)

    # VALOR MAXIMO
    MAXidade = max(DFdados["IDADE"])
    print("IDADE MAXIMA = ", MAXidade)
   
    # VALOR MINIMO
    MINidade = min(DFdados["IDADE"])
    print("IDADE MINIMA = ", MINidade)

    # AMPLITUDE
    AMPidade = MAXidade - MINidade
    print("IDADE MINIMA = ", AMPidade)

    # VARIANCIA
    VARidade = DFdados["IDADE"].var()
    print("\nVARIANCIA = ", VARidade)

    # DESVIO PADRÃO
    DVPidade = DFdados["IDADE"].std()
    print("DESVIO PADRAO = ", DVPidade)

    #  HISTOGRAMA
    hist = np.histogram(DFdados["IDADE"])
    print("HISTOGRAMA: ", hist)
    #  Plotar dados
    plt.hist(DFdados["IDADE"], bins='auto')
    plt.title("HISTOGRAMA - IDADE")
    plt.xlabel("FAIXA")
    plt.ylabel("OCORRENCIAS")
    plt.show()
    
    # CALCULAR A CORRELAÇÃO
    correlacao = DFdados.corr(method='pearson')
    print("\n\n",correlacao)
    