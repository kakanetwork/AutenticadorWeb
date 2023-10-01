from django.shortcuts import render
from .models import Usuario_BD
from django.contrib.auth.hashers import make_password, check_password
from django.conf import settings

# Função para a página de cadastro
def cadastro(request): 
    recaptcha_site_key = settings.RECAPTCHA_SITE_KEY
    mensagem_erro = None
    mensagem_sucesso = None

    # Verifica se a requisição é POST ou Outra (Get...)
    if request.method == 'POST': 

        # Se Post: realiza o filtro do formulário enviado e adição do usuário ao BD
        novo_usuario = Usuario_BD()
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        conf_senha = request.POST.get('conf_senha')

        # Verificação de senha 
        if senha != conf_senha:
            mensagem_erro = 'As senhas não coincidem. Digite sua senha novamente.'
            return render(request, 'users/cadastro.html', {'mensagem_erro': mensagem_erro})

        # Verificação se email já é cadastrado
        verifica = Usuario_BD.objects.filter(email=email).first()
        if verifica:
            mensagem_erro = 'Você já possui cadastro com esse email.'
            return render(request, 'users/cadastro.html', {'mensagem_erro':mensagem_erro})

        # Adição do usuário ao banco de dados 
        try:
            novo_usuario.email = email
            novo_usuario.senha = make_password(senha) # realizando a criptografia da senha antes da inserção no BD
            novo_usuario.save() 
        except:
            mensagem_erro = 'Outro erro'
            return render(request, 'users/cadastro.html', {'mensagem_erro':mensagem_erro})

        # Informando o sucesso do cadastro
        mensagem_sucesso = 'Seu cadastro foi concluído com sucesso!'
        return render(request,'users/cadastro.html', {'mensagem_sucesso': mensagem_sucesso})
    
    # Se requisição for GET, realiza apenas o render do HTML
    else:
        return render(request, 'users/cadastro.html', {'recaptcha_site_key': recaptcha_site_key})


# =============================================================================================================================


# Função para a página de Login
def login(request):

    # Verifica se a requisição é POST ou Outra (Get...)
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')

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
            return render(request, 'users/login.html', {'mensagem_erro': mensagem_erro})
        
        # Se requisição for GET, realiza apenas o render do HTML
    else:
        return render(request, 'users/login.html')
    

def contato(request):
    return render(request, 'users/contatos.html')