# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

salario_hora = input('Quanto você recebe por hora trabalhada? ')
horas_trabalhadas = input('Quantas horas você trabalha por mês? ')

salario_bruto = float(salario_hora) * float(horas_trabalhadas)

print(f'Seu salário bruto é de {salario_bruto}')