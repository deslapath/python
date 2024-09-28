def test_function(s=6):
    def inner_function(x='Я в области видимости функции test_function'):

     res = inner_function(x) # 3-е условие (скрин 1)
     print(res)

res2 = inner_function(x) # 4-е условие (скрин 2) - ошибка области 
print(res2)

