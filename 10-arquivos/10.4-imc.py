# Criando as variáveis e solicitando os dados do paciente
nome = input("Digite o nome do paciente: ")
altura = float(input("Digite a altura do paciente: "))
peso = float(input("Digite o peso do paciente: "))

# Calculando o IMC do paciente
imc = peso / (altura ** 2) 

# Apresentando a situação de saúde do paciente
if imc >= 30.0:
    print("Cuidado com a Saúde")
else:
    print("Tudo OK")

# Apresentando a situação do paciente
if imc < 18.5:
    print("Abaixo do peso")
elif imc < 24.9:
    print("Peso normal")
elif imc < 29.9:
    print("Sobrepeso")
elif imc < 34.9:
    print("Obesidade Grau I")
elif imc <39.9:
    print("Obesidade Grau II")
else:
    print("Obesidade Grau III")