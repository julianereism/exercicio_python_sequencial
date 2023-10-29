# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# o produto do dobro do primeiro com metade do segundo .
# a soma do triplo do primeiro com o terceiro.
# o terceiro elevado ao cubo.

num1 = input('Digite o primeiro número inteiro: ')
num2 = input('Digite o segundo número inteiro: ')
num3 = input('Digite um número real: ')

num1 = int(num1)
num2 = int(num2)
num3 = float(num3)

produto = (int(num1) * 2) + (int(num2) / 2)
soma = (int(num1) *3) + num3
cubo = num3 ** 3

print(f'O produto do dobre do primeiro com metade do segundo é: {produto}')
print(f'A soma do triplo do primeiro com o terceiro é: {soma}')
print(f'O terceiro elevado ao cubo é: {cubo:.2f}')