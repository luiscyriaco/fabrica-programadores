# Função converter dolar para real
def dolar_real(valor_dolar):
    taxa = 5.06 #taxa câmbio
    valor_real = valor_dolar * taxa
    return(valor_real)

# Função conveter real para dolar
def real_dolar(valor_real):
    taxa = 5.06 #taxa câmbio
    valor_dolar = valor_real / taxa
    return(valor_dolar)

 # Menu interativo
def menu():
    while True:
        print("\n=== Conversor de Moedas ===")
        print("1 - Dólar para Real")
        print("2 - Real para Dólar")
        print("0 - Sair")

        opcao = int(input("Escolha uma opção: ")) # Lê a opção do usuário

        if opcao == 1:
            valor = float(input("Digite o valor em Dólar $  "))
            resultado = dolar_real(valor)
            print(f"$ {valor} = R$ {resultado}")

        elif opcao == 2:
            valor = float(input("Digite o valor em Real R$ "))
            resultado = real_dolar(valor)
            print(f"R$ {valor} = $ {resultado}")
        
        elif opcao == 0:
            print("Obrigado por usar o Conversor de Moedas!")
            break
        
        else:
            print("Opção inválida. Tente novamente.")

# Executa o programa
menu()