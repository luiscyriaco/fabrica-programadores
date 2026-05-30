# Criando a variável
temperatura = float(input("Digite a temperatura em Celsius: "))

# Verificando a condição da temperatura
if temperatura < 10:
    print("Está Muito Frio")
elif temperatura < 20:
    print("Está Frio")
elif temperatura < 30:
    print("Está Agradável")
else:
    print("Está Muito Quente")