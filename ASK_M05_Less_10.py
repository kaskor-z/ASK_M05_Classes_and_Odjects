class Building():
    def __init__(self):
        self.set_numberOfFloors = 0
        self.buildingType = ''

    def __eq__(self, other):
        bool_1 = self.numberOfFloors == other.numberOfFloors
        bool_2 = self.buildingType == other.buildingType
        return bool_1 and bool_2


Built_1 = Building()
New_Floors_1 = 16
Built_1.numberOfFloors = New_Floors_1
Built_1.buildingType = str(New_Floors_1)
print(f'В  1 строени число этаже в (int) = {New_Floors_1}, а в (str) = {New_Floors_1}')
Built_2 = Building()
New_Floors_2 = 16
Built_2.numberOfFloors = New_Floors_2
Built_2.buildingType = str(New_Floors_2)
print(f'Во 2 строени число этаже в (int) = {New_Floors_2}, а в (str) = {New_Floors_2}')
print(f' Сравнение 2-x строений по числу этажей показало  равенство {Built_1 == Built_2}')
