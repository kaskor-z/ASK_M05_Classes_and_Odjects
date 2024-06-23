class Building():
    def __init__(self, numberOfFloors, buildingType):
        self.numberOfFloors = numberOfFloors
        self.buildingType = buildingType

    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType

New_Floors_1 = 16
Built_1 = Building(New_Floors_1, str(New_Floors_1))
print(f'В  1 строени число этаже в (int) = {New_Floors_1}, а в (str) = {New_Floors_1}')
New_Floors_2 = 16
Built_2 = Building(New_Floors_2, str(New_Floors_2))
print(f'Во 2 строени число этаже в (int) = {New_Floors_2}, а в (str) = {New_Floors_2}')
print(f' Сравнение 2-x строений по числу этажей показало  равенство {Built_1 == Built_2}')
