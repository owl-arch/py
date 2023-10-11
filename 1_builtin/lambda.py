
##
# Função LAMBDA é uma função pequena e anonima.
# --> pode ter qualquer numero de argumentos, mas apenas uma expressão.
# --> Sintax: lambda argumentos: experssão
##

# Exemplo: 1
def x(a): return a + 10


print(x(5))

# Exemplo: 2


def x(a, b): return a * b


print(x(5, 6))

# Exemplo: 3


def myfunc(n):
    return lambda a: a * n


mydoubler = myfunc(2)
print(mydoubler(11))

# Exemplo: 4
var1 = myfunc(2)
var2 = myfunc(3)

print(var1(11))
print(var2(11))


# Exemplo: 5


def perc(n):
    return lambda a: a * (n / 100)


lucro = perc(25)
custo = perc(40)
comissao = perc(10)

produto = 5000
print(lucro(produto))
print(custo(produto))
print(comissao(produto))
