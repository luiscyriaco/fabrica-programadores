# solicitando dados dos produtos ao usuário
nome_produto = input("Digite o nome do produto: ")
preco_produto = float(input("Digite o preço do produto: "))
quantidade_produto = input("Digite a quantidade: ")

# Acessando arquivo produtos.txt e gravando nome, preço e quantidade do produto
with open("10.5-produtos.txt","a",encoding="utf-8") as arquivo:
    arquivo.write(f"{nome_produto} | ")
    arquivo.write(f"{preco_produto:.2f} | ".replace(".",","))
    arquivo.write(f"{quantidade_produto} \n")

print("Produto cadastrado com sucesso")