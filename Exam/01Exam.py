import csv
import os
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

print('\033[1;34m===================================================================================== \033[m')
print('\033[1;34mEXERCICIO 1\n \033[m')

"""
    Prepara os dados para que estejam dentro da faixa de valores permitidos.
    Garantindo que a lista só seja retornada quando todos os valores estiverem dentro 
    do esperado.

    :param listValues: list
    :param range:tuple

    :return list com todos os valores dentro do range
    """
def prepareData(listValues, range):
    minRange, maxRange = range
    
    def replaceOutRangeValues(listValues):
        newListValues = []
        
        for outRangeValuesPosition, value in enumerate(listValues):
            if (value < minRange or value >= maxRange):
                # Obtem o numero anterior e posterior em relação ao atual.
                # Caso o numero incorreto esteja em uma das extremidades, pegamos a ponta oposta
                # Exemplo: Se a posição zero(0) esta fora do range, o previousValue = len(listValues) - 1
                previousValue = listValues[outRangeValuesPosition - 1] if outRangeValuesPosition > 0 else listValues[len(listValues) - 1] 
                nextValue = listValues[outRangeValuesPosition + 1] if outRangeValuesPosition < len(listValues) - 1 else listValues[0]
                
                newValue = (previousValue + nextValue) / 2
                newListValues.append(newValue)
            else:
                newListValues.append(value)
        
        return newListValues
    
    # Depois que a função replaceOutRangeValues foi aplicada pela primeira vez
    # vai ser gerado uma nova lista que contem os valores originais e as correções 
    # dos valores fora do range(se foi necessario).
    newListValues = replaceOutRangeValues(listValues)

    # Casos as listas sejam iguais, significa que todos os valores estão dentro
    # da faixa de valores permitidos. Porem se eles ainda forem diferentes significa 
    # que ainda existem valores fora da faixa então vamos chamar recursivamente a função
    #  replaceOutRangeValues até que todos os numeros fora do range sejam trocados
    while (newListValues != listValues):
        listValues = newListValues
        newListValues = replaceOutRangeValues(listValues)
    
    return newListValues

print('\033[33mImportando arquivo...\033[m')
currentDirectory = os.path.dirname(os.path.abspath(__file__)) # Define o diretorio atual como o diretorio do arquivo
fileName = os.path.join(currentDirectory, 'sinaisvitais003 100dias DV2 RAxxx9.txt') # Partindo do diretorio, procuramos pelo nome do arquivo

time = [] # Lista para armazenar as HORAS
cardiacBeatings = [] # Lista para armazenar BATIMENTOS CARDIACOS
bloodPressure = [] # Lista para armazenar PRESSÃO ARTERIAL
bodyTemperature = [] # Lista para armazenar TEMPERATURA CORPORAL

print('\033[33mLendo arquivo...\033[m')
with open(fileName,'r',newline='') as FILE:
    # csv.reader(FILE) -> Esse comando guarda um ponteiro para o arquivo
    cashedFile = list(csv.reader(FILE)) # trasnforma em array o ponteiro com os dados do arquivo txt
    
    print('\033[33mSeparando os dados...\033[m')
    for position in range(0,len(cashedFile)):
        dataOnLine = cashedFile[position][0].split("\t")

        time.append(float(dataOnLine[0]))
        cardiacBeatings.append(float(dataOnLine[1]))
        bloodPressure.append(float(dataOnLine[2]))
        bodyTemperature.append(float(dataOnLine[3]))

    print('\033[33mRemovendo ruídos...\033[m')
    #  PREPARA AS LISTAS CONFORME AS RESTRIÇÔES FORNECIDAS ================================
    cardiacBeatings = prepareData(cardiacBeatings, (0, 100)) # 0 <= BATIMENTO CARDÍACO <100
    bloodPressure = prepareData(bloodPressure, (0, 20)) # 0 <= PRESSÃO ARTERIAL < 20
    bodyTemperature = prepareData(bodyTemperature, (0, 40)) # 0 <= TEMPERATURA CORPORAL < 40
            

auxDF = []
auxDF += [(time[j], cardiacBeatings[j], bloodPressure[j], bodyTemperature[j]) for j in range(0, len(cashedFile))]
DFdatas = pd.DataFrame(auxDF, columns=['HORA', 'BATIMENTO', 'PRESSAO', 'TEMPERATURA'])
print(f"\033[0;32m\nDATA SET\033[m")
# print(DFdatas.to_string())
print(DFdatas)


print('\033[1;34m===================================================================================== \033[m')
print('\033[1;34mEXERCICIO 2\n \033[m')

# Aplicando correlação para todos os itens presentes dentro do data set
print(f"\033[0;32mAPLICANDO CORRELAÇÃO ENTRE TODOS OS ITENS(DATA SET COMPLETO)\n\033[m")

correlation = DFdatas.corr(method='pearson')
print(f'{correlation}\n\n')

# # SEPARANDO OS VALORES
# itens=[]
# for i in correlation:
#     # print("PARÂMETRO: ",i)
#     itens.append(i)
#     st=correlation[i]
#     sst=[]
#     for j in range(len(st)):
#         sst.append(str(st[j])+" ")
#     # print(sst)

