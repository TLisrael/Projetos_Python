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




# Criando botoes
b_1 = Button(frame_corpo, text='C', width=11, height=2, bg=gray_color, font=('Ivy 13 bold'), relief=RAISED,
             overrelief=RIDGE)
b_1.place(x=0, y=0)

b_2 = Button(frame_corpo, text='%', width=5, height=2, bg=gray_color, font=('Ivy 13 bold'), relief=RAISED,
             overrelief=RIDGE)
b_2.place(x=118, y=0)

b_3 = Button(frame_corpo, text='/', width=5, height=2, bg=orange_color, fg=white_color, font=('Ivy 13 bold'),
             relief=RAISED, overrelief=RIDGE)
b_3.place(x=177, y=0)

b_4 = Button(frame_corpo, text='7', width=5, height=2, bg=gray_color, font=('Ivy 13 bold'), relief=RAISED,
             overrelief=RIDGE)
b_4.place(x=0, y=52)
b_5 = Button(frame_corpo, text='8', width=5, height=2, bg=gray_color, font=('Ivy 13 bold'), relief=RAISED,
             overrelief=RIDGE)
b_5.place(x=59, y=52)
b_6 = Button(frame_corpo, text='9', width=5, height=2, bg=gray_color, font=('Ivy 13 bold'), relief=RAISED,
             overrelief=RIDGE)
b_6.place(x=118, y=52)

b_7 = Button(frame_corpo, text='*', width=5, height=2, bg=orange_color, fg=white_color, font=('Ivy 13 bold'),
             relief=RAISED, overrelief=RIDGE)
b_7.place(x=177, y=52)


b_8 = Button(frame_corpo, text='4', width=5, height=2, bg=gray_color, font=('Ivy 13 bold'), relief=RAISED,
             overrelief=RIDGE)
b_8.place(x=0, y=104)
b_9 = Button(frame_corpo, text='5', width=5, height=2, bg=gray_color, font=('Ivy 13 bold'), relief=RAISED,
             overrelief=RIDGE)
b_9.place(x=59, y=104)
b_10 = Button(frame_corpo, text='6', width=5, height=2, bg=gray_color, font=('Ivy 13 bold'), relief=RAISED,
             overrelief=RIDGE)
b_10.place(x=118, y=104)

b_11= Button(frame_corpo, text='-', width=5, height=2, bg=orange_color, fg=white_color, font=('Ivy 13 bold'),
             relief=RAISED, overrelief=RIDGE)
b_11.place(x=177, y=104)


b_12= Button(frame_corpo, text='1', width=5, height=2, bg=gray_color, font=('Ivy 13 bold'), relief=RAISED,
             overrelief=RIDGE)
b_12.place(x=0, y=155)
b_13 = Button(frame_corpo, text='2', width=5, height=2, bg=gray_color, font=('Ivy 13 bold'), relief=RAISED,
             overrelief=RIDGE)
b_13.place(x=59, y=155)
b_14 = Button(frame_corpo, text='3', width=5, height=2, bg=gray_color, font=('Ivy 13 bold'), relief=RAISED,
             overrelief=RIDGE)
b_14.place(x=118, y=155)

b_15 = Button(frame_corpo, text='+', width=5, height=2, bg=orange_color, fg=white_color, font=('Ivy 13 bold'),
             relief=RAISED, overrelief=RIDGE)
b_15.place(x=177, y=155)


b_16 = Button(frame_corpo, text='0', width=11, height=2, bg=gray_color, font=('Ivy 13 bold'), relief=RAISED,
             overrelief=RIDGE)
b_16.place(x=0, y=208)

b_17 = Button(frame_corpo, text='.', width=5, height=2, bg=gray_color, font=('Ivy 13 bold'), relief=RAISED,
             overrelief=RIDGE)
b_17.place(x=118, y=208)

b_18 = Button(frame_corpo, text='=', width=5, height=2, bg=orange_color, fg=white_color, font=('Ivy 13 bold'),
             relief=RAISED, overrelief=RIDGE)
b_18.place(x=177, y=208)



main_janela.mainloop()
