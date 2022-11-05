# Importando tkinter
from tkinter import *
from tkinter import ttk


# Definição de cores
main_color = '#242526' # cinza
white_color = '#FFFFFF'
black_color = '#00000'
blue_color = '#395285'
orange_color = '#ff8f1f'

# Criando janela
main_janela = Tk()
# Setando nome para a janela
main_janela.title("Calculadora")
# Setando largura e comprimento
main_janela.geometry("235x318")

main_janela.config(bg=main_color)

# Criando display
frame_tela = Frame(main_janela, width=235, height=50, bg=blue_color)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(main_janela, width=235, height=268)
frame_corpo.grid(row=1, column=0)

# Criando botoes
b_1 = Button(frame_corpo, text='C', width=11, height=2)
b_1.place(x=0, y=0)

b_2 = Button(frame_corpo, text='%', width=5, height=2)
b_2.place(x=90, y=0)

b_3 = Button(frame_corpo, text='/', width=5, height=2)
b_3.place(x=177, y=0)
main_janela.mainloop()
