from tkinter import *
import tkinter.messagebox
from tkinter import ttk
import random
import time;
import datetime
import os
import pygetwindow


from ttkthemes import themed_tk as tk

# ULTIMA VEZ EDITADO POR
#Video Tutorial
#pdf e excell


#BUGS
#edito, mas não carregou







AGENDA = {}
EQUIPI_DI = {}

def exportar(nome_do_arquivo):
    try:
        with open(nome_do_arquivo, "w") as arquivo:
            for crianca in AGENDA:
                numero = AGENDA[crianca]["numero"]
                endereco = AGENDA[crianca]["endereco"]
                mae = AGENDA[crianca]["mae"]
                idade = AGENDA[crianca]["Idade"]
                arquivo.write("kid,{},{},{},{},{}\n".format(crianca, numero, endereco, mae, idade))
            for adulto in EQUIPI_DI:
                telefone = EQUIPI_DI[adulto]["numero"]
                endereco = EQUIPI_DI[adulto]["endereco"]
                email = EQUIPI_DI[adulto]["funcao"]
                idade = EQUIPI_DI[adulto]['idade']
                arquivo.write("team,{},{},{},{},{}\n".format(adulto, telefone, endereco, email, idade))
    except Exception as erro:
        print("Erro ao exportar o arquivo!", erro)


def salvar():
    exportar("Database.csv")
    print("Tudo foi corretamente salvo!")

def load():
    try:
        with open("Database.csv", "r") as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                detalhes = linha.strip().split(",")
                if detalhes[0] == "kid":
                    nome = detalhes[1]
                    numero = detalhes[2]
                    endereco = detalhes[3]
                    mae = detalhes[4]
                    idade = detalhes[5]

                    AGENDA[nome] = {
                        'numero': numero,
                        'endereco': endereco,
                        'mae': mae,
                        "Idade": idade
                    }
                elif detalhes[0] == "team":
                    nome = detalhes[1]
                    telefone = detalhes[2]
                    endereco = detalhes[3]
                    funcao = detalhes[4]
                    idade = detalhes[5]

                    EQUIPI_DI[nome] = {
                        'numero': telefone,
                        'endereco': endereco,
                        'funcao': funcao,
                        'idade': idade
                    }
        print("Load completo!")
    except Exception as error:
        print("Erro ao carregar o arquivo!", error)



def main():
    root = tk.ThemedTk()
    root.get_themes()
    root.set_theme("scidmint")
    app = Window1(root)
    root.mainloop()

