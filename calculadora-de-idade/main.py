from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from dateutil.relativedelta import relativedelta
from datetime import date

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

l_calculadora = Label(frame_cima, text='CALCULADORA', width=25, height=1, padx=3, relief=FLAT, anchor='center',
                      font='Ivi 15 bold', bg=black_color, fg=white_color)
l_calculadora.place(x=0, y=30)

l_idade = Label(frame_cima, text='DE IDADE', width=11, height=1, relief=FLAT, anchor='center', font='Arial 35 bold',
                bg=black_color, fg=orange_color)
l_idade.place(x=0, y=70)


# Função de calculo
def idade():
    inicial = cal_1.get()
    termino = cal_2.get()

    # Separando os valores
    mes_1, dia_1, ano_1 = [int(f) for f in inicial.split('/')]
    # Conversão de valores em fortmato de data
    data_inicial = date(ano_1, mes_1, dia_1)

    # Separando os valores
    mes_2, dia_2, ano_2 = [int(f) for f in termino.split('/')]
    # Conversão de valores em fortmato de data
    data_nascimento = date(ano_2, mes_2, dia_2)

    anos = relativedelta(data_inicial, data_nascimento).years
    meses = relativedelta(data_inicial, data_nascimento).months
    dias = relativedelta(data_inicial, data_nascimento).days

    l_app_anos['text'] = anos
    l_app_meses['text'] = meses
    l_app_dias['text'] = dias



# ----------- Criando labels para frame de baixo

l_data_inicial = Label(frame_baixo, text='Data inicial', height=1, padx=0, pady=0, relief=FLAT, anchor=NW,
                       font='Arial 11', bg=black_color, fg=white_color)
l_data_inicial.place(x=50, y=30)

cal_1 = DateEntry(frame_baixo, width=13, bg='darkblue', fg=white_color, borderwidth=2, date_pattern='mm/dd/y', y=2022)
cal_1.place(x=190, y=30)

l_data_nascimento = Label(frame_baixo, text='Data de nascimento', height=1, padx=0, pady=0, relief=FLAT, anchor=NW,
                          font='Arial 11', bg=black_color, fg=white_color)
l_data_nascimento.place(x=50, y=70)

cal_2 = DateEntry(frame_baixo, width=13, bg='darkblue', fg=white_color, borderwidth=2, date_pattern='mm/dd/y', y=2022)
cal_2.place(x=190, y=70)
# --------------------------------------- Anos ---------------------------------------
l_app_anos = Label(frame_baixo, text='24', height=1, padx=0, pady=0, relief=FLAT, anchor='center', font='Ivi 15 bold',
                   bg=black_color, fg=white_color)
l_app_anos.place(x=60, y=135)

l_app_anos_text = Label(frame_baixo, text='Anos', height=1, padx=0, pady=0, relief=FLAT, anchor='center',
                        font='Ivi 15 bold', bg=black_color, fg=white_color)
l_app_anos_text.place(x=50, y=175)

# --------------------------------------- Meses ---------------------------------------
l_app_meses = Label(frame_baixo, text='12', height=1, padx=0, pady=0, relief=FLAT, anchor='center', font='Ivi 11 bold',
                   bg=black_color, fg=white_color)
l_app_meses.place(x=145, y=135)
l_app_meses_text = Label(frame_baixo, text='Meses', height=1, padx=0, pady=0, relief=FLAT, anchor='center',
                        font='Ivi 11 bold', bg=black_color, fg=white_color)
l_app_meses_text.place(x=130, y=175)
# ------------------------------------ Dias ---------------------------------------
l_app_dias = Label(frame_baixo, text='24', height=1, padx=0, pady=0, relief=FLAT, anchor='center', font='Ivi 11 bold',
                   bg=black_color, fg=white_color)
l_app_dias.place(x=220, y=135)

l_app_dias_text = Label(frame_baixo, text='Dias', height=1, padx=0, pady=0, relief=FLAT, anchor='center',
                        font='Ivi 11 bold', bg=black_color, fg=white_color)
l_app_dias_text.place(x=210, y=175)

# Adicionando botao
b_calculo = Button(frame_baixo, command=idade,
                   text='Calcular', height=1, width=20, relief=RAISED, overrelief=RIDGE, anchor='center',
                   font='Ivi 10 bold', bg=black_color, fg=white_color)
b_calculo.place(x=60, y=225)

# Mantendo ciclo da janela aberta até que se feche
janela.mainloop()
