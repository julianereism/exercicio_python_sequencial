# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

nota1 = input('Informe a primeira nota:')
nota2 = input('Informe a segunda nota:')
nota3 = input('Informe a terceira nota:')
nota4 = input('Informe a quarta e última nota:')

media = (float(nota1) + float(nota2) + float(nota3) + float(nota4)) / 4 # envolver notas em parenteses para somar todas primeiro e depois dividir por 4

media_formatada = f"{media:.1f}" # .1f mostra apenas uma casa decimal, .2f duas casas e assim sucessivamente
# é preciso criar uma nova variável para formatar a variável original

print(f'A média bimestral é: {media_formatada}')


# usar REPLACE para substituir a vírgula por ponto se o usuário digitar vírgula -> nota1 = input('Informe a primeira nota:').replace(',', '.')