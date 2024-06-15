def mediana_salarios(sport, futuro_clube):
    salarios = sport + futuro_clube

    def mergesort(lista):
        if len(lista) <= 1:
            return lista
        meio = len(lista) // 2
        esquerda = lista[:meio]
        direita = lista[meio:]
        esquerda_ordenada = mergesort(esquerda)
        direita_ordenada = mergesort(direita)
        return merge(esquerda_ordenada, direita_ordenada)

    def merge(lista1, lista2):
        i = 0
        j = 0
        resultado = []
        while i < len(lista1) and j < len(lista2):
            if lista1[i] <= lista2[j]:
                resultado.append(lista1[i])
                i += 1
            else:
                resultado.append(lista2[j])
                j += 1
        resultado += lista1[i:]
        resultado += lista2[j:]
        return resultado
    
    ordenados = mergesort(salarios)

    n = len(ordenados)
    if n % 2 == 0:
        mediana = (ordenados[n // 2] + ordenados[n // 2 - 1]) / 2
    else:
        mediana = ordenados[n // 2]
    
    return f"O salário sugerido por Juba na primeira negociação será de {mediana:.2f} mil reais."

sport = list(map(int, input().split()))
futuro_clube = list(map(int, input().split()))
print(mediana_salarios(sport, futuro_clube))