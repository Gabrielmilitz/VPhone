from tkinter import *
from new_model import Gerenciador_senha

class Interface:
    def __init__(self):
        self.gerenciador = Gerenciador_senha() #cria uma instancia do gerenciado_senhas que contem uma lista vazia

        self.janela = Tk() #cria o tk
        self.janela.title("Armazenamento temporário de senhas") #titulo
        self.janela.geometry("300x200")
        self.janela.resizable(False, False) #impede o redimensionamento
        self.janela.config(bg="black")
        

        self.frame = Frame(self.janela)
        self.frame.pack(expand=True)

        self.lbl = Label(self.frame, text="Bem-vindo!")
        self.lbl.pack(pady=5)

        self.enter = Entry(self.frame, width=50, show="*")
        self.enter.pack(pady=5)

        self.btn1 = Button(self.frame, text="Armazenar", command=self.armazenar_senha)
        self.btn1.pack(pady=5)

        self.btn2 = Button(self.frame, text="Exibir Senhas", command=self.exibir_senhas)
        self.btn2.pack(pady=5)

        self.lbl_resultado = Label(self.frame, text="", fg="blue", justify=LEFT)
        self.lbl_resultado.pack(pady=10)

        self.janela.mainloop()

    def armazenar_senha(self):
     senha = self.enter.get()  # Pega o que foi digitado no campo Entry
     resultado = self.gerenciador.armazenar_gui(senha)  # Chama o método da classe Gerenciador_senha
     self.lbl_resultado.config(text=resultado)  # Exibe a resposta (mensagem) no Label
     self.enter.delete(0, END)  # Limpa o campo de entrada


    def exibir_senhas(self):
        resultado = self.gerenciador.exibir_gui()
        self.lbl_resultado.config(text=resultado)


