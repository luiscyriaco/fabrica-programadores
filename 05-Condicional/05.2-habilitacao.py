# Criando as variáveis e solicianto os valores ao usuário
nome = input("Qual é o seu nome? ")
idade = int(input("Qual é a sua idade? "))
possui_carteira = int(input(("Possui carteira de motorista? \n (1-Sim / 2-Não) ")))

# Criando a condição de desvio
if idade >= 18:
    if possui_carteira == 1:
        print("Pode dirigir")
    else:
        print("Não pode dirigir")
 
else:
    print("Menor Idade")