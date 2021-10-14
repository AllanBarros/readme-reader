import requests
import json
from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.http import HttpResponse

def get_readme(request, slug):
    """Função para busca, leitura e gravação em banco de dados dos readme's de uma organização"""
    #slug é o nome da organização
    lista_repositorios = get_repos_list(slug)
    
    lista_readme = []

    for repositorio in lista_repositorios:

        link_arquivo_html = get_readme_html_link(repositorio, slug)

        arquivo = get_readme_content(link_arquivo_html['download_url'])

        lista_readme.append({'conteudo':str(arquivo.content), 'Repositorio':repositorio, 'Organizacao':slug})

    enviar_dados_readme(lista_readme)

    if request:
        return HttpResponse("E-mail com relatório enviado!")
    return True

    

def get_repos_list(org):
    """Função para busca de todos os repositórios dado uma organização específica"""
    
    lista_repositorios = []
    link_org = 'https://api.github.com/orgs/' + org +'/repos'

    result = requests.get(link_org)

    if result.status_code == 404:
        result.raise_for_status()

    resultados = json.loads(result.content)
    
    for repositorio in resultados:
        lista_repositorios.append(repositorio['name'])
    
    return lista_repositorios
    
def get_readme_html_link(repositorio, org):
    """ Função para busca do link para arquivo html do readme"""
    url_repositorio = 'https://api.github.com/repos/'+ org + '/' + repositorio + '/readme'

    result = requests.get(url_repositorio)
    
    if result.status_code == 404:
        result.raise_for_status()
        
    link_arquivo_html = json.loads(result.content)
    return link_arquivo_html

def get_readme_content(link_arquivo_html):
    """ Função para pegar o conteudo dos readmes localizados"""
    arquivo = requests.get(link_arquivo_html)
    if arquivo.status_code == 404:
        arquivo.raise_for_status()

    return arquivo

def enviar_dados_readme(lista):

    message = EmailMessage(
        subject = 'Relatorio',
        body = render_to_string("readme-report.html",{'lista': lista}),
        from_email = settings.DEFAULT_TO_EMAIL,
        to = [settings.DEFAULT_TO_EMAIL],
    )

    return message.send(fail_silently=False)
