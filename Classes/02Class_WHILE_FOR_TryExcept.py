
# Laço de repetição WHILE =============================================
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


# Laço de repetição FOR ===============================================
temperatures = [] # Lista de temperaturas

for day in range (0, 31):
    temperature = 0.011 * day**3 - 0.3 * day**2 + 0.04 * day
    print(f"||| Dia: {day:2d} ||| Temperatura: {temperature:6.2f} |||")

    temperatures.append(temperature)

temperatures.sort()
print(f"\nA menor temperatura foi: {temperatures[0]:6.2f}") 


# Validações com laço de repetição e TRY CATCH =========================
while True:
    try:
        number = int(input("Numero: "))
        break
    except:
        print("Apenas numeros\n")

