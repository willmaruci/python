# Random

"""
Exercício Proposto
Crie um script em Python que gere 6 números aleatórios para a Mega-Sena (neste jogo, 
você pode escolher dezenas de 1 até 60). Não pode repetir dezena.

"""

import random

for x in range (1, 6):
    print (f"Gerar número sorteado {x}: ", random.randint(1,61))