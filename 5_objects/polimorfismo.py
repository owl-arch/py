##
# Author: Marcos Antonio de Carvalho
# eMAil.: marcos.antonio.carvalho@gmail.com
# GitHub: https://github.com/owl-arch
# Descr.: SubClass and SuperClass
# Insp..: Facade Pattern
##


# subclass (subsystem) Circle (Circilo)
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius * self.radius

# subclass (subsystem) Rectangle (Retangulo)
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# subclass (subsystem) Triangle (Retangulo)
class Triangle:
    def __init__(self, height, base):
        self.height = height
        self.base = base

    def area(self):
        return self.base * self.height / 2

##
# Applicability of polymorphism (Aplicabilidade)
##

circle = Circle(5)
rectangle = Rectangle(4, 6)
triangle = Triangle(4, 6)

##
# Jeito 1 - macro-substituição
# Passando função como parametro
##

def calculate_area(shape):
    return shape.area()

print('\nJeito 1 - Macro-Substituição')
print('Circle Area..:', calculate_area(circle))
print('Rectange Area:', calculate_area(rectangle))
print('Triangle Area:', calculate_area(triangle))

##
# Jeito 2 - polimorfismo
# Criando superclass
##

# Superclass Shape (Forma)
class Shape:
    def area(self, shape):
        return shape.area()

shape = Shape()
print('\nJeito 2 - Polimorfismo')
print('Circle Area..:', shape.area(circle))
print('Rectange Area:', shape.area(rectangle))
print('Triangle Area:', shape.area(triangle))

print()