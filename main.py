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

dbManager = DbManager()

print("Bem vindo!\nJá possui cadastro?")
cadastrar = str(input("(Sim/Não) >> "))
if cadastrar.lower() == "sim":
    menu()