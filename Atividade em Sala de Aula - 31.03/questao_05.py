# questao 05 - Faca um programa que peca dois numeros inteiros e um numero real
#
# Importacao da funcao "pow" utilizando a biblioteca "math"
from math import pow
# Entrada de 2 valores inteiros e 1 real
num1 = int(input('Digite o primeiro numero inteiro: '));
num2 = int(input('Digite o segundo numero inteiro: '));
num3 = float(input('Digite um numero real: '));
# Calculo do 1º item
item1 = 2 * num1 + (num2/2);
# Calulo do 2º item
item2 = 3 * num1 + num3;
# Calculo do 3º item
item3 = pow(num3,3) ;
# Mostra os resultados dos 3 itens
print(f'O resultado do item 1 é: {item1:.3f}');
print(f'O resultado do item 2 é: {item2:.3f}');
print(f'O resultado do item 3 é: {item3:.3f}');
