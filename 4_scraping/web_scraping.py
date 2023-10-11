##
# Mantido: Marcos Antonio de Carvalho
# eMAil..: marcos.antonio.carvalho@gmail.com
# GitHub.: https://github.com/owl-arch
# Descr..: Faz Web Scraping na pagina da Kabun em
#         todas as paginas de Cadeiras Game
##
# Codifike
# Como fazer web scraping com python em sites dinâmicos // O site muda toda hora
# https://www.youtube.com/watch?v=VGroXCEaBiA&t=29s
##
# Library:
#  requests - Requisições HTTP
#  bs4 - Scraping
#  re - Expresões Regulares
#  Pandas - tratamento de Dataframes
##

# requests - Requisições HTTP
import requests

# bs4 - Scraping
from bs4 import BeautifulSoup

# re - Expresões Regulares
import re

# Pandas - tratamento de Dataframes
import pandas as pd

# math - Cálculos
import math

# Pesquisa pela inspeção do Browse
url = 'https://www.kabum.com.br/espaco-gamer/cadeiras-gamer'

# no browse 'myuser agent'
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}

# Captura o conteúdo e passa pelo parser
site = requests.get(url, headers=headers)
soup = BeautifulSoup(site.content, 'html.parser')

itens = soup.find('div', id='listingCount').get_text().strip()
print(itens)

index = itens.find(' ')
qtd = itens[:index]
print(index)  # posição do index
print(qtd)    # quantidade de itens

ultima_pagina = math.ceil(int(qtd)/20)

dict_produtos = {'marca': [], 'preco': []}

for i in range(1, ultima_pagina+1):

    # Captura o conteúdo da página e passa pelo parser
    url_page = f'https://www.kabum.com.br/espaco-gamer/cadeiras-gamer?page_number={i}&page_size=20&facet_filters=&sort=most_searched'
    site = requests.get(url_page, headers=headers)
    soup = BeautifulSoup(site.content, 'html.parser')
    # Procure em uma div que contém productCard
    produtos = soup.find_all('div', class_=re.compile('productCard'))

    for produto in produtos:
        # Procure em um span que contém nameCard
        marca = produto.find('span', class_=re.compile(
            'nameCard')).get_text().strip()

        # Procure em um span que contém priceCard
        preco = produto.find('span', class_=re.compile(
            'priceCard')).get_text().strip()

        print(marca, preco)

        dict_produtos['marca'].append(marca)
        dict_produtos['preco'].append(preco)

    print(url_page)

    # Dataframe
    df = pd.DataFrame(dict_produtos)
    df.to_csv('preco_cadeira.csv', encoding='utf-8', sep=';')
