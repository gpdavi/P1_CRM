from Cliente import Cliente
from Usuario import Usuario
from Dados import Dados
from Campanha import Campanha
from Oportunidade import Oportunidade
from datetime import datetime

Dados.create("usuario.json")
Dados.create("clientes.json")
Dados.create("campanhas.json")
Dados.create("oportunidades.json")

usuario_logado = {"nome": None, "cargo": None}

def parse_data(texto):
    return datetime.strptime(texto.strip(), "%d/%m/%Y").date()

def datas_se_sopoem(ini1, fim1, ini2, fim2):
    return ini1 <= fim2 and ini2 <= fim1

def finalizar():
    print("Obrigado por usar o sistema de CRM. Até logo!")
    exit()

def login():
    while True:
        print("|  Bem-vindo ao sistema de CRM!        |")
        print("|  1. Login                            |")
        print("|  2. Registrar                        |")
        print("|  0. Sair                             |")
        escolha = input("O que você deseja fazer? ").strip()
        match escolha:
            case "1":
                login_usuario()
            case "2":
                cadastro()
            case "0":
                finalizar()
            case _:
                print("\033[41m Opção inválida. Tente novamente. \033[0m")


def login_usuario():
    print("\n--- Login ---")
    nomeusuario = input("Nome de usuário ou e-mail: ").strip()
    senha = input("Senha: ").strip()

    usuarios = Dados.load("usuario.json")
    for u in usuarios:
        if (u["Nome de Usuario"] == nomeusuario or u["Email"] == nomeusuario) and u["Senha"] == senha:
            usuario_logado["nome"] = u["Nome de Usuario"]
            usuario_logado["cargo"] = u["Cargo"]
            print(f"\nBem-vindo, {u['Nome de Usuario']}! (Cargo: {u['Cargo']})\n")
            menu_principal()
            return

    print("\033[41m Nome de usuário ou senha incorretos. \033[0m\n")


def cadastro():
    print("\n--- Cadastro de Usuário ---")
    nomeusuario = input("Nome de usuário: ").strip()
    email = input("E-mail: ").strip()

    while True:
        senha = input("Senha: ").strip()
        if nomeusuario.lower() in senha.lower():
            print("\033[41m A senha não pode conter o nome de usuário. \033[0m")
        else:
            break

    while True:
        confirmar = input("Confirme a senha: ").strip()
        if senha != confirmar:
            print("\033[41m As senhas não coincidem. \033[0m")
        else:
            break

    print("Cargos: 1. Gerente  |  2. Vendedor")
    while True:
        cargo = input("Cargo: ").strip()
        if cargo in ["1", "2"]:
            break
        print("Opção inválida.")

    novo = Usuario(nomeusuario, senha, email, cargo)
    novo.setcargo(cargo)

    usuarios = Dados.load("usuario.json")
    usuarios.append(novo.to_dict())
    Dados.save("usuario.json", usuarios)
    print("Usuário cadastrado com sucesso!\n")


def menu_principal():
    while True:
        cargo = usuario_logado["cargo"]
        print("|  MENU PRINCIPAL                      |")
        print("|  1. Registrar Cliente                |")
        print("|  2. Listar Clientes                  |")
        print("|  3. Buscar Clientes/Oportunidades    |")
        if cargo == "Gerente":
            print("|  4. Cadastrar Campanha               |")
            print("|  5. Listar Campanhas                 |")
            print("|  6. Aprovar/Recusar Oportunidades    |")
        if cargo == "Vendedor":
            print("|  4. Criar Oportunidade de Venda      |")
            print("|  5. Minhas Oportunidades             |")
        print("|  0. Logout                           |")
        escolha = input("Escolha: ").strip()

        if cargo == "Gerente":
            match escolha:
                case "1": registrar_cliente()
                case "2": listar_clientes()
                case "3": buscar()
                case "4": cadastrar_campanha()
                case "5": listar_campanhas()
                case "6": aprovar_recusar_oportunidades()
                case "0":
                    usuario_logado["nome"] = None
                    usuario_logado["cargo"] = None
                    print("Logout realizado.\n")
                    return
                case _: print("\033[41m Opção inválida. \033[0m")
        else:
            match escolha:
                case "1": registrar_cliente()
                case "2": listar_clientes()
                case "3": buscar()
                case "4": criar_oportunidade()
                case "5": minhas_oportunidades()
                case "0":
                    usuario_logado["nome"] = None
                    usuario_logado["cargo"] = None
                    print("Logout realizado.\n")
                    return
                case _: print("\033[41m Opção inválida. \033[0m")

