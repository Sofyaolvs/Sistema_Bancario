menu = """
[D] = depositar
[S] = sacar
[E] = extrato
[Q] = sair
"""

saldo = 0
limite = 500
extrato = ""
limite_saque = 3
LIMITE_SAQUES = 3
numero_saque = 0

while True:
    opcao = input(menu)

    if opcao == "D":
        valor = float(input("Informe o valor desejado para depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Valor do depósito inválido")

    elif opcao == "S":
        valor = float(input("Informe o valor desejado para saque: "))
        
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_limite_saques = numero_saque >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Valor do saldo é menor do que o valor desejado para saque")
        elif excedeu_limite:
            print("Valor de limite para saque excedido")
        elif excedeu_limite_saques:
            print("Limite de saques por dia excedido")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R${valor:.2f}\n"
            numero_saque += 1
        else:
            print("Operação falhou! valor inválido")

    elif opcao == "E":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações" if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("===========================================")
    
    elif opcao == "Q":
        print("Saindo do programa...")
        break

    else:
        print("Opção inválida!")



     

