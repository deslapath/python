print('1. Функция с параметрами по умолчанию:')

def print_params(a=1, b='строка', c=True): # создали функцию
    print(a, b, c) # вывели функцию

# далее несовсем понятно, если с разным количеством аргументов, включая вызов без аргументов, то:
print_params(a=[2,5], b=['truru', 'lolo'], c=['True', 'True'])

# без аргументов
print_params()

# а если с различным количеством параметров, то:
print_params(4, 5)

# проверяем вызовы с измененными параметрами
print_params(b=25)
print_params(c=[1, 2, 3])

print()
print('2. Распаковка параметров:')

values_list = [29, False, "listopad"]
values_dict = {"a": 4, "b": 'Speak', "c":'Month'}

print_params(*values_list)
print_params(**values_dict)

print()
print('3.Распаковка + отдельные параметры:')

values_list_2 = [0.421, True]


print_params(*values_list_2, 42) # работает