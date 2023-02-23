# Questao 07 - Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuario. Calcule o total em segundos
#
dias = int(input('Quantos dias: '));
horas = int(input('Quantas horas: '));
minutos = int(input('Quantos minutos: '));
segundos = int(input('Quantos s10egundos: '));
# Transformar dias em segundos
result1 = dias * 24 * 3600;
# Transformar horas em segundos
result2 = horas * 3600;
# Transformar minutos em segundos
result3 = minutos * 60
# Resultado em segundos
total_de_segundos = result1 + result2 + result3 + segundos;
# Mostra o resultado do total de segundos
print(f'O total do tempo em segundos é: {total_de_segundos:.2f}');
