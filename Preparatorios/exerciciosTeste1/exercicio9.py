#Faca um algoritmo que receba a medida do raio de um circulo e retorne a area do circulo.
# Nao esqueça de importar a biblioteca 'math' para trabalhar com a variavel necessaria para calcular a area do circulo

import math

raio = int(input("Informe a medida do raio de um circulo: "))
print("A area do circulo de raio", raio, "eh", (2*math.pi*raio))