class Window1:
    def __init__(self, master):
        load()
        self.master = master
        self.master.title("UnderFox")
        self.master.geometry('750x500+0+0')
        self.master.iconbitmap("fox.ico")
        self.master.maxsize(750,500)
        self.image = PhotoImage(file="download.png")
        self.frame = Frame(self.master)
        self.frame.pack()

        self.User = StringVar()
        self.Password = StringVar()
        self.LabelTitle = Label(self.frame, text="Registro Geral", font=('arial', 30, 'bold'), bd=20)
        self.LabelTitle.grid(row=0, column=0, columnspan=2, pady=20)

        self.Loginframe1 = Frame(self.frame, width=1010, height=300, bd=20, relief='ridge')
        self.Loginframe1.grid(row=1, column=0)
        self.Loginframe2 = Frame(self.frame, width=1010, height=100, bd=20, relief='ridge')
        self.Loginframe2.grid(row=2, column=0)
        self.Loginframe3 = Frame(self.frame, width=1010, height=200, bd=20, relief='ridge')
        self.Loginframe3.grid(row=3, column=0, pady=2)

        self.LabelUser = Label(self.Loginframe1, text="Nome", font=('arial', 15, 'bold'), bd=22)
        self.LabelUser.grid(row=0, column=0)
        self.txtUser = Entry(self.Loginframe1, text="Nome", font=('arial', 15, 'bold'), bd=22,
                                 textvariable=self.User)
        self.txtUser.grid(row=0, column=1)

        self.LabelPassword = Label(self.Loginframe1, text="Senha", font=('arial', 15, 'bold'), bd=22)
        self.LabelPassword.grid(row=1, column=0)
        self.txtPassword = Entry(self.Loginframe1, text="Senha", font=('arial', 15, 'bold'), bd=22,
                                     textvariable=self.Password, show='*')
        self.txtPassword.grid(row=1, column=1)
        self.btnLogin = Button(self.Loginframe2, text='Login', width=17, font=('arial', 10, 'bold'),
                                   command=self.Login_System)
        self.btnLogin.grid(row=0, column=0)

        self.btnReset = Button(self.Loginframe2, text='Resetar', width=17, font=('arial', 10, 'bold'),
                                   command=self.Reset)
        self.btnReset.grid(row=0, column=1)

        self.btnExit = Button(self.Loginframe2, text='Sair', width=17, font=('arial', 10, 'bold'),
                                  command=self.iExit)
        self.btnExit.grid(row=0, column=2)

        self.btnResgistration = Button(self.Loginframe3, text='Login necessário', font=('arial', 10, 'bold'),
                                           state=DISABLED, command=self.resgistration_window)
        self.btnResgistration.grid(row=0, column=0)

        self.btnHospital = Button(self.Loginframe3, text='Login necessário', font=('arial', 10, 'bold'),
                                      state=DISABLED, command=self.hospital_window)
        self.btnHospital.grid(row=0, column=1)
    def Login_System(self):
        user = (self.User.get())
        passwd = (self.Password.get())

        if (user == "admin") and (passwd == "admin"):
            self.btnResgistration.config(state = NORMAL, text="Registro Infantil", fg="red")
            self.btnHospital.config(state=NORMAL, text='Registro Equipe DI', fg="red")
        else:
            tkinter.messagebox.showerror("Erro no login","Senha ou Usuário não registrados!")
            self.btnResgistration.config(state=DISABLED)
            self.btnHospital.config(state=DISABLED)
            self.User.set('')
            self.Password.set('')
            self.txtUser.focus()
    def Reset(self):
        self.btnResgistration.config(state=DISABLED, text="Login necessário")
        self.btnHospital.config(state=DISABLED, text="Login necessário")
        self.User.set('')
        self.Password.set('')
        self.txtUser.focus()
        self.newWindow1.destroy()
        self.newWindow2.destroy()

    def iExit(self):
        self.iExit = tkinter.messagebox.askyesno("Fechar", "Você deseja fechar o programa?")
        if self.iExit > 0:
            self.master.destroy()
            salvar()
            return


    # ===============================================================================================================================================
    def resgistration_window(self):
        self.newWindow1 = Toplevel(self.master)
        self.app = Window2(self.newWindow1)
        window = pygetwindow.getWindowsWithTitle("UnderFox")[0]
        window.minimize()

    def hospital_window(self):
        self.newWindow2 = Toplevel(self.master)
        self.app = Window3(self.newWindow2)


class Window2:
    def __init__(self, master):
        load()
        self.master = master
        self.master.title("Crianças")
        self.master.iconbitmap("kid.ico")
        self.master.minsize(560,330)
        self.master.maxsize(560, 330)
        self.master.geometry('500x350+0+0')
        ############################################################################################################
        ##TAB

        prof_img = PhotoImage(file=r're.png')

        self.TAB = ttk.Notebook(self.master)
        self.tabADD = ttk.Frame(self.TAB)
        self.tabPAD = ttk.Frame(self.TAB)
        self.TAB.add(self.tabPAD, text="Inicio")
        self.TAB.grid(row=1, column=0, columnspan=550, rowspan=549, sticky='NESW')
        #############################################################

        self.tabHID = ttk.Frame(self.TAB, height=1000, width=1000)
        self.TAB.add(self.tabHID, state="hidden")

        ############################################################################################################

        self.search_var = StringVar()
        self.search_var.trace("w", lambda name, index, mode: self.update_list())


        ############################################################################################################
        self.menu = Menu(self.master)
        self.menukids = Menu(self.menu, tearoff=0)
        self.menukids.add_command(label="Registrar uma nova criança", command=self.criar_registro)
        self.menukids.add_command(label="Sair", command=self.iExit)
        self.menu.add_cascade(label="Opções", menu=self.menukids)
        self.frame = ttk.Frame(self.tabPAD)
        self.frame.grid(sticky=W)

        self.ListaFrame = ttk.Frame(self.tabPAD)
        self.ListaFrame.grid(row=1, column=0, sticky=W)
        self.ButtonFrame = ttk.Frame(self.tabPAD)
        self.ButtonFrame.grid(row=5, column=0, sticky=W)
        self.BuscarFrame = ttk.Frame(self.tabPAD)
        self.BuscarFrame.grid(row=0, column=0, sticky=W)

        self.lista = Listbox(self.ListaFrame, height=15, width=int(24.01))
        self.lista.grid(row=1, column=0)

        self.buscar = ttk.Entry(self.BuscarFrame, font=("arial", 10), textvariable=self.search_var)
        self.buscar.grid(row=3, column=0)
        self.Button = ttk.Button(self.ButtonFrame, text="Ver Informações", command=self.ler_dados)
        self.Button.grid(row=4, column=1, sticky=W)
        self.Button1 = ttk.Button(self.ButtonFrame, text="Editar", command=self.editar_dados)
        self.Button1.grid(row=4, column=0, sticky=W)
        self.Button2 = ttk.Button(self.ButtonFrame, text="Informações adicionais", command=self.focar)
        self.Button2.grid(row=4, column=2, sticky=W)


        for nome in AGENDA:
            self.lista.insert(END, nome)

        self.master.config(menu=self.menu)

    def iExit(self):
        self.iExit = tkinter.messagebox.askyesno("Fechar", "Você deseja fechar a página de Registro?", parent=self.master)
        if self.iExit > 0:
            self.master.destroy()
            salvar()
            window = pygetwindow.getWindowsWithTitle("UnderFox")[0]
            window.maximize()
            return

    def update_list(self):
        search_term = self.buscar.get()


        self.lista.delete(0, END)

        for item in AGENDA:
            if search_term.lower() in item.lower():
                self.lista.insert(END, item)


    def mostrarTAB(self):
        prof_img = PhotoImage(file=r'sinais (1).png')
        self.TAB.add(self.tabADD, text="Registrar", image=prof_img, compound=TOP)
        self.TAB.select(self.tabADD)

    def focar(self):
        self.ler_dados_adicionais()
        self.TAB.select(self.tabAPD)

