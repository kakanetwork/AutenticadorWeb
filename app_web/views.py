from django.shortcuts import render
from .models import Usuario_BD
from django.contrib.auth.hashers import make_password, check_password
from django.conf import settings
import requests

 # definindo variáveis sensíveis do recaptcha
recaptcha_site_key = settings.RECAPTCHA_SITE_KEY

def captcha_verify(captcha):
    secret_key = settings.RECAPTCHA_SECRET_KEY
    dados = requests.post(
        'https://www.google.com/recaptcha/api/siteverify',
        data={
            'secret': secret_key,
            'response': captcha
        }
    )
    result = dados.json()
    if result['success']:
        return True
    else:
        return False

# Função para a página de cadastro
def cadastro(request): 
    mensagem_erro = None
    mensagem_sucesso = None

    # Verifica se a requisição é POST ou Outra (Get...)
    if request.method == 'POST': 

        # Se Post: realiza o filtro do formulário enviado e adição do usuário ao BD
        novo_usuario = Usuario_BD()

        captcha = request.POST.get('g-recaptcha-response') # capturando o resultado do recaptcha
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        conf_senha = request.POST.get('conf_senha') # capturando o resultado da confirmação de senha

        # Verificação de senha 
        if senha != conf_senha:
            mensagem_erro = 'As senhas não coincidem. Digite sua senha novamente.'
            return render(request, 'users/cadastro.html', {'mensagem_erro': mensagem_erro, 'recaptcha_site_key': recaptcha_site_key})

        # Verificação se email já é cadastrado
        verifica = Usuario_BD.objects.filter(email=email).first()
        if verifica:
            mensagem_erro = 'Você já possui cadastro com esse email.'
            return render(request, 'users/cadastro.html', {'mensagem_erro': mensagem_erro, 'recaptcha_site_key': recaptcha_site_key})

        # Verificação do recaptcha
        if captcha_verify(captcha) == False:
            mensagem_erro = 'O reCAPTCHA não foi realizado corretamente, tente novamente.'
            return render(request, 'users/cadastro.html', {'mensagem_erro': mensagem_erro, 'recaptcha_site_key': recaptcha_site_key})
        
        # Adição do usuário ao banco de dados 
        novo_usuario.email = email
        novo_usuario.senha = make_password(senha) # realizando a criptografia da senha antes da inserção no BD
        novo_usuario.save() 

        # Informando o sucesso do cadastro
        mensagem_sucesso = 'Seu cadastro foi concluído com sucesso!'
        return render(request,'users/cadastro.html', {'mensagem_sucesso': mensagem_sucesso, 'recaptcha_site_key': recaptcha_site_key})
    
    # Se requisição for GET, realiza apenas o render do HTML
    else:
        # passo junto ao render do html, a hash do recaptcha para marcação
        return render(request, 'users/cadastro.html', {'recaptcha_site_key': recaptcha_site_key}) 


# =============================================================================================================================


# Função para a página de Login
def login(request):

    # Verifica se a requisição é POST ou Outra (Get...)
    if request.method == 'POST':
        captcha = request.POST.get('g-recaptcha-response') # capturando o resultado do recaptcha
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        # Verificação do recaptcha
        if captcha_verify(captcha) == False:
            mensagem_erro = 'O reCAPTCHA não foi realizado corretamente, tente novamente.'
            return render(request, 'users/login.html', {'mensagem_erro': mensagem_erro, 'recaptcha_site_key': recaptcha_site_key})

        try:
            # faço a verificação se o email existe no BD
            usuario_email = Usuario_BD.objects.get(email=email) 

            # faço a verificação se a senha também existe associada ao email anterior
            verifica_senha = check_password(senha, usuario_email.senha)

            # retorno a página se estiver tudo correto ou retorno erro 
            if verifica_senha:
                return render(request, 'users/homepage.html')
            else:
                raise Usuario_BD.DoesNotExist # para reaproveitar a mensagem de erro (é a mesma)
        except Usuario_BD.DoesNotExist:
            mensagem_erro = 'A senha ou email informados estão incorretos!'
            return render(request, 'users/login.html', {'mensagem_erro': mensagem_erro, 'recaptcha_site_key': recaptcha_site_key})
        
        # Se requisição for GET, realiza apenas o render do HTML
    else:
        return render(request, 'users/login.html', {'recaptcha_site_key': recaptcha_site_key})
    

def contato(request):
    return render(request, 'users/contatos.html')