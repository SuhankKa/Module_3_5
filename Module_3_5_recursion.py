# "Рекурсивное умножение цифр"

def get_multiplied_digits(number):

    a = list(str(number))
    for i in a[0:]:
        if i == '0':
            a.remove(i)

    str_number = ''.join(a)
    first = int(a[0]) 

    if first == 0:
        return get_multiplied_digits(int(str_number[1:]))
    
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    
    if len(str_number) == 1:
        return first 

result = get_multiplied_digits(40203)
print(result)

result2 = get_multiplied_digits(402030)
print(result2)

result2 = get_multiplied_digits(4000000000000002030)
print(result2)