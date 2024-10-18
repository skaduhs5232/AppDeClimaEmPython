import tkinter
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import requests
from datetime import datetime
import json

import pytz

import pycountry_convert as pc

co0 = '#444466'
c01 = '#feffff'
c02 = '#6f9fbd'

fundo_dia = '#6cc4cc'
fundo_noite = '#484f60'
fundo_tarde = '#bfd86d'
fundo = fundo_dia
 
global imagem

janela = Tk()
janela.title('')
janela.geometry('320x350')
janela.configure(bg=fundo)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=157)

frame_top = Frame(janela, width=320, height=50, bg=c01, pady=0, padx=0)
frame_top.grid(row=1, column=0)

frame_corpo = Frame(janela, width=300, height=300, bg=fundo, pady=12, padx=0)
frame_corpo.grid(row=2, column=0, sticky=NW)

estilo = ttk.Style(janela)
estilo.theme_use('clam')


def informacao():
  chave = '1e1f7645e061867dfaa9062b4f587e9b'
  cidade = e_local.get()
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
  l_cidade['text'] = cidade + " - " + pais + " / " + continente
  l_data['text'] = zona_horas
  l_umidade['text'] = umidade
  l_pressao['text'] = "Pressao : "+str(pressao) + "atm"
  l_velocidade['text'] = "Velocidade do vento : "+ str(velocidade) + "m/s"
  l_descricao['text'] = descricao
  l_porcentagem['text'] = "%"
  l_nome['text'] = "Humidade"

  zona_periodo = datetime.now(zona)
  zona_periodo = zona_periodo.strftime("%H")

  global imagem

  zona_periodo = int(zona_periodo)

  if zona_periodo <= 5:
    imagem = Image.open(r'imagens/noite.png')  
    fundo = fundo_noite
  elif zona_periodo<=11:
    imagem = Image.open(r'imagens/dia.png')  
    fundo = fundo_dia
  elif zona_periodo<=17:
      imagem = Image.open(r'imagens/nublado.png')  
      fundo = fundo_tarde
  elif zona_periodo<=23:
      imagem = Image.open(r'imagens/noite.png')  
      fundo = fundo_noite
  else:
     pass    


  imagem = imagem.resize((130, 130))
  imagem = ImageTk.PhotoImage(imagem)
  
  l_icon = Label(frame_corpo, image=imagem, bg=fundo)  # Alterado de text para image
  l_icon.place(x=160, y=50)

  janela.configure(bg=fundo)
  frame_top.configure(bg=fundo)
  frame_corpo.configure(bg=fundo)

  l_cidade['bg'] = fundo
  l_data['bg'] = fundo
  l_umidade['bg'] = fundo
  l_pressao['bg'] = fundo
  l_velocidade['bg'] = fundo
  l_descricao['bg'] = fundo
  l_porcentagem['bg'] = fundo
  l_nome['bg'] = fundo


e_local = Entry(frame_top, width=20, justify='left', font=("", 14), highlightthickness=1, relief='solid')
e_local.place(x=15, y=10)

b_local = Button(frame_top, command=informacao ,text='Ver Clima', bg=c01, fg=c02, font=("Ivy 9 bold"), relief='raised', overrelief=RIDGE)
b_local.place(x=250, y=10)

l_cidade = Label(frame_corpo, text='', anchor='center', bg=fundo, fg=c01, font=("Arial 13"))
l_cidade.place(x=10, y=4)

l_data = Label(frame_corpo, text='', anchor='center', bg=fundo, fg=c01, font=("Arial 10"))
l_data.place(x=10, y=54)

l_umidade = Label(frame_corpo, text='', anchor='center', bg=fundo, fg=c01, font=("Arial 45"))
l_umidade.place(x=10, y=100)

l_porcentagem = Label(frame_corpo, text='', anchor='center', bg=fundo, fg=c01, font=("Arial 10 bold"))
l_porcentagem.place(x=85, y=110)

l_nome = Label(frame_corpo, text='', anchor='center', bg=fundo, fg=c01, font=("Arial 10 bold"))
l_nome.place(x=85, y=140)

l_pressao = Label(frame_corpo, text='', anchor='center', bg=fundo, fg=c01, font=("Arial 10"))
l_pressao.place(x=10, y=184)

l_velocidade = Label(frame_corpo, text='', anchor='center', bg=fundo, fg=c01, font=("Arial 10"))
l_velocidade.place(x=10, y=212)

# Correções na carga da imagem




l_descricao = Label(frame_corpo, text='', anchor='center', bg=fundo, fg=c01, font=("Arial 14"))
l_descricao.place(x=170, y=190)

janela.mainloop()
