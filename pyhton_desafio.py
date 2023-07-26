menu = """""

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """
i=0
j=0
saldo = 0.0
limite = 500.00
extrato=""
numero_saques=0
LIMITES_SAQUES=3

while True:
    opcao=input(menu)

    if opcao =="d":
        deposito=float(input("Digite o valor do deposito: "))
        if deposito>0:
            i+=1
            saldo+=deposito
            extrato+=f"Deposito: R${deposito:.2f}\n"
            print(f"Valor depositado: R${deposito:.2f}")
        else:
            print("Valor invalido")        
    elif opcao =="s":
        saque=float(input("Digite o valor que deseja sacar: "))
        
        if saque<limite and numero_saques<LIMITES_SAQUES:
            saldo=saldo-saque
            numero_saques+=1
            limite=limite-saque
            extrato+=f" Saque: R${saque:.2f}"
            print(f"Valor sacado R${saque:.2f}")
        else:
            print("Operação falhou! saque invalido.")

    elif opcao=="e":
      print("Extrato:\n")
      print(extrato)
    elif opcao =="q":
        break
    else:
        print("Operação invalida, por favor selecione novamente a opção desejada")