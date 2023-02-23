# Questao 06 - Faca um programa que peca a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius
# Entrada do valor da temperatura em Fahrenheit
temperatura = float(input('Digite o valor da temperatura em (°F): '));
# Calculo de conversao de Fahrenheit para Celsius
converter = (temperatura - 32) * 5/9;
# Mostra o resultado da conversao de temperatura
print(f'O valor da temperatura em (ºC) é: {converter:.2f}');
