from django.http.response import JsonResponse
import requests
import json

def get_readme(request, slug):
    """Função para busca e leitura dos readme's de uma organização"""
    
    dados_readme = []

    lista_repositorios = get_repos_list(slug)

    for repositorio in lista_repositorios:

        link_arquivo_html = get_readme_html_link(repositorio, slug)

        arquivo = get_readme_content(link_arquivo_html['download_url'])

        dados_readme.append(str(arquivo.content))

    return JsonResponse({'resultado':dados_readme})

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

    url_repositorio = 'https://api.github.com/repos/'+ org + '/' + repositorio + '/readme'

    result = requests.get(url_repositorio)
    
    if result.status_code == 404:
        result.raise_for_status()
        
    link_arquivo_html = json.loads(result.content)
    return link_arquivo_html

def get_readme_content(link_arquivo_html):

    arquivo = requests.get(link_arquivo_html)
    if arquivo.status_code == 404:
        arquivo.raise_for_status()

    return arquivo