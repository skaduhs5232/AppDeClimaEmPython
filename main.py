import tkinter
from tkinter import *
from tkinter import ttk

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
janela.mainloop()