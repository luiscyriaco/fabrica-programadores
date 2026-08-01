# Criando as variáveis e solicitando os dados ao usuário
nome_aluno = input("Digite o nome do aluno: ")
nota_1 = float(input("Digite a primeira nota: "))
nota_2 = float(input("Digite a segunda nota: "))
nota_3 = float(input("Digite a terceira nota: "))

# Calculando a média das notas do aluno
media = (nota_1 + nota_2 + nota_3) / 3

print(f"A média do aluno(a) {nome_aluno} é {media}")

# Criando as condições
if media >= 7:
    situacao = "Aprovado"
    print(f"Situação: {situacao}")
elif media > 4:
    situacao = "Recuperação"
    print(f"Situação: {situacao}")
else:
    situacao = "Reprovado"
    print(f"Situação: {situacao}")

# Gravando o nome, média e situação do aluno
with open("10.3-fabpro.txt","a", encoding="utf-8") as arquivo:
    arquivo.write(nome_aluno + " | " + str(media) + " | " + situacao + "\n")
