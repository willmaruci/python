# While

# Exemplo 1

numero_sorteado = 7
numero_escolhido = int(input("Digite um número entre 1 e 10: "))

while numero_sorteado != numero_escolhido:
    print ("Você errou, tente novamente...")
    numero_escolhido = int(input("Digite um número entre 1 e 10: "))

print ("Parabéns, você acertou!")

# Exemplo 2

contador = 0

while contador < 5:
    print (contador)

    contador = contador + 1
    
