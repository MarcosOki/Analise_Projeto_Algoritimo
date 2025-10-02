"""
TAREFA 06 - ANÁLISE DE ALGORITMOS SOMA DE QUADRADOS
===================================================
"""
import time
import matplotlib.pyplot as plt

def soma_quadrados_a(n):
    x = 0                      
    for j in range(1, n + 1):  
        x = x + j * j        
    return x       

def soma_quadrados_b(n):  
    x = (n * (n + 1) * (2 * n + 1)) // 6   
    return x

def medir_tempo(algoritmo, n):
    inicio = time.perf_counter()
    resultado = algoritmo(n)
    tempo = time.perf_counter() - inicio
    return resultado, tempo

def plotar_grafico():
    valores_n = [1000, 5000, 10000, 50000, 100000]
    tempos_a, tempos_b = [], []
    
    print("Coletando dados de performance...")
    for n in valores_n:
        _, tempo_a = medir_tempo(soma_quadrados_a, n)
        _, tempo_b = medir_tempo(soma_quadrados_b, n)
        tempos_a.append(tempo_a)
        tempos_b.append(tempo_b)
        print(f"n={n:6d}: A={tempo_a:.6f}s | B={tempo_b:.6f}s")
    
    plt.figure(figsize=(10, 6))
    plt.plot(valores_n, tempos_a, 'ro-', label='Algoritmo A (O(n))', linewidth=2)
    plt.plot(valores_n, tempos_b, 'bo-', label='Algoritmo B (O(1))', linewidth=2)
    plt.xlabel('Tamanho da entrada (n)')
    plt.ylabel('Tempo de execução (s)')
    plt.title('Comparação de Performance: Soma de Quadrados')
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    print("ANÁLISE: SOMA DOS QUADRADOS (1² + 2² + ... + n²)")
    print("Linguagem: Python 3.13 | IDE: Visual Studio Code")
    print("="*55)
    
    # Teste de equivalência com n=5
    n = 5
    resultado_a, tempo_a = medir_tempo(soma_quadrados_a, n)
    resultado_b, tempo_b = medir_tempo(soma_quadrados_b, n)
    
    print(f"\nTeste com n={n}:")
    print(f"Algoritmo A: {resultado_a} (tempo: {tempo_a:.6f}s)")
    print(f"Algoritmo B: {resultado_b} (tempo: {tempo_b:.6f}s)")
    print(f"Resultados iguais? {'SIM' if resultado_a == resultado_b else 'NÃO'}")
    
    # Gráfico de performance
    plotar_grafico()

if __name__ == "__main__":
    main()


