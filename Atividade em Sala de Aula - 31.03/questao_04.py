# questao 04 - Faca um programa que peca o raio de um circulo, calcule  e mostre sua area
# Importacao do valor do "pi" utilizando a biblioteca "math"
from math import pi
# Entrada do valor do raio
raio = float(input('Digite o valor do raio: '));
# Calulo da area do circulo
area = pi * raio ** 2;
# Mostra o resultado da area do circulo
print(f'O valor da area do circulo é: {area:.2f}');
