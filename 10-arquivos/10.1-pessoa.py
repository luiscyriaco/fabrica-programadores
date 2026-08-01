# Solicitando nome e email ao usuário
nome = str(input("Digite o nome: "))
email = str(input("Digite o e-mail: "))

# Acessando arquivo e gravando dados do usuário
arquivo = open("10.1-pessoa.txt","a")
arquivo.write(nome + " | " + email + "\n")
arquivo.close()


