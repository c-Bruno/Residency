# Carregando as bibliotecas que vão ser utilizadas nos exercicios
import csv
import os
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import linear_model

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
# -----------------------------------------------------------------------------------------------------------------------------------------------------

# Lendo os dados do arquivo externo 
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
print('\033[33m\nImportação concluida...\033[m')


print('\033[1;34m\n===================================================================================== \033[m')
print('\033[1;34mEXERCICIO 2\n \033[m')

# Aplicando correlação para todos os itens presentes dentro do data set
print('\033[33mAplicando correlação geral...\033[m')
print(f"\033[0;32m\nAPLICANDO CORRELAÇÃO ENTRE TODOS OS ITENS(DATA SET COMPLETO)\n\033[m")
correlation = DFdatas.corr(method='pearson')
print(f'{correlation}\n\n')

# Plotando a matriz de correlação de todo o data set
print('\033[33mPlotando matrix de correlação...\033[m')
sns.heatmap(correlation, cmap='coolwarm', annot=True)
plt.show()
print('\033[33mMatrix de correlação plotada...\033[m')

# Descobrindo quantos pacotes existem dentro do arquivo de input
packages=int(len(cashedFile) / 24)
print("\nNÚMERO TOTAL DE PACOTES PARA ANÁLISE:  ", packages)

