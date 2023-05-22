'''Задача №51. Напишите функцию same_by(characteristic, objects), которая проверяет, все ли объекты имеют одинаковое значение 
некоторой характеристики, и возвращают True, если это так. Если значение характеристики для разных объектов отличается - то False. 
Для пустого набора объектов, функция должна возвращать True. Аргумент characteristic - это функция, которая принимает объект и вычисляет его 
характеристику.
Ввод:
values = [0, 2, 10, 6]
if same_by(lambda x: x % 2, values):
print(‘same’)
else:
print(‘different’)
Вывод:
same'''

def same_by(characteristic, objects):
    return len(list(filter(characteristic,objects))) == len(objects)

values = [0,2,4,6,8,10,12]
if same_by(lambda x: True if x % 2 == 0 else False, values):
    print('same')
else:
    print('different')