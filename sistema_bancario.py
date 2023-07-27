menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair
 


=> """


saldo_atual = float()
limite_saque = 500
extrato = ""
numero_saques = 3

while True:
    
    opcao = input(menu)
         
         
    if opcao == "1":
        deposito = float(input("Valor do depósito: "))
        
        if deposito >0:
            saldo_atual += deposito
            extrato += f"Depósito: R${deposito:.2f}\n"
            print("Seu saldo atual é de :", saldo_atual)
        else:
             print("Valor inválido") 
    elif opcao == "2":
        saque =float(input("Valor saque: "))
        if saque <= saldo_atual and saque <= 500 and numero_saques > 0 and saque > 0:
                saldo_atual -= saque
                numero_saques = numero_saques - 1
                extrato += f"Saque: R${saque:.2f}\n"
                print("Saque realizado com sucesso e seu saldo atual é de:", saldo_atual, "e possui mais ", numero_saques, "saques hoje")
        
        elif numero_saques == 0:
                print("Você atingiu seu limite de saques hoje, tente novamente amanhã.")
        
        elif saldo_atual < saque:
             print("Saldo insuficiente;")
        
        elif saque > 500:
             print("O seu limite de saque por vez é de R$ 500")

        else:
             print("Valor inválido!")
    elif opcao == "3":
        print("\n====== extrato ======")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print( f"\nSaldo: R$ {saldo_atual:.2f}")
        print("=======================")
    elif opcao == "4":
        break

    else:
        print("Operador inválido, tente novamente...")                 


