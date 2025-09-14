import itertools
import time


def mostrar_rotas(cidades):
    cidade_inicial = cidades[0]
    outras_cidades = cidades[1:]


    # Gerar todas as permutações das outras cidades
    permutacoes = itertools.permutations(outras_cidades)


    # Exibir todas as rotas com a cidade inicial fixa
    for i, rota in enumerate(permutacoes, 1):
        rota_completa = (cidade_inicial,) + rota
        if i % 50000000 == 0:
            print(f"{i} combinações geradas...")


# Função para gerar cidades de 0 até n-1
def gerar_cidades(n):
    return list(range(n))


# Recebe o número de cidades
n_cidades = int(input("Digite o número de cidades: "))  # Exemplo: 5 ou 10


# Gerar a lista de cidades
cidades = gerar_cidades(n_cidades)


# Marca o tempo antes da execução
start_time = time.time()


# Exibe todas as rotas possíveis com a primeira cidade fixa
mostrar_rotas(cidades)


# Marca o tempo após a execução
end_time = time.time()


# Calcula o tempo de execução
execution_time = end_time - start_time


# Exibe o tempo de execução
print(f'\nTempo de execução: {execution_time:.6f} segundos.')