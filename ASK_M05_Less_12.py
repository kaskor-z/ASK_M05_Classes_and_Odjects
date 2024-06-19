class Buiding():
    total = 0

    def __init__(self, Name_Object):
        self.Name_Object = Name_Object
        Buiding.total += 1


House_ = []
for i in range(1, 41):
    build_n = 'Object_'
    build_n += str(i)
    House_.append(Buiding(build_n))
    print(f' Строение : {build_n}   Значение параметра "total" класса "Building()" = {Buiding.total}')
print('\n В списке House_ находится ', len(House_), ' объектов класса "Building()"')