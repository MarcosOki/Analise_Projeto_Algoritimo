# TAREFA 9: SOMA DA DIREITA PARA ESQUERDA

def Soma_Dir_Esq(k, n, A):
    if k > n:
        s = 0
    else:
        s = A[k-1] + Soma_Dir_Esq(k+1, n, A)  # A[k-1] porque Python usa índice 0
    print(f"k={k}, n={n}, s={s}")
    return s

def Soma_Esq_Dir(k, n, A):
    if k > n:
        s = 0
    else:
        s = Soma_Esq_Dir(k+1, n, A) + A[k-1]
    print(f"k={k}, n={n}, s={s}")
    return s

# n=50
print("Soma-Dir-Esq para n=50:")
A = list(range(1, 51))
Soma_Dir_Esq(1, 50, A)

print("\nSoma-Esq-Dir para n=50:")
A = list(range(1, 51))
Soma_Esq_Dir(1, 50, A)

print("\nSoma-Dir-Esq para n=100:")
A = list(range(1, 101))
Soma_Dir_Esq(1, 100, A)

print("\nSoma-Esq-Dir para n=100:")
A = list(range(1, 101))
Soma_Esq_Dir(1, 100, A)

