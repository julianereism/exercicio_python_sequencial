# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área. 

import math # importar biblioteca pra puxar o valor de pi

raio = input('Digite o raio do círculo: ')
area = math.pi * (float(raio) *2)

area_formatada = f"{area:.2f}"

print(f'A área do círculo é: {area_formatada}')