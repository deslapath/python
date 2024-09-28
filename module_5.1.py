class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floor = number_of_floors


    def go_to(self, new_floor):
        self.go_to = new_floor
        if new_floor > self.number_of_floor or new_floor < 1:
            print('Такого этажа не существует')
        else:
            print(new_floor)


h1 = House('ЖК Смит', 14)
h2 = House('ЖК Ласточка', 9)
h1.go_to(6)
h2.go_to(11)




