##
# Author: Marcos Antonio de Carvalho
# eMAil: marcos.antonio.carvalho@gmail.com
# GitHub: https://github.com/owl-arch
# Descr.: Criar uma classe Python personalizada para converter
#         dados JSON para objeto Python personalizado.
##

import json

class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

# JSON data as a string
json_data = '{"name": "Carvalho", "age": 60, "city": "Brasília"}'

# Convert JSON string to custom Python object
def custom_object_hook(obj):
    return Person(obj['name'], obj['age'], obj['city'])

##
# ATENÇÃO:
#   json.loads() é usada para carregar dados JSON de uma cadeia de caracteres e
#   json.load()  é usada para carregar dados JSON de um arquivo.
##
# Usamos o parâmetro object_hook, para converter os dados JSON para o objeto Python desejado
python_object = json.loads(json_data, object_hook=custom_object_hook)

print(type(python_object))  # <class '__main__.Person'>
print(python_object.name)   # Carvalho
print(python_object.age)    # 60
print(python_object.city)   # Brasília
