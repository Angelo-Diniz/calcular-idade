# Calcular Idade

Este projeto é um aplicativo Flask que calcula a idade de um usuário com base na data de nascimento fornecida. Ele usa uma interface HTML responsiva com o Bootstrap e funciona como um Progressive Web App (PWA) para permitir o uso offline.

## Requisitos

- Python 3.6+
- Flask
- Gunicorn (opcional, para implantação em produção)

## Instalação

1. Clone este repositório:

git clone https://github.com/Angelo-Diniz/calcular-idade.git


2. Entre no diretório do projeto:

cd calcular-idade


3. Crie um ambiente virtual:

python -m venv venv



4. Ative o ambiente virtual:

- No Windows:
venv\Scripts\activate


- No Linux ou macOS:
source venv/bin/activate


5. Instale as dependências:

pip install -r requirements.txt


## Uso

Execute o aplicativo Flask localmente:
flask run


Abra um navegador e acesse: http://localhost:5000

## Implantação em produção

Para implantar o aplicativo em um servidor de produção, use o Gunicorn:
gunicorn app:app

## Funcionalidades

- Calcular a idade com base na data de nascimento fornecida
- Interface HTML responsiva usando Bootstrap
- Funciona como um Progressive Web App (PWA) para uso offline


## Licença

Livre






