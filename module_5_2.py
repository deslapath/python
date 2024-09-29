class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors



    def go_to(self, new_floor):
        self.go_to = new_floor
        if 1 < new_floor < self.number_of_floors:
            for new_floor in range(1, new_floor+1):
                print(new_floor)
        else:
            print('Такого этажа не существует')

    def __len__(self):
         return self.number_of_floors


    def __str__(self):
         return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'


h1 = House('ЖК Смит', 16)
h2 = House('ЖК Ласточка', 8)
h1.go_to(22)
h2.go_to(7)
print(len(h1))
print(len(h2))
print(str(h1))
print(str(h2))
