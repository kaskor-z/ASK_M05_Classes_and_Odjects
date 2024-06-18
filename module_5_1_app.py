class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
        self.new_floor = number_of_floors

    def go_to(self, new_floor):
        self.new_floor = new_floor
        if 0 < self.new_floor <= self.number_of_floors:
            print('***************************')
            print(F'  Наименование объекта: "{self.name}"')
            print(F' Общее колличество этажей в доме: {self.number_of_floors}')
            print(F' !!! Номер этажа в Заявке: {self.new_floor}')
        else:
            print('***************************')
            print(F'  Наименование объекта: "{self.name}"')
            print(F' Общее колличество этажей в доме: {self.number_of_floors}')
            print(F'WWWW  ЛОЖНЫЙ ВЫЗОВ  {self.new_floor} - Такого этажа не существует')


h1 = House('ЖК Эльбрус', 30)
h2 = House('ЖК Горский', 18)
h3 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)
h3.go_to(12)
