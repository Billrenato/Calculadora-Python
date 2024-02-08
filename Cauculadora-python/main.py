#impotando o tkinter biblioteca


from tkinter import *
from tkinter import ttk

# cores

cor1 = "#36353b" #preto
cor2 = "#5f9e61" #verde
cor3 = "#a19954" #amarelo
cor4 = "#8f334d" #vermelho
cor5 = "#2b237a" #azul



 # criando janela
janela = Tk ()
janela.title("Cauculadora")
janela.geometry("235x318")
janela.config()

#criando os frames
frame_tela = Frame(janela, width=235, height=50, bg=cor3)
frame_tela.grid(row=0, column=0)
frame_corpo = Frame(janela, width=235, height=268)
frame_corpo.grid(row=1, column=0)

#variavel todos valores
todos_valores = ''

#criando o label 
valor_texto = StringVar()


#criando a função
def entrar_valores(event):
    global todos_valores

    todos_valores = todos_valores + str (event)
    
    #passando o valor na tela
    valor_texto.set(todos_valores)
    # função para calcular
def calcular():
    global todos_valores
    resultado = eval(todos_valores)
    valor_texto.set(str (resultado))

# função limpar tela
def limpar_tela():
    global todos_valores
    todos_valores = ""
    valor_texto.set ("")


app_label = Label(frame_tela, textvariable=valor_texto, width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT ,font=('Ivy 18'))
app_label.place(x=0,y=0)


#criando botoes
b_1 = Button(frame_corpo, command=limpar_tela, text="C", width=11, height=2, font=('Ivy 13'))
b_1.place(x=5,y=0)
b_2 = Button(frame_corpo, command= lambda: entrar_valores('%'), text="%", width=5, height=2, font=('Ivy 13'))
b_2.place(x=118,y=0)
b_3 = Button(frame_corpo, command= lambda: entrar_valores('/'), text="/", width=5, height=2, font=('Ivy 13'))
b_3.place(x=177,y=0)

b_4 = Button(frame_corpo, command= lambda: entrar_valores('7'), text="7", width=5, height=2, font=('Ivy 13'))
b_4.place(x=0,y=52)
b_5 = Button(frame_corpo, command= lambda: entrar_valores('8'), text="8", width=5, height=2, font=('Ivy 13'))
b_5.place(x=59,y=52)
b_6 = Button(frame_corpo, command= lambda: entrar_valores('9'), text="9", width=5, height=2, font=('Ivy 13'))
b_6.place(x=118,y=52)
b_7 = Button(frame_corpo, command= lambda: entrar_valores('*'), text="*", width=5, height=2, font=('Ivy 13'))
b_7.place(x=177,y=52)

b_8 = Button(frame_corpo, command= lambda: entrar_valores('4'), text="4", width=5, height=2, font=('Ivy 13'))
b_8.place(x=0,y=104)
b_9 = Button(frame_corpo, command= lambda: entrar_valores('5'), text="5", width=5, height=2, font=('Ivy 13'))
b_9.place(x=59,y=104)
b_10 = Button(frame_corpo, command= lambda: entrar_valores('6'), text="6", width=5, height=2, font=('Ivy 13'))
b_10.place(x=118,y=104)
b_11 = Button(frame_corpo, command= lambda: entrar_valores('-'), text="-", width=5, height=2, font=('Ivy 13'))
b_11.place(x=177,y=104)

b_12 = Button(frame_corpo, command= lambda: entrar_valores('1'), text="1", width=5, height=2, font=('Ivy 13'))
b_12.place(x=0,y=156)
b_13 = Button(frame_corpo, command= lambda: entrar_valores('2'), text="2", width=5, height=2, font=('Ivy 13'))
b_13.place(x=59,y=156)
b_14 = Button(frame_corpo, command= lambda: entrar_valores('3'), text="3", width=5, height=2, font=('Ivy 13'))
b_14.place(x=118,y=156)
b_15 = Button(frame_corpo, command= lambda: entrar_valores('+'), text="+", width=5, height=2, font=('Ivy 13'))
b_15.place(x=177,y=156)

b_16 = Button(frame_corpo, command= lambda: entrar_valores('0'), text="0", width=11, height=2, font=('Ivy 13'))
b_16.place(x=5,y=208)
b_17 = Button(frame_corpo, command= lambda: entrar_valores(','), text=",", width=5, height=2, font=('Ivy 13'))
b_17.place(x=118,y=208)
b_18 = Button(frame_corpo, command= calcular, text="=", width=5, height=2, font=('Ivy 13'))
b_18.place(x=177,y=208)




janela,mainloop()
