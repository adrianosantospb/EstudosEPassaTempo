'''
    Exemplo de implementação de uma rede neural do tipo Perceptron
    Dev: Adriano Santos
'''

import random

class Perceptron():

    def __init__(self, entradas, saidas, taxa_aprendizado=0.1, epocas=1000):

        self.entradas = entradas
        self.saidas = saidas
        self.taxa_aprendizado = taxa_aprendizado
        self.epocas = epocas
        self.quantidade_entradas = len(entradas)
        self.quantidade_atributos = len(entradas[0])
        self.pesos = []

    # Função de treinamento
    def treinar(self):
        # Obtem os pesos
        for i in range(self.quantidade_atributos):
            self.pesos.append(random.random())

        # Valor dos pesos iniciais    
        print ('Os pesos foram ', self.pesos)
        # Inicia o contador de épocas
        contador_epocas = 0
        # Inicia a varivavel auxiliar de status
        erro = True

        # Loop de aprendizado
        while True:
            erro = False    
            for i in range(self.quantidade_entradas):
                # Potencial de ativação
                u = 0
                for j in range(self.quantidade_atributos):
                    u +=  self.pesos[j] * self.entradas[i][j]   
                u = u + self.__constante_teta()
                # Valor de saída
                y = self.degrau(u)
                # Atualização dos pesos
                if y != self.saidas[i]:
                    for j in range(self.quantidade_atributos):
                        self.pesos[j] = self.pesos[j] + self.taxa_aprendizado * (self.saidas[i] - y) * self.entradas[i][j]
                        erro = True
                # Incrementa época
                contador_epocas +=1   
            # Condição de parada
            if not erro or contador_epocas > self.epocas:
                break
        # Infoma a quantidade de épocas
        print ('Épocas utilizadas para o treinamento %d' % contador_epocas)
        # Valor dos pesos iniciais    
        print ('Pesos finais: ', self.pesos)

    # Função de teste
    def teste(self, amostra):
        u = 0
        for i in range(len(amostra)):
            u +=  self.pesos[i] * amostra[i]   
        u = u + self.__constante_teta()
        # Valor de saída
        print ('Saída: %d' % self.degrau(u))

    
    # Função degrau
    def degrau(self, u):
        return 1 if u > 0 else 0

    # constante Teta        
    def __constante_teta(self):
        return -1


# Valores de entrada e saída para o treinamento
#entradas = [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0],  [1, 1, 1]]
#saidas = [0, 1, 1, 1, 1, 1, 1, 1]

# Para uma porta AND
entradas = [[0, 0], [0, 1], [1, 0], [1, 1]]
saidas = [0, 0, 0, 1]


# Cria uma rede
rede = Perceptron(entradas, saidas)
rede.treinar()


# Define a saída
amostra = [0, 1]
print('Entrada de teste', amostra)
rede.teste(amostra)
