# Projeto Autenticador Web

Este é um projeto de exemplo onde criei um site de Login/Cadastro de Usuários em Django integrado ao SQLite, com a tecnologia reCAPTCHA para segurança adicional. Utilizando templates HTML/Bootstrap para proporcionar uma experiência personalizada aos usuários.

## Exemplos:
![Gif Site](https://imgur.com/a/Ex80iBa)

## Para utilizar este Projeto siga os passos abaixo:
### Clone este Repositório

<code> git clone https://github.com/kakanetwork/AutenticadorWeb </code>

### Configuração do Projeto Django
##### Antes de executar o projeto, é necessário configurar o Django e o reCAPTCHA.


```markdown
# Navegue até o diretório do projeto
cd AutenticadorWeb 

# Crie um ambiente virtual
python -m venv nome-do-ambiente

# Ative o ambiente virtual (windows)
./venv/script/activate.ps1 

# Ative o ambiente virtual (linux)
./venv/bin/activate

# Instalação de Dependências
pip install -r requirements.txt 

# Aplique as migrações do Django para criar o banco de dados
python ./manage.py migrate

# Crie migrações (se necessário)
python ./manage.py makemigrations

# Inicie o servidor de desenvolvimento do Django
python manage.py runserver
```

##### Agora, o projeto Django estará rodando localmente em http://localhost:8000/.

### Configuração do reCAPTCHA
Para configurar o reCAPTCHA no seu projeto, siga os seguintes passos:

<b>1 - Visite o site do reCAPTCHA e registre o seu site para obter as chaves do reCAPTCHA.
2 - Abra o arquivo settings.py no diretório do projeto Django e adicione as chaves reCAPTCHA
</b>

##### settings.py:

<b>RECAPTCHA_PUBLIC_KEY = 'sua-chave-publica'
RECAPTCHA_PRIVATE_KEY = 'sua-chave-privada'</b>

No mesmo arquivo settings.py, configure a variável CSRF_TRUSTED_ORIGINS para confiar nas origens do seu site, substituindo 'https://autenticadorweb.up.railway.app' pela origem correta.


### Contribuição
<b>Fique à vontade para contribuir com melhorias para este projeto. Basta fazer um fork, criar um branch para sua feature e enviar um pull request.</b>

<code>by kakanetwork</code>