def registrar_cliente():
    print("\n--- Registrar Cliente ---")
    nome = input("Nome: ").strip()
    email = input("E-mail: ").strip()
    telefone = input("Telefone: ").strip()
    cidade = input("Cidade: ").strip()
    valor = input("Valor potencial (R$): ").strip()

    print("Status: 1.Lead  2.Em contato  3.Negociando  4.Fechado  5.Perdido")
    while True:
        status = input("Status: ").strip()
        if status in ["1", "2", "3", "4", "5"]:
            break
        print("\033[41m Opção inválida. \033[0m")

    c = Cliente(nome, email, telefone, cidade, valor, status)
    c.setstatus(status)
    
    clientes = Dados.load("clientes.json")
    clientes.append(c.to_dict())
    Dados.save("clientes.json", clientes)
    print("Cliente registrado com sucesso!\n")


def listar_clientes():
    clientes = Dados.load("clientes.json")
    if not clientes:
        print("Nenhum cliente cadastrado.\n")
        return
    print("\n--- Lista de Clientes ---")
    for i, c in enumerate(clientes, 1):
        print(f"{i}. {c['Nome']} | {c['Cidade']} | R$ {c['Valor']} | Status: {c['Status']}")
    print()

def cadastrar_campanha():
    print("\n--- Cadastrar Campanha ---")
    titulo = input("Título: ").strip()
    descricao = input("Descrição: ").strip()

    while True:
        data_inicio = input("Data de início (DD/MM/AAAA): ").strip()
        if parse_data(data_inicio):
            break
        print("\033[41m Data inválida. Use o formato DD/MM/AAAA. \033[0m")

    while True:
        data_fim = input("Data de fim (DD/MM/AAAA): ").strip()
        d_fim = parse_data(data_fim)
        if d_fim and d_fim >= parse_data(data_inicio):
            break
        print("\033[41m Data inválida ou anterior à data de início. \033[0m")

    orcamento = input("Orçamento (R$): ").strip()

    camp = Campanha(titulo, descricao, data_inicio, data_fim, orcamento, usuario_logado["nome"])
    
    campanhas = Dados.load("campanhas.json")
    campanhas.append(camp.to_dict())
    Dados.save("campanhas.json", campanhas)
    print("Campanha cadastrada com sucesso!\n")


def listar_campanhas():
    campanhas = Dados.load("campanhas.json")
    if not campanhas:
        print("Nenhuma campanha cadastrada.\n")
        return
    print("\n--- Campanhas ---")
    for i, c in enumerate(campanhas, 1):
        print(f"{i}. [{c['Titulo']}] {c['Data Inicio']} até {c['Data Fim']} | R$ {c['Orcamento']} | Criada por: {c['Criado Por']}")
        print(f"   Descrição: {c['Descricao']}")
    print()

