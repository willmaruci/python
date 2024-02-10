# Front-End -> O que o usuário vê/interage
# Back-End -> O que o usuário não vê, isto é, a lógica por trás do site

# Frameworks

# Django
# Flask
# Flet

# Título do chat
# Botão de iniciar o chat
    # Pop-up
        # Bem vindo ao Hashzap
        # Escreva seu nome
        #   Entrar no chat
# Chat
    # Will entrou no chat
    # Mensagens do usuário
# Campo para enviar mensagens
# Botão de enviar

import flet

def main(pagina):
    titulo = flet.Text('Hashzap')
    pagina.add(titulo)

    nome_usuario = flet.TextField(label='Escreva seu nome')

    chat = flet.Column()

    def enviar_mensagem_tunel(informacoes):
        chat.controls.append(flet.Text(informacoes))
        pagina.update()
    pagina.pubsub.subscribe(enviar_mensagem_tunel)
    
    def enviar_mensagem(evento):
        texto_campo_mensagem = f'{nome_usuario.value}: {campo_mensagem.value}'
        chat.controls.append(flet.Text(texto_campo_mensagem))

        pagina.pubsub.send_all(texto_campo_mensagem)

        # limpar o campo_mensagem
        campo_mensagem.value = ''
        pagina.update()

    campo_mensagem = flet.TextField(label='Escreva sua mensagem aqui')

        
    botao_enviar = flet.ElevatedButton('Enviar', on_click=enviar_mensagem)

    def entrar_chat(evento):
        # Fechar o popup
        popup.open = False

        # Tirar o botão "Iniciar chat" da tela
        pagina.remove(botao_iniciar)

        # Adicionar o nosso chat
        pagina.add(chat)

        # Criar o campo de enviar mensagem
        linha_mensagem = flet.Row(
            [campo_mensagem, botao_enviar]
        )
        pagina.add(linha_mensagem)

        #  Botão de enviar mensagem
        texto = f'{nome_usuario.value} entrou no chat'
        chat.controls.append(flet.Text(texto))
        pagina.update()

    popup = flet.AlertDialog(
        open=False,
        modal=True,
        title=flet.Text('Bem Vindo ao Hashzap'), 
        content=nome_usuario,
        actions=[flet.ElevatedButton('Entrar', on_click=entrar_chat)]
        )


    def iniciar_chat(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()

    botao_iniciar = flet.ElevatedButton('Iniciar chat', on_click=iniciar_chat)

    pagina.add(botao_iniciar)
    
# flet.app (main)
flet.app(main, view=flet.WEB_BROWSER)
