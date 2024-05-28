menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

continuar = ""
while True:

    opcao = input(menu)

    if opcao == "d":
        print("Deposito")
        aux = float(input("Valor a ser depositado: "))
        if aux < 0:
            print("Não é posivel depositar um valor negativo!!")
            continuar = input("Continuar...")
        else:
            saldo += aux
            print("Deposito feito com sucesso!!")
            continuar = input("Continuar...")
        
    
    elif opcao == "s":
        print("Saque")
        saque = 0
        saque = float(input("Valor a ser sacado: "))
        if numero_saques > LIMITE_SAQUES:
            print("Limite de saques diarios exedido")
            continuar = input("Continuar...")
        elif saque < 0:
                print("Não é posivel sacar um valor negativo!!")
                continuar = input("Continuar...")
        elif saldo < saque:
            print("Não é possivel sacar por falta de saldo!")
            continuar = input("Continuar...")
        elif saque> 500.00:
            print("Valor de saque execedido")
            continuar = input("Continuar...")
        
        else:
            saldo -= saque
            print("Saque feito com sucesso!!")
            numero_saques += 1
            continuar = input("Continuar...")    

                
    elif opcao == "e":
        print("Extrato")
        if saldo == 0 :
            print("Não foram realizadas movimentações")
            continuar = input("Continuar...")
        else:
            print(f"Extrato: {saldo: .2f} ")
            continuar = input("Continuar...")
    
    elif opcao == "q":
        break
    else:
        print("Operação invalida, por favor selecione a operação desejada")