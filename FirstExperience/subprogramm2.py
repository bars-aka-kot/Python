def sum_str(*args):
    res = ''
    for i in args:
        res += i
    return res


a = sum_str(str(input("Введите буквы: ").split(" ")))
print(a)
