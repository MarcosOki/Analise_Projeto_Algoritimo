import itertools
import time


def mostrar_rotas(cidades):
    cidade_inicial = cidades[0]
    outras_cidades = cidades[1:]

    permutacoes = itertools.permutations(outras_cidades)

    for i, rota in enumerate(permutacoes, 1):
        rota_completa = (cidade_inicial,) + rota
        if i % 50000000 == 0:
            print(f"{i} combinações geradas...")

def gerar_cidades(n):
    return list(range(n))
n_cidades = int(input("Digite o número de cidades: "))
cidades = gerar_cidades(n_cidades)
start_time = time.time()
mostrar_rotas(cidades)
end_time = time.time()
execution_time = end_time - start_time
print(f'\nTempo de execução: {execution_time:.6f} segundos.')