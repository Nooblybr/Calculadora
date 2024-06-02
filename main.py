import tkinter as tk
from sympy import sympify
 

def pressionar_botao(valor):
    atual = entrada.get()
    entrada.delete(0,tk.END)
    entrada.insert(0,atual + str(valor))

def limpar():
    entrada.delete(0,tk.END)

def igual():
    expressao = entrada.get()
    try:
        resultado = sympify(expressao)
        entrada.delete(0,tk.END)
        entrada.insert(0,resultado)
    except:
        entrada.delete(0,tk.END)
        entrada.insert(0,"error")

janela = tk.Tk()
janela.title("Calculadora")
janela.geometry("400x550")

entrada = tk.Entry(janela,width=20, font=("arial",20),borderwidth=5)
entrada.grid(row=0,column=0,columnspan=4)

linha = 1
coluna=0

botoes = [
    '7','8','9','/',
    '4','5','6','*',
    '1','2','3','+',
    '0','C','=','-'
]

for botao in botoes:
    if botao == "C":
        tk.Button(janela,text=botao, font=("arial",15),width=7,height=3, command= limpar).grid(row=linha,column=coluna)
    elif botao == "=":
        tk.Button(janela,text=botao, font=("arial",15),width=7,height=3,command = igual).grid(row=linha,column=coluna)
    else:
        tk.Button(janela,text=botao, font=("arial",15),width=7,height=3,command= lambda var = botao: pressionar_botao(var)).grid(row=linha,column=coluna)

    coluna += 1

    if coluna > 3:
        coluna = 0
        linha += 1
    



janela.mainloop()

