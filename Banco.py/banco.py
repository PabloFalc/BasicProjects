saquesdiario = 3
saquestotal= 0
valorsaque = 500
saldo = 0
extrato = ""



def sacar ():
    global saquesdiario, saquestotal, saldo, extrato

    if saquestotal == saquesdiario:
        
        print("""
              +=======================================+
              | Seu limite de saques já foi atingindo |
              +=======================================+""")
        return

    while True: 
        valor = float(input("Qual o valor do saque: "))

        if valor > 500:
            print("""
                  +=======================+
                  | Está fora dos limites |
                  +=======================+""")
        else:
            print(f"foram sacados: R${valor: .2f}")
            saquestotal += 1 
            saldo += valor
            extrato += f"Foi sacado R${valor: .2f}\n"
            return
        
    
def deposito():

    global saldo, extrato

    if saldo <=0:
        print("""
               +=============================================+
               | Saldo insuficiente para realizar a operação |
               +=============================================+""")
    while True:

        valor = float(input("Qual valor deseja adicionar: "))
        if valor > saldo:
            print("o valor depositado é maior que o saldo")
        else:
            print(f"Foram depositado R${valor: .2f}")
            saldo -= valor
            extrato += f"Foi depositado R$ {valor: .2f}\n"
            return


menu = """
+=================================+
|       Bem-vindo ao Banco        |
|                                 |
|  [1]  Sacar       [2] Extrato   |
|                                 | 
|  [3] Deposito     [4] Saldo     |
|                                 |
|            [5] Sair             |
|                                 |
+=================================+
      """



while True:

    opcao = int(input(menu))

    if opcao == 1:
        sacar()
    elif opcao ==2:
        print(extrato)
    elif opcao == 3:
        deposito()
    elif opcao == 4:
        print(saldo)
    elif opcao == 5:
        print("saindo do sistema")
        exit()
    else:
        print("opção inválida")
