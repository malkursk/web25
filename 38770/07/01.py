name = input('Имя: ')
print('Привет, ' + name + '!')

year = int(input('Год рождения: '))
month = int(input('Месяц рождения (в виде числа): '))
day = int(input('День рождения (в виде числа): '))

current_year = 2024
current_month = 11
current_day = 9

age = current_year - year

if current_month < month or (current_month == month and current_day < day):
    age -= 1

if age > 20:
    s = 'у Вас прекрасный возраст'
elif age < 20:
    s = 'Вам нужно еще немного времени'
else:
    s = 'Вы в норме'

print(name + ', ' + s)
