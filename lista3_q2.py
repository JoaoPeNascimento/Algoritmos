espacos = int(input())
memoria = [None] * espacos

def hash(x):
    return x % espacos


#verifica os espaços próximos
def verificacao(indice):
    i = (indice + 1) % espacos
    while memoria[i] is not None and i != indice:
        i = (i + 1) % espacos
    if i == indice:
        print('Toda memoria utilizada')
        exit()
    return i

#loop para receber os comandos
c = int(input())
while c != 0:
    comando = input().split()
    #comando para adicionar os números 
    if comando[0] == 'ADD':
        x = int(comando[1])
        indice = hash(x)
        if memoria[indice] is None:
            memoria[indice] = x
            print(f'E: {indice}')
        else:
            i = verificacao(indice)
            memoria[i] = x
            print(f'E: {i}')
        c -= 1
    #comando para pesquisar os números 
    elif comando[0] == 'SCH':
        d = int(comando[1])
        indice = hash(d)
        i = indice
        while memoria[i] is not None:
            if memoria[i] == d:
                print(f'E: {i}')
                break
            i = (i + 1) % espacos
            if i == indice:
                print('NE')
                break
        else:
            print('NE')
        c -= 1
    #comando para fazer a consulta dos espaços
    elif comando[0] == 'CAP':
        m = int(comando[1])
        if memoria[m] is None:
            print('D')
        else:
            print(f'A: {memoria[m]}')
        c -= 1