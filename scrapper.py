from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

from typing import List, NamedTuple


class Pokemon(NamedTuple):
    id: int
    name: str
    avatar: str
    details_url: str
    types: List[str]
    total: int
    hp: int
    attack: int
    defense: int
    sp_atk: int
    sp_def: int
    speed: int
    entry: str


url = "https://pokemondb.net/pokedex/all"


# User agent para evitar que o site bloqueie o acesso
request = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

page = urlopen(request)
page_contet_bytes = page.read()
page_content = page_contet_bytes.decode('utf-8')

soup = BeautifulSoup(page_content, 'html.parser')

# Pegando a tabela de pokemons

pokemons_row = soup.find_all('table', id='pokedex')[
    0].find_all('tbody')[0].find_all('tr')
soup.find
counter = 1
for pokemon in pokemons_row:
    pokemon_td = pokemon.find_all('td')
    id = pokemon_td[0]['data-sort-value']
    img = pokemon_td[0].find("img")["src"]
    name = pokemon_td[1].find("a", class_="ent-name").text
    if pokemon_td[1].find_all("small"):
        name = pokemon_td[1].find_all("small")[0].text

    description_url = pokemon_td[1].find_all("a")[0]["href"]
    types = []
    for type in pokemon_td[2].find_all("a"):
        types.append(type.text)

    total = pokemon_td[3].text
    hp = pokemon_td[4].text
    attack = pokemon_td[5].text
    defense = pokemon_td[6].text
    sp_atk = pokemon_td[7].text
    sp_def = pokemon_td[8].text
    speed = pokemon_td[9].text

    entry_url = f'https://pokemondb.net{description_url}'

    request = Request(entry_url, headers={'User-Agent': 'Mozilla/5.0'})

    page = urlopen(request)
    page_contet_bytes = page.read()
    page_content = page_contet_bytes.decode('utf-8')

    soup = BeautifulSoup(page_content, 'html.parser')
    try:
        entry_text = soup.find_all('main')[0].find_all(
            "div", {"class": "resp-scroll"})[2].find_all("tr")[0].find_all("td")[0].text
    except:
        entry_text = ""

    pokemon_save = Pokemon(
        id=int(id),
        name=name,
        avatar=img,
        details_url=entry_url,
        types=types,
        total=int(total),
        hp=int(hp),
        attack=int(attack),
        defense=int(defense),
        sp_atk=int(sp_atk),
        sp_def=int(sp_def),
        speed=int(speed),
        entry=entry_text
    )
    counter = counter + 1
    print(pokemon_save.name)
    print("Total of scraping: " + str(round((counter/len(pokemons_row) * 100), 2)) + "%") 
    print("=====================================")
