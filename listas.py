# Listas

# Antes

nota1 = 9
nota2 = 8
nota3 = 10

# Com listas

notas = [9, 8, 10]

# Criando listas

lista = []
lista = list()
lista = ["Willian", 24, 3.14, True]
lista_de_listas = [7, [14, 15]]

# Indexação e Fatiamentos(slices)

lista = ["Willian", 24, 3.14, True]

print (lista[0])
print (lista[1])
print (lista[2])
print (lista[3])
print (lista[-1])

# Slices

lista = [7, 13, 14, 19, 24, 33, 51]

print (lista[0:3])
print (lista[3:7])
print (lista[2:])
print (lista[1:5:2])

# Iterações com for

## Utilizando os próprios elementos da lista

for elemento in lista:
    print (elemento)

### Utilizando os índices

lista = [7, 13, 14, 19, 24, 33, 51]

print ("Comprimento da lista: ", len(lista))

for x in range(len(lista)):
    print (lista[x])


# Métodos de Listas

lista = [7, 13, 14, 19, 24, 33, 51]

# append

print ("Antes do append: ", lista)

lista.append(3)

print ("Depois do append: ", lista)
 
# insert

lista.insert(3, 16)

print("Depois do insert: ", lista)

# extend

lista2 = [1, 3, 5]
lista.extend(lista2)

print ("Depois do extend: ", lista) 

# pop

lista.pop()
lista.pop(3)

print ("Lista após o pop: ", lista)

# remove

lista.remove(13)

print ("Lista após o remove: ", lista)

# count

print ("Quantidade de 3 na lista: ", lista.count(3))

# index

print ("O elemento 19 está no index: ", lista.index(19))

# sort

lista.sort(reverse=True)

print (lista)


# Funções para listas

# len

print (len(lista))

# sum

print (sum(lista))

# max

print ("O maior elemento da lista é: ", max(lista))

# min

print ("O maior elemento da lista é: ", min(lista))