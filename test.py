import requests
from datetime import datetime
import json

import pytz

import pycountry_convert as pc

chave = '1e1f7645e061867dfaa9062b4f587e9b'
cidade = 'Bangalore'
api_link = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'.format(cidade, chave)

# Fazendo a requisição
r = requests.get(api_link)

dados = r.json()

pais_codigo = dados['sys']['country']

zona_fuso = pytz.country_timezones[pais_codigo]

pais = pytz.country_names[pais_codigo]

zona = pytz.timezone(zona_fuso[0])
zona_horas = datetime.now(zona)
zona_horas = zona_horas.strftime("%d %m %Y | %H:%M:%S %p")


tempo = dados['main']['temp']
pressao = dados['main']['pressure']
umidade = dados['main']['humidity']
velocidade = dados['wind']['speed']
descricao = dados['weather'][0]['description']


def pais_para_continente(i):
  pais_alpha = pc.country_name_to_country_alpha2(i)
  pais_continent_codigo = pc.country_alpha2_to_continent_code(pais_alpha)
  pais_continente_nome = pc.convert_continent_code_to_continent_name(pais_continent_codigo)

  return pais_continente_nome

continente = pais_para_continente(pais)





