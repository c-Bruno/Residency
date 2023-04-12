# Exercise 01 ================================================
#  Definindo uma constante para ser a senha pré-cadastrada
password = "1234"

# Leitura de dados
typedPassword = input("Digite a senha numérica: ")

# Verificando se a senha é válida
if (typedPassword == password):
    print("ACESSO PERMITIDO")
else:
    print("ACESSO NEGADO")
# ==============================================================================================================

# Exercise 02 ================================================
# Leitura dos dados
firstSide = float(input("Comprimento do primeiro lado do triângulo: "))
secondSide = float(input("Comprimento do segundo lado do triângulo: "))
thirdSide = float(input("Comprimento do terceiro lado do triângulo: "))

# Definindo a classificação do triângulo
if (firstSide == secondSide == thirdSide):
    print("Triângulo é equilátero.")
elif ((firstSide == secondSide) or 
      (firstSide == thirdSide) or 
      (secondSide == thirdSide)
    ): print("O triângulo é isósceles.")
else:
    print("O triângulo é escaleno.")
# ==============================================================================================================

#  Exercise 03 ================================================
# Leitura de dados
number = int(input("Digite um número inteiro: "))

# Verificando se o número é par ou ímpar
if (number % 2 == 0):
    print("O número é par.")
else:
    print("O número é ímpar.")
# ==============================================================================================================

#  Exercise 04 ================================================
# Leitura de dados
firstNumber = int(input("Primeiro número: "))
secondNumber = int(input("Segundo número: "))

# Verificando se é possivel dividir o primeiro número pelo segundo
if (firstNumber % secondNumber == 0):
    print(f"O primeiro número é divisível pelo segundo. Resultado da divisão foi {firstNumber / secondNumber}")
else:
    print("O primeiro número não é divisível pelo segundo.")
# ==============================================================================================================

#  Exercise 05 ================================================
#Leitura dos pesos
primeiroPeso = float(input("Entre com o primeiro peso:"))
segundoPeso = float(input("Entre com o segundo peso:"))

# Leitura das notas
primeiraNota = float(input("Nota primeira prova: "))
segundaNota = float(input("Nota segunda prova: "))

# Calcular media
media= ((primeiraNota * primeiroPeso) + (segundaNota * segundoPeso))/ (primeiroPeso + segundoPeso)
print("====================================================")
print(f'NOTA 01 = {primeiraNota:,.2f}    PESO 01 = {primeiroPeso:,.2f}')
print(f'NOTA 02 = {segundaNota:,.2f}    PESO 02 = {segundoPeso:,.2f}')
print(f'\nMedia = {media:,.2f}')

#Verifica situação do aluno
if (media >= 5):
    print("APROVADO")
elif (media < 5):
    print("REPROVADO")

if (media >= 9):
    print("PARABENS, VOCÊ FOI APROVADO COM LOUVOR!")
elif (media >= 8):
    print("PARABENS O SEU DESEMPENHO FOI MUITO BOM!")
print("====================================================")
#  ==============================================================================================================


#  Exercise 06 ================================================
# === Calculos ===#=================#=================
# Fahrenheit para Celsius: (F - 32) / 1.8
# Kelvin para Celsius: K - 273.15
# Rankine para Celsius: (R - 491.67) / 1.8
# Réaumur para Celsius: R / 0.8
#=================#=================#=================

# Leitura de dados
temperatura = float(input("Temperatura: "))

# Estrutura constante com as escalas e suas respectivas contas
scales = [
    {'scale': 'Fahrenheit', 'celsius': ((temperatura - 32) / 1.8)},
    {'scale': '', 'celsius': (temperatura - 273.15)},
    {'scale': 'Rankine', 'celsius': ((temperatura - 491.67) / 1.8)},
    {'scale': 'Réaumur', 'celsius': (temperatura / 0.8)}
]

# Saída de dados
for item in scales:
    print(f"{temperatura:.2f} graus {item['scale']} equivalem a {item['celsius']:.2f} graus Celsius.")
#  ==============================================================================================================


#  Exercise 07 ================================================
# Entrada de dados
temperatura = float(input("Temperatura: "))

#Exibe o menu par ao usuario e enquanto ele não informar corretamente repete a pergunra
checkMenu = True
while checkMenu: 
    scale = input("Informe a escala da temperatura \n- F = Fahrenheit\n- K = Kelvin\n- R = Rankine\n- Re = Réaumur)\nInforme a letra par continuar: ").upper()
    if (scale == "F"):
        celsius = (temperatura - 32) / 1.8
    elif (scale == "K"):
        celsius = temperatura - 273.15
    elif (scale == "R"):
        celsius = (temperatura - 491.67) / 1.8
    elif (scale == "RE"):
        celsius = temperatura / 0.8
    else:
        print("\nEscala inválida.\n")
        continue
    checkMenu = False

# Saída de dados
print(f"{temperatura:.2f} graus {scale} equivalem a {celsius:.2f} graus Celsius.")
#  ==============================================================================================================