# Importando tkinter
from tkinter import *
from tkinter import ttk

# Definição de cores
main_color = '#242526'
gray_color = '#d1d1d1'
white_color = '#FFFFFF'
black_color = '#00000'
blue_color = '#395285'
orange_color = '#ffa940'

# Criando janela
main_janela = Tk()
# Setando nome para a janela
main_janela.title("Calculadora")
# Setando largura e comprimento
main_janela.geometry("235x310")

main_janela.config(bg=main_color)

# Criando display
frame_tela = Frame(main_janela, width=235, height=50, bg=blue_color)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(main_janela, width=235, height=268)
frame_corpo.grid(row=1, column=0)

# variavel todos valores
todos_valores = ''


# Criando função
def entrada_valores(event):
    global todos_valores
    todos_valores = todos_valores + str(event)
    # Passando valor para a tela
    valor_texto.set(todos_valores)


# Calculo de caracteres
def calcular():
    global todos_valores
    resultado = eval(todos_valores)

    valor_texto.set(str(resultado))


# Limpando a tela
def limpar_tela():
    global todos_valores
    todos_valores = ""
    valor_texto.set("")


# criando display
valor_texto = StringVar()

app_label = Label(frame_tela, textvariable=valor_texto, width=16, height=2, padx=7, relief=FLAT, anchor='e',
                  justify=RIGHT,
                  font=('Ivy 18'), bg=blue_color, fg=white_color)
app_label.place(x=0, y=0)

# Criando botoes
b_1 = Button(frame_corpo, text='C', width=11, height=2, bg=gray_color, font=('Ivy 13 bold'), relief=RAISED,
             overrelief=RIDGE, command=limpar_tela)
b_1.place(x=0, y=0)

b_2 = Button(frame_corpo, text='%', width=5, height=2, bg=gray_color, font=('Ivy 13 bold'), relief=RAISED,
             overrelief=RIDGE, command=lambda: entrada_valores('%'), )
b_2.place(x=118, y=0)

b_3 = Button(frame_corpo, text='/', width=5, height=2, bg=orange_color, fg=white_color, font=('Ivy 13 bold'),
             relief=RAISED, overrelief=RIDGE, command=lambda: entrada_valores('/'), )
b_3.place(x=177, y=0)

b_4 = Button(frame_corpo, text='7', width=5, height=2, bg=gray_color, font=('Ivy 13 bold'), relief=RAISED,
             overrelief=RIDGE, command=lambda: entrada_valores('7'), )
b_4.place(x=0, y=52)
b_5 = Button(frame_corpo, text='8', width=5, height=2, bg=gray_color, font=('Ivy 13 bold'), relief=RAISED,
             overrelief=RIDGE, command=lambda: entrada_valores('8'), )
b_5.place(x=59, y=52)
b_6 = Button(frame_corpo, text='9', width=5, height=2, bg=gray_color, font=('Ivy 13 bold'), relief=RAISED,
             overrelief=RIDGE, command=lambda: entrada_valores('9'), )
b_6.place(x=118, y=52)

b_7 = Button(frame_corpo, text='*', width=5, height=2, bg=orange_color, fg=white_color, font=('Ivy 13 bold'),
             relief=RAISED, overrelief=RIDGE, command=lambda: entrada_valores('*'), )
b_7.place(x=177, y=52)

b_8 = Button(frame_corpo, text='4', width=5, height=2, bg=gray_color, font=('Ivy 13 bold'), relief=RAISED,
             overrelief=RIDGE, command=lambda: entrada_valores('4'), )
b_8.place(x=0, y=104)
b_9 = Button(frame_corpo, text='5', width=5, height=2, bg=gray_color, font=('Ivy 13 bold'), relief=RAISED,
             overrelief=RIDGE, command=lambda: entrada_valores('5'), )
b_9.place(x=59, y=104)
b_10 = Button(frame_corpo, text='6', width=5, height=2, bg=gray_color, font=('Ivy 13 bold'), relief=RAISED,
              overrelief=RIDGE, command=lambda: entrada_valores('6'), )
b_10.place(x=118, y=104)

b_11 = Button(frame_corpo, text='-', width=5, height=2, bg=orange_color, fg=white_color, font=('Ivy 13 bold'),
              relief=RAISED, overrelief=RIDGE, command=lambda: entrada_valores('-'), )
b_11.place(x=177, y=104)

b_12 = Button(frame_corpo, text='1', width=5, height=2, bg=gray_color, font=('Ivy 13 bold'), relief=RAISED,
              overrelief=RIDGE, command=lambda: entrada_valores('1'), )
b_12.place(x=0, y=155)
b_13 = Button(frame_corpo, text='2', width=5, height=2, bg=gray_color, font=('Ivy 13 bold'), relief=RAISED,
              overrelief=RIDGE, command=lambda: entrada_valores('2'), )
b_13.place(x=59, y=155)
b_14 = Button(frame_corpo, text='3', width=5, height=2, bg=gray_color, font=('Ivy 13 bold'), relief=RAISED,
              overrelief=RIDGE, command=lambda: entrada_valores('3'), )
b_14.place(x=118, y=155)

b_15 = Button(frame_corpo, text='+', width=5, height=2, bg=orange_color, fg=white_color, font=('Ivy 13 bold'),
              relief=RAISED, overrelief=RIDGE, command=lambda: entrada_valores('+'), )
b_15.place(x=177, y=155)

b_16 = Button(frame_corpo, text='0', width=11, height=2, bg=gray_color, font=('Ivy 13 bold'), relief=RAISED,
              overrelief=RIDGE, command=lambda: entrada_valores('0'), )
b_16.place(x=0, y=208)

b_17 = Button(frame_corpo, text='.', width=5, height=2, bg=gray_color, font=('Ivy 13 bold'), relief=RAISED,
              overrelief=RIDGE, command=lambda: entrada_valores('.'), )
b_17.place(x=118, y=208)

b_18 = Button(frame_corpo, text='=', width=5, height=2, bg=orange_color, fg=white_color, font=('Ivy 13 bold'),
              relief=RAISED, overrelief=RIDGE, command=calcular, )
b_18.place(x=177, y=208)

main_janela.mainloop()
