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
    string_lower = string.lower()
    list_to_search_lower = [item.lower() for item in list_to_search]
    if string_lower in list_to_search_lower:
        return True
    else:
        return False


print(string_info('Galactica'))
print(string_info('bumerang'))
print(string_info('Bambaleylo'))
print(is_contains('September',('ffhh', 'SEPTEMBER')))
print(is_contains('Doberman', ('hfj', 'DoBeRmAn', 'LIStopad')))
print(calls)


