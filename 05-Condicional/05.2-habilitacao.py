# Criando as variáveis
nome = input("Qual é o seu nome? ")
idade = int(input("Qual é sua idade? "))

# Verificando condição da idade
if idade >= 18:
    possui_carteira = input("Possui carteira de motorista? \n (1-Sim / 2-Não) ")
    if possui_carteira == "1":
        print("Pode dirigir")
    else:
        print("Não pode dirigir")

else:
    print("Menor de idade")