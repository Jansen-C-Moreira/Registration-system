CRIANÇAS = {}
EQUIPI_DI = {}


def exportar(nome_do_arquivo):
    try:
        with open(nome_do_arquivo, "w") as arquivo:
            for crianca in CRIANÇAS:
                telefone = CRIANÇAS[crianca]["telefone"]
                endereco = CRIANÇAS[crianca]["endereço"]
                responsavel = CRIANÇAS[crianca]["responsável"]
                arquivo.write("kid,{},{},{},{}\n".format(crianca, telefone, endereco, responsavel))
            for adulto in EQUIPI_DI:
                telefone = EQUIPI_DI[adulto]["telefone"]
                endereco = EQUIPI_DI[adulto]["endereço"]
                email = EQUIPI_DI[adulto]["email"]
                arquivo.write("team,{},{},{},{}\n".format(adulto, telefone, endereco, email))
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
                    telefone = detalhes[2]
                    endereco = detalhes[3]
                    responsavel = detalhes[4]

                    CRIANÇAS[nome] = {
                        'telefone': telefone,
                        'endereço': endereco,
                        'responsável': responsavel,
                    }
                elif detalhes[0] == "team":
                    nome = detalhes[1]
                    telefone = detalhes[2]
                    endereco = detalhes[3]
                    email = detalhes[4]

                    EQUIPI_DI[nome] = {
                        'telefone': telefone,
                        'endereço': endereco,
                        'email': email,
                    }
        print("Load completo!")
    except:
        print("Erro ao carregar o arquivo!")


def ler_detalhes_criancas():
    telefone = input('Digite o nome do telefone: ')
    responsavel = input('Digite o nome do responsavel: ')
    endereco = input('Digite o nome do endereco: ')
    return telefone, responsavel, endereco

def ler_detalhes_equipe():
    telefone = input('Digite o número do telefone: ')
    email = input('Digite o nome do email: ')
    endereco = input('Digite o nome do endereco: ')
    return telefone, email, endereco

def adicionar():
    grupo = input("Deseja adicionar uma criança ou num novo voluntário?\n1- Criança\n2- Voluntário\n---> ")
    nome = input("Qual o nome? ")
    if grupo == "1":
        if nome not in CRIANÇAS:
            telefone, responsavel, endereco = ler_detalhes_criancas()
            CRIANÇAS[nome] = {
                "telefone": telefone,
                "endereço": endereco,
                "responsável": responsavel
            }
        else:
            print("Criança com o mesmo nome já presente no banco de dados, tente de novo especificando um sobrenome diferente")
    elif grupo == "2":
        if nome not in EQUIPI_DI:
            telefone, endereco, email = ler_detalhes_equipe()
            EQUIPI_DI[nome] = {
                "telefone": telefone,
                "endereço": endereco,
                "email": email
            }
        else:
            print("O nome digitado já consta em nosso banco de dados, tente novamente com o nome completo.")
    else:
        print("opção inválida")


def mostrar():
    grupo = input("\033[1;95m1- Equipe do DI\n2- Crianças\n---> ")
    try:
        if grupo == "2":
            print("\033[1;31m_______________Crianças__________________")
            grupo2 = []
            for index, criança in enumerate(CRIANÇAS):
                print("\033[1;34m", index, "\033[1;34m-" , criança)
                grupo2.append(criança)
            while True:
                escolha = input("\033[1;37m-----------\nDeseja ver as informações de alguém desta lista?\n1- Sim\n2- Não\n---> ")
                if escolha == "1":
                    escolha2 = input("\033[1;93mOk! Digite o número dela\n\033[1;91m---> ")
                    try:
                        buscar(grupo2[int(escolha2)])
                        break
                    except:
                        print("Opção inválida")
                elif escolha == "2":
                    print("Ok!")
                    break
                else:
                    print("Opção inválida")
        elif grupo == "1":
            print("\033[1;31m_______________Equipe__________________")
            for index, voluntario in enumerate(EQUIPI_DI):
                grupo2=[]
                print("\033[1;34m", index,"\033[1;34m-", voluntario)
                grupo2.append(voluntario)
            while True:
                escolha = input("\033[1;37m-----------\nDeseja ver as informações de alguém desta lista?\n1- Sim\n2- Não\n---> ")
                if escolha == "1":
                    escolha2 = input("Ok! Digite o número dela\n\033[1;93m---> ")
                    try:
                        buscar(grupo2[int(escolha2)])
                        break
                    except:
                        print("Opção inválida")
                elif escolha == "2":
                    print("Ok!")
                    break
                else:
                    print("Opção inválida")
    except Exception as error:
        print("Erro ao mostrar {}".format(grupo))
        print(error)


