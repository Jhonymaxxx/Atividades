def div():
    try:
        num1 = int(input('Digite um número: '))
        num2 = int(input('Digite um número: '))
        res = num1 / num2
    except ZeroDivisionError:
        print('Erro divisão por Zero')
    except:
        print('Algo deu errado')
    else:
        return res
    finally:
         print('Executara sempre!')
print(div())