num = '5'

enter = input('')

if enter == 'game':
    while enter != 'off' :
        enter = input()
        if enter == num :
            print('Вы выиграли билет на концерт')