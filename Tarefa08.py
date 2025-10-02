# TAREFA 8: SOMA RECURSIVA

def Soma(n, A):
    if n == 0:
        s = 0
    else:
        s = Soma(n-1, A) + A[n-1]
    print(f"n={n}, s={s}")
    return s


print("n=50:")
A = list(range(1, 51))
Soma(50, A)

print("\nn=100:")
A = list(range(1, 101))
Soma(100, A)

