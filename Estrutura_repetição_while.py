media = 0
notas = 1
while notas <= 5:
    nota = float(input(f'Digite a {notas} nota:'))
    media += nota
    notas += 1
print(f'Media final:{(media)/5}')


# exercicio 2

while True:
    x = input('Digite uma palavra que repetirei para você\npara enscerrar o programa digite: (sair)\n')
    print(x)
    if x == 'sair':
        break
print('Encerrando o programa')
