#  Exercise 08 ==============================================================================================================
# Leitura de dados
currentYear = int(input("Entre com o ano atual: "))
yearContruction = int(input("Entre com o ano de construção do imóvel: "))

# Calcula a idade do imovel e com base nessa informação define a porcentagem de desconto aplicada
immobileAge = currentYear - yearContruction
print(f"Seu imovel possui {immobileAge} anos, desta forma o desconto do IPTU eh:")
if (immobileAge >= 40):
    print ("- 30%")
elif (immobileAge >=20):
    print ("- 20%")
elif (immobileAge >=5):
    print ("- 15%")
else:
    print("- 0%")
#============================================================================================================================

#  Exercise 09 ==============================================================================================================
# Leitura dos dados
weight = float(input("Entre com seu peso(kg): "))
height = float(input("Entre com seu peso(metros): "))

# Calculando o IMC e devolvendo a sua classificação
bmi = weight / (height ** 2)
print("======= SEU IMC =======")
if(bmi >= 30):
    print("Obesidade")
elif(bmi >= 25):
    print("Sobrepeso")
elif(bmi >= 18.5):
    print("Normal")
else:
    print("Baixo peso")
print("=======================")
#============================================================================================================================

#  Exercise 10 ==============================================================================================================
# Leitura de dados
numbers = []
numbers.append(input("Entre com o primeiro numero: "))
numbers.append(input("Entre com o segundo numero: "))
numbers.append(input("Entre com o terceiro numero: "))

# Gera um cópia dos numeros compiados em uma outra lista
sortedNumbers = numbers[:]

# Organiza essa nova lista para comparar se elas estão iguais
sortedNumbers.sort()
if( sortedNumbers == numbers):
    print("\n- Estão em ordem crescente")
else: 
    print ("\n- Não estão em ordem crescente")
#============================================================================================================================

#  Exercise 11 ==============================================================================================================
# Leitura de dados
firstGrade = float(input("Entre com a nota da primeira aula: "))
secondGrade = float(input("Entre com a nota da primeira aula: "))
frequency = int(input("Entre com a frequencia(0% a 100%): "))

# Calcula a média do aluno
finalGrade = (firstGrade + secondGrade) / 2

# Verifica a aprovação do aluno
print("\n")
if(frequency >= 75 and frequency <=100):   
    if (finalGrade >=6 and finalGrade <= 10):
        print("APROVADO")
    elif(finalGrade >= 4 and finalGrade < 6):
        print("EXAME")
    else: 
        print("Reprovado")
else: 
    print("Reprovado")
#============================================================================================================================

#  Exercise 12 ==============================================================================================================
# Leitura de dados
while True:
    xValue = float(input("Entre com o valor para x: "))
    if(xValue != 0): break

print(f"O valor de X eh: {(4 * ( xValue ** 2) - (3 * xValue) + 9) / xValue}")
#============================================================================================================================