#################
#Adicionar foto
    def ler_dados(self):
        try:
            try:
                self.nomeV.destroy()
            except:
                pass
            self.nom = self.lista.get(ACTIVE)
            self.telefone = AGENDA[self.nom]['numero']
            self.responsavel = AGENDA[self.nom]['mae']
            self.endereco = AGENDA[self.nom]['endereco']
            self.info = AGENDA[self.nom]['Idade']
            self.TUDO = StringVar()
            self.TUDO.set(self.nom + '\n' + self.telefone + '\n' + self.endereco + '\n' + self.responsavel + '\n' + self.info)

            self.nome = ttk.Label(self.ListaFrame, text="Nome:\nTelefone:\nEndereço:\nResponsáveis:\nIdade:", font=("arial", 9, "bold"), justify=LEFT)
            self.nome.grid(row=1, column=4, sticky='WN')
            self.nomeV = ttk.Label(self.ListaFrame, textvariable=self.TUDO, justify=LEFT, font=('arial', 9))
            self.nomeV.grid(row=1, column=5, sticky='WN')
            self.ex = ttk.Button(self.ListaFrame, text="Excluir", command=self.excluir)
            self.ex.grid(row=1, column=4)

            self.ler_dados_adicionais()
        except:
            tkinter.messagebox.showerror("ERROR", 'Nenhum usuário válido selecionado!')

    def ler_dados_adicionais(self):
        try:
            self.tabAPD.destroy()
        except:
            pass
        self.tabAPD = Frame(self.TAB)
        prof_img = PhotoImage(file=r'x.png')
        self.TAB.add(self.tabAPD, text="Adicional Info", image=prof_img, compound=LEFT)

        self.nom = self.lista.get(ACTIVE)
        print(self.nom)

        if self.nom != "":
            try:
                texto = open("[KID]"+self.nom + ".txt", "x")
                TEXT = texto.read()

                self.t = Text(self.tabAPD, height=15, width=70)
                self.t.grid()
                self.t.insert(END, TEXT)
                texto_digitado = self.t.get(1.0, END)

                self.Save_BUTTON = ttk.Button(self.tabAPD, text="Salvar", command=self.salvar_texto)
                self.Save_BUTTON.grid()

            except Exception as error:
                print(error)
                texto = open("[KID]"+self.nom + ".txt", "r+")
                TEXT = texto.read()
                self.t = Text(self.tabAPD, height=15, width=70)
                self.t.grid()
                self.t.insert(END, TEXT)

                texto_digitado = self.t.get(1.0, END)

                self.Save_BUTTON = ttk.Button(self.tabAPD, text="Salvar", command=self.salvar_texto)
                self.Save_BUTTON.grid()

        else:
            tkinter.messagebox.showerror("","Ninguém foi selecionado", parente=self.master)

    def salvar_texto(self):
        texto = self.t.get(1.0, END)
        opcao = tkinter.messagebox.askyesno("", "Você deseja salvar as alterações?", parent=self.master)
        if opcao > 0:
            with open("[KID]"+self.nom+".txt", 'w') as f:
                f.write(texto)
                self.Save_BUTTON["text"]="Salvar(Salvo)"
        else:
            pass

