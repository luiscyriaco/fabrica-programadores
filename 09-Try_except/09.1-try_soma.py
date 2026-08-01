# Criando as variáveis
num1 = input("Digite o primeiro número: ")
num2 = input("Digite o segundo número: ")

# Convertendo variáveis em número inteiro
try:
    num1 = int(num1)
    num2 = int(num2)

    print(f"A soma dos números é {num1 + num2}")

# Tratando a excessão de erro de número inteiro
except:
    print("São permitidos apenas números inteiros")