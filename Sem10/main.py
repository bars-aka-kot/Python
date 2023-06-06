class Human:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def say_hello(self):
        return f"Привет, меня зовут {self.name}, мне {self.age}. Мой вес - {self.weight} кг!"

    def __str__(self):
        return f"{self.name}"

    def __add__(self, other):
        if type(other) == Human:
            return f"{self.name} и {other.name} теперь братья"
        if type(other) == int:
            return f"теперь ваш возраст {self.age + other}"

    def __eq__(self, other):
        if type(other) == int:
            if self.age > other:
                return f"Ваш возраст больше"
            else:
                return f"Ваш возраст меньше"
        if type(other) == Human:
            if self.age > other.age:
                return f"Возраст {human1} больше"
            else:
                return f"Возраст {human1} меньше"

    def __len__(self):
        return len(self.name)


human1 = Human("Ivan", 37, 75)
human2 = Human("Maxim", 35, 81)
# print(human1)
# print(human1 + human2)
# print(human1 + 5)
# print(human1 == human2)
# print(len(human1))
print(Human.say_hello(human1))

# a = 7
# b = a
# a = "asdf"
# print(a) # "asdf"
# print(b) # 7

# a = [1, 2, 3]
# b = a
# a.append(5)
# print(a) # [1, 2, 3, 5]
# print(b) # [1, 2, 3, 5]

# a = [1, 2, 3]
# b = a.copy()
# a.append(5)
# print(a) # [1, 2, 3, 5]
# print(b) # [1, 2, 3]

# Изменяемые и неизменяемые объекты
#  Изменяемые - list, set, dict. Остальное все неизменяемое
# a = {1:"a", 2:"b", 3:"c"}
# print(a)
# print(id(a))
# a[4] = "d"
# print(a)
# print(id(a))
# import time
# a = "1"
# start = time.perf_counter()
# for i in range(1000000):
#     a += "1"
# finish = time.perf_counter()

# print(f"time1 is {finish - start} s")

# b = [1]
# start = time.perf_counter()
# for i in range(1000000):
#     b.append(1)
# finish = time.perf_counter()

# print(f"time2 is {finish - start} s")