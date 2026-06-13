import random
# Função que sorteia uma tarefa aleatória de uma lista
def sorteio(lista):
    return random.choice(lista)

# Apresenta lista de tarefasdomésticas após o sorteio
print(sorteio(['Diogo', 'Gabriel', 'Juliano', 'Miguel']))