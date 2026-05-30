# Criando as variáveis e solicitando os valores ao usuário
nome_produto = input("Digite o nome do produto: ")
valor = float(input("Digite o valor do produto: "))
desconto = float(input("Digite o percentual de desconto: "))

# Calculando a porcentagem e o valor do desconto
valor_desconto = valor * (desconto / 100)
preco_final = valor - valor_desconto

# Apresentando o preço final do produto ao usuário
print(f"Produto: {nome_produto} - Preço Final: {preco_final}")