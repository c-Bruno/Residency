# Por favor, realizar os exercícios 1 a 11 da apostila CDBDA - AULA005 ARRAY PARTE I.pdf

#  Exercise 01 ===============================================================================================================
numbers = [] # Armazena os numeros lidos
repetitions = int(input("Quantidade de numeros que vão ser lidos: "))

# Faz a entrada dos dados
for number in range(repetitions):
    numbers.append(float(input(f"Entre com o numero {number}: ")))

# Printando a saida
print(f"\n- Maior numero: {max(numbers)}")
print(f"- Menor numero: {min(numbers)}")
print(f"- Media aritmética: {sum(numbers) / len(numbers)}")
#=============================================================================================================================

#  Exercise 02 ===============================================================================================================
numbers = [] # Armazena os numeros lidos
repetitions = int(input("Quantidade de numeros que vão ser lidos: "))

# Faz a entrada dos dados
for number in range(repetitions):
    numbers.append(float(input(f"Entre com o numero {number}: ")))

# Printando a saida
numbers.reverse()
print(f"Ordem inversa: {numbers}")
#=============================================================================================================================

#  Exercise 03 ===============================================================================================================
grades = {} # Inicializa um dicionario vazia para armazenar as notas dos alunos
students = int(input("Quantidade alunos: "))

# Faz a entrada dos dados
for student in range(students):
    ra = input(f"Digite o RA do {student+1}º aluno: ")
    
    grades[ra] = []
    for colunm in range(4):
        grade = float(input(f"- {colunm+1}º  nota: "))
        grades[ra].append(grade)

# Calculando medias
for ra in grades:
    media = sum(grades[ra]) / len(grades[ra])
    grades[ra].append(media)

# Printando a saida
print("Médias aritméticas dos alunos:")
for ra in grades:
    print(f"Aluno {ra}: {grades[ra][-1]:.2f}")
#=============================================================================================================================

#  Exercise 04 ===============================================================================================================
numbers = [] # Armazena os numeros lidos
repetitions = int(input("Quantidade de numeros que vão ser lidos: "))

for number in range(repetitions):
    numbers.append(float(input(f"Entre com o numero {number}: ")))

numbers.sort()
print(f"Vetor ordenado: {numbers}")
#=============================================================================================================================

#  Exercise 05 ===============================================================================================================
numbers = [] # Armazena os numeros lidos
repetitions = int(input("Quantidade de numeros que vão ser lidos: "))

for number in range(repetitions):
    numbers.append(float(input(f"Entre com o numero {number}: ")))

# Ordena o vetor sem usar sort
for number in range(len(numbers)):
    # Primeiro definimos que o menor index é igual ao numero apenas para ter um valor inicial
    lowerValueIndex = number

    # Agora varremos o vetor de numeros procurando saber qual o index do menor numero existente
    for j in range(number + 1, len(numbers)):
        if numbers[j] < numbers[lowerValueIndex]:
            lowerValueIndex = j

    # Agora que sabemos seu index podemos fazer a inversão, invertendo a posição number
    # (posição atual do vetor) com o index encontrado(infex do menor valor)
    numbers[number], numbers[lowerValueIndex] = numbers[lowerValueIndex], numbers[number]

print(f"Vetor ordenado: {numbers}")
#=============================================================================================================================

#  Exercise 06 ===============================================================================================================
bits = [] # Vetor para armazenar os bits em binário
number = int(input("Digite o número: "))

# Converte o número para binário
while number > 0:
    bit = number % 2
    bits.insert(0, bit)
    number //= 2 # Divisão inteira por 2

# Imprime o vetor com os bits do número em binário
print("O número em binário é:")
print(bits)
#=============================================================================================================================

#  Exercise 07 ===============================================================================================================
import math

# Definindo a lista de coordenadas com base 
# na imagem do exercicio
coordinates = [
    (200, 200), 
    (800, 200), 
    (800, 300), 
    (1600, 300), 
    (1600, 200), 
    (2100, 500), 
    (2100, 1100), 
    (1600, 1400), 
    (200, 1400), 
    (500, 800), 
    (500, 500), 
    (200, 500)
]

# Gerando a matriz de coordenadas
coordenadas = []
for point in coordinates:
    x, y = point
    coordenadas.append([x, y])

# Calculando o perímetro
perimeter = 0
for point in range(len(coordenadas)):
    x1, y1 = coordenadas[point]
    x2, y2 = coordenadas[(point + 1) % len(coordenadas)]
    perimeter += math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Printando a saida
print(f"Perímetro: {perimeter:.5f}")
#=============================================================================================================================

#  Exercise 08 ===============================================================================================================
names = [] # lista responsavel por armazenar todos os nomes
number = int(input("Entre com o numero de entradas: "))

# Faz a entrada dos dados
for i in range(number):
    name = input(f"- {i+1}° nome: ")
    names.append(name)

#  Busca peplo nome especifico
nameQuery = input("Entre com o nome pelo qual deseja procurar: ")
if (nameQuery in names):
    print("O nome", nameQuery, "esta na lista")
else:
    print("O", nameQuery, "NÃO esta na lista.")
#=============================================================================================================================

#  Exercise 09 ===============================================================================================================
number = int(input("Digite o número de linhas da meia pirâmide: "))

for item in range(number):
    # Aqui precisamos de um segundo for para fazer o print equivalente
    # a quantidade de number + 1 em *
    for j in range(item + 1):
        print("*", end="")
    print() # Um print vazio apenas para termos as quebras de linha
#=============================================================================================================================

#  Exercise 10 ===============================================================================================================
number = int(input("Digite o número de linhas da meia pirâmide: "))

for item in range(number):
    # Primeiro precisamos gerar os espaçoes vazios que teremos 
    # No print da piramide
    for j in range(number - item - 1):
        print(" ", end="") # Esse espaço precisa ser proporcional
    
    # Com os espaços printados, começamos a exibir os *
    for j in range(2 * item + 1):
        print("*", end="")
    print() # Um print vazio apenas para termos as quebras de linha
#=============================================================================================================================

#  Exercise 11 ===============================================================================================================
# Definindo o tamanho da matriz de alunos
number = int(input("Digite o número de alunos: "))

# Inicializando a matriz com zeros para garantirmos que teremos um 
# valor conhecido em todas as posições da matriz
matriz = [[0 for colunm in range(6)] for line in range(number)]

# Lendo os dados
for line in range(number):
    matriz[line][0] = int(input("\nDigite o RA do aluno: ")) # Guarda o RA na primeira coluna
    average = 0

    for colunm in range(1, 5):
        nota = float(input(f"Digite a nota {colunm} do aluno: "))
        matriz[line][colunm] = nota
        average += nota
    matriz[line][5] = average / 4

# Printando a saida
for line in range(number):
    print (f"\n- RA: {matriz[line][0]:<10} \n- 1° Nota: {matriz[line][1]:<10} \n- 2° Nota: {matriz[line][2]:<10}\n- 3° Nota: {matriz[line][3]:<10}\n- 4° Nota: {matriz[line][4]:<10}\n- Media: {matriz[line][5]:<10}")

#=============================================================================================================================