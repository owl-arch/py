##
# Author: Marcos Antonio de Carvalho
# eMAil.: marcos.antonio.carvalho@gmail.com
# GitHub: https://github.com/owl-arch
# Descr.: Interface simplificada para um conjunto de outras interfaces,
#         abstrações e implementações dentro de um sistema que pode ser
#         complexo e/ou fortemente acoplado.
# Insp..: https://medium.com/design-patterns-in-python/facade-design-pattern-a29c94776870
##

##
# O Facade Pattern agiliza as interações com subsistemas complexos,
# apresentando uma interface simplificada ao cliente.
##


class SubSystemClassA:
    @staticmethod
    def method():
        return "A"


class SubSystemClassB:
    @staticmethod
    def method():
        return "B"


class SubSystemClassC:
    @staticmethod
    def method():
        return "C"


# facade
class Facade:
    def __init__(self):
        self.sub_system_class_a = SubSystemClassA()
        self.sub_system_class_b = SubSystemClassB()
        self.sub_system_class_c = SubSystemClassC()

    def create(self):
        result = self.sub_system_class_a.method()
        result += self.sub_system_class_b.method()
        result += self.sub_system_class_c.method()
        return result


# client
FACADE = Facade()
RESULT = FACADE.create()
print("The Result = %s" % RESULT)


##
# Exemplo básico de Facade Design Pattern
##