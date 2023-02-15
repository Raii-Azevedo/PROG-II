print('''1.12.2. Tem-se um conjunto de dados contendo a altura e o sexo (masculino, feminino) de 50 
pessoas. Fazer um algoritmo que calcule e escreva:
- a maior e a menor altura do grupo;
- a média de altura das mulheres;
- o número de homens\n''')
F = H = mediaF =  menor = 0
for c in range(6):
    sexo = input('Gênero [F|M]: ').upper()[0]
    altura = float(input('Altura: '))
    if sexo == 'M':
        H += 1
    elif sexo == 'F':
        F += 1
        mediaF += altura
    elif altura < altura:
        menor = altura

media = mediaF/F

print(f'Menor altura: {menor}')
print(f'Nº de homens: {H}')
print(f'Nº de mulheres: {F}')
print(f'Média altura feminina: {media:.2f}')
