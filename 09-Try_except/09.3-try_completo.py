
# Criando as variáveis e realizando a divisão entre elas
try:
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input(" Digite o segundo número: "))

    resultado = num1 / num2

# Caso o erro seja de divisão por zero (denominador = 0)
except ZeroDivisionError:
    print("Erro: divisão por zero não é permitida.")

# Caso o erro seja por algum valor não numérico (digitar letras, por exemplo)
except ValueError:
    print("Erro: você precisa digitar apenas números inteiros.")

# Caso não haja erro, mostramos o resultado
else:
    print(f"Resultado da divisão: {resultado}")

# Este bloco sempre será executado, não importa se houve erro ou não
finally:
    print("Operação finalizada.")
