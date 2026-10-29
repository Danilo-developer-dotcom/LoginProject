from src.dbManager import DbManager

def menu():
    while True:
        print("Login")
        email = str(input("Digite seu e-mail >> "))
        if "@" not in email and "." not in email:
            print("e-mail inválido")
            continue
        senha = str(input("Digite sua senha >> "))
        print(f"Bem vindo, {email.split("@")[0]}!")
        break

def confirma(mensagem):
    print(mensagem)
    resposta = str(input("Sim/Nao\n>> "))
    if resposta.lower() == "nao":
        return False
    elif resposta.lower() == "sim":
        return True

def cadastro() -> tuple:
    while True:
        nome = str(input("Digite seu nome\n>> "))
        check = confirma(f"O nome digitado foi: {nome}, esse nome está certo?")
        if check:
            break
        else:
            continue
    while True:
        email = str(input("Digite seu e-mail:\n>> "))
        if "@" not in email and "." not in email:
            print("e-mail inválido")
            continue
        else:
            check = confirma(f"O e-mail digitado foi {email}, esse email está certo?")
            if check:
                break
            else:
                continue
    while True:
        senha = str(input("Digite sua senha\n>> "))
        senha_confirmacao = str(input("Confirme sua senha\n>> "))
        if senha != senha_confirmacao:
            print("As senhas estão diferentes")
            continue
        else:
            break

    return nome, email, senha




#Cria/acessa o Banco de Dados e a tabela de usuarios
dbManager = DbManager()

print("Bem vindo!\nJá possui cadastro?")
cadastrar = str(input("(Sim/Não) >> "))
if cadastrar.lower() == "sim":
    menu()
elif cadastrar.lower() == "nao":
    usuario = cadastro()
    dbManager.create(usuario)