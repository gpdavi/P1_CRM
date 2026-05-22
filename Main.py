from Cliente import Cliente
from Usuario import Usuario
from Dados import Dados

Dados.create("usuario.json")
Dados.create("clientes.json")

def finalizar():
    print("Obrigado por usar o sistema de CRM. Até logo!")
    exit()
    
def login():
    print (
        "|=====================================|"
        "\n|Bem-vindo ao sistema de CRM!         |"+
        "\n|Por favor, faça login para continuar.|"+
        "\n|1. Login                             |"+
        "\n|2. Registrar                         |"+
        "\n|0. Sair                              |"+ 
        "\n|=====================================|")
    escolha = input("O que você deseja fazer? ")
    match escolha:
        case "1":
            login_usuario()
        case "2":
            cadastro()
        case "0":
            finalizar()
        case _:
            print("\033[41m Opção inválida. Por favor, tente novamente. \033[0m")

def login_usuario():
    print("Login de usuário")
    nomeusuario = input("Digite seu nome de usuário: ")
    senha = input("Digite sua senha: ")
    usuarios = Dados.load("usuario.json")
    for usuario in usuarios:
        if (usuario["Nome de Usuario"] == nomeusuario or usuario["Email"] == nomeusuario) and usuario["Senha"] == senha:
            print(f"Bem-vindo, {nomeusuario}!")
            menu()
            return
    print("\033[41m Nome de usuário ou senha incorretos.\033[0m")
    login_usuario() 

def cadastro():
    print("Cadastro de usuário")
    nomeusuario = input("Digite seu nome: ")
    email = input("Digite seu email: ")
    while True:
        senha = input("Digite sua senha: ")
        if nomeusuario.lower() in senha.lower():
            print("\033[41m A senha não pode conter o nome de usuário.")
        else:   
            break
    while True:
        confirmar_senha = input("Confirme sua senha: ")
        if senha != confirmar_senha:
            print("\033[41m As senhas não coincidem. Por favor, tente novamente.")
        else:
            break
    print("Cargos disponíveis:")
    print("1. Gerente")
    print("2. Vendedor")
    while True:
        cargo = input("Qual o cargo do usuário? ")
        if cargo in ["1", "2"]:
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")
    
    
    validar = Usuario(nomeusuario, senha, email, cargo)
    validar.setsenha(senha)
    validar.setcargo(cargo)
    
    usuarios = Dados.load("usuario.json")  
    usuarios.append(validar.to_dict())     
    Dados.save("usuario.json", usuarios)
    login()

def menu():
     print (
        "|=====================================|"
        "\n|Menu Principal                       |"+
        "\n|1. Registrar Clientes                |"+
        "\n|2. Listar Clientes                   |"+
        "\n|0. Sair                              |"+ 
        "\n|=====================================|")
       

def regcliente():
    print("Registrar cliente")
    nome = input("Digite o nome do cliente: ")
    email = input("Digite o email do cliente: ")
    telefone = input("Digite o telefone do cliente: ")
    cidade = input("Digite a cidade do cliente: ")
    valor = input("Digite o valor da venda: ")
    print("Status do cliente:")
    print("1. Lead")
    print("2. Em contato")
    print("3. Negociando")
    print("4. Fechado")
    print("5. Perdido")
    while True:
        status = input("Qual o status do cliente? ")
        if status in ["1", "2", "3", "4", "5"]:
            break
        else:
            print("\033[41m Opção inválida. Por favor, tente novamente.\033[0m")
    
    cliente_arq = Cliente(nome, email, telefone, cidade, valor, status)
    cliente_arq.setstatus(status)
    
    clientes = Dados.load("clientes.json")
    clientes.append(cliente_arq.to_dict())
    Dados.save("clientes.json", clientes)

login()
