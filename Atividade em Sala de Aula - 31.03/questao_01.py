# Questão 01 - Faca um programa que calcule a media de 3 notas
#
# Entrada das notas
nota1 = float(input('Entre com a primeira nota: '));
nota2 = float(input('Entre com a segunda nota: '));
nota3 = float(input('Entre com a terceira nota: '));
# Calculo da media com 3 notas
media = (nota1 + nota2 + nota3)/3;
# Mostra o resultado da media com duas casas decimais
print(f'O valor da sua média é: {media:.2f}');
