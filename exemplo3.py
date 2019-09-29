import numpy as np
#calcular area do circulo

raio = input("digite o numero do raio do circulo: ") # recebe valor informado pelo usuário
raio = float(raio) #tranforma a string em float

pi = np.pi #define valor de pi
area = pi * (raio ** 2) # calcula área do circulo

area = round( area, 2 ) #arredonda a área

print("A área é igual a :", area) #exibe a área calculada e arredondada