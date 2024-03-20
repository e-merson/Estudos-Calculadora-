# importando tkinter
from tkinter import *
from tkinter import ttk

cor_1 = '#0c0d0c' # preta
cor_2 = '#b1b8e3' # azul
cor_3 = '#cfd7e6' # cinza
cor_4 = '#e38654' # laranja
cor_5 = '#cf4646' # vermelho

janela = Tk()
janela.title("CALCULADORA")
janela.geometry("275x350")
janela.config(bg=cor_1)

# Frames
frame_tela = Frame(janela, width= 275, height= 75, bg= cor_2)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width= 275, height= 375, bg= cor_3)
frame_corpo.grid(row=1, column=0)

valor_texto = StringVar()
app_label = Label(frame_tela, textvariable= valor_texto, width=21, height=3, padx=11, relief=FLAT, anchor='e', justify=RIGHT, font=('Ivy 15 bold'), bg=cor_2)
app_label.place(x=0, y=0)



todos_os_valores = ''
# funções


def entrar_valores(event):
    global todos_os_valores
    todos_os_valores = todos_os_valores + str(event)
    


# passar valor para a tela
    valor_texto.set(todos_os_valores)


# função cálculo
    
def calcular():
    global todos_os_valores
    resultado = eval(todos_os_valores)
    valor_texto.set(str(resultado))

# limpar a tela
    
def limpar_tela():
    global todos_os_valores
    todos_os_valores = ''
    valor_texto.set('')

   


# Botões

b_1 = Button(frame_corpo, command= limpar_tela, text='C', width= 17, height= 3, bg= cor_3, relief= RAISED, overrelief= RIDGE)
b_1.place(x=0, y=0)

b_2 = Button(frame_corpo, command= lambda: entrar_valores('%'), text='%', width= 10, height= 3, bg= cor_3, relief= RAISED, overrelief= RIDGE)
b_2.place(x=120, y=0)

b_3 = Button(frame_corpo, command= lambda: entrar_valores('/'), text='/', width= 10 , height= 3, bg= cor_4, relief= RAISED, overrelief= RIDGE)
b_3.place(x=204, y=0)


b_4 = Button(frame_corpo, command= lambda: entrar_valores('7'), text='7', width= 10, height= 3, bg= cor_3, relief= RAISED, overrelief= RIDGE)
b_4.place(x=0, y=55)

b_5 = Button(frame_corpo, command= lambda: entrar_valores('8'), text='8', width= 10, height= 3, bg= cor_3, relief= RAISED, overrelief= RIDGE)
b_5.place(x=60, y=55)

b_6 = Button(frame_corpo, command= lambda: entrar_valores('9'), text='9', width= 10, height= 3, bg= cor_3, relief= RAISED, overrelief= RIDGE)
b_6.place(x=120, y=55)

b_7 = Button(frame_corpo, command= lambda: entrar_valores('*'), text='*', width= 10 , height= 3, bg= cor_4, relief= RAISED, overrelief= RIDGE)
b_7.place(x=204, y=55)


b_8 = Button(frame_corpo, command= lambda: entrar_valores('4'), text='4', width= 10, height= 3, bg= cor_3, relief= RAISED, overrelief= RIDGE)
b_8.place(x=0, y=110)

b_9 = Button(frame_corpo, command= lambda: entrar_valores('5'), text='5', width= 10, height= 3, bg= cor_3, relief= RAISED, overrelief= RIDGE)
b_9.place(x=60, y=110)

b_10 = Button(frame_corpo, command= lambda: entrar_valores('6'), text='6', width= 10, height= 3, bg= cor_3, relief= RAISED, overrelief= RIDGE)
b_10.place(x=120, y=110)

b_11 = Button(frame_corpo, command= lambda: entrar_valores('-'), text='-', width= 10 , height= 3, bg= cor_4, relief= RAISED, overrelief= RIDGE)
b_11.place(x=204, y=110)


b_12 = Button(frame_corpo, command= lambda: entrar_valores('1'), text='1', width= 10, height= 3, bg= cor_3, relief= RAISED, overrelief= RIDGE)
b_12.place(x=0, y=165)

b_13 = Button(frame_corpo, command= lambda: entrar_valores('2'), text='2', width= 10, height= 3, bg= cor_3, relief= RAISED, overrelief= RIDGE)
b_13.place(x=60, y=165)

b_14 = Button(frame_corpo, command= lambda: entrar_valores('3'), text='3', width= 10, height= 3, bg= cor_3, relief= RAISED, overrelief= RIDGE)
b_14.place(x=120, y=165)

b_15 = Button(frame_corpo, command= lambda: entrar_valores('+'), text='+', width= 10 , height= 3, bg= cor_4, relief= RAISED, overrelief= RIDGE)
b_15.place(x=204, y=165)


b_16 = Button(frame_corpo, command= lambda: entrar_valores('0'), text='0', width= 17, height= 3, bg= cor_3, relief= RAISED, overrelief= RIDGE)
b_16.place(x=0, y=220)

b_17 = Button(frame_corpo, command= lambda: entrar_valores('.'), text='.', width= 10, height= 3, bg= cor_3, relief= RAISED, overrelief= RIDGE)
b_17.place(x=120, y=220)

b_18 = Button(frame_corpo, command= calcular, text='=', width= 10 , height= 3, bg= cor_4, relief= RAISED, overrelief= RIDGE)
b_18.place(x=204, y=220)




janela.mainloop()




