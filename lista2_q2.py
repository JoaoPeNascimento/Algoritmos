#classe que cria os nós
class No:
    def __init__(self, valor):
        self.valor = valor
        self.filho_esq = None
        self.filho_dir = None

#classe que cira a árvore binaria 
class arvore:
    def __init__(self):
        self.root = None

#função para adicionar os nós na árvore 
    def adc(self, valor, node=None, altura=0):
        #verifica se a raiz está vazia para adicionar o nó na raiz 
        if node is None:
            node = self.root
        if self.root is None:
            self.root = No(valor)
            return altura
        #verifica o valor do nó para colocá-lo na posição correta conforme seu valor
        else:
            if valor < node.valor:
                if node.filho_esq is None:
                    node.filho_esq = No(valor)
                    altura += 1
                    return altura 
                else:
                    return self.adc(valor, node.filho_esq, altura + 1)
            elif valor > node.valor:
                if node.filho_dir is None:
                    node.filho_dir = No(valor)
                    altura += 1
                    return altura 
                else:
                    return self.adc(valor, node.filho_dir, altura + 1)

#função para procurar os nós na árvore e subir ao topo
    def sear(self, valor):
        if not self.root:           
            print("-1")
            return

        anterior = None        
        atual = self.root   
        level = 0               

        
        while atual:                              
            if atual.valor == valor:  
            
                if anterior:          
                    anterior.filho_esq = atual.filho_dir 
                    atual.filho_dir = self.root 
                    self.root = atual
                    print(level)
                else:
                    print(level)
                return
            anterior = atual
            if valor < atual.valor:
                atual = atual.filho_esq
            else:
                atual = atual.filho_dir
            
            level += 1

        print("-1")
    
arvre = arvore()

#recebe os comandos para caso queira adicionar ou procurar o nó inserido 
while True:
    try:
        comando = input().split()
        if comando[0] == "ADD":
            print(arvre.adc(int(comando[1])))
        elif comando[0] == "SCH":
            arvre.sear(int(comando[1]))
        else:
            break
    except:
        break