# # CORRELACAO EM BI
# for pos,i in enumerate(correlation):
#     st=correlation[i]
#     print("\n\nAVALIANDO: ",i)
#     for j in range(pos,len(st)):
#         if pos!=j:
#             if st[j]>=0.8:
#                 print(itens[pos]," E ",itens[j]," APRESENTA ALTA CORRELAÇÃO, PROPOR PROPAGANDA DE MANUTENÇÃO DE VENDAS")
#             elif st[j]>=0.5 and st[j]<0.8:
#                 print(itens[pos]," E ",itens[j]," APRESENTA ALGUMA CORRELAÇÃO, PROPOR DIVULGAÇÃO")
#             else:
#                 print(itens[pos]," E ",itens[j]," APRESENTA BAIXA CORRELAÇÃO, AVALIAR A POSSIBILIDADE DE INTEGRAÇÃO DE VENDAS COM PROMOÇÃO")
        

# input('aaaa')
print('\033[1;34m===================================================================================== \033[m')
print('\033[1;34mEXERCICIO 3\n \033[m')



print('\033[1;34m===================================================================================== \033[m')
print('\033[1;34mEXERCICIO 4\n \033[m')

packages=int(len(cashedFile) / 24)
print("NÚMERO TOTAL DE PACOTES PARA ANÁLISE:  ", packages)

# Dividindo o data set em pacotes de 24 e aplicando a correlação para cada um dos parametros
# (BATIMENTO CARDÍACO, PRESSÃO ARTERIAL E TEMPERATURA CORPORAL)
for i in range(packages):
    packageCardiacBeatings = cardiacBeatings[i*24:(i+1)*24]
    packageBloodPressure = bloodPressure[i*24:(i+1)*24]
    packageBodyTemperature = bodyTemperature[i*24:(i+1)*24]

    PauxDF=[]  
    PauxDF+=[(packageCardiacBeatings[j],packageBloodPressure[j],packageBodyTemperature[j]) for j in range(0,24)]  
    PDFdata = pd.DataFrame(PauxDF, columns=["BATIMENTO","PRESSAO","TEMPERATURA"])

    print("\n ***********************************************")
    print("ANALISANDO PACOTE DO DIA: ", i + 1)
    # -------------------------------------------------------------------------------------------
    print("CORRELAÇÃO") # Aplicando correlação no dia i
    packageCorrelation = PDFdata.corr(method='pearson')
    print(packageCorrelation)
    # print(PDFdata.describe())

    # -------------------------------------------------------------------------------------------
    print("\nVALOR MEDIO") # Aplicando valor médio no dia i
    print("BATIMENTO = ",PDFdata["BATIMENTO"].mean())
    print("PRESSAO = ",PDFdata["PRESSAO"].mean())
    print("TEMPERATURA = ",PDFdata["TEMPERATURA"].mean())

    # -------------------------------------------------------------------------------------------
    print("\nVALOR MEDIO NumPy") # Aplicando média com avarege no dia i
    print("BATIMENTO = ", np.average(PDFdata["BATIMENTO"]))
    print("PRESSAO = ", np.average(PDFdata["PRESSAO"]))
    print("TEMPERATURA = ", np.average(PDFdata["TEMPERATURA"]))

    # -------------------------------------------------------------------------------------------
    print("\nMEDIANA") # Aplicando mediana no dia i
    print("BATIMENTO = ",PDFdata["BATIMENTO"].median())
    print("PRESSAO = ",PDFdata["PRESSAO"].median())
    print("TEMPERATURA = ",PDFdata["TEMPERATURA"].median())

    # -------------------------------------------------------------------------------------------
    print("\nMODA") # Aplicando moda no dia i
    print("BATIMENTO = ",PDFdata["BATIMENTO"].mode())
    print("PRESSAO = ",PDFdata["PRESSAO"].mode())
    print("TEMPERATURA = ",PDFdata["TEMPERATURA"].mode())

    # -------------------------------------------------------------------------------------------
    print("\nVALOR MAXIMO") # Aplicando Valor maximo no dia i
    print("BATIMENTO =",max(PDFdata["BATIMENTO"]))
    print("PRESSAO =",max(PDFdata["PRESSAO"]))
    print("TEMPERATURA =",max(PDFdata["TEMPERATURA"]))

    # -------------------------------------------------------------------------------------------
    print("\nVALOR MINIMO") # Aplicando minimo no dia i
    print("BATIMENTO =",min(PDFdata["BATIMENTO"]))
    print("PRESSAO =",min(PDFdata["PRESSAO"]))
    print("TEMPERATURA =",min(PDFdata["TEMPERATURA"]))

    # -------------------------------------------------------------------------------------------
    print("\nAMPLITUDE") # Aplicando amplitude no dia i
    print("BATIMENTO =",max(PDFdata["BATIMENTO"])-min(PDFdata["BATIMENTO"]))
    print("PRESSAO =",max(PDFdata["PRESSAO"])-min(PDFdata["PRESSAO"]))
    print("TEMPERATURA =",max(PDFdata["TEMPERATURA"])-min(PDFdata["TEMPERATURA"]))

    checkBreak = input("Digite qualquer tecla para continuar ou 'S' para sair...")
    if checkBreak.upper() == 'S':
        break