def criar_oportunidade():
    print("\n--- Criar Oportunidade de Venda ---")

    clientes = Dados.load("clientes.json")
    if not clientes:
        print("Nenhum cliente cadastrado. Registre um cliente primeiro.\n")
        return
    print("Clientes disponíveis:")
    for i, c in enumerate(clientes, 1):
        print(f"  {i}. {c['Nome']} ({c['Cidade']})")
    while True:
        try:
            idx = int(input("Número do cliente: ").strip()) - 1
            if 0 <= idx < len(clientes):
                cliente_nome = clientes[idx]["Nome"]
                break
        except ValueError:
            pass
        print("\033[41m Opção inválida. \033[0m")


    while True:
        data_inicio = input("Data de início (DD/MM/AAAA): ").strip()
        d_ini = parse_data(data_inicio)
        if d_ini:
            break
        print("\033[41m Data inválida. \033[0m")

    while True:
        data_fim = input("Data de fim (DD/MM/AAAA): ").strip()
        d_fim = parse_data(data_fim)
        if d_fim and d_fim >= d_ini:
            break
        print("\033[41m Data inválida ou anterior à data de início. \033[0m")

    oportunidades = Dados.load("oportunidades.json")
    for op in oportunidades:
        if op["Status"] == "Recusada":
            continue
        op_ini = parse_data(op["Data Inicio"])
        op_fim = parse_data(op["Data Fim"])
        if op["Vendedor"] == usuario_logado["nome"] and datas_se_sopoem(d_ini, d_fim, op_ini, op_fim):
            print(f"\033[41m Conflito: você já tem uma oportunidade com {op['Cliente']} nesse período ({op['Data Inicio']} - {op['Data Fim']}). \033[0m\n")
            return
        if op["Cliente"] == cliente_nome and datas_se_sopoem(d_ini, d_fim, op_ini, op_fim):
            print(f"\033[41m Conflito: o cliente {cliente_nome} já possui uma oportunidade nesse período. \033[0m\n")
            return

    valor = input("Valor potencial (R$): ").strip()

    campanhas = Dados.load("campanhas.json")
    campanha_titulo = None
    if campanhas:
        print("Vincular a uma campanha? (opcional)")
        for i, c in enumerate(campanhas, 1):
            print(f"  {i}. {c['Titulo']} ({c['Data Inicio']} - {c['Data Fim']})")
        print("  0. Sem campanha")
        while True:
            try:
                idx_c = int(input("Número da campanha: ").strip())
                if idx_c == 0:
                    break
                if 1 <= idx_c <= len(campanhas):
                    campanha_titulo = campanhas[idx_c - 1]["Titulo"]
                    break
            except ValueError:
                pass
            print("\033[41m Opção inválida. \033[0m")

    op = Oportunidade(usuario_logado["nome"], cliente_nome, data_inicio, data_fim, valor, campanha_titulo)
    oportunidades.append(op.to_dict())
    Dados.save("oportunidades.json", oportunidades)
    print("Oportunidade criada com sucesso! Aguardando aprovação do gerente.\n")


def minhas_oportunidades():
    oportunidades = Dados.load("oportunidades.json")
    minhas = [op for op in oportunidades if op["Vendedor"] == usuario_logado["nome"]]
    if not minhas:
        print("Você não possui oportunidades cadastradas.\n")
        return
    print("\n--- Minhas Oportunidades ---")
    for i, op in enumerate(minhas, 1):
        campanha = op["Campanha"] if op["Campanha"] else "—"
        print(f"{i}. Cliente: {op['Cliente']} | {op['Data Inicio']} - {op['Data Fim']} | R$ {op['Valor']} | Campanha: {campanha} | Status: {op['Status']}")
    print()

