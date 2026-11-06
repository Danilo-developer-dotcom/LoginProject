from random import randint
from src.emailManager import EmailManager
from hashlib import sha256
from src.dbManager import DbManager


def confirma(mensagem):
    print(mensagem)
    resposta = str(input("Sim/Nao\n>> "))
    if resposta.lower() == "nao":
        return False
    elif resposta.lower() == "sim":
        return True

def cadastro() -> tuple | bool:
    while True:
        nome = str(input("Digite seu nome\n>> "))
        check = confirma(f"O nome digitado foi: {nome}, esse nome está certo?")
        if check:
            break
        else: continue
    while True:
        email = str(input("Digite seu e-mail:\n>> "))
        if "@" not in email and "." not in email:
            print("e-mail inválido")
            continue
        else:
            check = confirma(f"Será enviado um número de verificação para o email:\n{email}\nEsse email está certo?")
            if check:
                verificador = randint(1000, 9999)
                EmailManager().enviar(email, verificador)
                verificar = int(input("Digite o Número recebido no seu e-mail:\n>> "))
                if verificar != verificador:
                    print("Código incorreto! Verifique se o E-mail está correto e tente novamente.")
                    return False
                else: break
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

def acesso(informado, coluna, onde=None):
    if not onde:
        onde = coluna
    dado = DbManager().select_acesso(informado, coluna, where=onde)
    if dado:
        return dado[0][0]
    else:
        return False

def calendario():
    while True:
        print("Insira a data no formato DD/MM/AAAA")
        print("Digite o dia:")
        dia = int(input(">> "))
        if dia > 31:
            print("Dia inválido")
            continue
        print("Digite o mes:")
        mes = int(input(">> "))
        if mes > 12:
            print("Mes inválido")
            continue
        elif (mes in [4, 6, 9, 11] and dia == 31) or (mes == 2 and dia > 28):
            if mes != 2:
                print(f"O mês {mes} possui apenas 30 dias")
            else:
                print("O mês 2 posssui apenas 28 dias")
                continue
        print("Digite o ano:")
        ano = int(input(">> "))
        return f"{dia}/{mes}/{ano}"