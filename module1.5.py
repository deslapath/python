immutable_var = (6, 10, 'Elena','bluesky', True)
print(immutable_var)

# С изменением значения immutable_var[2] = 'Galina' в консоль выходит ошибка:
# tuple' object does not support item assignment
# потому что кортеж относится к неизменяемым типам данных

mutable_var = ['music', 'wibe', 22, 'snow', False]
print(mutable_var)
mutable_var[3] = 8
print(mutable_var)
