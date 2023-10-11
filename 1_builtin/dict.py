##
# https://www.linkedin.com/feed/update/urn:li:activity:7092955215561199616/?utm_source=share&utm_medium=member_android
##
# Um dicionário é uma coleção de pares chave-valor. 
# É um tipo de dados não ordenado e mutável, representado usando chaves {}. 
# Cada chave no dicionário deve ser exclusiva e é usada para acessar seu 
# valor associado. 
# Os dicionários são amplamente utilizados para mapear, armazenar em cache e 
# armazenar dados de forma estruturada. 
##
# Author: Marcos Antonio de Carvalho
# eMAil: marcos.antonio.carvalho@gmail.com
# GitHub: https://github.com/owl-arch
# Descr.: Criar uma classe Python personalizada para converter
#         dados JSON para objeto Python personalizado.
##
# Inspiração: https://www.linkedin.com/feed/update/urn:li:activity:7092955215561199616/?utm_source=share&utm_medium=member_android
##

##
# Python fornece vários métodos para trabalhar com dicionários: 
##
# keys()..: retorna uma lista de todas as chaves no dicionário. 
# values(): retorna uma lista de todos os valores no dicionário. 
# items().: retorna uma lista de pares chave-valor (tuplas) no dicionário. 
# get()...: retorna o valor para a chave fornecida. Se a chave não for encontrada,
#           ela retornará um valor padrão (ou Nenhum). 
# pop()...: Remove e retorna o valor da chave fornecida. 
# clear().: Remove todas as entradas do dicionário, tornando-o vazio. 
# copy()..: Cria uma cópia rasa do dicionário. 
# update(): Atualiza o dicionário com pares chave-valor de outro dicionário. 
##

# exemplo 1 - clear()
my_dict={'name': 'eu', 'age': 60}
my_dict.clear()
print(my_dict)
print()

# exemplo 2 - copy()
my_dict={'name': 'eu', 'age': 60}
new_dict=my_dict.copy()
new_dict['age']=59
print(my_dict)
print(new_dict)
print()

# exemplo 3 - get()
my_dict={'name': 'eu', 'age': 60}
age=my_dict.get('age')
print(age)
# tenta pegar uma chave/key que não existe
occupation=my_dict.get('occupation')
print(occupation)
# configurando um valor default quando a chave/key não existe
occupation=my_dict.get('occupation', 'desempregado')
print(occupation)
print()

# exemplo 4 - items()
items=my_dict.items()
print(items)
print()

# exemplo 5 - keys()
keys=my_dict.keys()
print(keys)
print()

# exemplo 6 - values()
values=my_dict.values()
print(values)
print()

# exemplo 7 - pop()
age=my_dict.pop('age')
print(age)
print(my_dict)
print()

# exemplo 8 - update()
my_dict={'name': 'eu', 'age': 60, 'country': 'brasil'}
my_dict.update({'age': 59})
print(my_dict)
print()

# exemplo 9 - setdefault()
my_dict={'name': 'eu', 'age': 60}
country=my_dict.setdefault('country', 'brasil')
print(country)
print(my_dict)






