from operator import index

calls = 0
def count_calls():
    global calls
    calls += 1
def string_info(string):
    print(len(string), string.upper(), string.lower())
calls += 1
count_calls()
def is_contains(string, list_to_search):
    if string in list_to_search:
        return True
    else:
        return False
calls += 1
count_calls()


print(string_info('Galactica'))
print(string_info('bumerang'))
print(string_info('Bambaleylo'))
print(is_contains('Drevo', ['derevnya', 'september', 'food']))
print(is_contains('Delphin', ['derevnya', 'Delphin', 'food']))
print(calls)


