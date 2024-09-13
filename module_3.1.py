from operator import index

calls = 0
def count_calls():
    global calls
    calls += 1
def string_info(string):
    count_calls()
    return (len(string), string.upper(), string.lower())
def is_contains(string, list_to_search):
    count_calls()
    if string in list_to_search:
        return True
    else:
        return False



print(string_info('Galactica'))
print(string_info('bumerang'))
print(string_info('Bambaleylo'))
print(is_contains('Drevo', ['derevnya', 'september', 'food']))
print(is_contains('Delphin', ['derevnya', 'Delphin', 'food']))
print(calls)


