# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
# C = 5 * ((F-32) / 9).

fahrenheit = input('Informe a temperatura em Farenheit: ')
celsius = 5 * ((float(fahrenheit) -32) /9)

print(f'A temperatura em Celcius é {celsius:.2f}') # passar a quantidade de pontos flutuantes (f) no print deixa o código mais limpo
