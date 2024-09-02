grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
print(grades)
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
print(sorted(students)) 

sum_grades = list(sum(inner_list) for inner_list in grades)
print(sum_grades)

int = list(len(inner_list) for inner_list in grades)
print(int)

average = list((sum_grades/int) for sum_grades, int in zip(sum_grades,int))
print(average)

dict=dict(zip(students,average))
print(dict)
print(type(dict))
print(dict["Bilbo"]) # проверили ключ





