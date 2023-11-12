# Estruturas de Condição

idade = int(input ("Digite sua idade: "))

if idade >= 18:
    print ("Você é maior de idade")
else:
    print ("Você é menor de idade")

"""
Imprima aprovado(a) se o estudante tenha uma média superior ou igual a 7, 
e reprovado se a média for menor que 7

"""

"""
media = float(input("Digite a média final do estudante: "))

if media >= 7:
    print ("Aprovado(a)")
elif media >= 5:
    print ("Recuperação")
else:
    print ("Reprovado(a)")
"""

media = float(input("Digite a média do estudante: "))
presença = float (input("Digite o percentual de presença do estudante: "))

if media >= 7 and presença >= 50:
    print ("Aprovado(a)")
else:
    print("Reprovado(a)")
