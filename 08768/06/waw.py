names=["Настя", "Коля", "Лиза"]
while True:
    print("текущий массив пользователей ", names)
    i=input("введите ваше имя ")
    if i in names:
        print("вы приглашены на вечеринку")
    else:
        names.append(i)
        print("вы будете приглашены на следующую вечеринку")