def aprovar_recusar_oportunidades():
    oportunidades = Dados.load("oportunidades.json")
    pendentes = [(i, op) for i, op in enumerate(oportunidades) if op["Status"] == "Pendente"]

    if not pendentes:
        print("Nenhuma oportunidade pendente.\n")
        return

    print("\n--- Oportunidades Pendentes ---")
    for pos, (i, op) in enumerate(pendentes, 1):
        campanha = op["Campanha"] if op["Campanha"] else "—"
        print(f"{pos}. Vendedor: {op['Vendedor']} | Cliente: {op['Cliente']} | {op['Data Inicio']} - {op['Data Fim']} | R$ {op['Valor']} | Campanha: {campanha}")

    while True:
        try:
            escolha = int(input("\nNúmero da oportunidade para avaliar (0 para voltar): ").strip())
            if escolha == 0:
                return
            if 1 <= escolha <= len(pendentes):
                break
        except ValueError:
            pass
        print("\033[41m Opção inválida. \033[0m")

    idx_real = pendentes[escolha - 1][0]
    print("1. Aprovar  |  2. Recusar")
    while True:
        acao = input("Ação: ").strip()
        if acao in ["1", "2"]:
            break
        print("\033[41m Opção inválida. \033[0m")

    oportunidades[idx_real]["Status"] = "Aprovada" if acao == "1" else "Recusada"
    Dados.save("oportunidades.json", oportunidades)
    status_texto = "Aprovada" if acao == "1" else "Recusada"
    print(f"Oportunidade {status_texto} com sucesso!\n")

def buscar():
    print("\n--- Busca de Clientes e Oportunidades ---")
    print("Deixe em branco os filtros que não deseja usar.\n")

    filtro_cidade = input("Cidade: ").strip().lower()
    filtro_valor_min = input("Valor mínimo (R$): ").strip()
    filtro_valor_max = input("Valor máximo (R$): ").strip()
    filtro_data_ini = input("Data início disponível (DD/MM/AAAA): ").strip()
    filtro_data_fim = input("Data fim disponível (DD/MM/AAAA): ").strip()

    v_min = float(filtro_valor_min) if filtro_valor_min else None
    v_max = float(filtro_valor_max) if filtro_valor_max else None
    d_ini = parse_data(filtro_data_ini) if filtro_data_ini else None
    d_fim = parse_data(filtro_data_fim) if filtro_data_fim else None

    clientes = Dados.load("clientes.json")
    resultado_clientes = []
    for c in clientes:
        if filtro_cidade and filtro_cidade not in c["Cidade"].lower():
            continue
        try:
            valor_c = float(str(c["Valor"]).replace(",", "."))
        except (ValueError, TypeError):
            valor_c = 0
        if v_min is not None and valor_c < v_min:
            continue
        if v_max is not None and valor_c > v_max:
            continue
        resultado_clientes.append(c)

    print(f"\n=== Clientes encontrados: {len(resultado_clientes)} ===")
    for c in resultado_clientes:
        print(f"  • {c['Nome']} | {c['Cidade']} | R$ {c['Valor']} | Status: {c['Status']}")
    oportunidades = Dados.load("oportunidades.json")
    resultado_ops = []
    for op in oportunidades:
        if filtro_cidade:
            cliente_op = next((c for c in clientes if c["Nome"] == op["Cliente"]), None)
            if not cliente_op or filtro_cidade not in cliente_op["Cidade"].lower():
                continue
        try:
            valor_op = float(str(op["Valor"]).replace(",", "."))
        except (ValueError, TypeError):
            valor_op = 0
        if v_min is not None and valor_op < v_min:
            continue
        if v_max is not None and valor_op > v_max:
            continue
        op_ini = parse_data(op["Data Inicio"])
        op_fim = parse_data(op["Data Fim"])
        if d_ini and op_fim and op_fim < d_ini:
            continue
        if d_fim and op_ini and op_ini > d_fim:
            continue
        resultado_ops.append(op)

    print(f"\n=== Oportunidades encontradas: {len(resultado_ops)} ===")
    for op in resultado_ops:
        campanha = op["Campanha"] if op["Campanha"] else "—"
        print(f"  • Vendedor: {op['Vendedor']} | Cliente: {op['Cliente']} | {op['Data Inicio']} - {op['Data Fim']} | R$ {op['Valor']} | Campanha: {campanha} | Status: {op['Status']}")
    print()

    login()
