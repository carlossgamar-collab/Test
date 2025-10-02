def bubble_sort(lista):
    n = len(lista)
    # Recorremos todos los elementos de la lista
    for i in range(n):
        # Últimos i elementos ya están ordenados, no es necesario revisarlos
        for j in range(0, n-i-1):
            # Intercambiamos si el elemento encontrado es mayor que el siguiente
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]

    return lista

# Ejemplo de uso
numeros = [64, 34, 25, 12, 22, 11, 90]
print("Lista original:", numeros)
ordenada = bubble_sort(numeros)
print("Lista ordenada:", ordenada)

