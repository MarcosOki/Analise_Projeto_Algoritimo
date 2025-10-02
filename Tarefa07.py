"""
TAREFA 07 - CÁLCULO DE T(n) E ANÁLISE DE EFICIÊNCIA
"""
import matplotlib.pyplot as plt

def soma_iterativa(A, n):
    soma = 0                   
    for i in range(n):       
        soma = soma + A[i]    
    return soma                 

def soma_recursiva(A, n):
    if n == 1:           
        return A[0]
    else:
        return A[n-1] + soma_recursiva(A, n-1)

def plotar_grafico():
    n_values = [100, 500, 1000, 2000, 5000]
    tempo_iterativo = [n * 0.001 for n in n_values]
    tempo_recursivo = [n * 0.002 for n in n_values]
    
    plt.figure(figsize=(10, 6))
    plt.plot(n_values, tempo_iterativo, 'bo-', label='Iterativo O(n)')
    plt.plot(n_values, tempo_recursivo, 'ro-', label='Recursivo O(n)')
    plt.xlabel('Tamanho da entrada (n)')
    plt.ylabel('Tempo de execução')
    plt.title('Complexidade Temporal - Ambos O(n)')
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    print("Executando análise dos algoritmos...") 
    plotar_grafico()

if __name__ == "__main__":
    main()


