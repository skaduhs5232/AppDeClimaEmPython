import tkinter
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

co0 = '#444466'
c01 = '#feffff'
c02 = '#6f9fbd'

fundo_dia = '#6cc4cc'
fundo_noite = '#484f60'
fundo_tarde = '#bfd86d'
fundo = fundo_dia

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

e_local = Entry(frame_top, width=20, justify='left', font=("", 14), highlightthickness=1, relief='solid')
e_local.place(x=15, y=10)

b_local = Button(frame_top, text='Ver Clima', bg=c01, fg=c02, font=("Ivy 9 bold"), relief='raised', overrelief=RIDGE)
b_local.place(x=250, y=10)

l_cidade = Label(frame_corpo, text='Ver Clima', anchor='center', bg=fundo, fg=c01, font=("Arial 13"))
l_cidade.place(x=10, y=4)

l_data = Label(frame_corpo, text='teste', anchor='center', bg=fundo, fg=c01, font=("Arial 10"))
l_data.place(x=10, y=54)

l_umidade = Label(frame_corpo, text='84', anchor='center', bg=fundo, fg=c01, font=("Arial 45"))
l_umidade.place(x=10, y=100)

l_porcentagem = Label(frame_corpo, text='%', anchor='center', bg=fundo, fg=c01, font=("Arial 10 bold"))
l_porcentagem.place(x=85, y=110)

l_nome = Label(frame_corpo, text='Humidade', anchor='center', bg=fundo, fg=c01, font=("Arial 10 bold"))
l_nome.place(x=85, y=140)

l_pressao = Label(frame_corpo, text='Pressão : ', anchor='center', bg=fundo, fg=c01, font=("Arial 10"))
l_pressao.place(x=10, y=184)

l_velocidade = Label(frame_corpo, text='Velocidade do vento : ', anchor='center', bg=fundo, fg=c01, font=("Arial 10"))
l_velocidade.place(x=10, y=212)

# Correções na carga da imagem
imagem = Image.open(r'imagens/dia.png')  # Usar r'' ou barra normal
imagem = imagem.resize((130, 130))
imagem = ImageTk.PhotoImage(imagem)

l_icon = Label(frame_corpo, image=imagem, bg=fundo)  # Alterado de text para image
l_icon.place(x=160, y=50)

l_descricao = Label(frame_corpo, text='nublado: ', anchor='center', bg=fundo, fg=c01, font=("Arial 14"))
l_descricao.place(x=170, y=190)

janela.mainloop()
