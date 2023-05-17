from bs4 import BeautifulSoup
from urllib.request import Request, urlopen


url = "https://pokemondb.net/pokedex/all"


#User agent para evitar que o site bloqueie o acesso
request = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

page = urlopen(request)
page_contet_bytes = page.read()
page_content = page_contet_bytes.decode('utf-8')

soup = BeautifulSoup(page_content, 'html.parser')

# Pegando a tabela de pokemons
# print(soup.prettify())



