# Passo a Passo do Projeto

# pip install pyautogui

# pyautogui.press
# pyautogui.write
# pyautogui.click
# pyautogui.scroll

# Passo 1: Entrar no sistema da empresa
    # link: https://dlp.hashtagtreinamentos.com/python/intensivao/login

import pyautogui
import time

pyautogui.PAUSE = 2

# Aperta a tecla do Windows
pyautogui.press('win')
# Digita Google Chrome na pesquisa
pyautogui.write('google chrome')
# Aperta a tecla Enter
pyautogui.press('enter')
time.sleep(5)

# Passo 2: Fazer login

# Digita o link do sistema
link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
pyautogui.write(link)
# Aperta a tecla Enter
pyautogui.press('enter')
# Espera 5 segundos
time.sleep(5)
#  Clica na barra de login
pyautogui.click(x=583, y=417)
# Digita o login
pyautogui.write('will_maruci@hashtag.com')
# Aperta a tecla Tab
pyautogui.press('tab')
# Digita a senha
pyautogui.write('hashtag')
# Clica no botão Logar
pyautogui.click(x=672, y=573)
time.sleep(1)

# Passo 3: Importar a base de dados

# pip install pandas numpy openpyxl

import pandas

tabela = pandas.read_csv('produtos.csv')
print(tabela)

for linha in tabela.index:
    # Passo 4: Cadastrar um produto

    # Clica na barra do código do produto
    pyautogui.click(x=477, y=294)
    # Escreve o código do produto e passa para o próximo campo
    pyautogui.write(tabela.loc[linha, 'codigo'])
    pyautogui.press('tab')
    # Escreve a marca do produto
    pyautogui.write(tabela.loc[linha, 'marca'])
    pyautogui.press('tab')
    # Escreve o tipo do produto
    pyautogui.write(tabela.loc[linha, 'tipo'])
    pyautogui.press('tab')
    # Escreve a categoria do produto
    pyautogui.write(str(tabela.loc[linha, 'categoria']))
    pyautogui.press('tab')
    # Escreve o preço unitário do produto
    pyautogui.write(str(tabela.loc[linha, 'preco_unitario']))
    pyautogui.press('tab')
    # Escreve o custo do produto
    pyautogui.write(str(tabela.loc[linha, 'custo']))
    pyautogui.press('tab')
    # Escreve a observação sobre o produto
    obs = tabela.loc[linha, 'obs']
    if not pandas.isna(obs):
        pyautogui.write(obs)
    # Envia o produto
    pyautogui.press('tab')
    pyautogui.press('enter')
    pyautogui.scroll(1000)

# Passo 5: Repetir isso até acabar a base de dados



