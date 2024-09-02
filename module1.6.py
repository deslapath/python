my_dict = {'Family':4, 'Child':2, 'Grandmothers':2}
print(my_dict)
print(my_dict['Child'])
print(my_dict.get('Grandfathers'))
my_dict.update({'Aunts': 5, 'Uncles': 3})
print(my_dict)
a = my_dict.pop('Child')
print(a)
print(my_dict)

my_set = {3, 7, 2, 2.6, 3, 5, 2, 'Ololo', 'Je', False, 'bonbon', 'Je', False}
print(my_set)
print(my_set.add(9))
print(my_set.add('Soul'))
print(my_set)
print(my_set.remove('Je'))
print(my_set)
