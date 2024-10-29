

name1 = 'Мастера кода'
name2 = 'Волшебники данных'
team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2



print('В команде Мастера кода участников: %s' % str(team1_num))
print('В команде Мастера кода участников: %s и %d' % (str(team1_num), 6))
print('Команда Волшебники данных решила задач: {}'.format (score_2))
print('Волшебники данных решили задачи за {}{}'.format(str(team2_time), ' с!'))
print(f'Команды решили {score_1} и {score_2} задач')

if score_1 > score_2:
    print(f'Результат битвы: победа команды {name1}!')
else:
    print(f'Результат битвы: победа команды {name2}!')


print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!')