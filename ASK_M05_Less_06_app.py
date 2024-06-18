class House():
    def __init__(self):
        self.numberOfFloors = 0

    def setNewNumberOfFloors(self,floors):
        self.numberOfFloors = floors
        print(f'======     Колличество этажей здания: {self.numberOfFloors}')


My_House = House()
My_House.setNewNumberOfFloors(63)
print('\n *****  Колличкество этажей здания:', My_House.setNewNumberOfFloors(35))
print('\n ------------    Колличество этажей здания :  ', My_House.numberOfFloors)