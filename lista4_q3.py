# Ler a sequência de números e a constante
nums = list(map(int, input().split()))
const = int(input())

# Calcular o valor de K
min_val = min(nums)
k = max(nums) - abs(min_val * const)

# Inicializar o número de rodadas
rounds = 0

# Enquanto a lista não estiver vazia
while nums:
    # Remover o maior valor da lista
    max_val = max(nums)
    nums.remove(max_val)
    
    # Se K for maior que zero, adicionar K à lista
    if k > 0:
        nums.append(k)
    
    # Calcular o valor de K para a próxima iteração
    if nums:
        min_val = min(nums)
        k = max(nums) - abs(min_val * const)
    
    # Incrementar o número de rodadas
    rounds += 1

# Imprimir o número de rodadas
print(f"{rounds} rodadas, partindo para a próxima!")