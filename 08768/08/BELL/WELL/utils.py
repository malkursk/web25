from django.shortcuts import render, HttpResponse

def RELL(v,b1=10,b2=16):
    try:
        number = int(v,b1)
    except:
        return 'Неверное число'
    digits = "0123456789ABCDEF"
    if number == 0:
        return '0'
    result = []
    while number>0:
        number, mod = divmod(number, b2)
        result.append(digits[mod])
    result = ''.join(reversed(result))
    return f'{v} in base {b1} = {result} in base {b2}'
