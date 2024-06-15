def busca(u, visitado, lista):
    visitado.add(u)
    for v in lista[u]:
        if v not in visitado:
            busca(v, visitado, lista)

n, m = map(int, input().split())
lista = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    lista[u-1].append(v-1)
    lista[v-1].append(u-1)

resultado = [0] * n
for i in range(n):
    visitado = set()
    busca(i, visitado, lista)
    resultado[i] = len(visitado)

print(*resultado)