# Função

"""Funções já utilizadas

print (): imprime uma mensagem (int, str, float) no console (terminal, cmd)
input (): retorna uma informação dada pelo usuário e pode receber uma string
len (): recebe uma lista e retorna o tamanho dessa lista
max (): retorna o maior valor de uma lista"""

## Criação de funções

# Função inicial

def saudaçao():
    print ("Olá, seja bem vindo(a)!")
    print("É um prazer contar com você nessa empresa!")
saudaçao()

# Função com parâmetros

def saudaçao(nome, empresa):
    print (f"Olá, seja bem vindo(a) {nome}!")
    print(f"É um prazer contar com você aqui na {empresa}!")
saudaçao("Willian", "Electrolux")
saudaçao("Vandressa", "Santa Casa")

# Função com parâmetro default

def saudaçao(nome, empresa="Serasa Experian"):
    print (f"Olá, seja bem vindo(a) {nome}!")
    print (f"É um prazer contar com você aqui na {empresa}!")
saudaçao ("Willian")

# Funções com retorno

def soma (num1, num2):
    return num1 + num2

resultado = soma(10, 10)

print ("O resultado da soma é", resultado)

def calculadora(num1, num2, operação="+"):
    if operação == "+":
        return num1 + num2
    elif operação == "-":
        return num1 - num2
    elif operação =="*":
        return num1 * num2

resultado1 = calculadora(456, 743)
resultado2 = calculadora(89, 65, "-")
resultado3 = calculadora(147, 563, "*" )

print (resultado1)
print (resultado2)
print (resultado3)