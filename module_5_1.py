class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
        self.new_floor = number_of_floors

    def go_to(self, new_floor):
        self.new_floor = new_floor
        if 0 < self.new_floor <= self.number_of_floors:
            i = 0
            for i in range(self.new_floor):
                i += 1
                print(i)
        else:
            self.new_floor = 1
            print(F'Такого этажа не существует')


h1 = House('ЖК МЕРА', 30)
h2 = House('ЖК Кузнецкий', 9)
h1.go_to(7)
h2.go_to(10)
