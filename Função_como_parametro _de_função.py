def icc(num, cc):
    if cc(num):
        print(num)
def par(x):
    return x % 2 == 0
def impar(x):
    return not par(x)
icc(6, par)