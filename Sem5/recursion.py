def recr(num, count):
    num *= degree
    count -= 1
    if count == 1:
        return num
    return recr(num, count)


degree = 2
num = 2
count = 5
print(recr(num, count))