##################_________________________________________________________________________________________________________________
    def editar_dados(self):
        try:
            self.tabACD.destroy()
        except:
            pass
        self.nom = self.lista.get(ACTIVE)
        self.tabACD = Frame(self.TAB)
        prof_img = PhotoImage(file=r'x.png')
        self.TAB.add(self.tabACD, text="Edição de "+self.nom, image=prof_img, compound=LEFT)
        self.TAB.select(self.tabACD)

        #############################################################
        #Labels
        labelNo = Label(self.tabACD, text="Nome:", font="arial 10 bold", justify=LEFT)
        labelNo.grid(column=0, row=0, sticky=W)
        labelTelefone = Label(self.tabACD, text="Telefone:", font="arial 10 bold")
        labelTelefone.grid(column=0, row=1, sticky=W)
        labelEN = Label(self.tabACD, text="Endereço:", font="arial 10 bold", justify=LEFT)
        labelEN.grid(column=0, row=2, sticky=W)
        labelRes = Label(self.tabACD, text="Responsável:", font="arial 10 bold", justify=LEFT)
        labelRes.grid(column=0, row=3, sticky=W)
        labelIda = Label(self.tabACD, text="Idade:", font="arial 10 bold", justify=LEFT)
        labelIda.grid(column=0, row=4, sticky=W)

        labeldesnecessario = Label(self.tabACD)
        labeldesnecessario.grid(row=5, column=1)
        labeldesnecessario1 = Label(self.tabACD)
        labeldesnecessario1.grid(row=5, column=1)

        #############################################################
        #Stringvar

        sN = StringVar()
        sT = StringVar()
        sE = StringVar()
        sR = StringVar()
        sI = StringVar()

        ##############################################################
        #Entrys
        self.entryN = Entry(self.tabACD, textvariable=sN)
        self.entryN.grid(row=0, column=1)
        self.entryT = Entry(self.tabACD, textvariable=sT)
        self.entryT.grid(row=1, column=1)
        self.entryE = Entry(self.tabACD, textvariable=sE)
        self.entryE.grid(row=2, column=1)
        self.entryR = Entry(self.tabACD,textvariable=sR)
        self.entryR.grid(row=3, column=1)
        self.entryI = Entry(self.tabACD, textvariable=sI)
        self.entryI.grid(row=4, column=1)

        sN.set(self.nom)
        sT.set(AGENDA[self.nom]['numero'])
        sE.set(AGENDA[self.nom]['endereco'])
        sR.set(AGENDA[self.nom]['mae'])
        sI.set(AGENDA[self.nom]['Idade'])

        ##############################################################
        # Buttons
        Bsalvar = Button(self.tabACD, text="Salvar e fechar", command=self.salvar_editados)
        Bsalvar.grid(row=10, column=0, sticky='SW')



        Bsair = Button(self.tabACD, text="Sair sem salvar", command=self.sair_semsalvar1)
        Bsair.grid(row=10, column=1, sticky='SW')

    def excluir(self):
        nom = self.lista.get(ACTIVE)
        option = tkinter.messagebox.askyesno("Atenção!/ Watch out!", "VOCÊ TEM CERTEZA QUE DESEJA DELETAR O CONTATO "+nom+"?", parent=self.master)
        if option > 0:
            AGENDA.pop(nom)
            os.remove("[kid]"+ nom + ".txt")
            salvar()
            self.master.destroy()

            Window1.resgistration_window(self.master)


        else:
            pass



    def salvar_editados(self):

        self.nom = self.lista.get(ACTIVE)

        Nome = self.entryN.get()
        Telefone = self.entryT.get()
        Endereco = self.entryE.get()
        Responsavel = self.entryR.get()
        Idade =  self.entryI.get()
        if Nome == "" or Nome == " ":
            tkinter.messagebox.showerror("ERROR!", "Nome inválido")
        else:
            if Nome in AGENDA:
                tkinter.messagebox.showerror('ERROR!', "Nome já registrado!")
            else:
                opcao = tkinter.messagebox.askyesno("", "Você deseja salvar as alterações?", parent=self.master)
                if opcao > 0:
                    AGENDA[Nome] = {
                        'numero': Telefone,
                        'endereco': Endereco,
                        'mae': Responsavel,
                        "Idade": Idade
                    }

                    os.rename('[KID]'+self.nom+".txt", "[KID]"+Nome+".txt")

                    self.tabACD.destroy()
                    self.master.destroy()
                    AGENDA.pop(self.nom)
                    print(self.nom)
                    salvar()
                    Window1.resgistration_window(self.master)
                else:
                    pass



    def sair_semsalvar(self):
        self.top.destroy()
        Window1.resgistration_window(self.master)
    def sair_semsalvar1(self):
        self.tabACD.destroy()
    def criar_registro(self):
        self.master.destroy()
        self.top = Toplevel()
        self.top.geometry("230x160")
        self.top.title("Criar")

        labelNo = Label(self.top, text="Nome:", font="arial 10 bold", justify=LEFT)
        labelNo.grid(column=0, row=0, sticky=W)
        labelTelefone = Label(self.top, text="Telefone:", font="arial 10 bold")
        labelTelefone.grid(column=0, row=1, sticky=W)
        labelEN = Label(self.top, text="Endereço:", font="arial 10 bold", justify=LEFT)
        labelEN.grid(column=0, row=2, sticky=W)
        labelRes = Label(self.top, text="Responsável:", font="arial 10 bold", justify=LEFT)
        labelRes.grid(column=0, row=3, sticky=W)
        labelIda = Label(self.top, text="Idade:", font="arial 10 bold", justify=LEFT)
        labelIda.grid(column=0, row=4, sticky=W)

        labeldesnecessario = Label(self.top)
        labeldesnecessario.grid(row=5, column=1)
        labeldesnecessario1 = Label(self.top)
        labeldesnecessario1.grid(row=5, column=1)
        #############################################################
        #Stringvar

        sN = StringVar()
        sT = StringVar()
        sE = StringVar()
        sR = StringVar()
        sI = StringVar()
        #################################################################
        ##############################################################
        # Entrys
        self.entryN1= Entry(self.top, textvariable=sN)
        self.entryN1.grid(row=0, column=1)
        self.entryT1 = Entry(self.top, textvariable=sT)
        self.entryT1.grid(row=1, column=1)
        self.entryE1 = Entry(self.top, textvariable=sE)
        self.entryE1.grid(row=2, column=1)
        self.entryR1 = Entry(self.top, textvariable=sR)
        self.entryR1.grid(row=3, column=1)
        self.entryI1 = Entry(self.top, textvariable=sI)
        self.entryI1.grid(row=4, column=1)
        #################################################################


        Bsalvar = Button(self.top, text="Salvar e fechar", command=self.Salvar_criado)
        Bsalvar.grid(row=10, column=0, sticky='SW')
        Bsair = Button(self.top, text="Sair sem salvar", command=self.sair_semsalvar)
        Bsair.grid(row=10, column=1, sticky='SW')


    def Salvar_criado(self):

        Nome = self.entryN1.get()
        Telefone = self.entryT1.get()
        Endereco = self.entryE1.get()
        Responsavel = self.entryR1.get()
        Idade = self.entryI1.get()

        if Nome in AGENDA:
            tkinter.messagebox.showinfo("Não foi possível realizar a ação desejada!","Nome já existente no registro! Porfavor diferencie este contato do outro, ou, caso esteja querendo edita-lo, vá na opção editar.")
        else:
            if Nome == "" or Nome == " ":
                tkinter.messagebox.showerror("ERROR", "Nome Inválido")
            else:
                opcao = tkinter.messagebox.askyesno("", "Você deseja salvar as alterações?", parent=self.top)
                if opcao > 0:
                    AGENDA[Nome] = {
                        'numero': Telefone,
                        'endereco': Endereco,
                        'mae': Responsavel,
                        "Idade": Idade
                    }

                    texto = open("[KID]" + Nome + ".txt", "x")

                    self.top.destroy()
                    self.master.destroy()
                    Window1.resgistration_window(self.master)
                    salvar()
                else:
                    pass

