# ================== Primeiro exercicio =========================================================================
#Leitura nota 1
primeiraNota = float(input("Digitar primeira nota: "))

#Leitura nota 2
segundaNota = float(input("Digite a segunda nota: "))

#MEDIA
media = (primeiraNota + segundaNota) / 2

#Exibe o resultado
print("Media= ", media)
#  ==============================================================================================================

#  ================== Segundo exercicio =========================================================================
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
