import csv
import os
import pandas as pd

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

currentDirectory = os.path.dirname(os.path.abspath(__file__)) # Define o diretorio atual como o diretorio do arquivo
fileName = os.path.join(currentDirectory, 'sinaisvitais003 100dias DV2 RAxxx9.txt') # Partindo do diretorio, procuramos pelo nome do arquivo

time = [] # Lista para armazenar as HORAS
cardiacBeatings = [] # Lista para armazenar BATIMENTOS CARDIACOS
bloodPressure = [] # Lista para armazenar PRESSÃO ARTERIAL
bodyTemperature = [] # Lista para armazenar TEMPERATURA CORPORAL

with open(fileName,'r',newline='') as FILE:
    cashedFile = list(csv.reader(FILE))
    
    for position in range(0,len(cashedFile)):
        dataOnLine = cashedFile[position][0].split("\t")

        time.append(float(dataOnLine[0]))
        cardiacBeatings.append(float(dataOnLine[1]))
        bloodPressure.append(float(dataOnLine[2]))
        bodyTemperature.append(float(dataOnLine[3]))

  
    #  PREPARA AS LISTAS CONFORME AS RESTRIÇÔES FORNECIDAS ================================
    prepareData(cardiacBeatings, (0, 100)) # 0 <= BATIMENTO CARDÍACO <100
    prepareData(bloodPressure, (0, 20)) # 0 <= PRESSÃO ARTERIAL < 20
    prepareData(bodyTemperature, (0, 40)) # 0 <= TEMPERATURA CORPORAL < 40
            


auxDF = []
auxDF += [(time[j], cardiacBeatings[j], bloodPressure[j], bodyTemperature[j]) for j in range(0, len(cashedFile))]
DFdatas = pd.DataFrame(auxDF, columns=['HORA', 'BATIMENTO', 'PRESSAO', 'TEMPERATURA'])

print(DFdatas)