#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 17:43:27 2019

@author: Adriano Santos
"""

import random

class Perceptron:
    
    def __init__(self, descritores, labels, taxa_aprendizado=0.1, epocas=10):
        self.descritores = descritores
        self.labels = labels
        self.taxa_aprendizado = taxa_aprendizado
        self.epocas = epocas
        self.pesos = []

    # Definição da função de treinamento
    def treinamento(self, funcao = 0):

        # Iniciando o treinamento
        print ('Iniciando o processo de treinamento.')
        
        # ********************* Instanciando os pesos *********************
        pesos = []
        # Limiar de ativação
        limiar_ativacao = -1

        for i in range(len(self.descritores[0])):
            self.pesos.append(random.random())

        # ********************* Inicia Treinamento  *********************
        for i in range(self.epocas):
            print('Epoca ', i + 1)
            # Analisa os descritores
            for j in range(len(self.descritores)):
                # Potencial de ativação
                u = 0
                # Combinador Linear
                x = self.descritores[j]
                for k in range (len(x)):
                    u += x[k] * self.pesos[k]
                
                # Limiar de ativação (Estático)
                u = u + limiar_ativacao

                # Obtem saída
                y = self.__degrau(u) if funcao == 0 else self.__bipolar(u) 
                
                # Regra de Hebb
                if y != self.labels[j]:
                    for l in range(len(self.pesos)):
                        self.pesos[l] = self.pesos[l] + self.taxa_aprendizado * (self.labels[j][0] - y) * x[l]        

        print ('Finalizando o processo de treinamento.')
    
    # Função de classificação
    def classificar(self, label):
        u = 0
        for i in range(len(label)):
            u +=  self.pesos[i] * label[i]   
        u = u - 1
        # Valor de saída
        print ('Saída: %d' % self.__degrau(u))
    
    # Função degrau
    def __degrau(self, u):
        return 1 if u >= 1 else 0

    # Função bipolar
    def __bipolar(self, u):
        return 1 if u >= 1 else -1

 

# Teste da rede Perceptron
if __name__ == "__main__":
    #  ******************** Dados para o treinamento ******************** 
    # Exemplo 1
    # descritores = [[0, 0], [0, 1], [1, 0], [1, 1]]
    # labels = [[0], [0], [0], [1]]
    
    # Exemplo 2
    descritores = [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0],  [1, 1, 1]]
    labels = [[0], [1], [1], [1], [1], [1], [1], [1]]
    
    # Instanciando o objeto
    p = Perceptron(descritores, labels, taxa_aprendizado=0.05, epocas=10)
    # Realizando o treinamento
    p.treinamento(funcao=0)
    # Realizando o processo de classificação
    p.classificar([1, 1, 1])