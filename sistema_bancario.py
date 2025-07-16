menu = """
   [d] Depositar
   [s] Sacar
   [e] Extrato
   [q] Sair
   Escolha uma opção: """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    if opcao == "d":
        valor = float(input("Informe o valor a ser depositado: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Valor inválido para depósito.")

    elif opcao == "s":
        valor = float(input("Informe o valor a ser sacado: "))
        if 0 < valor <= saldo and valor <= limite and numero_saques < LIMITE_SAQUES:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Saque inválido. Verifique o saldo, limite ou número de saques.")

    elif opcao == "e":
        print("Extrato:")
        print(extrato if extrato else "Nenhuma movimentação realizada.")
        print(f"Saldo atual: R$ {saldo:.2f}")

    elif opcao == "q":
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida. Tente novamente.")