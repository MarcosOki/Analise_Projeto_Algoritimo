# TAREFA 10: MAIOR ELEMENTO DO VETOR

import time
import matplotlib.pyplot as plt

def Max_I(A, n):
    x = A[0]
    for i in range(1, n):
        print(f"i={i+1}, A[{i+1}]={A[i]}, x={x}")
        if A[i] > x:
            x = A[i]
    return x

def Max_R(A, n):
    if n == 1:
        return A[0]
    else:
        x = Max_R(A, n-1)
        print(f"n={n}, x={x}, A[{n}]={A[n-1]}")
        return A[n-1] if x < A[n-1] else x

# n=10
print("n=10:")
A10 = list(range(1, 11))
start = time.time()
Max_I(A10, 10)
t1 = time.time() - start

start = time.time()
Max_R(A10, 10)
t2 = time.time() - start

# n=100
print("\nn=100:")
A100 = list(range(1, 101))
start = time.time()
Max_I(A100, 100)
t3 = time.time() - start

start = time.time()
Max_R(A100, 100)
t4 = time.time() - start

# Gráfico
plt.plot([10, 100], [t1, t3], 'b-o', label='Iterativo')
plt.plot([10, 100], [t2, t4], 'r-s', label='Recursivo')
plt.xlabel('n')
plt.ylabel('Tempo (s)')
plt.legend()
plt.show()

print(f"n=10: Iter={t1:.6f}s, Rec={t2:.6f}s")
print(f"n=100: Iter={t3:.6f}s, Rec={t4:.6f}s")
