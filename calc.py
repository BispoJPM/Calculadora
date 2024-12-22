def ad (n1, n2):return n1 + n2
def sb (n1, n2):return n1 - n2
def mt (n1, n2):return n1 * n2
def dv (n1, n2):   
    if n2 == 0: 
        return "Erro"
    return n1 / n2

while True:
    print("\nOpções:")
    print("\n1. Somar")
    print("2. Subtrair")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Sair", "\n")
    escolha = input("Escolha uma das opções: ")\

    if escolha == "5":

        break
    n1 = float(input("Digite o primeiro numero: "))
    n2 = float(input("Digite o segundo numero: "))

    if escolha == "1":
        print(f"A soma de {n1} + {n2} é igual a: {ad(n1, n2)}")
    elif escolha == "2":
        print(f"A subtração de {n1} - {n2} é igual a: {sb(n1, n2)}")
    elif escolha == "3":
        print(f"A multiplicacao de {n1} * {n2} é igual a: {mt(n1, n2)}")
    elif escolha == "4":
        print(f"A divisao de {n1} / {n2} é igual a: {dv(n1, n2)}")
    else:
        print("\nOpção inválida.")
    
