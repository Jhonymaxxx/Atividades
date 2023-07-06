nome = ''
while not nome:
    nome = input('Digite seu nome:')
    valor = int(input('Digite um número:'))
    if valor:
        print('Você digitou um valor diferente de zero')
    else:
        print('Você digitou zero')
