from math import sqrt

print(sqrt(25))


def fatorial(n):
    f = 1
    for c in range(1, n+1):
        f = f * c  # f *= c
    return f


print(fatorial(5))


# Fibonacci numbers module
# Numero de Fibonacci até n
def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()


def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result


print(fib(500))
print(fib2(500))
