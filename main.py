from src.dbManager import DbManager
from src.emailManager import EmailManager
from hashlib import sha256
from src.agendaManager import AgendaManager
import sys
from src.utils import cadastro, acesso

#Cria/acessa o Banco de Dados e a tabela de usuarios
dbManager = DbManager()
email_v = EmailManager()
login = 0

#Acesso ao Sistema
while login == 0:
    print("Bem vindo!\nJá possui cadastro?")
    cadastrar = str(input("(Sim/Não) >> "))
    if cadastrar.lower() == "nao":
        usuario = cadastro()
        if not usuario:
            continue
        else:
            dbManager.create_usuario(usuario)

    elif cadastrar.lower() == "sim":
        print("Login")
        email = str(input("Digite seu e-mail >> "))
        if "@" not in email and "." not in email:
            print("e-mail inválido")
            continue
        else:
            email_cadastrado = acesso(email, "email")
            user_id: int = acesso(email, "id", onde="email")
            if not email_cadastrado:
                print("e-mail inválido")
                continue
        for i in range(5, 0, -1):
            senha = str(input("Digite sua senha >> "))
            __hash = sha256(senha.encode('utf-8')).hexdigest()
            senha_cadastrada = acesso(user_id, "senha", onde="id")
            if __hash != senha_cadastrada and i > 1:
                print(f"Senha inválida, mais {i - 1} tentativas")
                continue

            elif __hash == senha_cadastrada:
                nome = acesso(user_id, "nome", onde="id")
                print(f"Seja muito bem vindo(a), {nome}")
                login = user_id
                break

            else:
                print("O número de tentativas foi excedido")
                continue

# Sistema de Agendamento
agenda = AgendaManager(login)
while True:
    print("O que deseja fazer?")
    print("1 - Consultar meus agendamentos")
    print("2 - Agendar uma data")
    print("3 - Consultar disponibilidade")
    print("4 - Sair")

    escolha = int(input(">> "))
    match escolha:
        case 1:
            agendados = agenda.meus_agendamentos()
            for i in agendados:
                print(i[0])
            continue

        case 2:
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
                data = f"{dia}/{mes}/{ano}"
                agendar = agenda.marcar_data(data)
                if not agendar:
                    print(f"Não foi possível realizar o agendamento para o dia: {data}")
                break
        case 4:
            print("Encerrando Sistema...")
            sys.exit()
