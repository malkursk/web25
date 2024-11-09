name = input('Имя:')
print('привет,'+ name + '!')
year=int(input('Год рождения'))
if(2024-year)>20:
    s='у Вас прекрасный возраст'
else:
    if(2024-year)<20:
        s='Вам нужно еще немного времени'
    else:
        s='Вы в норме'
print (name + ',' + s)