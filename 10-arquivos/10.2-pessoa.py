# Solicitando nome e email ao usuário
nome = str(input("Digite o nome: "))
email = str(input("Digite o e-mail: "))

# Acessando arquivo e gravando dados do usuário
with open("10.2-pessoa.txt","a") as arquivo:
    arquivo.write(nome + " | " + email + "\n")