from tkinter import *
from tkinter import ttk

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
frame_cima = Frame(janela, width=310, height=140, bg=orange_color, pady=0, relief=FLAT)
frame_cima.grid(row=0, column=0)
frame_baixo = Frame(janela, width=310, height=300, bg=black_color, pady=0, relief=FLAT)
frame_baixo.grid(row=1, column=0)

# Criando labels para frame cima

l_calculadora = Label(frame_cima, text='Calculadora', width=25, height=1, padx=3, relief=FLAT, anchor='center', font=('Ivy 15 bold'), bg=orange_color,)
l_calculadora.place(x=0, y=30)

janela.mainloop()

