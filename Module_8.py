
def add_everything_up(a,b):
    try:
        result = a + b
        print(f'Такое за основу взято {result}')
    except:
        print(f'{a}{b}')

add_everything_up(4,'hop')
add_everything_up('vecherelo',4.8)
add_everything_up('october', 'urban')
