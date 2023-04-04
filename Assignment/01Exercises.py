#  Exercise 01 ==============================================================================================================
#Leitura dos dados
weight = float(input("Entre com o peso: "))
height = float(input("Entre com a altura: "))

# Claculo e exibição do IMC
print(f'\nSeu IMC é {(weight / height ** 2):,.2f}')
#============================================================================================================================



#  Exercise 02 ==============================================================================================================
speed = float(input("Entre com a velocidade(m/s): "))

# Exibição em tela
print(f'\nSua velocidade é {(speed * 3.6):,.2f} km/h')
#============================================================================================================================



#  Exercise 03 ================================================ ==============================================================
routes = [] # estrutura de dados para armazenar os dados de cada trecho que vai ser lido

print("========================= Leitura dos dados ===========================")
for reding in range(4):
    distance = float(input(f"\nDistância do trecho {reding + 1}: "))
    time = float(input(f"Tempo do trecho {reding + 1}: "))
    routes.append({'distancia': distance, 'tempo': time})

print("=======================================================================\n")

speeds = [] # Velocidade média de cada trecho
times = [] # Todos os tempos percorridos

for route in routes:
    speed = round((route['distancia'] / route['tempo']), 2)
    speeds.append(speed)
    times.append(time)

# Aceleração entre dois trechos consecutivos
accelerations = []
for i in range(len(speeds) - 1):
    acceleration = round(((speeds[i + 1] - speeds[i]) / routes[i + 1]['tempo']), 2)
    accelerations.append(acceleration)

# Imprimindo os resultados
print(f"- Velocidades médias dos trechos: {speeds}")
print(f"- Velocidade média total: {round((sum(speeds) / sum(times)), 2)}")
print(f"- Acelerações entre trechos consecutivos: {accelerations}")
#============================================================================================================================



#  Exercise 04 ==============================================================================================================
import math #blibioteca para uso do cos, sin e radians

# No programa a gravidade é constante
gravity = 10

# Leitura dos dados
angle = float(input("Angulo com o solo: "))
time = int(input("Tempo(segundos): "))
initialSpeed = float(input("Velocidade inicial(m/s): "))
initialHeight =  float(input("Altura inicial(metros): "))

# Passar o angulo lido para radianos
radianAngle = math.radians(angle)

# Calculando a posição horizontal e a altura em função do tempo
print("============================================================================================\n")
for second in range(time):
    x = initialSpeed * math.cos(radianAngle) * second
    y = initialHeight + (initialSpeed * math.sin(radianAngle) * second) - ((1/2) * gravity * second **2)
    print(f"||| Tempo: {second}s ||| A posição horizontal: {x:.2f}m ||| Altura: {y:.2f}m |||")
print("============================================================================================\n")
#============================================================================================================================



#  Exercise 05 ==============================================================================================================
import math # importando a blibioteca math para fazer uso do sqrt

# Leitura do ponto de partida
print("====================================================\n")
x1 = float(input("Coordenada X da origem: "))
y1 = float(input("Coordenada Y da origem: "))

# Leitura do ponto de destino
print("====================================================\n")
x2 = float(input("Coordenada X do destino: "))
y2 = float(input("Coordenada Y do destino: "))

print("====================================================\n")

# Imprimindo a distância linear
print(f"Distância linear entre as coordenadas é: {math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2)):.2f}")
#============================================================================================================================