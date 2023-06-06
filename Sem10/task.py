import random
from statistics import mean

class Human:
    def __init__(self, first_name, last_name, age, grades):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.grades = grades
    
    def __repr__(self):
        return f"{self.first_name} {self.average_grade()}"

    def __str__(self):
        return f"Имя: {self.first_name} {self.last_name} Возвраст: {self.age}"

    def greet(self):
        return f"Привет, меня зовут {self.last_name} {self.first_name}, мне {self.age} лет"
    
    def average_grade(self):
        return mean(self.grades)

human1 = Human("Ильгиз", "Басиров", 36, [])
human2 = Human("Саша", "Иванова", 35, [])
human3 = Human("Оля", "Петрова", 33, [])
human4 = Human("Катя", "Сидорова", 34, [])

human_list = [human1, human2, human3, human4]

for i in human_list:
    i.grades = [random.randint(2,5) for j in range(10)]

human_list.sort(key = lambda x: x.average_grade())
print(human_list)

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rectangle():
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def get_a_cords(self):
        return [a.x, a.y, b.x, b.y]

    def square(self):
       return abs((a.x - b.x) * (a.y - b.y))

    def perimeter(self):
        return 2 * abs(a.x - b.x) + 2 * abs(a.y - b.y)
    
    def has_point(self, point_1):
        if (min(a.x, b.x) < point_1.x < max(a.x, b.x)) & (min(a.y, b.y) < point_1.y < max(a.y, b.y)): 
            return True
        else: 
            return False

a = Point(1, 10)
b = Point(9, 1)

pryam = Rectangle(a,b)
print(pryam.square())
print(pryam.perimeter())
point_1 = Point(3,4)
print(pryam.has_point(point_1))
