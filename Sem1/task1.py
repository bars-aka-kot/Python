''' За день машина проезжает n километров. Сколько дней нужно, чтобы проехать маршрут длиной m километров? 
При решении этой задачи нельзя пользоваться условной инструкцией if и циклами. '''
import math


n = int(input('Enter the distance in the km that the car passes on the day: '))
m = int(input('Enter the distance in the km that you need to drive: '))

print(
    f"First option: the number of days for which the distance will pass {m} km:", math.ceil(m/n))
print(
    f"Second option: the number of days for which the distance will pass {m} km:", (m+n-1)//n)
print(f"Third option: the number of days for which the distance will pass {m} km:", (
    m // n + int(m % n != 0)))
