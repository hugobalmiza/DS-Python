# Versão da Linguagem Python
from platform import python_version
print('Versão da Linguagem Python Usada Neste Jupyter Notebook:', python_version())

# Biblioteca usada para requisitar uma página de um web site
import urllib.request

# Definimos a url
# Verifique as permissões em https://www.python.org/robots.txt
with urllib.request.urlopen("https://www.python.org") as url:
    page = url.read()
	
# Imprime o conteúdo
print(page)

# Importando BeautifulSoup
from bs4 import BeautifulSoup

# Analise o html na variável 'page' e armazene-o no formato Beautiful Soup
soup = BeautifulSoup(page, "html.parser")

soup.title

soup.title.string

soup.a

soup.find_all("a")

tables = soup.find('table')

# Imprimindo resultado
print(tables)