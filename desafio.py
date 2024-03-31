def depositar(valor,saldo,extrato, /):
    mensagem = ""
    if valor > 0:
        saldo += valor
        extrato += f"Depósito R$ {valor:.2f}\n"
        mensagem = f"O valor de R${valor} foi depositado na sua conta!"
    else:
        mensagem = "Operação falhou! O valor informado é inválido."
    print(mensagem)
    return saldo, extrato

def sacar(saldo,valor,extrato,limite,numeros_saques,limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numeros_saques > limite_saques
    if excedeu_saldo:
        mensagem = f"Você não tem saldo o suficinete para retirar! Seu saldo: R${saldo} | Valor que desejava sacar: R${valor}\n ------------"
    elif excedeu_limite:
        mensagem = f"Você já excedeu o limite do valor de saque! Valor desejado para sacar R${valor} | Limite é R$500\n ------------"
    elif excedeu_saques:
        mensagem = "Você já alcançou o número de saques do dia que são 3, volte amanhã para sacar\n ------------"
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: {valor:.2f}\n"
        numeros_saques += 1
        mensagem = f"O saque com o valor de R${valor} foi realizado com sucesso!"
    else:
        mensagem = "A operação falhou! O valor de saque é inválido\n ------------"
    print(mensagem)
    return saldo, extrato, numeros_saques

def exibir_saldo(saldo,extrato):
    print("------------Extrato------------")
    print(f"{extrato}\nSaldo: {saldo} \n--------------------")

def verificar_usuario(cpf,usuarios):
        usuarios_encontrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
        return usuarios_encontrados[0] if usuarios_encontrados else None

def criar_usuario(usuarios):
    cpf = input("Digite o seu CPF (Apenas números): ")
    if verificar_usuario(cpf, usuarios):
        print("Esse usuario já existe!")
        return
    nome = input("Digite o seu nome: ")
    data_nascimento = input("Informe a data do seu nascimento (dd-mm-aaaa): ")
    endereco = input("Digite o seu endereço (Logradouro, nro - Bairro - Cidade/Sigla estado): ")
    usuarios.append({'nome': nome,'cpf': cpf,'data_nascimento': data_nascimento,'endereço':endereco})
    print("Usuario cadastrado com sucesso")

def criar_conta(agencia,numero_conta,usuarios):
    cpf = input("Digite o seu CPF (Apenas números): ")
    usuario = verificar_usuario(cpf, usuarios)
    if usuario:
        print("\nA conta foi criada com sucesso!")
        return {'agencia': agencia,'cpf': cpf,'numero_conta': numero_conta,'usuario': usuario}
    print("Ocorreu um erro na criação da conta, encerrando processo!")

def listar_contas(contas):
    for conta in contas:
        mensagem = f"""
        Agência: {conta['agencia']}
        Número conta: {conta['numero_conta']}
        Titular: {conta['usuario']['nome']}
        """
        print("-" * 100)
        print(mensagem)

def main():
    menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nu] Novo Usuario
    [na] Nova Conta
    [lc] Listar Contas
    [q] Sair
    --> """

    saldo = 0
    LIMITE = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    usuarios = []
    contas = []
    AGENCIA = "0001"

    while True:
        opcao = input(menu)
        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(valor, saldo, extrato)
        elif opcao == "s":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato, numero_saques = sacar(saldo=saldo,valor=valor,extrato=extrato,limite=LIMITE,numeros_saques=numero_saques,limite_saques=LIMITE_SAQUES)
        elif opcao == "e":
            exibir_saldo(saldo,extrato=extrato)
        elif opcao == "nu":
            criar_usuario(usuarios)
        elif opcao == "na":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA,numero_conta,usuarios)
            if conta:
                contas.append(conta)
        elif opcao == "lc":
            listar_contas(contas)
        elif opcao == "q":
            print("O sistema foi encerrado, tenha um ótimo dia!")
            break;
        else:
            print("O valor dado está incorreto!")
main()