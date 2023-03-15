def remover_duplicados(lista):
    return list(set(lista))

lista = [1, 2, 3, 3, 4, 4, 5, 6, 7, 8, 9, 9]
listaSemDuplicados = remover_duplicados(lista)
print(listaSemDuplicados)

