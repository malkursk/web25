from datetime import datetime

# Запрашиваем имя у пользователя
name = input('Имя: ')
print('Привет, ' + name + '!')

# Запрашиваем год, месяц и день рождения
year = int(input('Год рождения: '))
month = int(input('Месяц рождения (1-12): '))
day = int(input('День рождения (1-31): '))

# Текущая дата
today = datetime.now()

# Вычисляем текущий возраст
age = today.year - year

# Проверяем, был ли день рождения в этом году
if (today.month, today.day) < (month, day):
    age -= 1  # Если день рождения еще не был, вычитаем 1

# Формируем сообщение в зависимости от возраста
if age > 20:
    message = 'У Вас прекрасный возраст!'
elif age < 20:
    message = 'Вам нужно еще немного времени.'
else:
    message = 'Вы в норме.'

# Выводим результат
print(name + ', ' + message)
