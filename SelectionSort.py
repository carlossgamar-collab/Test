def selection_sort(lista):
    n = len(lista)
    # Recorremos toda la lista
    for i in range(n):
        # Suponemos que el elemento mínimo es el primero no ordenado
        indice_minimo = i

        # Buscamos el elemento más pequeño en el resto de la lista
        for j in range(i+1, n):
            if lista[j] < lista[indice_minimo]:
                indice_minimo = j

        # Intercambiamos el elemento encontrado con el primero no ordenado
        lista[i], lista[indice_minimo] = lista[indice_minimo], lista[i]

    return lista


# Ejemplo de uso
numeros = [64, 25, 12, 22, 11]
print("Lista original:", numeros)
ordenada = selection_sort(numeros)
print("Lista ordenada:", ordenada)