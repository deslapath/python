class Vehicle:

    __COLOR_VARIANTS = ['red', 'blue', 'black']

    def __init__(self, owner, __model, __engine_power, __color):
        self.owner = str(name)
        self.__model = str(model)
        self.__engine_power = int(engine_power)
        self.__color = str(color)


    def get_model(self):
        return f'Модель: {model}'

    def get_horsepower(engine_power):
        return f'Мощность двигателя: {engine_power}'

    def get_color(color):
        return f'Цвет: {color}'

    def print_info():
        return f'{model}, {engine_power}, {color}, Владелец: {name}'

    def set_color(self, new_color):
        if new_color in set:
         color = new_color

        else:
            return f'Нельзя сменить цвет на {new_color}'

class Sedan(Vehicle):



# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
Vehicle = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
Vehicle.print_info()

# Меняем свойства (в т.ч. вызывая методы)
Vehicle.set_color('Pink')
Vehicle.set_color('BLACK')
Vehicle.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()