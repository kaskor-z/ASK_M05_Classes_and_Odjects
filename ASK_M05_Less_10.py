class Building():
    def __init__(self):
        self.numberOfFloors = 0
        self.buildingType = ''

    def __eq__(self, other):
        bool_1 = self.buildingType == str(other.numberOfFloors)
        bool_2 = other.buildingType == str(self.numberOfFloors)
        if bool_1 and bool_2:
            return True
        else:
            return False


Built_1 = Building()
New_Floors_1 = 16
Built_1.numberOfFloors = New_Floors_1 - 1
Built_1.buildingType = str(New_Floors_1 + 1)
print(f'В  1 строени число этаже в (int) = {New_Floors_1 - 1}, а в (str) = {New_Floors_1 + 1}')
Built_2 = Building()
New_Floors_2 = 16
Built_2.numberOfFloors = New_Floors_2 + 1
Built_2.buildingType = str(New_Floors_2 - 1)
print(f'Во 2 строени число этаже в (int) = {New_Floors_2 + 1}, а в (str) = {New_Floors_2 - 1}')
print(f' Сравнение 2-x строений по числу этажей показало  равенство {Built_1 == Built_2}')
