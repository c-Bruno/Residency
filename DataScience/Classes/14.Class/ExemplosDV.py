# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 19:42:39 2023

@author: AM
"""


import statistics
import math
from scipy import stats
from collections import Counter
import os

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv
import scipy.stats as stats


print("***********************************************")
print("EFETUANDO A LEITURA DOS DADOS DO ARQUIVO PADRAO")

# LOCAL DE ARMAZENAMENTO DO ARQUIVO
currentDirectory = os.path.dirname(os.path.abspath(__file__)) # Define o diretorio atual como o diretorio do arquivo
fileName = os.path.join(currentDirectory, 'vendas.txt') # Partindo do diretorio, procuramos pelo nome do arquivo
with open(fileName,'r',newline='') as ARQUIVO:
 # Efetuar a leitura dos dados no arquivo
 d = csv.reader(ARQUIVO)
 dados=list(d)
 print("LEITURA DOS DADOS DO ARQUIVO - EFETUADO\n")
 
 # CAMPOS 
 hora=[]
 geladeira=[]
 fogao=[]
 microondas=[]
 airfryer=[]
 lavaroupas=[]
 lavaloucas=[]
 pagamentovista=[]
 pagamentoprazocartao=[]
 pagamentoprazofinanciado=[]
 
 # SEPARANDO OS DADOS
 for i in dados:
    hora.append(int(i[0]))
    geladeira.append(int(i[1]))
    fogao.append(int(i[2]))
    microondas.append(int(i[3]))
    airfryer.append(int(i[4]))
    lavaroupas.append(int(i[5]))
    lavaloucas.append(int(i[6]))
    pagamentovista.append(int(i[7]))
    pagamentoprazocartao.append(int(i[8]))
    pagamentoprazofinanciado.append(int(i[9]))
     

 TOTALVENDASDIA=[]
 DIA=[]
 for i in range(0,int(len(hora)/24)):
     soma=0
     for j in range(i*24,(i+1)*24):
        soma+=pagamentovista[j]+pagamentoprazocartao[j]+pagamentoprazofinanciado[j]
     TOTALVENDASDIA.append(int(soma))
     DIA.append(i)
     
 plt.plot(DIA,TOTALVENDASDIA,'b')
 plt.title("TOTAL DE VENDAS POR DIA")
 plt.xlabel("DIAS")
 plt.ylabel("VENDAS")
 plt.show()

 # DATA FRAME COM DADOS DE DIA E TOTAL DE VENDAS 
 auxDF=[]  
 auxDF+=[(DIA[j],TOTALVENDASDIA[j]) for j in range(0,len(DIA))]  
 DFdados = pd.DataFrame(auxDF, columns=["DIA","TOTALVENDASDIA"])
  
 # https://scikit-learn.org/stable/
 from sklearn import linear_model
 from sklearn.metrics import r2_score
 # CALCULANDO A REGRESSÃO - TOTAL DE VENDAS
 # "regressao" OBJETO PARA Regressao Linear
 regressao=linear_model.LinearRegression()

 # SEPARANDO OS CAMPOS
 ValorDia=np.array(DFdados[["DIA"]])
 TotalVendas=np.array(DFdados[["TOTALVENDASDIA"]])

 regressao.fit(ValorDia,TotalVendas)

 # PRINT PARAMETROS DA REGRESSAO LINEAR
 print("\n*********************************************")
 print("***** AVALIAÇÃO DO PERFIL DA CURVA DE VENDAS")
 print("Coeficiente de Regressão =",regressao.coef_)
 print("Interceptação = ",regressao.intercept_)
 
 # BI - Business Intelligence - UTILIZANDO 
 if (regressao.coef_>0):
     print("BI - VENDAS EM CRESCIMENTO")
 elif regressao.coef_==0:
     print("BI - VENDAS ESTAVEIS")
 else:
     print("BI - VENDAS EM QUEDA")

 input("DIGITE ALGO: " )
 
 
 TOTALVENDASDIAGELADEIRA=[]
 DIA=[]
 for i in range(0,int(len(hora)/24)-1):
     soma=0
     for j in range(i*24,(i+1)*24):
        soma+=geladeira[j]
     TOTALVENDASDIAGELADEIRA.append(int(soma))
     DIA.append(i)

 # ORGANIZANDO UM DATAFAME DIA - GELADEIRA   
 auxDF2=[]  
 auxDF2+=[(DIA[j],TOTALVENDASDIAGELADEIRA[j]) for j in range(0,len(TOTALVENDASDIAGELADEIRA))]  
 DFdados2 = pd.DataFrame(auxDF2, columns=["DIA","GELADEIRA"])

 print("\n\nDADOS ESTATÍSTICOS - VENDAS DIÁRIAS DE GELADEIRAS:")
 # VALOR MEDIO
 VMgeladeira=DFdados2["GELADEIRA"].mean()
 print("VENDA DIARIA DE GELADEIRA - VALOR MEDIO = ",VMgeladeira)
 # VALOR MEDIO NumPy
 AVRGgeladeira=np.average(DFdados2["GELADEIRA"])
 print("VENDA DIARIA DE GELADEIRA - VALOR MEDIO NumPy = ",AVRGgeladeira)
 # MEDIANA
 VMDgeladeira=DFdados2["GELADEIRA"].median()
 print("VENDA DIARIA DE GELADEIRA - VALOR MEDIANA = ",VMDgeladeira)
 # MODA
 VMODAgeladeira=DFdados2["GELADEIRA"].mode()
 print("VENDA DIARIA DE GELADEIRA - VALOR MODA = \n",VMODAgeladeira)
 # VALOR MAXIMO
 MAXgeladeira=max(DFdados2["GELADEIRA"])
 print("VENDA DIARIA DE GELADEIRA - VALOR MÁXIMO =",MAXgeladeira)
 # VALOR MINIMO
 MINgeladeira=min(DFdados2["GELADEIRA"])
 print("VENDA DIARIA DE GELADEIRA - VALOR MÍNIMO =",MINgeladeira)
 # AMPLITUDE
 AMPgeladeira=MAXgeladeira-MINgeladeira
 print("VENDA DIARIA DE GELADEIRA - VALOR AMPLITUDE =",AMPgeladeira)

 plt.plot(TOTALVENDASDIAGELADEIRA,'g')
 plt.title("TOTAL DE VENDAS POR DIA - GELADEIRAS")
 plt.xlabel("DIAS")
 plt.ylabel("VENDAS")
 plt.show()
  
 regressao=linear_model.LinearRegression()

 # SEPARANDO OS CAMPOS
 ValorDia=np.array(DFdados2[["DIA"]])
 TotalVendas=np.array(DFdados2[["GELADEIRA"]])

 regressao.fit(ValorDia,TotalVendas)

 # PRINT PARAMETROS DA REGRESSAO LINEAR
 print("\n*********************************************")
 print("***** AVALIAÇÃO DO PERFIL DA CURVA DE VENDAS")
 print("Coeficiente de Regressão =",regressao.coef_)
 print("Interceptação = ",regressao.intercept_)
 
 # BI - Business Intelligence - UTILIZANDO 
 if (regressao.coef_>0):
     print("BI - VENDAS DE GELADEIRAS EM CRESCIMENTO")
 elif regressao.coef_==0:
     print("BI - VENDAS DE GELADEIRAS ESTAVEIS")
 else:
     print("BI - VENDAS DE GELADEIRAS EM QUEDA")

 input("DIGITE ALGO: " )


 # ORGANIZANDO UM DATAFAME COM OS DADOS DISPONIBILIZADOS NO ARQUIVO   
 auxDF=[]  
 auxDF+=[(hora[j],geladeira[j],fogao[j],microondas[j],airfryer[j],lavaroupas[j],
          lavaloucas[j],pagamentovista[j],pagamentoprazocartao[j],pagamentoprazofinanciado[j]) for j in range(0,len(dados))]  
 DFdados = pd.DataFrame(auxDF, columns=["HORA","GELADEIRA","FOGAO","MICROONDAS",
                                        "AIRFRYER","LAVAROUPAS","LAVALOUCAS","PAGAMENTOVISTA","PAGAMENTOPRAZOCARTAO","PAGAMENTOPRAZOFINANCIDO"])
 
 # FERRAMENTA GERAL
 print("\nDADOS ESTATISTICOS BÁSICOS - TEMPORAL - POR HORA: ")
 print("NUMERO DE AMOSTRAS/CAMPOS: ",DFdados.shape)
 print("DADOS ESTATÍSTIVOS: ",DFdados.describe())
 estatistica=DFdados.describe()
 print(estatistica)
 for i in estatistica.items():
     print("\n",i)
     
 input("DIGITE ALGO: " )

 # APLICANDO CORRELAÇÃO ENTRE OS PARÂMETROS; GELADEIRA, FOGÃO, MICROONDAS e AIRFRLYER
 print("\n\n*********************************************************************")
 print("APLICANDO CORRELAÇÃO ENTRE: GELADEIRA, FOGAO , MICROONDAS, AIRFRYER: ")
 # ORGANIZANDO UM DATAFAME COM OS DADOS DISPONIBILIZADOS NO ARQUIVO   
 auxDF3=[]  
 auxDF3+=[(geladeira[j],fogao[j],microondas[j],airfryer[j]) for j in range(0,len(dados))]  
 DFdados3 = pd.DataFrame(auxDF3, columns=["GELADEIRA","FOGAO","MICROONDAS","AIRFRYER"])
 
 # CALCULAR A CORRELAÇÃO
 correlacao = DFdados3.corr(method='pearson')
 print(correlacao)
 
 # SEPARANDO OS VALORES
 itens=[]
 for i in correlacao:
      print("PARÂMETRO: ",i)
      itens.append(i)
      st=correlacao[i]
      sst=[]
      for j in range(len(st)):
         sst.append(str(st[j])+" ")
      print(sst)
     
 input("DIGITE ALGO: " )

 # CORRELACAO EM BI
 for pos,i in enumerate(correlacao):
      st=correlacao[i]
      print("\n\nAVALIANDO: ",i)
      for j in range(pos,len(st)):
         if pos!=j:
          if st[i]>=0.8:
             print("A VENDA DE ",itens[pos]," E ",itens[j]," APRESENTA ALTA CORRELAÇÃO, PROPOR PROPAGANDA DE MANUTENÇÃO DE VENDAS")
          elif st[i]>=0.5 and st[i]<0.8:
             print("A VENDA DE ",itens[pos]," E ",itens[j]," APRESENTA ALGUMA CORRELAÇÃO, PROPOR DIVULGAÇÃO")
          else:
             print("A VENDA DE ",itens[pos]," E ",itens[j]," APRESENTA BAIXA CORRELAÇÃO, AVALIAR A POSSIBILIDADE DE INTEGRAÇÃO DE VENDAS COM PROMOÇÃO")
             
 input("DIGITE ALGO: ")
     
 
 CORGELADEIRAFOGAO=[]
 CORGELADEIRAMICROONDAS=[]
 CORGELADEIRAAIRFRYER=[]   
 # SEGMENTANDO O PACOTE DE DADOS - 24 AMOSTRAS
 pacotes=int(len(dados)/24)
 print("NÚMERO TOTAL DE PACOTES PARA ANÁLISE:  ",pacotes)
 
 for i in range(pacotes-1):
     PGeladeira=geladeira[i*24:(i+1)*24]
     PFogao=fogao[i*24:(i+1)*24]
     PMicroondas=microondas[i*24:(i+1)*24]
     PAirfryer=airfryer[i*24:(i+1)*24]
     PLavaroupas=lavaroupas[i*24:(i+1)*24]
     PLavaloucas=lavaloucas[i*24:(i+1)*24]
     PPagamentovista=pagamentovista[i*24:(i+1)*24]
     PPagamentoprazocartao=pagamentoprazocartao[i*24:(i+1)*24]
     PPagamentoprazofinanciado=pagamentoprazofinanciado[i*24:(i+1)*24]
 
     PauxDF=[]  
     PauxDF+=[(PGeladeira[j],PFogao[j],PMicroondas[j],PAirfryer[j]) for j in range(0,24)]  
     PDFdados = pd.DataFrame(PauxDF, columns=["GELADEIRA","FOGAO","MICROONDAS","AIRFRYER"])
    
     print("\n ***********************************************")
     print("ANALISANDO CORRELAÇÃO DO PACOTE:  ",i)
     # CALCULAR A CORRELAÇÃO
     correlacao = PDFdados.corr(method='pearson')
     print(correlacao)
     
     #SALVANDO CORRELACAO GELADEIRA x OUTROS
     CORGELADEIRAFOGAO.append(correlacao["GELADEIRA"][1])
     CORGELADEIRAMICROONDAS.append(correlacao["GELADEIRA"][2])
     CORGELADEIRAAIRFRYER.append(correlacao["GELADEIRA"][3])
     
     input("\nDIGITE ALGO PARA CONTINUAR:")
 
 # PLOTANDO CORRELACAO   
 plt.plot(CORGELADEIRAFOGAO,'g')
 plt.plot(CORGELADEIRAMICROONDAS,'b')
 plt.plot(CORGELADEIRAAIRFRYER,'y')
 plt.title("EVOLUCAO CORRELACAO - GELADEIRAS x FOGAO(verde),MICROONDAS(azul),AIRFRYER(amarelo)")
 plt.xlabel("PACOTES DIAS")
 plt.ylabel("CORRELACAO")
 plt.show()

 print("GRÁFICO PLOTADO.")








