# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 14:55:55 2023

@author: AM
"""

import statistics
import math
from scipy import stats
from collections import Counter

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv
import scipy.stats as stats
import json


df = pd.read_json(r"C:\Users\bcaboclo\Desktop\Tecprogramspace\Classes\15Class\products.json")
produtos=list(df.items())

idx=df["id"]
nome=df["name"]
descricao=df["description"]
preco=df["price"]
tamanho=df["tamanho"]
aval=df["available"]

print("\n******************")
for i in range(len(idx)):
    print("\n******************")
    print("ID: ",idx[i])
    print("NOME: ",nome[i])
    print("PRECO: ",preco[i])
    print("TAMANHO: ",int(tamanho[i]))
    print("AVALIACO: ",aval[i])
    print("DESCRIÇÃO: ",descricao[i])

print("ESTATISTICA DOS PARAMETROS NUMÉRICOS:")
print(df.describe())

df = pd.read_json(r"C:\Users\bcaboclo\Desktop\Tecprogramspace\Classes\15Class\doencas.json")
doenca=df["DOENCA"]
print("DOENCAS: \n",doenca)
sintomas=df["SINTOMAS"]
print("SINTOMAS: \n",sintomas)

print(df['SINTOMAS'].apply(pd.Series))

