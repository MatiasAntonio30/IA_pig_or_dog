# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 06:44:42 2020

@author: Hashirama
"""

#features 
#pelo longo?
#perna curta
#fa auau?

from sklearn.svm import LinearSVC

porco1 = [0,1,0]
porco2 = [0,1,1]
porco3 = [1,1,0]

cachorro1 = [0,1,1]
cachorro2 = [1,0,1]
cachorro3 = [1,1,1]

#Classes dos meus animais, CLASSIFICAÇÂO 1=> porco 0=> Cachorro
dados = [porco1, porco2, porco3, cachorro1, cachorro2, cachorro3]
classes = [1,1,1,0,0,0]

#Instanciando um estimador
model = LinearSVC()

#Ensinando o meu modelo aprender com os dados
model.fit(dados, classes)

#Prevendo um animal estranho
animal_strage = [1,1,0]

print("O seu animal e" , model.predict([animal_strage]))
#1=> porco 0=> Cachorro



