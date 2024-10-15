import random
import time

# Gerando uma lista de 10 milhões de números inteiros aleatórios
tamanho_lista = 10_000_000
lista_original = [random.randint(0, tamanho_lista) for _ in range(tamanho_lista)]

def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]

def selection_sort(lista):
    n = len(lista)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if lista[j] < lista[min_idx]:
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]

# Testando o tempo de execução do Bubble Sort
lista_bubble = lista_original.copy()
inicio_bubble = time.time()
# bubble_sort(lista_bubble)
fim_bubble = time.time()
print(f"Tempo do Bubble Sort: {fim_bubble - inicio_bubble} segundos")

# Testando o tempo de execução do Selection Sort
lista_selection = lista_original.copy()
inicio_selection = time.time()
# selection_sort(lista_selection)
fim_selection = time.time()
print(f"Tempo do Selection Sort: {fim_selection - inicio_selection} segundos")