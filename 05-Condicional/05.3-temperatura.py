# Criando a variável e solicitando a temperatura ao usuário
temperatura = float(input("Digite a temperatura em Celsius: "))

# Criando as regras da condição de SE
if  temperatura < 10:
    print("Está muito frio!")
elif temperatura < 20:
    print("Está Frio.")
elif temperatura < 30:
    print("Está agradável")
else:
    print("Está quente")