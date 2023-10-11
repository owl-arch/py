##
# Author: Marcos Antonio de Carvalho
# eMAil.: marcos.antonio.carvalho@gmail.com
# GitHub: https://github.com/owl-arch
# Descr.: Decorator atribui uma nova funcionalidade para a função 
#         que está logo abaixo dele.
# Insp..: https://www.programiz.com/python-programming/decorator#google_vignette
##
import time

# Exemplo básico de Decorator
def decorator(funcao):
    def wrapper():
        print ("Estou antes da execução da função passada como argumento")
        funcao()
        print ("Estou depois da execução da função passada como argumento")

    return wrapper

def outra_funcao():
    print ("Sou um belo argumento!")

funcao_decorada = decorator(outra_funcao)
funcao_decorada()

# Output: 
#  Estou antes da execução da função passada como argumento
#  Sou um belo argumento
#  Estou depois da execução da função passada como argumento

print('')

##
# Controle maior sobre funções
##

def smart_divide(func):
    def inner(a, b):
        print("I am going to divide", a, "and", b)
        if b == 0:
            print("Whoops! cannot divide")
            return

        return func(a, b)
    return inner

@smart_divide
def divide(a, b):
    print(a/b)

divide(2,5)

divide(2,0)

# Output
#
# I am going to divide 2 and 5
# 0.4
# I am going to divide 2 and 0
# Whoops! cannot divide

print('')

##
# Chaining Decorators in Python
##

def star(func):
    def inner(*args, **kwargs):
        print("*" * 15)
        func(*args, **kwargs)
        print("*" * 15)
    return inner


def percent(func):
    def inner(*args, **kwargs):
        print("%" * 15)
        func(*args, **kwargs)
        print("%" * 15)
    return inner


@star
@percent
def printer(msg):
    print(msg)

printer("Hello")

# Output
#
## ***************
## %%%%%%%%%%%%%%%
## Hello
## %%%%%%%%%%%%%%%
## ***************

print('')

##
# Log de Performance: Mede o tempo de execução de uma função
# Util para levantamento de custo de funções AWS Lambda
##

def log_performance(func):
    def wrapper(*args, **kwargs): # encapsulamento 
        start_time = time.time()
        result =  func(*args, **kwargs)
        end_time = time.time()
        execution_time =  end_time - start_time
        print(f"Function '{func.__name__}' took {execution_time:.4f} seconds to execute.")
        return result
    return wrapper

@log_performance
def calculate_total():
    total = 0
    for i in range(1, 1000001):
        total += i
    return total
    
# Teste
# Output: Function 'calculate_total' took 0.0868 seconds to execute.
calculate_total()   