# Aqui vamos dividir o data set em pacotes de 24 e aplicar a correlação para cada um dos parametros
# (BATIMENTO CARDÍACO, PRESSÃO ARTERIAL E TEMPERATURA CORPORAL)
for i in range(packages):
    packageTime = time[i*24:(i+1)*24]
    packageCardiacBeatings = cardiacBeatings[i*24:(i+1)*24]
    packageBloodPressure = bloodPressure[i*24:(i+1)*24]
    packageBodyTemperature = bodyTemperature[i*24:(i+1)*24]

    print('\033[1;34m\n=================================================== \033[m')
    print('\033[1;34m                    EXERCICIO 3\033[m')
    print('\033[1;34m=================================================== \033[m')

    PauxDF=[]  
    PauxDF+=[(packageTime[j], packageCardiacBeatings[j],packageBloodPressure[j],packageBodyTemperature[j]) for j in range(0,24)]  
    PDFdata = pd.DataFrame(PauxDF, columns=["HORA", "BATIMENTO","PRESSAO","TEMPERATURA"])

    print(f"\033[0;32m\nANALISANDO PACOTE DO DIA: {i + 1}\n\033[m")
    # -------------------------------------------------------------------------------------------
    packageCorrelation = PDFdata.corr(method='pearson')
    print(packageCorrelation)
    print('\n')

    # -------------------------------------------------------------------------------------------    
    # SEPARANDO OS VALORES
    itens=[]
    for count in packageCorrelation:
        itens.append(count)
        st = packageCorrelation[count]
        sst = []
        for j in range(len(st)):
            sst.append(str(st[j]) + " ")

    # CORRELACAO EM BI
    print(f"\033[0;32m\nAnalise de correlação: {i + 1}\n\033[m")
    for position, parameter in enumerate(packageCorrelation):
        st = packageCorrelation[parameter]
        for j in range(position,len(st)):
            if (position != j):
                if (st[j] >= 0.8):
                    print(f'{itens[position]} E {itens[j]} APRESENTAM \033[1;31mALTA\033[m CORRELAÇÃO')
                elif ((st[j] >= 0.5) and (st[j] < 0.8)):
                    print(f'{itens[position]} E {itens[j]} APRESENTAM \033[1;34mALGUMA\033[m CORRELAÇÃO')
                else:
                    print(f'{itens[position]} E {itens[j]} APRESENTAM BAIXA CORRELAÇÃO')
    
    # -------------------------------------------------------------------------------------------
    # Plotando a matriz de correlação de todo o data set
    print(f'\033[33m\nPlotando matrix de correlação...\033[m')
    sns.heatmap(packageCorrelation, cmap='coolwarm', annot=True)
    plt.show()
    print(f'\033[33mMatrix de correlação plotada...\n\033[m')

    # -------------------------------------------------------------------------------------------
    regressao = linear_model.LinearRegression()
    # SEPARANDO OS CAMPOS
    vBeatings=np.array(PDFdata[["BATIMENTO"]])
    vPressure=np.array(PDFdata[["PRESSAO"]])
    regressao.fit(vBeatings, vPressure)

    # PRINT PARAMETROS DA REGRESSAO LINEAR
    print("Coeficiente de Regressão =",regressao.coef_) # inclinação da curva
    print("Interceptação = ",regressao.intercept_) # é o ponto onde X=0 e a reta vao cruzar o eixo Y
    
    # Regressão linear para prever os batimentos com base na temperatura, resultado plotado com o gráfico de dispersão
    X = PDFdata[['TEMPERATURA']]
    y = PDFdata['BATIMENTO']
    print('\n')
    regressao =  linear_model.LinearRegression().fit(X, y)
    print('Coeficiente de regressão:', regressao.coef_)
    print('Intercepto de regressão:', regressao.intercept_)
    y_pred = regressao.predict(X)
    sns.scatterplot(x=PDFdata['TEMPERATURA'], y=PDFdata['BATIMENTO'])
    sns.lineplot(x=PDFdata['TEMPERATURA'], y=y_pred)
    plt.show()
    
    # Regressão linear para prever os batimentos com base na pressão, resultado plotado com o gráfico de dispersão 
    X = PDFdata[['PRESSAO']]
    y = PDFdata['BATIMENTO']
    print('\n')
    regressao =  linear_model.LinearRegression().fit(X, y)
    print('Coeficiente de regressão:', regressao.coef_)
    print('Intercepto de regressão:', regressao.intercept_)
    y_pred = regressao.predict(X)
    sns.scatterplot(x=PDFdata['PRESSAO'], y=PDFdata['BATIMENTO'])
    sns.lineplot(x=PDFdata['PRESSAO'], y=y_pred)
    plt.show()


    print('\033[1;34m\n=================================================== \033[m')
    print('\033[1;34m                    EXERCICIO 4\033[m')
    print('\033[1;34m=================================================== \033[m')
    # -------------------------------------------------------------------------------------------
    # Aplicando valor médio no dia i para cada parametro
    print(f"\033[0;32m\nVALOR MEDIO\033[m")
    print("BATIMENTO = ",PDFdata["BATIMENTO"].mean())
    print("PRESSAO = ",PDFdata["PRESSAO"].mean())
    print("TEMPERATURA = ",PDFdata["TEMPERATURA"].mean())

    # -------------------------------------------------------------------------------------------
    # Aplicando média com avarege no dia i para cada parametro
    print(f"\033[0;32m\nVALOR MEDIO NumPy\033[m")
    print("BATIMENTO = ", np.average(PDFdata["BATIMENTO"]))
    print("PRESSAO = ", np.average(PDFdata["PRESSAO"]))
    print("TEMPERATURA = ", np.average(PDFdata["TEMPERATURA"]))

    # -------------------------------------------------------------------------------------------
    # Aplicando mediana no dia i para cada parametro
    print(f"\033[0;32m\nMEDIANA\033[m")
    print("BATIMENTO = ", PDFdata["BATIMENTO"].median())
    print("PRESSAO = ", PDFdata["PRESSAO"].median())
    print("TEMPERATURA = ", PDFdata["TEMPERATURA"].median())

    # -------------------------------------------------------------------------------------------
    # Aplicando moda no dia i para cada parametro
    print(f"\033[0;32m\nMODA\033[m")
    print("BATIMENTO = ", PDFdata["BATIMENTO"].mode())
    print("PRESSAO = ", PDFdata["PRESSAO"].mode())
    print("TEMPERATURA = ", PDFdata["TEMPERATURA"].mode())

    # -------------------------------------------------------------------------------------------
    # Aplicando Valor maximo no dia i para cada parametro
    print(f"\033[0;32m\nVALOR MAXIMO\033[m")
    print("BATIMENTO =",max(PDFdata["BATIMENTO"]))
    print("PRESSAO =",max(PDFdata["PRESSAO"]))
    print("TEMPERATURA =",max(PDFdata["TEMPERATURA"]))

    # -------------------------------------------------------------------------------------------
    # Aplicando minimo no dia i para cada parametro
    print(f"\033[0;32m\nVALOR MINIMO\033[m")
    print("BATIMENTO =", min(PDFdata["BATIMENTO"]))
    print("PRESSAO =", min(PDFdata["PRESSAO"]))
    print("TEMPERATURA =", min(PDFdata["TEMPERATURA"]))

    # -------------------------------------------------------------------------------------------
    # Aplicando amplitude no dia i para cada parametro
    print(f"\033[0;32m\nAMPLITUDE\033[m")
    print("BATIMENTO =", max(PDFdata["BATIMENTO"]) - min(PDFdata["BATIMENTO"]))
    print("PRESSAO =", max(PDFdata["PRESSAO"]) - min(PDFdata["PRESSAO"]))
    print("TEMPERATURA =", max(PDFdata["TEMPERATURA"]) - min(PDFdata["TEMPERATURA"]))

    # -------------------------------------------------------------------------------------------

    print(f'\033[33m\nIniciando tomada de decisão...\n\033[m')
    # Tomando decisões com base nas médias
    # Analise de batimentos cardiacos -------------------------------------------------------------------------------------------
    if (PDFdata["BATIMENTO"].mean() < 50):
        print(f"O batimento está abaixo do normal. Verifique se há sinais de fadiga ou desidratação. Batimento médio: {PDFdata['BATIMENTO'].mean():,.2f}")
    elif (PDFdata["BATIMENTO"].mean() > 90):
        print(f"O batimento está acima do normal. Verifique se há sinais de estresse ou atividade física intensa. Batimento médio:{PDFdata['BATIMENTO'].mean():,.2f}", )
    else:
        print(f"O batimento está dentro do normal. Batimento médio: {PDFdata['BATIMENTO'].mean():,.2f}")

    #  Analise de pressão arterial -------------------------------------------------------------------------------------------
    if ((PDFdata["PRESSAO"].mean() * 10 < 120) or (PDFdata["PRESSAO"].mean()  * 10 > 140)):
        print(f"A pressão arterial está fora da faixa normal. Consulte um médico. Pressão média {PDFdata['PRESSAO'].mean():,.2f}", )
    else:
        print(f"A pressão arterial está dentro da faixa normal. Pressão média {PDFdata['PRESSAO'].mean():,.2f}")

    #  Analise de temperatura corporal -------------------------------------------------------------------------------------------
    if (PDFdata["TEMPERATURA"].mean() > 37.5):
        print(f"A temperatura está alta. Verifique se há sinais de febre ou infecção. Temperatura média {PDFdata['TEMPERATURA'].mean():,.2f}")
    else:
        print(f"A temperatura está dentro da faixa normal. Temperatura média {PDFdata['TEMPERATURA'].mean():,.2f}")
      
    fig, axs = plt.subplots(1, 3, figsize=(10, 4))
    axs[0].boxplot(PDFdata['PRESSAO'])
    axs[0].set_title('Pressão')
    axs[1].boxplot(PDFdata['BATIMENTO'])
    axs[1].set_title('Batimento')
    axs[2].boxplot(PDFdata['TEMPERATURA'])
    axs[2].set_title('Temperatura')
    plt.show()

    checkBreak = input("\033[33m\nDigite qualquer tecla para continuar ou 'S' para sair... \033[m")
    if checkBreak.upper() == 'S':
        break
