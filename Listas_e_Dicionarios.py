                     # Variáveis compostas e estruturas de dados

                                # (tuplas)

# bolsa = ('lapis ','caderno','tesoura','borracha','apontador')
# up = ('lanche','agasalho')
# bolsa_up = bolsa + up
# for materiais in bolsa_up:
#    print(f'Em minha bolsa têm: {materiais}')

               #  Desempacotamento de parâmetros em função

# def soma(*num):
#     soma = 0
#     print(f'tuplas: {num}')
#     for i in num:
#       soma += i
#     return soma
# print(f'Resultado: {soma(7, 4, 5, 100)}')

                            # [listas]

# bolsa = ['lapis ','caderno','tesoura','borracha','apontador']
# bolsa.append('caneta')
# bolsa.insert(1,'lapiseira')
# bolsa.remove('borracha')
# del bolsa[0]
# print(bolsa)

                        # copia de listas

# x = [1,2,3,4,5]
# y = x # aponta endereço
# y[0] = 6
# print(x)
# print(y)


# x = [1,2,3,4,5]
# y = x[:] # faz a cópia
# y[0] = 6
# print(x)
# print(y)

                            # strings e listas dentro de listas
                     # indexação dupla

# bolsa = ['lapis ','caderno','tesoura','borracha','apontador']
# for item in bolsa:
#     for letra in item:
#      print(letra, end='')
#     print()

                         # lista dentro de lista
# armario = [['bolsa',2],['maleta',3],['sacola',4]]
# print(armario[0][0])



# mercado = []
# for i in range(3):
#     item = input('Digite um item: ')
#     qtd = int(input('Digite a quantidade: '))
#     valor = float(input('Digite o valor: '))
#     mercado.append([item, qtd, valor])
# print(mercado)
# soma = 0
# print('       Lista de compras     ')
# print('Item   |   QTD   |   V unitario   |   Total')
# for item in mercado:
#     print(f'{item[0]} | {item[1]} | {item[2]} | {item[1] * item[2]}')
#     soma += item[1] * item[2]
# print(f'Total a ser pago: {soma}')



                        # dicionários

# game = {'Nome':'Super Mario',
#         'Plataforma':'Snes',
#         'Ano':1990}
# print(game)
# print(game['Nome'])
# print(game['Plataforma'])
# print(game['Ano'])

# print(game.values())

# for i in game.values():
#     print(i)

# for i in game.keys():
#     print(i)

# for m,n in game.items():
#     print(f'{m} = {n}')

                           # Listas com dicionários
jogo = {}
jogos = []
for i in range(3):
    jogo['nome'] = input('Digite o titulo do jogo: ')
    jogo['plataforma'] = input('Plataforma do jogo: ')
    jogo['ano'] = int(input('Ano de lançamento: '))
    jogos.append(jogo.copy())
print('-'* 20)
for e in jogos:
    for i,j in e.items():
         print(f'{i} = {j},')