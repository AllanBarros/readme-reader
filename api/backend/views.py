from django.http.response import JsonResponse
import requests
import json

def get_readme(request):
    dados_readme = []

    lista_repositorios = get_repos_list()
    for i, repositorio in enumerate(lista_repositorios):
        url_repositorio = 'https://api.github.com/repos/allan-testing-organization/' + repositorio + '/readme'
        result = requests.get(url_repositorio)
        link_arquivo_html = json.loads(result.content)
        arquivo = requests.get(link_arquivo_html['download_url'])
        dados_readme.append(str(arquivo.content))

    return JsonResponse({'resultado':dados_readme})

def get_repos_list():

    lista_repositorios = []

    result = requests.get('https://api.github.com/orgs/allan-testing-organization/repos')
    resultados = json.loads(result.content)
    for repositorio in resultados:
        lista_repositorios.append(repositorio['name'])
    return lista_repositorios
    