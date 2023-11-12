# Dicionários

# Criando dicionários

dicionário = {}
dicionário = dict()

dicionário = { "nome": "Willian", "idade": 24, "altura": 1.75 }

print (dicionário)
print (dicionário ["idade"])

# Adicionando elementos em um dicionário

dicionário["Palmeirense"] = True
dicionário["nome"] = "Willian Mateus Maruci"

print (dicionário)

# Iterações sobre um dicionário

for chave in dicionário:
    print (chave, dicionário[chave])

# Testando a chave de um dicionário

print ("peso" in dicionário)
print ("altura" in dicionário)