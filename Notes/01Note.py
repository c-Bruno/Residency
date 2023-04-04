routes = {} # Armazena os dados do trecho
accelerations = [] # Armazena as acelerações

# Leitura dos dados
for reding in range(4):
    distance = float(input(f"Distancia do trecho 0{reding + 1}: "))
    time = float(input(f"Tempo do trecho 0{reding + 1}: "))
    routes[f'trecho {reding + 1}'] = {'distance': distance, 'time': time}
    
    print("====================================================\n")

# Calculando as velocidade
print("================ Velocidades Medias ================")
totalSpeed = 0 # velocidade total
totalTime = 0 # Tempo total

for route, information in routes.items():
    print(f"Velocidade média do {route}: {(information['distance'] / information['time']):,.2f}")
    totalSpeed += information['distance']
    totalTime += information['time']

    accelerations.append(information['distance'])

print(f"\nVelocidade média TOTAL: {(totalSpeed / totalTime):,.2f}")
print("====================================================\n")



import math

# Entrada de dados
angulo_graus = float(input("Digite o ângulo de lançamento em graus: "))
velocidade_inicial = float(input("Digite a velocidade inicial em m/s: "))
altura_inicial = float(input("Digite a altura inicial em metros: "))

# Convertendo o ângulo para radianos
angulo_radianos = math.radians(angulo_graus)

# Constantes
g = 9.81  # aceleração da gravidade

# Calculando a posição horizontal e a altura em função do tempo
for t in range(11):
    x = velocidade_inicial * math.cos(angulo_radianos) * t
    y = altura_inicial + (velocidade_inicial * math.sin(angulo_radianos) * t) - ((1/2) * g * t**2)
    print("Tempo: {} s | Posição horizontal: {:.2f} m | Altura: {:.2f} m".format(t, x, y))



import math

# Entrada de dados
x1 = float(input("Digite a coordenada X da origem: "))
y1 = float(input("Digite a coordenada Y da origem: "))
x2 = float(input("Digite a coordenada X do destino: "))
y2 = float(input("Digite a coordenada Y do destino: "))

# Calculando a distância linear
distancia = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Imprimindo o resultado
print("A distância linear entre as coordenadas é: {:.2f}".format(distancia))