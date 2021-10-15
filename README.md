# readme-reader

## Como rodar

A aplicação está funcionando em docker que para ser iniciado só precisa do comando abaixo Na pasta raiz da aplicação

> docker-compose up --build

Para o funcionamento correto de todas as funções é necessário criar um arquivo local.env no seguinte formato:

PYTHONUNBUFFERED=1
DEBUG=1
DB-NAME='nome_banco'
DB-USER='usuario_banco'
DB-PASSWORD='senha_banco'
DB-HOST='db'
SECRET_KEY='secret_key'
EMAIL_TO='email'
EMAIL_FROM='email'
EMAIL_HOST_USER='email'
EMAIL_HOST_PASSWORD='senha_email'

## Testes

O último teste realizado teve a seguinte cobertura:

Name                             Stmts   Miss  Cover
----------------------------------------------------
api/__init__.py                      2      0   100%
api/backend/__init__.py              0      0   100%
api/backend/tests/__init__.py        0      0   100%
api/backend/tests/test_gets.py      30      0   100%
api/backend/views.py                43     13    70%
api/celery.py                        9      0   100%
----------------------------------------------------
TOTAL                               84     13    85%


Caso seja interessante é possível rodar os teste seguindo esses comandos:

> docker exec -ti <container> bash

> coverage run -m pytest

> coverage report


## Arquitetura

Foram utilizadas as seguintes tecnologias:

Python com Django para toda a aplicação;
Celery com RabbitMQ para o schedule da busca;
Postgres como banco de dados (por mais que não esteja sendo usado nesse momento);

## Próximos passos

Adicionar o Gunicorn web server e o Nginx como proxy reverso;
Criação de multiplos .env;
Realizar o deploy da aplicação no Heroku;
Melhorar segurança da aplicação;



