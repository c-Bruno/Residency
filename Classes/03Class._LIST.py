#  LIST [ ] ====================================================================
people = [
    ["Juvenal", 20 , 1.75, 60],
    ["Ana", 10 , 4.75, 50],
    ["Andre", 30 , 3.75, 40],
    ["Sandro", 40 , 2.75, 20]
]

# Listando Linhas
for row in people:
    print(row)

lista1 = list()
lista2 = []

num = [2, 5, 9, 1]

num.append(7) # vai add o numero 7 no fim

num.sort() # ordem crescente
num.sort(reverse=True) # ordem decrescente
len(num) # quantos elementos tem
num.insert(2, 0) # num.insert(posição, valor)
num.pop() # elimina o ultimo valor
num.pop(2) # elimina elemento da posição 2
num.remove(2) # elimina o primeiro elemento 2 que encontra

if 4 in num:
    num.remove(4)

a = [2, 3, 4, 7]
b = a # uma ligação entre as duas
b = a[:] # um clone


#  Dictionary { } ====================================================================
dicionario1 = dict()
dicionario2 = {}

dicionario2['nome'] = 'carlos'
dicionario2['media'] = 7
dicionario2['situacao'] = 'Aprovado'

for key,value in dicionario1.items():
    print(key + " => " + value)

dicionario1 = {
    'titulo': 'star wars',
    'ano': 1977,
    'diretor': 'george lucas'
}

filme = dicionario1.copy() # para copiar um dicionario nao se usa [:] e sim o copy()

print(dicionario2.values()) # carlos, 7, aprovado
print(dicionario2.keys()) # nome, media, situacao
print(dicionario2.items()) # keys e values

del dicionario2['media'] # apaga um item inteiro
for k, v in dicionario2.items():
    print(f' - {k} é igual a {v}')
# - nome é igual a carlos
# - situacao é igual a Aprovado