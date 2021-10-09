import pytest
import requests
from ..views import get_repos_list, get_readme_html_link, get_readme_content

url_completa = 'http://localhost:8000/get-readme/allan-testing-organization/'
org_acerto = 'allan-testing-organization'
org_erro = 'allan-testings-organization'
link_arquivo_html = 'https://raw.githubusercontent.com/allan-testing-organization/test-2/main/README.md'
link_arquivo_html_erro = 'https://raw.githubusercontent.com/allan-testing-organization/test-3/main/README.md'
repositorio = 'test-2'

def test_repos_list():
    lista_repos = get_repos_list(org_acerto)
    assert len(lista_repos) == 2

def test_repos_list_fail():
    with pytest.raises(Exception):
        get_repos_list(org_erro)

def test_readme_html_link():
    link_arquivo_html = get_readme_html_link(repositorio ,org_acerto)
    assert link_arquivo_html

def test_readme_html_link_fail():
    with pytest.raises(Exception):
        get_readme_html_link(repositorio ,org_erro)

def test_readme_content():
    arquivo = get_readme_content(link_arquivo_html)
    assert arquivo

def test_readme_content_fail():
    with pytest.raises(Exception):
        get_readme_content(link_arquivo_html_erro)

def test_readme_complete():
    resultado = requests.get(url_completa)
    assert resultado.content  
