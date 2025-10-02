import time
import matplotlib.pyplot as plt

def lista_primo(n):
    x = 1
    A = [0] * (n + 1)
    
    for i in range(2, n + 1):
        j = 2
        while j < i and i % j != 0:
            j = j + 1
        if j == i:
            A[x] = i
            x = x + 1
    
    return [A[i] for i in range(1, x)]

def medir_tempo(n):
    """Mede tempo de execução do algoritmo."""
    inicio = time.time()
    lista_primo(n)
    return time.time() - inicio

def main():
    print("ANÁLISE DO ALGORITMO LISTA_PRIMO")
    print("=" * 40)
    
    # Gráfico de performance
    valores_n = [50, 100, 200, 300, 500, 700, 1000]
    tempos = [medir_tempo(n) for n in valores_n]
    
    print(f"\nDados:")
    for n, t in zip(valores_n, tempos):
        print(f"n={n}: {t:.6f}s")
    
    plt.figure(figsize=(10, 6))
    plt.plot(valores_n, tempos, 'bo-')
    plt.xlabel('Tamanho da entrada (n)')
    plt.ylabel('Tempo de execução (s)')
    plt.title('Performance do Algoritmo LISTA_PRIMO')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()