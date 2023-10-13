#
# https://pythonacademy.com.br/blog/list-comprehensions-no-python
#
##
# list.append(x): Adiciona um item ao fim da lista.
# list.extend(iterable): Adiciona todos os itens do iterável iterable ao fim da lista.
# list.insert(i, x): Insere um item em uma dada posição i.
# list.remove(x): Remove o primeiro elemento, cujo valor seja x.
# list.pop(i): Remove o item de posição i da lista e o retorna. Caso i não seja especificado, retorna o último elemento da lista.
# list.clear(): Remove todos os elementos da lista.
# list.index(x[, start[, end]]): Retorna o índice do primeiro elemento cujo valor seja x.
# list.count(x): Retorna o número de vezes que o valor x aparece na lista.
# list.sort(key=None, reverse=False): Ordena os items da lista (os argumentos podem ser usados para customizar a ordenação).
# list.reverse(): Reverte os elementos da lista.
# list.copy(): Retorna uma lista com a cópia dos elementos da lista de origem.
##

# Apenas números
lista_numerica = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Letras e números
lista_alfanumerica = ['a', 'b', 'c', 1, 2, 3]

lista = []
for item in range(10):
  lista.append(item**2)
print(lista)  

##
# List Comprehensions (Compreensão de Listas)
# Sintaxe básica: [expr for item in lista]
##

lista = [item**2 for item in range(10)]
print(lista)

##
# List Comprehensions com vários if’s
##
resultado = [numero for numero in range(100) if numero % 5 == 0 if numero % 6 == 0]
print(resultado)
# Out: resultado = [0, 30, 60, 90]

##
# List Comprehensions com if + else
##
# [resultado_if if expr else resultado_else for item in lista]
resultado = ['1' if numero % 5 == 0 else '0' for numero in range(16)]
print(resultado)
# Out: resultado = ['1', '0', '0', '0', '0', '1', '0', '0', '0', '0', '1', '0', '0', '0', '0', '1']


  