def buscar(individuo):
    if individuo in CRIANÇAS:
        print('Nome:', individuo)
        print('Telefone:', CRIANÇAS[individuo]['telefone'])
        print('Responsável(eis):', CRIANÇAS[individuo]['responsável'])
        print('Endereço:', CRIANÇAS[individuo]['endereço'])
        print('--------------------------------------------')
    elif individuo in EQUIPI_DI:
        print('Nome:', individuo)
        print('Telefone:', EQUIPI_DI[individuo]['telefone'])
        print('Endereço:', EQUIPI_DI[individuo]['endereço'])
        print("Email:", EQUIPI_DI[individuo]['email'])
        print('--------------------------------------------')
    elif individuo in EQUIPI_DI and CRIANÇAS:
        print("Este nome pertence à uma criança e à um membro do DI!\nPortanto ambos estão ai")
        print('------------------Criança--------------------')
        print('Nome:', individuo)
        print('Telefone:', CRIANÇAS[individuo]['telefone'])
        print('Responsável(eis):', CRIANÇAS[individuo]['responsável'])
        print('Endereço:', CRIANÇAS[individuo]['endereço'])
        print('----------------Equipe Do DI-------------------')
        print('Nome:', individuo)
        print('Telefone:', EQUIPI_DI[individuo]['telefone'])
        print('Endereço:', EQUIPI_DI[individuo]['endereço'])
        print("Email:", EQUIPI_DI[individuo]['email'])
        print('--------------------------------------------')
    else:
        print("Nome não encontrado em nossos bancos de dados! Veja se o nome e sobrenome estão corretos.")


def editar():
    Grupo = input("Primeiro escolha a que grupo a pessoa pertence\n1- Crianças\n2- Equipe do DI\n---> ")
    if Grupo == "1":
        Nome = input("OK! Agora digite o nome e o sobrenome da criança.\n---> ")
        if Nome in CRIANÇAS:
            print("Ok! Achamos este nome em nosso sistema.")
            novo_nome = input("Vamos lá, para começar digite o nome inteiro da criança:\n---> ")
            telefone = input("Digite agora o novo telefone da criança:\n---> ")
            endereco = input("O endereço agora:\n---> ")
            responsavel = input("Para finalizar escreva o nome de um dos responsáveis\n---> ")

            CRIANÇAS[novo_nome] = {
                "telefone": telefone,
                "endereço": endereco,
                "responsável": responsavel
            }
            print("\033[1;31m-------------Resultado------------------")
            buscar(novo_nome)
        else:
            print("Lamentamos muito, mas {} não corresponde a nenhum nome em nosso sistema".format(Nome))
    elif Grupo == "2":
        Pessoa = input("OK! Agora digite o nome e o sobrenome da pessoa.\n--->")
        if Pessoa in EQUIPI_DI:
            print("Ok! Achamos este nome em nosso sistema.")
            novo_nome = input("Vamos lá, para começar digite o nome inteiro da pessoa:\n---> ")
            telefone = input("Digite agora o novo telefone da pessoa:\n---> ")
            endereco = input("O endereço agora:\n---> ")

            EQUIPI_DI[novo_nome] = {
                "telefone": telefone,
                "endereço": endereco
            }
            buscar(novo_nome)
        else:
            print("Lamentamos muito, mas {} não corresponde a nenhum nome em nosso sistema".format(Pessoa))
    else:
        print("Opção inválida!")


def excluir():
    pessoa = input("Ok! Quem deseja excluir?(colocar sobrenome se possível)\n---> ")
    try:
        buscar(pessoa)
    except:
        print("Erro ao buscar nome!")
    while True:
         escolha = input("\033[1;31mDeseja mesmo excluir?\n1- Sim\n2- Não\n---> ")
         if escolha == "1":
            if pessoa in CRIANÇAS:
                CRIANÇAS.pop(pessoa)
                print("Ok! Registro de {} excluido com sucesso.".format(pessoa))
                break
            elif pessoa in EQUIPI_DI:
                EQUIPI_DI.pop(pessoa)
                print("Ok! Registro de {} excluido com sucesso.".format(pessoa))
                break
            else:
                print("Algum erro ocorreu")
         elif escolha == "2":
             print("Ok! Contato mantido")
             break


def menu():
    print("---------------Menu----------------")
    print("1- Adicionar à lista")
    print("2- Buscar")
    print("3- Excluir")
    print("4- Editar")
    print("5- Mostrar toda a lista")
    print("6- Salvar")
    print("0- Sair do programa")


if __name__== "__main__":
    load()
    while True:
        menu()
        escolhaI= input("Opção\n--> ")
        if escolhaI == "1":
            try:
                adicionar()
                print("Adicionado com sucesso!")
            except:
                print("Erro ao adicionar!")
        elif escolhaI == "2":
            try:
                individuo = input("Por quem deseja procurar? ")
                buscar(individuo)
            except:
                print("Erro ao buscar")
        elif escolhaI == "3":
            try:
                excluir()
            except:
                print("Erro ao excluir !")
        elif escolhaI == "4":
            try:
                editar()
            except:
                print("Erro ao tentar editar!")
        elif escolhaI == "5":
            try:
                mostrar()
            except:
                print("Erro ao mostrar a lista!")
        elif escolhaI == "6":
            salvar()
            if salvar():
                print("Tudo slavo com sucesso!")
        elif escolhaI == "0":
            salvar()
            print("------END------")
            print("OK! Até breve!")
            break