class Window3():
    def __init__(self, master):
        load()
        self.master = master
        self.master.title("Equipe DI")
        self.master.iconbitmap("team.ico")
        self.master.minsize(560, 330)
        self.master.maxsize(560, 330)
        self.master.geometry('500x350+0+0')
        ############################################################################################################
        ##TAB

        prof_img = PhotoImage(file=r're.png')

        self.TAB = ttk.Notebook(self.master)
        self.tabADD = ttk.Frame(self.TAB)
        self.tabPAD = ttk.Frame(self.TAB)
        self.TAB.add(self.tabPAD, text="Inicio")
        self.TAB.grid(row=1, column=0, columnspan=550, rowspan=549, sticky='NESW')
        #############################################################

        self.tabHID = ttk.Frame(self.TAB, height=1000, width=1000)
        self.TAB.add(self.tabHID, state="hidden")

        ############################################################################################################

        self.search_var = StringVar()
        self.search_var.trace("w", lambda name, index, mode: self.update_list())

        ############################################################################################################
        self.menu = Menu(self.master)
        self.menukids = Menu(self.menu, tearoff=0)
        self.menukids.add_command(label="Registrar um novo coloborador", command=self.criar_registro)
        self.menukids.add_command(label="Sair", command=self.iExit)
        self.menu.add_cascade(label="Opções", menu=self.menukids)
        self.frame = ttk.Frame(self.tabPAD)
        self.frame.grid(sticky=W)

        self.ListaFrame = ttk.Frame(self.tabPAD)
        self.ListaFrame.grid(row=1, column=0, sticky=W)
        self.ButtonFrame = ttk.Frame(self.tabPAD)
        self.ButtonFrame.grid(row=5, column=0, sticky=W)
        self.BuscarFrame = ttk.Frame(self.tabPAD)
        self.BuscarFrame.grid(row=0, column=0, sticky=W)

        self.lista = Listbox(self.ListaFrame, height=15, width=int(24.01))
        self.lista.grid(row=1, column=0)

        self.buscar = ttk.Entry(self.BuscarFrame, font=("arial", 10), textvariable=self.search_var)
        self.buscar.grid(row=3, column=0)
        self.Button = ttk.Button(self.ButtonFrame, text="Ver Informações", command=self.ler_dados)
        self.Button.grid(row=4, column=1, sticky=W)
        self.Button1 = ttk.Button(self.ButtonFrame, text="Editar", command=self.editar_dados)
        self.Button1.grid(row=4, column=0, sticky=W)
        self.Button2 = ttk.Button(self.ButtonFrame, text="Informações adicionais", command=self.focar)
        self.Button2.grid(row=4, column=2, sticky=W)

        for nome in EQUIPI_DI:
            self.lista.insert(END, nome)

        self.master.config(menu=self.menu)

    def iExit(self):
        self.iExit = tkinter.messagebox.askyesno("Fechar", "Você deseja fechar a página de Registro?",
                                                 parent=self.master)
        if self.iExit > 0:
            self.master.destroy()
            salvar()
            window = pygetwindow.getWindowsWithTitle("UnderFox")[0]
            window.maximize()
            return

    def update_list(self):
        search_term = self.buscar.get()

        self.lista.delete(0, END)

        for item in EQUIPI_DI:
            if search_term.lower() in item.lower():
                self.lista.insert(END, item)

    def mostrarTAB(self):
        prof_img = PhotoImage(file=r'sinais (1).png')
        self.TAB.add(self.tabADD, text="Registrar", image=prof_img, compound=TOP)
        self.TAB.select(self.tabADD)

    def focar(self):
        self.ler_dados_adicionais()
        self.TAB.select(self.tabAPD)

    #################
    # Adicionar foto
    def ler_dados(self):
        try:
            try:
                self.nomeV.destroy()
            except:
                pass
            self.nom = self.lista.get(ACTIVE)
            self.telefone = EQUIPI_DI[self.nom]['numero']
            self.responsavel = EQUIPI_DI[self.nom]['funcao']
            self.endereco = EQUIPI_DI[self.nom]['endereco']
            self.info = EQUIPI_DI[self.nom]['idade']
            self.TUDO = StringVar()
            self.TUDO.set(
                self.nom + '\n' + self.telefone + '\n' + self.endereco + '\n' + self.responsavel + '\n' + self.info)

            self.nome = ttk.Label(self.ListaFrame, text="Nome:\nTelefone:\nEndereço:\nFunção:\nIdade:",
                                  font=("arial", 9, "bold"), justify=LEFT)
            self.nome.grid(row=1, column=4, sticky='WN')
            self.nomeV = ttk.Label(self.ListaFrame, textvariable=self.TUDO, justify=LEFT, font=('arial', 9))
            self.nomeV.grid(row=1, column=5, sticky='WN')
            self.ex = ttk.Button(self.ListaFrame, text="Excluir", command=self.excluir)
            self.ex.grid(row=1, column=4)

            self.ler_dados_adicionais()
        except:
            tkinter.messagebox.showerror("ERROR", 'Nenhum usuário válido selecionado!')

    def ler_dados_adicionais(self):
        try:
            self.tabAPD.destroy()
        except:
            pass
        self.tabAPD = Frame(self.TAB)
        prof_img = PhotoImage(file=r'x.png')
        self.TAB.add(self.tabAPD, text="Adicional Info", image=prof_img, compound=LEFT)

        self.nom = self.lista.get(ACTIVE)
        print(self.nom)

        if self.nom != "":
            try:
                texto = open("[TEAM]"+self.nom + ".txt", "x")
                TEXT = texto.read()

                self.t = Text(self.tabAPD, height=15, width=70)
                self.t.grid()
                self.t.insert(END, TEXT)
                texto_digitado = self.t.get(1.0, END)

                self.Save_BUTTON = ttk.Button(self.tabAPD, text="Salvar", command=self.salvar_texto)
                self.Save_BUTTON.grid()

            except Exception as error:
                print(error)
                texto = open("[TEAM]"+self.nom + ".txt", "r+")
                TEXT = texto.read()
                self.t = Text(self.tabAPD, height=15, width=70)
                self.t.grid()
                self.t.insert(END, TEXT)

                texto_digitado = self.t.get(1.0, END)

                self.Save_BUTTON = ttk.Button(self.tabAPD, text="Salvar", command=self.salvar_texto)
                self.Save_BUTTON.grid()

        else:
            tkinter.messagebox.showerror("", "Ninguém foi selecionado", parente=self.master)

    def salvar_texto(self):
        texto = self.t.get(1.0, END)
        opcao = tkinter.messagebox.askyesno("", "Você deseja salvar as alterações?", parent=self.master)
        if opcao > 0:
            with open("[TEAM]"+self.nom + ".txt", 'w') as f:
                f.write(texto)
                self.Save_BUTTON["text"] = "Salvar(Salvo)"
        else:
            pass

    ##################_________________________________________________________________________________________________________________
    def editar_dados(self):
        try:
            self.tabACD.destroy()
        except:
            pass
        self.nom = self.lista.get(ACTIVE)
        self.tabACD = Frame(self.TAB)
        prof_img = PhotoImage(file=r'x.png')
        self.TAB.add(self.tabACD, text="Edição de " + self.nom, image=prof_img, compound=LEFT)
        self.TAB.select(self.tabACD)

        #############################################################
        # Labels
        labelNo = Label(self.tabACD, text="Nome:", font="arial 10 bold", justify=LEFT)
        labelNo.grid(column=0, row=0, sticky=W)
        labelTelefone = Label(self.tabACD, text="Telefone:", font="arial 10 bold")
        labelTelefone.grid(column=0, row=1, sticky=W)
        labelEN = Label(self.tabACD, text="Endereço:", font="arial 10 bold", justify=LEFT)
        labelEN.grid(column=0, row=2, sticky=W)
        labelRes = Label(self.tabACD, text="Função:", font="arial 10 bold", justify=LEFT)
        labelRes.grid(column=0, row=3, sticky=W)
        labelIda = Label(self.tabACD, text="Idade:", font="arial 10 bold", justify=LEFT)
        labelIda.grid(column=0, row=4, sticky=W)

        labeldesnecessario = Label(self.tabACD)
        labeldesnecessario.grid(row=5, column=1)
        labeldesnecessario1 = Label(self.tabACD)
        labeldesnecessario1.grid(row=5, column=1)

        #############################################################
        # Stringvar

        sN = StringVar()
        sT = StringVar()
        sE = StringVar()
        sR = StringVar()
        sI = StringVar()

        ##############################################################
        # Entrys
        self.entryN = Entry(self.tabACD, textvariable=sN)
        self.entryN.grid(row=0, column=1)
        self.entryT = Entry(self.tabACD, textvariable=sT)
        self.entryT.grid(row=1, column=1)
        self.entryE = Entry(self.tabACD, textvariable=sE)
        self.entryE.grid(row=2, column=1)
        self.entryR = Entry(self.tabACD, textvariable=sR)
        self.entryR.grid(row=3, column=1)
        self.entryI = Entry(self.tabACD, textvariable=sI)
        self.entryI.grid(row=4, column=1)

        sN.set(self.nom)
        sT.set(EQUIPI_DI[self.nom]['numero'])
        sE.set(EQUIPI_DI[self.nom]['endereco'])
        sR.set(EQUIPI_DI[self.nom]['funcao'])
        sI.set(EQUIPI_DI[self.nom]['idade'])

        ##############################################################
        # Buttons
        Bsalvar = Button(self.tabACD, text="Salvar e fechar", command=self.salvar_editados)
        Bsalvar.grid(row=10, column=0, sticky='SW')

        Bsair = Button(self.tabACD, text="Sair sem salvar", command=self.sair_semsalvar1)
        Bsair.grid(row=10, column=1, sticky='SW')

    def excluir(self):
        nom = self.lista.get(ACTIVE)
        option = tkinter.messagebox.askyesno("Atenção!/ Watch out!",
                                             "VOCÊ TEM CERTEZA QUE DESEJA DELETAR O CONTATO " + nom + "?", parent=self.master)
        if option > 0:
            EQUIPI_DI.pop(nom)
            os.remove("[TEAM]"+ nom + ".txt")
            salvar()
            self.master.destroy()

            Window1.hospital_window(self.master)


        else:
            pass

    def salvar_editados(self):

        self.nom = self.lista.get(ACTIVE)

        Nome = self.entryN.get()
        Telefone = self.entryT.get()
        Endereco = self.entryE.get()
        Funcao = self.entryR.get()
        Idade = self.entryI.get()
        if Nome == "" or Nome == " ":
            tkinter.messagebox.showerror("ERROR!", "Nome inválido")
        else:
            if Nome in EQUIPI_DI:
                tkinter.messagebox.showerror('ERROR!', "Nome já registrado!")
            else:
                opcao = tkinter.messagebox.askyesno("", "Você deseja salvar as alterações?", parent=self.master)
                if opcao > 0:
                    EQUIPI_DI.pop(self.nom)
                    EQUIPI_DI[Nome] = {
                        'numero': Telefone,
                        'endereco': Endereco,
                        'funcao': Funcao,
                        "idade": Idade,
                    }

                    os.rename("[TEAM]"+self.nom + ".txt", "[TEAM]"+Nome + ".txt")
                    EQUIPI_DI.pop(self.nom)
                    self.tabACD.destroy()
                    self.master.destroy()
                    salvar()
                    Window1.hospital_window(self.master)

                else:
                    pass

    def sair_semsalvar(self):
        self.top.destroy()
        Window1.hospital_window(self.master)
    def sair_semsalvar1(self):
        self.tabACD.destroy()

    def criar_registro(self):
        self.master.destroy()
        self.top = Toplevel()
        self.top.geometry("230x160")
        self.top.title("Criar")

        labelNo = Label(self.top, text="Nome:", font="arial 10 bold", justify=LEFT)
        labelNo.grid(column=0, row=0, sticky=W)
        labelTelefone = Label(self.top, text="Telefone:", font="arial 10 bold")
        labelTelefone.grid(column=0, row=1, sticky=W)
        labelEN = Label(self.top, text="Endereço:", font="arial 10 bold", justify=LEFT)
        labelEN.grid(column=0, row=2, sticky=W)
        labelRes = Label(self.top, text="Responsável:", font="arial 10 bold", justify=LEFT)
        labelRes.grid(column=0, row=3, sticky=W)
        labelIda = Label(self.top, text="Idade:", font="arial 10 bold", justify=LEFT)
        labelIda.grid(column=0, row=4, sticky=W)

        labeldesnecessario = Label(self.top)
        labeldesnecessario.grid(row=5, column=1)
        labeldesnecessario1 = Label(self.top)
        labeldesnecessario1.grid(row=5, column=1)
        #############################################################
        # Stringvar

        sN = StringVar()
        sT = StringVar()
        sE = StringVar()
        sR = StringVar()
        sI = StringVar()
        #################################################################
        ##############################################################
        # Entrys
        self.entryN1 = Entry(self.top, textvariable=sN)
        self.entryN1.grid(row=0, column=1)
        self.entryT1 = Entry(self.top, textvariable=sT)
        self.entryT1.grid(row=1, column=1)
        self.entryE1 = Entry(self.top, textvariable=sE)
        self.entryE1.grid(row=2, column=1)
        self.entryR1 = Entry(self.top, textvariable=sR)
        self.entryR1.grid(row=3, column=1)
        self.entryI1 = Entry(self.top, textvariable=sI)
        self.entryI1.grid(row=4, column=1)
        #################################################################

        Bsalvar = Button(self.top, text="Salvar e fechar", command=self.Salvar_criado)
        Bsalvar.grid(row=10, column=0, sticky='SW')
        Bsair = Button(self.top, text="Sair sem salvar", command=self.sair_semsalvar)
        Bsair.grid(row=10, column=1, sticky='SW')

    def Salvar_criado(self):

        Nome = self.entryN1.get()
        Telefone = self.entryT1.get()
        Endereco = self.entryE1.get()
        Funcao = self.entryR1.get()
        Idade = self.entryI1.get()

        if Nome in EQUIPI_DI:
            tkinter.messagebox.showinfo("Não foi possível realizar a ação desejada!",
                                        "Nome já existente no registro! Porfavor diferencie este contato do outro, ou, caso esteja querendo edita-lo, vá na opção editar.")
        else:
            if Nome == "" or Nome == " ":
                tkinter.messagebox.showerror("ERROR", "Nome Inválido")
            else:
                opcao = tkinter.messagebox.askyesno("", "Você deseja salvar as alterações?", parent=self.top)
                if opcao > 0:
                    EQUIPI_DI[Nome] = {
                        'numero': Telefone,
                        'endereco': Endereco,
                        'funcao': Funcao,
                        "idade": Idade,
                    }

                    texto = open("[TEAM]" + Nome + ".txt", "x")
                    TEXT = texto.read()

                    self.top.destroy()
                    self.master.destroy()
                    Window1.hospital_window(self.master)
                    salvar()
                else:
                    pass


if __name__ == '__main__':
    main()
    salvar()