# Por favor, realizar os exercícios 1 a 16 da apostila CDBDA - AULA004 ESTRUTURA REPETICAO PARTE I.pdf

#  Exercise 01 ===============================================================================================================
#  Leitura de dados
firstNumber = int(input("- Primeiro numero: "))
lastNumber = int(input("- Segundo numero: "))

for number in range(firstNumber, lastNumber + 1):
    print(number)
#=============================================================================================================================

#  Exercise 02 ===============================================================================================================
sum = 0
decision = 'S'
count = 0

while decision != 'N':
    sum += float(input("Entre com um numero: "))
    count += 1
    decision = input("Deseja continuar? (s/n): ").upper()

print(sum/count)
#=============================================================================================================================

#  Exercise 03 ===============================================================================================================
values = [] # Lista que fica responsavel por armazenar todos os valores que entraram

while True:
    userInput = input("Digite um valor (ou 'fim' para encerrar): ")

    # Primeiro vamos garantir que o usuario não decidiu parar
    if userInput.upper() == 'FIM': break

    try:
        valor = float(userInput)
        values.append(valor)
    except ValueError:
        print("Apenas numeros.")

# Garante que o usuario digitou ao menos um valor
print("==========================================================================")
if values:
    print(f"A média é {sum(values) / len(values):.2f}.\n****** Valores lidos {values} *******")
    print(f"O maior: {max(values):.2f}")
    print(f"O menor: {min(values):.2f}")
else:
    print("Nenhum valor foi lido.")
print("==========================================================================")
#=============================================================================================================================

#  Exercise 04 ===============================================================================================================
#  Le o numero que vai ter o fatorial calculado
number = int(input("Entre com um numero inteiro: "))
factorial = number

# Rola a interação fatorial
for element in range(1, number):
    factorial *= element

print(f"Fatorial: {factorial}")
#=============================================================================================================================

#  Exercise 05 ===============================================================================================================
number = int(input("Entre com um numero inteiro: "))

for element in range(0, 11):
    print(f"||| {(number):2.0f} X {(element):2.0f} = {(number * element):3.0f} |||")
#=============================================================================================================================

#  Exercise 06 ===============================================================================================================
temperatures = [] # Lista de temperaturas

for day in range (0, 31):
    temperature = 0.011 * day**3 - 0.3 * day**2 + 0.04 * day
    print(f"||| Dia: {day:2d} ||| Temperatura: {temperature:6.2f} |||")

    temperatures.append(temperature)

temperatures.sort()
print(f"\nA menor temperatura foi: {temperatures[0]:6.2f}") 
#=============================================================================================================================

#  Exercise 07 ===============================================================================================================
import random
computerNumber = (random.randint(0, 100))

while True:
    try:           
        playerNumber = int(input("Seu numero: "))
        if (playerNumber < computerNumber):
            print("***** Seu numero eh MENOR! *****\n")
        elif (playerNumber > computerNumber):
            print("***** Seu numero eh MAIOR! *****\n")
        else:
            print("\n********** Você acertou!!! **********")
            break
    except:
        print("Apenas numeros\n")
#=============================================================================================================================

#  Exercise 08 ===============================================================================================================
import random
computerNumber = (random.randint(0, 100))
userAttempts = 0

while True:
    try:           
        playerNumber = int(input("Seu numero: "))
        userAttempts += 1
        if (playerNumber < computerNumber):
            print("***** Seu numero eh MENOR! *****\n")
        elif (playerNumber > computerNumber):
            print("***** Seu numero eh MAIOR! *****\n")
        else:
            print("\n********** Você acertou!!! **********")
            print(f"********** Numero de tentativas: {userAttempts} **********")
            break
    except:
        print("Apenas numeros\n")
#=============================================================================================================================

#  Exercise 09 ===============================================================================================================
import random
computerNumber = (random.randint(0, 100))
userAttempts = 0

while True:   
    value = input("Seu numero(ou 'fim' para encerrar): ")

    try:
        playerNumber = int(value)
    except:
        if ((value.upper() == "FIM")): break
        else: 
            print("Apenas numeros inteiros(Ou 'fim' para encerrar)")
            continue

    userAttempts += 1
    if (playerNumber < computerNumber):
        print("\n***** Seu numero eh MENOR! *****")
    elif (playerNumber > computerNumber):
        print("\n***** Seu numero eh MAIOR! *****")
    else:
        print("\n********** Você acertou!!! **********")
        break

print(f"\n********** Numero de tentativas: {userAttempts} **********")
print("********** Obrigado por participar!!**********")
#=============================================================================================================================

#  Exercise 10 ===============================================================================================================
import random
computerNumber = random.randint(0, 100)
userAttempts = 0

while True:   
    value = input("------------------------- DIGITE ------------------------- \n- Seu numero OU\n- 'fim' para encerrar OU\n- 'nova' para iniciar uma nova partida\n")

    try:
        playerNumber = int(value)
    except:
        if (value.upper() == "FIM"): break
        elif(value.upper() == "NOVA"):
            userAttempts = 0
            computerNumber = random.randint(0, 100)
            print( "\n\n------------------------- PARTIDA ENCERRADA, COMEÇANDO UMA NOVA -------------------------\n\n")
        else: 
            print("Apenas numeros inteiros(Ou 'fim' para encerrar)")
        continue

    userAttempts += 1
    if (playerNumber < computerNumber):
        print("\n************************* Seu numero eh MENOR! *************************")
    elif (playerNumber > computerNumber):
        print("\n************************* Seu numero eh MAIOR! *************************")
    else:
        print("\n****************************** Você acertou!!! ******************************")
        break

print(f"\n********** Numero de tentativas: {userAttempts} **********")
print("********** Obrigado por participar!!**********")
#=============================================================================================================================

