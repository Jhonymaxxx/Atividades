                        # função
# def linhas():
#    print('|','_' * 20,'|')
#    print('|', '_' * 20, '|')
                     # programa princípal
# linhas()
# print('      Olá Mundo')
# linhas()


                       # função
# def linhas(s1):
#    print('|','_' * 20,'|')
#    print('|', '_' * 20, '|')
#    print(s1)
#    print('|', '_' * 20, '|')
#    print('|', '_' * 20, '|')

                    # programa principal
# linhas('      Olá mundo')



                                 # função
# def div(a, b):
#    res = a / b
#    print(res)
                                  # programa princípal
# div(55, 5)

# def media(a=0, b=0, c=0):
#    res = (a + b + c) / 3
#    print(res)
# media(5,10,15)


                                # função

# def s(s1):
#    tam = len(s1)
#    if tam:
#        print('+','-' * tam,'+')
#        print('|', s1, '|')
#        print('+', '-' * tam, '+')
                       #programa princípal
# s('')

                        # Escopo de variáveis


                 # função
# def comida():
#    ovos = 11
#    print(ovos)

           # programa princípal
# ovos = 13
# comida()
# print(ovos)

                               # função dentro de função
                # função 1
# def comida1():
#    ovos = 'variável local comida1'
#    comida2()
#    print(ovos)

              # função 2
# def comida2():
#    ovos = 'variável local comida2'
#    print(ovos)

            # programa princípal
# ovos = 'variavel global'
# comida1()
# comida2()
# print(ovos)


                     # A introdução ( global )

# def comida():
#    global ovos
#    ovos = 'cozido'

# ovos ='frito'
# comida()
# print(ovos)

# def media(a=0, b=0, c=0):
#    a = int(input('digite um número:'))
#    b = int(input('digite um número:'))
#    c = int(input('digite um número:'))
#    res = (a + b + c) / 3
#    return(res)
# r = media()
# print(f'A média entre os três números é {r/2}')

#def vs(string, min, max):
#    s1 = input(string)
#    tam = len(s1)
#    while((tam < min) or (tam > max)):
#        s1 = input(string)
#        tam = len(s1)
#    return(s1)
# x = vs('Digite uma string: ',10, 30)
# print(f'Vocẽ digitou {x}\nDado valido fechando o programa')

