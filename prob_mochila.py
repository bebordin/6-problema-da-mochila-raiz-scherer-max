class Objetos:
    def __init__(self, valor, peso):
        self.valor = valor
        self.peso = peso
        self.hash = 0
    def get_valor(self):
        return self.valor

    def get_peso(self):
        return self.peso

    def get_hash(self):
        return self.hash

    def set_hash(self, hash):
        self.hash = hash    

class Mochila:
 
    def __init__(self, peso_maximo):
        self.peso_maximo = peso_maximo
        self.maior_valor = 0
        self.peso_usado = 0
        #self.vetor_quebra_recursao = []
    def coloca_coisas(self, vet, peso_atual, valor_soma):
        if len(vet) == 0 or peso_atual > self.peso_maximo:
            return    
        elif valor_soma > self.maior_valor and peso_atual <= self.peso_maximo:
            self.peso_usado = peso_atual
            self.maior_valor = valor_soma
        for i in range(len(vet)):
            peso = peso_atual + vet[i].get_peso()
            soma = valor_soma + vet[i].get_valor()
            new_vetor = vet.copy()
            del(new_vetor[i])
            self.coloca_coisas(new_vetor, peso, soma)    

    def print_resultados(self):
        print(self.peso_usado)
        print(self.maior_valor)
        '''
        print(valor_atual)
        if len(vet) == 0 or peso_atual > self.peso_maximo:
            return 
        if valor_atual > self.maior_valor:
            self.maior_valor = valor_atual
            self.peso_usado = peso_atual
        for i in range(len(vet)):
            objeto = vet[i]
            peso_atual += objeto.get_peso()
            valor_atual += objeto.get_valor()
            vetr = vet.copy()
            vetr.remove(vet[i])
            self.coloca_coisas(vetr, valor_atual, peso_atual)
    def get_peso(self):
        return self.peso_usado
    def get_valor(self):
        return self.maior_valor
    '''
'''

    def define_mochila(self, vetor_objetos):
        print('vetor_quebra: ' + str(len(self.vetor_quebra_recursao)))
        #print(self.vetor_quebra_recursao)
        var = self.coloca_coisas(0, vetor_objetos, 0, 0)
        print(self.vetor_quebra_recursao)
                    
        
    def gera_vetor_hash(self, vetor_objetos):
        tamanho_vetor = (2 ** len(vetor_objetos))
        for i in range(tamanho_vetor):
            self.vetor_quebra_recursao.append(0)
        
        for j in range(len(vetor_objetos)):
            vetor_objetos[j].set_hash(2 ** j)
                
    def coloca_coisas_tentativa(self, index_objeto, vetor_objetos, valor_atual, peso_atual, soma_hash):
        if len(vetor_objetos) == 0: #se o vetor está vazio
            return self.maior_valor
            
        self.objeto = vetor_objetos[index_objeto]
        del(vetor_objetos[index_objeto])
        peso_atual += self.objeto.get_peso()
        soma_hash += self.objeto.get_hash()
        valor_atual += self.objeto.get_valor()
        if int(self.vetor_quebra_recursao[soma_hash]) < valor_atual: #verifica se existe algum elemento no vetor de quebra
            self.vetor_quebra_recursao[soma_hash] = valor_atual
        else: 
            return self.maior_valor
        for i in range(len(vetor_objetos)):
            #self.coloca_coisas(i, vetor_objetos, valor_atual, peso_atual, soma_hash)
'''
    
    
obj1 = Objetos(5,5)
obj2 = Objetos(10,10)
obj3 = Objetos(30,15)
obj4 = Objetos(15,30)
obj5 = Objetos(40,15)
obj6 = Objetos(7,7)
vetor_objetos = [obj1, obj2, obj3, obj4, obj5, obj6]
mochila = Mochila(15)
#mochila.gera_vetor_hash(vetor_objetos)
#mochila.define_mochila(vetor_objetos)
mochila.coloca_coisas(vetor_objetos, 0, 0)
#print(mochila.get_peso())
#print(mochila.get_valor())
mochila.print_resultados()                            
