def converter (v,b1=10,b2=16):
    try:
        number = int(v,b1)
    except:
        return 'Неверное число для данной системы счисления'
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTYVWXYZ"
    if number == 0:
        return '0'
    result = []
    while number>0:
        number, mod = divmod(number,b2)
        result.append(digits[mod])
    result = ''.join(reversed(result))
    return f'{v}, (base1: {b1}) => {result}, (base2: {b2})'