# TAREFA 11: BUSCA ITERATIVA E RECURSIVA

import time
import matplotlib.pyplot as plt

def busca_iterativa(A, n, x):
    i = 1
    while i <= n and A[i-1] != x:
        print(f"Iterativo: i={i}, A[{i}]={A[i-1]}")
        i += 1
    if i > n:
        print("Resultado: NÃO")
        return False
    else:
        print(f"Resultado: SIM na posição {i}")
        return True

def busca_recursiva(A, n, x):
    print(f"Recursivo: n={n}, A[{n}]={A[n-1] if n > 0 else 'vazio'}")
    if n == 0:
        print("Resultado: NÃO")
        return False
    if A[n-1] == x:
        print("Resultado: SIM")
        return True
    else:
        return busca_recursiva(A, n-1, x)

# Teste n=10
print("=== BUSCA COM n=10 ===")
A10 = list(range(1, 11))
print("Busca iterativa por 8:")
start = time.time()
busca_iterativa(A10, 10, 8)
tempo_iter_10 = time.time() - start

print("\nBusca recursiva por 8:")
start = time.time()
busca_recursiva(A10, 10, 8)
tempo_rec_10 = time.time() - start

# Teste n=100
print("\n=== BUSCA COM n=100 ===")
A100 = list(range(1, 101))
print("Busca iterativa por 80:")
start = time.time()
busca_iterativa(A100, 100, 80)
tempo_iter_100 = time.time() - start

print("\nBusca recursiva por 80:")
start = time.time()
busca_recursiva(A100, 100, 80)
tempo_rec_100 = time.time() - start

# Gráfico
tamanhos = [10, 100]
tempos_iter = [tempo_iter_10, tempo_iter_100]
tempos_rec = [tempo_rec_10, tempo_rec_100]

plt.figure(figsize=(10, 6))
plt.plot(tamanhos, tempos_iter, 'b-o', label='Iterativo')
plt.plot(tamanhos, tempos_rec, 'r-s', label='Recursivo')
plt.xlabel('Tamanho do vetor (n)')
plt.ylabel('Tempo (segundos)')
plt.title('Comparação: Busca Iterativa vs Recursiva')
plt.legend()
plt.grid(True)
plt.show()

print(f"n=10:  Iterativo={tempo_iter_10:.6f}s, Recursivo={tempo_rec_10:.6f}s")
print(f"n=100: Iterativo={tempo_iter_100:.6f}s, Recursivo={tempo_rec_100:.6f}s")
