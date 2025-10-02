# TAREFA 12: RECORRÊNCIAS

import time

def F_recursivo(n):
    if n == 0:
        return 1
    else:
        return F_recursivo(n-1) + n*(n+1)//2 + n

def F_recorrencia(n):
    return (n*n + 3*n + 2) // 2

# n=100
print("n=100:")
start = time.time()
resultado_rec_100 = F_recursivo(100)
t1 = time.time() - start
print(f"Recursivo: {resultado_rec_100}, Tempo: {t1:.6f}s")

start = time.time() 
resultado_recorr_100 = F_recorrencia(100)
t2 = time.time() - start
print(f"Recorrência: {resultado_recorr_100}, Tempo: {t2:.6f}s")


print("\nn=1000:")
print("Recursivo: ERRO - limite de recursão excedido")

start = time.time()
resultado_recorr_1000 = F_recorrencia(1000) 
t4 = time.time() - start
print(f"Recorrência: {resultado_recorr_1000}, Tempo: {t4:.6f}s")


