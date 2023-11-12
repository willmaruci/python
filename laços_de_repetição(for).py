# For

# Exemplo 1

"""for x in range(10):
    print (x)"""

"""for x in range(1, 10):
    print (x)"""

"""for x in range(1, 15, 3):
    print (x)"""

# Exercício

"""nota1 = float(input("Digite sua nota 1: "))
nota2 = float(input("Digite sua nota 2: "))
nota3 = float(input("Digite sua nota 3: "))"""

soma = 0

for x in range(1, 4):
    nota = float(input(f"Digite sua nota {x}:"))

    soma = soma + nota

print (soma / 3)