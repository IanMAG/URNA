from tkinter import *
import mysql.connector
from time import sleep
import pygame

pygame.mixer.init()

class UE:
    def __init__(self, janela, candidato):
        self.main = janela

        self.candidato = candidato

        self.frame = Frame(self.main, bg = "#3F3F3F")
        self.frame.place(relx = 0.561, rely = 0.23, relwidth = 0.3666, relheight = 0.581)

        self.botao1 = Button(self.frame, font = "Calibri 16 italic bold", text = "1", width = 8, height = 2, fg = "white", bg = "black", command = lambda: self.mostrarNumero("1"))
        self.botao1.grid(row = 0, column = 0)

        self.botao2 = Button(self.frame, font = "Calibri 16 italic bold", text = "2", width = 8, height = 2, fg = "white", bg = "black", command = lambda: self.mostrarNumero("2"))
        self.botao2.grid(row = 0, column = 2)

        self.botao3 = Button(self.frame, font = "Calibri 16 italic bold", text = "3", width = 8, height = 2, fg = "white", bg = "black", command = lambda: self.mostrarNumero("3"))
        self.botao3.grid(row = 0, column = 3)

        self.botao4 = Button(self.frame, font = "Calibri 16 italic bold", text = "4", width = 8, height = 2, fg = "white", bg = "black", command = lambda: self.mostrarNumero("4"))
        self.botao4.grid(row = 1, column = 0)
        
        self.botao5 = Button(self.frame, font = "Calibri 16 italic bold", text = "5", width = 8, height = 2, fg = "white", bg = "black", command = lambda: self.mostrarNumero("5"))
        self.botao5.grid(row = 1, column = 2)

        self.botao6 = Button(self.frame, font = "Calibri 16 italic bold", text = "6", width = 8, height = 2, fg = "white", bg = "black", command = lambda: self.mostrarNumero("6"))
        self.botao6.grid(row = 1, column = 3)

        self.botao7 = Button(self.frame, font = "Calibri 16 italic bold", text = "7", width = 8, height = 2, fg = "white", bg = "black", command = lambda: self.mostrarNumero("7"))
        self.botao7.grid(row = 2, column = 0)

        self.botao8 = Button(self.frame, font = "Calibri 16 italic bold", text = "8", width = 8, height = 2, fg = "white", bg = "black", command = lambda: self.mostrarNumero("8"))
        self.botao8.grid(row = 2, column = 2)

        self.botao9 = Button(self.frame, font = "Calibri 16 italic bold", text = "9", width = 8, height = 2, fg = "white", bg = "black", command = lambda: self.mostrarNumero("9"))
        self.botao9.grid(row = 2, column = 3)

        self.botaoNulo = Button(self.frame, font = "Calibri 16 italic bold", text = "0", width = 8, height = 2, fg = "white", bg = "black", command = lambda: self.mostrarNumero("0"))
        self.botaoNulo.grid(row = 3, column = 2)

        self.botaoACC = Button(self.main, font = "Calibri 14 italic bold", text = "CONFIRMAR", width = 10, height = 1, fg = "BLACK", bg = "GREEN", command = self.ac)
        self.botaoACC.place(relx = 0.79, rely = 0.85)

        self.botaoApagar = Button(self.main, font = "Calibri 11 italic bold", text = "CORRIGE", width = 10, height = 1, fg = "BLACK", bg = "#DB3B0F", command = self.apagar)
        self.botaoApagar.place(relx = 0.67, rely = 0.857)
        
        self.botaoBranco = Button(self.main, font = "Calibri 10 italic bold", text = "BRANCO", width = 10, height = 1, fg = "BLACK", bg = "#B6B6B6", command = self.branco)
        self.botaoBranco.place(relx = 0.56, rely = 0.8666)

        self.quadro = Label(self.main, bg = "black", width = 50, height = 19)
        self.quadro.place(relx = 0.05, rely = 0.23)

        self.nome = Label(self.main, text = "Candidato: ", font = "calibri 16 italic bold", bg = "black", fg = "white")
        self.nome.place(relx = 0.07, rely = 0.28)

        self.num = Label(self.main, text = "Número: ", font = "calibri 16 italic bold", bg = "black", fg = "white")
        self.num.place(relx = 0.07, rely = 0.36)

        self.campoNum = Label(self.main, font = "calibri 16 italic bold")
        self.campoNum.place(relx = 0.22, rely = 0.36, relwidth = 0.1)

        self.campoNome = Label(self.main, font = "calibri 16 italic bold")
        self.campoNome.place(relx = 0.22, rely = 0.28, relwidth = 0.25 )

        self.imagem = Label(self.main, bg = "black")
        self.imagem.place(relx = 0.13, rely = 0.48, relwidth = 0.3, relheight = 0.3)



        self.main.bind('<KeyPress>', self.teclado)


    def teclado(self, evento):
        numeros = ["0", '1', '2', '3', '4', '5', '6', '7', '8', '9']
        for valor in numeros:
            if str(evento.char) == valor:
                self.mostrarNumero(valor)


    def mostrarNumero(self, parametro):
        tamanho = len(self.campoNum['text'])  #limita para apenas dois numeros.
        if tamanho < 2:
            self.campoNum["text"] += parametro
            tamanho += 1

        if tamanho == 2:
            numCandidato = self.campoNum['text']

            conexao = mysql.connector.connect(user='root', host='localhost')
            try:
                cursor = conexao.cursor()
                cursor.execute("USE iandb;")
                cursor.execute("SELECT numero FROM candidato;")
                for x in cursor:
                    if x[0] == int(numCandidato):
                        numerovoto = x[0]

                if numerovoto in self.candidato:
                    cursor.execute("USE iandb;")
                    cursor.execute(f"SELECT nome FROM candidato WHERE numero = '{numerovoto}';")

                    for y in cursor:
                        nomecand = y[0]
                        conexao.close()
                        
                    self.campoNome["text"] = nomecand
                    self.loadimage = PhotoImage(file = str(numerovoto)+'.png')
                    self.imagem["image"] = self.loadimage
                            
            except:
                pass

    def ac(self):
        conexao = mysql.connector.connect(user='root', host='localhost')
        cursor = conexao.cursor()
        cursor.execute('USE iandb;')
        voto = self.campoNum['text']
        if voto in str(self.candidato):
            cursor.execute(f'INSERT INTO lista(voto) VALUES("{voto}");')
        elif voto == "":
            cursor.execute(f'INSERT INTO lista(voto) VALUES(66);') #66 representa voto nulo, pois a tabela que contêm o voto aceita apenas inteiro.
        else:
            cursor.execute(f'INSERT INTO lista(voto) VALUES(00);')
        conexao.commit()
        conexao.close()
        pygame.mixer.music.load("somurna2.mp3")
        pygame.mixer.music.play(loops = 0)
        self.apagar()
        


    def branco(self):
        conexao = mysql.connector.connect(user='root', host='localhost')
        cursor = conexao.cursor()
        cursor.execute('USE iandb;')
        cursor.execute(f'INSERT INTO lista(voto) VALUES(00);')
        conexao.commit()
        conexao.close()
        

    def apagar(self):
        self.campoNum["text"] = ""
        self.campoNome["text"] = ""
        self.remover = PhotoImage(file = "vazia.png") 
        self.imagem["image"] = self.remover
    

    def exibir(self):
        self.tela = Label(self.original, text = "", font = "calibri 14 italic bold")
        self.tela.place(relx=0.12, rely=0.27)       



if __name__=="__main__":
    janela = Tk()
    janela.geometry("800x500")
    janela.resizable(False, False)
    janela.title("URNA ELETRÔNICA")
    janela["bg"] = "white"
    objeto = UE(janela, [35,47,84,93])


    janela.mainloop()
