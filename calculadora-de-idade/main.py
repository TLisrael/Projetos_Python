from tkinter import *
from tkinter import ttk

from tkcalendar import Calendar, DateEntry
# Definição de cores
main_color = '#242526'
gray_color = '#d1d1d1'
white_color = '#FFFFFF'
black_color = '#000000'
blue_color = '#395285'
orange_color = '#ffa940'

# Criando janela
janela = Tk()
# Nome da janela
janela.title('Calculadora de idade')
# Impondo largura e altura da janela
janela.geometry('310x400')


# Dividindo tela
frame_cima = Frame(janela, width=310, height=140, bg=black_color, pady=0, relief=FLAT)
frame_cima.grid(row=0, column=0)
frame_baixo = Frame(janela, width=310, height=300, bg=black_color, pady=0, relief=FLAT)
frame_baixo.grid(row=1, column=0)

# ----------- Criando labels para frame cima -----------

l_calculadora = Label(frame_cima, text='CALCULADORA', width=25, height=1, padx=3, relief=FLAT, anchor='center', font=('Ivi 15 bold'), bg=black_color, fg=white_color)
l_calculadora.place(x=0, y=30)

l_idade = Label(frame_cima, text='DE IDADE', width=11, height=1, relief=FLAT, anchor='center', font='Arial 35 bold', bg=black_color, fg=orange_color)
l_idade.place(x=0, y=70)


# ----------- Criando labels para frame de baixo

l_data_inicial = Label(frame_baixo, text='Data inicial', height=1, padx=0,pady=0, relief=FLAT, anchor=NW, font='Arial 11', bg=black_color, fg=white_color)
l_data_inicial.place(x=50, y=30)

cal_1 = DateEntry(frame_baixo, width=13, bg='darkblue', fg=white_color, borderwidth=2, date_patter='mm/dd/y', y=2022)
cal_1.place(x=170, y=30)

l_data_nascimento = Label(frame_baixo, text='Data de nascimento', height=1, padx=0,pady=0, relief=FLAT, anchor=NW, font='Arial 11', bg=black_color, fg=white_color)
l_data_nascimento.place(x=50, y=70)


#
janela.mainloop()

