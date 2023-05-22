#filter
#filter(fincion_a_aplicar, iterable)
lista = [1,2,3,4,5,6]

def espar(x):
    return x%2 == 0

resultado = filter(espar, lista)
resutlado = filter(lambda x: x%2 ==0, lista)


print(lista)

#reduce
# from functools import reduce

# suma = reduce(lambda a,b: a+b, lista)
# suma = sum(lista)

