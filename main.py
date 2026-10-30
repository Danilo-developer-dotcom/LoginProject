from src.dbManager import DbManager
from hashlib import sha256

def acesso(informado, coluna, onde=None):
    if not onde:
        onde = coluna
    dado = dbManager.select_dado(informado, coluna, where=onde)
    if dado:
        return dado[0][0]
    else:
        return False

def menu():
    while True:
        print("Login")
        email = str(input("Digite seu e-mail >> "))
        if "@" not in email and "." not in email:
            print("e-mail inválido")
            continue
        else:
            email_cadastrado = acesso(email, "email")
            if not email_cadastrado:
                print("e-mail inválido")
                continue
            print(email_cadastrado)
        for i in range(5, 0, -1):
            senha = str(input("Digite sua senha >> "))
            __hash = sha256(senha.encode('utf-8')).hexdigest()
            senha_cadastrada = acesso(email, "senha", onde="email")
            if __hash != senha_cadastrada and  i> 1:
                print(f"Senha inválida, mais {i-1} tentativas")
                continue

            elif __hash == senha_cadastrada:
                print(senha_cadastrada)
                nome = acesso(email, "nome", onde="email")
                print(f"Seja muito bem vindo(a), {nome}")
                return True

            else:
                print("O número de tentativas foi excedido")
                break

        return False


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
            __hash = sha256(senha.encode('utf-8')).hexdigest()
            break

    return nome, email, __hash




#Cria/acessa o Banco de Dados e a tabela de usuarios
dbManager = DbManager()

while True:
    print("Bem vindo!\nJá possui cadastro?")
    cadastrar = str(input("(Sim/Não) >> "))
    if cadastrar.lower() == "sim":
        login = menu()
        if not login:
            continue
        else:
            print("Agenda")

    elif cadastrar.lower() == "nao":
        usuario = cadastro()
        dbManager.create(usuario)
