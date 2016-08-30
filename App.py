#coding=utf-8
from Tkinter import *
from tkFileDialog import askopenfilename
import tkMessageBox
from Personagem import *

personagem = None

class MenuBar(Menu):
    def __init__(self, parent):
        Menu.__init__(self, parent)
        fileMenu = Menu(self, tearoff=False)
        self.add_cascade(label="File",underline=0, menu=fileMenu)

        fileMenu.add_command(label="New", underline=1, command=self.NewChar)
        fileMenu.add_command(label="Load...", underline=1, command=self.LoadChar)
        fileMenu.add_separator()
        fileMenu.add_command(label="Exit", underline=1, command=self.quit)

        helpMenu = Menu(self, tearoff=False)
        self.add_cascade(label="Help",underline=0, menu=helpMenu)

        helpMenu.add_command(label="About...", underline=1, command=self.About)
    def NewChar(self):
        print "New File!"
    def LoadChar(self):
        char = askopenfilename()
        personagem = load_personagem(char)
        print personagem
        tkMessageBox.showinfo("Personagem carregado", personagem.__str__())
    def About(self):
        mensagem = "O RPG Filler é um programa para automatizar a criação de personagens para o sistema de rpg D&D 3.5."
        mensagem += "\n"
        mensagem += "Para mais informações acessar https://github.com/rodrigondec/RPG-Filler"
        tkMessageBox.showinfo("About", mensagem)
    def quit(self):
        sys.exit(0)

class Application(Frame):
    def att(self): 
        if personagem:       
            self.result.set(personagem.nome)

    def createWidgets(self):
        # self.nome = Text(self, state="disabled", height="1", width=30)
        # self.nome.insert(END, str(personagem.nome))
        self.result = StringVar()
        if personagem:
            self.result.set(personagem.nome)
        self.nome = Label(self, textvariable=self.result, bg="white")
        self.nome.pack()

        self.upd = Button(self)
        self.upd["text"] = "Atualizar",
        self.upd["command"] = self.att

        self.upd.pack(side="bottom")

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
        menubar = MenuBar(self)
        master.config(menu=menubar)

root = Tk()
root.resizable(width=False, height=False)
root.geometry('{}x{}'.format(600, 480))

# app = Application(master=root)

app.mainloop()
root.destroy()