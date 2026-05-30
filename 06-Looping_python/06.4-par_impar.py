# Criando a variável de contagem
contador_par = 0

# Laço de repetição for
for numero in range(1,11):
    if numero % 2 == 0:
        print(f"O número {numero} é PAR")
        contador_par += 1
    else:
        print(f"O número {numero} é ÍMPAR")

print("-" * 20)
print(f"Total de números pares encontrados {contador_par}")