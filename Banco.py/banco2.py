
import os
import time

def menuBanco():
    print("""
========= MENU BANCO =========      
| [1] Sacar                  |
| [2] Deposito               |
| [3] Extrato                |
| [4] Criar Usuário          |
| [5] Criar Conta            |
| [6] Listar Contas          |
| [0] Sair                   |
==============================
          """)
    return("=> ")

def criar_usuario(usuarios):
    limparTela()
    print("======================================")
    print("|         Criar novo usuário         |")
    print("======================================")

    while True:
        cpf = str(input("Digite o CPF ex.: 044.034.566-90:\n=> "))
        cpf.replace(".", "")
        cpf.replace("-", "")
        if verificar_cpf(cpf,usuarios)==True:
            print("CPF já cadastrado")
        else:
            break
    nome = str(input("Digite seu nome: "))
    
    data_nascimento = str(input("Digite a data de nascimento ex.: 01/01/2000: "))
    data_nascimento.replace("/", "")

    endereco = str(input("Digite o endereço ex.: Cidade, Estado: "))

    senha = str(input("Digite a senha: "))

    usuarios.append({"nome": nome,"cpf": cpf, "data Nascimento": data_nascimento ,"Endereço": endereco, "senha": senha})

    print("======================================")
    print("|     Usuário criado com sucesso     |")
    print("======================================")
    time.sleep(3)

def verificar_usuario(cpf,senha,usuarios):
    for usuario in usuarios:
        if usuario["cpf"] == cpf and usuario["senha"] == senha:
         
           return usuario
        
    else:
        return False

def verificar_cpf(cpf,usuarios):

    #verificacao = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    #return verificacao[0] if verificacao else None

    # verificação = [usuario] se usuario["cpf"] = cpf
    # retorna vefiricação[0] se lista é True (com algum elemento), retorna verificação[0], se  lista é False (vazia) retona None


    for variavel in usuarios:
       if variavel["cpf"] == cpf:
            return True
    else:
        return False

def criar_conta(usuarios, agencia, numero_conta, contas):
    
    limparTela()
    print("======================================")
    print("|         Criar nova conta           |")
    print("======================================")
    while True:
        cpf = str(input("Insira seu cpf ex.: 033.344.334-44\n=>"))
        cpf.replace(".", "")
        cpf.replace("-", "")
        senha = str(input("Insira a senha: "))
        usuario = verificar_usuario(cpf,senha,usuarios)

        if usuario: 
            print("======================================")
            print("|      Conta criada com sucesso      |")
            print("======================================")
            numero_conta += 1
            break
        else:
            print("==============================================")
            print("|  CPF ou senha incorretos, tente novamente  |")
            print("==============================================")
            time.sleep(3)
            return
        
    contas.append({"Agência": agencia, "numero_conta": numero_conta , "usuario": usuario})

def listar_contas(contas):
    limparTela()
    print("======================================")
    print("|         Listagem de contas         |")
    print("======================================")
    opcao = str(input("Deseja lista alguma conta específica? ex.: nome ou cpf\n\ndigite 'não' para contar todas as contas\n=>"))
    
    
    if opcao == "não":
        for conta in contas:
            print(f"""
            Agência: {conta["Agência"]}
            Número da conta: {conta["numero_conta"]}
            Títular: {conta["usuario"]["nome"]}
            CPF: {conta["usuario"]["cpf"]}
            """)
    else:
        for conta in contas:
            if conta["usuario"]["cpf"] == opcao or conta["usuario"]["nome"] == opcao:
                print(f"""
                Agência: {conta["Agência"]}
                Número da conta: {conta["numero_conta"]}
                Títular: {conta["usuario"]["nome"]}
                CPF: {conta["usuario"]["cpf"]}
                """)

    input("Pressione enter para continuar...")

def sacar(*,limite, extrato, numeroSaques,limiteSaque, saldo, valor):
    limparTela
    limiteUltrapassado = valor > limite
    saquesUltrapassado = numeroSaques >= limiteSaque
    saldoInsuficiente = valor > saldo

    if limiteUltrapassado:
        print("======================================")
        print("|    Valor do saque ultrapassado     |")
        print("======================================")

    elif saquesUltrapassado:
        print("=====================================")
        print("| limite de saques diários atingido |")
        print("=====================================")
        time.sleep(3)
    elif saldoInsuficiente:
        print("=====================================")
        print("|   Saldo insuficiente para saque   |")
        print("=====================================")
        time.sleep(3)
    else:
        saldo -= valor
        extrato += f"Foi sacado R${valor: .2f}\n"
        print(numeroSaques)
        print("=====================================")
        print("|          Saque realizado          |")
        print("=====================================")
        time.sleep(3)
        

    return saldo, extrato

def depositar(saldo, extrato, valor,/):
 
    if valor == 0:
        print("======================================")
        print("|   Valor de depósito inválido       |")
        print("======================================")
        time.sleep(3)
    else:
        saldo += valor
        extrato += f"Foram depositados R${valor: .2f}\n"
        print("======================================")
        print("|        Depósito realizado          |")
        print("======================================")
        time.sleep(3)

    return saldo, extrato

def exbExtrato(saldo,/,*, extrato):

    limparTela()
    print("====== Histórico de Movimentações ======")
    print("Não foram realizadas movimentações" if not extrato else extrato) #printe "não foram..." se extrato for falso, ou seja ""
    print(f"Saldo: {saldo: .2f}")
    print("========================================")
    input("Pressione enter para continuar...")

def limparTela():

    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def main():
    
    limite_Saque = 3
    numero_saques = 0
    limite = 500
    
    agencia = "0001"
    saldo = 0
    extrato = ""
    usuarios = []
    contas = []
    numero_contas = 0

    while True:
        limparTela()
        opcao = int(input(menuBanco()))

        if opcao == 1:
            valor = float(input("Qual o valor do saque: "))
            saldo, extrato = sacar(
                saldo=saldo, 
                valor=valor, 
                extrato=extrato, 
                limite=limite, 
                limiteSaque=limite_Saque,
                numeroSaques=numero_saques,
                )
            numero_saques += 1
        elif opcao == 2:
            valor = float(input("Qual o valor do depósito: "))
            saldo, extrato = depositar(saldo, extrato, valor)

        elif opcao == 3:
            exbExtrato(saldo, extrato=extrato)

        elif opcao == 4:
            criar_usuario(usuarios)
        elif opcao == 5:
            criar_conta(usuarios, agencia, numero_contas, contas)
        elif opcao == 6:
            listar_contas(contas)
        elif opcao == 0:
            break
        else:
            print("======================================")
            print("|            Opção inválida          |")
            print("======================================")
            time.sleep(1)
        
main()



