#  Exercise 11 ===============================================================================================================
firstNumber = int(input("- Primeiro numero: "))
lastNumber = int(input("- Segundo numero: "))

print("\nNumeros divisiveis por 3:")
for number in range(firstNumber, lastNumber + 1):
    if(number % 3 == 0):
        print(f"- {number}")
#=============================================================================================================================

#  Exercise 12 ===============================================================================================================
firstNumber = int(input("- Primeiro numero: "))
lastNumber = int(input("- Segundo numero: "))
divisor = int(input("Digite o número pelo qual deseja a divisibilidade: "))


print(f"\nNumeros divisiveis por {divisor}:")
for number in range(firstNumber, lastNumber + 1):
    if(number % divisor == 0):
        print(f"- {number}")
#=============================================================================================================================

#  Exercise 13 ===============================================================================================================
# Lista com os times iniciais
list = [
    'GUARANI',
    'SÃO PAULO',
    'PALMEIRAS',
    'CRUZEIRO',
    'SANTOS',
    'FERROVIÁRIA',
    'JUVENTUS',
    'GOIÁS',
    'ÍBIS',
    'SINOP'
]

# Impressão da lista
for index, team in enumerate(list):
    print (f"||| {index} - {team}")
#=============================================================================================================================

#  Exercise 14 ===============================================================================================================
import random

# Função para converter a move em string
def playerChoice(move):
    if (move == 0):
        return "Pedra"
    elif (move == 1):
        return "Papel"
    else:
        return "Tesoura"


# Leitura de dados
playersChosenNumber = int(input("Escolha Pedra (0), Papel (1) ou Tesoura (2): "))

# Gera um numero para o computador
computersChosenNumber = random.randint(0, 2)

print(f"\n- Você escolheu {playerChoice(playersChosenNumber)}.\n- O computador escolheu {playerChoice(computersChosenNumber)}.")
# Verifica quem ganhou
if (playersChosenNumber == computersChosenNumber):
    print("--- Empate! ---")
elif ((playersChosenNumber == 0 and computersChosenNumber == 2) or 
        (playersChosenNumber == 1 and computersChosenNumber == 0) or
        (playersChosenNumber == 2 and computersChosenNumber == 1)
    ):
    print("--- Você ganhou! ---")
else:
    print("--- Você perdeu! ---")
#=============================================================================================================================

#  Exercise 15 ===============================================================================================================
import random

# Função para converter a move em string
def playerChoice(move):
    if (move == 0):
        return "Pedra"
    elif (move == 1):
        return "Papel"
    else:
        return "Tesoura"


while True:
    try:
        # Leitura de dados
        playersChosenNumber = int(input("Escolha Pedra (0), Papel (1) ou Tesoura (2): "))

        # Verifica se a escolha do usuário é válida
        if (playersChosenNumber < 0 or playersChosenNumber > 2):
            print("||| Escolha inválida. Ecolhas validas: 0, 1, 2 |||")
            continue
    except:
        print("||| Apenas numeros inteiros |||")
        continue


    # Gera um numero para o computador
    computersChosenNumber = random.randint(0, 2)

    print(f"\n- Você escolheu {playerChoice(playersChosenNumber)}.\n- O computador escolheu {playerChoice(computersChosenNumber)}.")
    # Verifica quem ganhou
    if (playersChosenNumber == computersChosenNumber):
        print("--- Empate! ---")
    elif ((playersChosenNumber == 0 and computersChosenNumber == 2) or 
          (playersChosenNumber == 1 and computersChosenNumber == 0) or
          (playersChosenNumber == 2 and computersChosenNumber == 1)
        ):
        print("--- Você ganhou! ---")
    else:
        print("--- Você perdeu! ---")

    # Pergunta se o usuário quer jogar novamente
    playAgain = input("Deseja jogar novamente? (s/n)").lower()
    if playAgain == "n":
        break
#=============================================================================================================================

#  Exercise 16 ===============================================================================================================
import random

# Função para converter a move em string
def playerChoice(move):
    if (move == 0):
        return "Pedra"
    elif (move == 1):
        return "Papel"
    else:
        return "Tesoura"


computerWins = 0
playerWins = 0
tie = 0

while True:
    try:
        # Leitura de dados
        playersChosenNumber = int(input("Escolha Pedra (0), Papel (1) ou Tesoura (2): "))

        # Verifica se a escolha do usuário é válida
        if (playersChosenNumber < 0 or playersChosenNumber > 2):
            print("||| Escolha inválida. Ecolhas validas: 0, 1, 2 |||")
            continue
    except:
        print("||| Apenas numeros inteiros |||")
        continue


    # Gera um numero para o computador
    computersChosenNumber = random.randint(0, 2)

    print(f"\n- Você escolheu {playerChoice(playersChosenNumber)}.\n- O computador escolheu {playerChoice(computersChosenNumber)}.")
    # Verifica quem ganhou
    if (playersChosenNumber == computersChosenNumber):
        print("--- Empate! ---")
        tie += 1
    elif ((playersChosenNumber == 0 and computersChosenNumber == 2) or 
          (playersChosenNumber == 1 and computersChosenNumber == 0) or
          (playersChosenNumber == 2 and computersChosenNumber == 1)
        ):
        print("--- Você ganhou! ---")
        playerWins += 1
    else:
        print("--- Você perdeu! ---")
        computerWins += 1

    # Pergunta se o usuário quer jogar novamente
    playAgain = input("Deseja jogar novamente? (s/n)").lower()
    if playAgain == "n":
        break

print(f"||| PLACAR FINAL |||\n- Empates: {tie}\n- Vitorias: {playerWins}\n- Derrotas: {computerWins}")
#=============================================================================================================================
