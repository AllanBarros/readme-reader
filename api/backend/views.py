import requests
import json
from django.shortcuts import render
from django.core.exceptions import ValidationError
from django.http.response import JsonResponse
from .models import Relatorio

def get_readme(request, slug):
    """Função para busca, leitura e gravação em banco de dados dos readme's de uma organização"""
    #slug é o nome da organização
    lista_repositorios = get_repos_list(slug)

    for repositorio in lista_repositorios:

        link_arquivo_html = get_readme_html_link(repositorio, slug)

        arquivo = get_readme_content(link_arquivo_html['download_url'])

        dado_salvo = salvar_dados_readme(str(arquivo.content), repositorio, slug)

    return JsonResponse({'Resposta':'Readmes atualizados no link do relatório.'})

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

def salvar_dados_readme(dado, rep, org):
    """ Salvar dados dos readmes para demonstração futura"""
    try:
        Relatorio.objects.create(dados=dado, repositorio=rep, organizacao=org)
    except:
        raise ValidationError('Não foi possível adicionar o relatório a base de dados')

    return True

def relatorio_render(request):
    """ Renderizar relatório com os dados dos readmes"""
    lista_readme = Relatorio.objects.all()

    context = {'lista':lista_readme}

    return render(request, 'readme-report.html', context)