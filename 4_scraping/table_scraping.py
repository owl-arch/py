##
# Mantido: Marcos Antonio de Carvalho
# eMAil..: marcos.antonio.carvalho@gmail.com
# GitHub.: https://github.com/owl-arch
# Descr..: Faz Web Scraping na pagina da Kabun em
#         todas as paginas de Cadeiras Game
# Somente para Tabelas
##
# Codifike
# Web scraping com python pandas
# https://www.youtube.com/watch?v=mF9qEcQQdRs&t=316s
##
# Library:
#  requests - Requisições HTTP
#  Pandas - tratamento de Dataframes
##

# requests - Requisições HTTP
import requests

# Pandas - tratamento de Dataframes
import pandas as pd

import time

##
# Caso não utilize 'my user agent', sera enviado:
#   User-Agent: 'python-requests/2.26.0'
# Nesse caso, o seu scraping poderá ser detectado por um 'anti-bot'. 
##
# Então vamos usar no browse 'my user agent' para descobri nosso agente.
HEADERS = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}

##
# Target:
#  br.investing --> Mercados --> Ações --> Brasil
#  https://br.investing.com/equities/brazil
##
url = 'https://br.investing.com/equities/brazil'
    
result = requests.get(url, headers=HEADERS)
time.sleep(3)
#print(result.text)
print('ok')

# with já fecha automaticamente o arquivo depois de utilizado
with open('result.txt', 'w') as arquivo:
    arquivo.write(result.text)

df = pd.read_html(result.text)
#print(df)
