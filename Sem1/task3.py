''' В некоторой школе решили набрать три новых математических класса и оборудовать кабинеты для
них новыми партами. За каждой партой может сидеть два учащихся. Известно количество учащихся в
каждом из трех классов. Выведите наименьшее число парт, которое нужно приобрести для них. '''

# import math

# firstClass = int(input('The number of students in first grade: '))
# secondClass = int(input('The number of students in the second grade: '))
# thirdClass = int(input('The number of students in the third grade: '))

# print("First option: The minimum number of desks for purchase ", (firstClass // 2 + secondClass // 2 + thirdClass //
#       2 + firstClass % 2 + secondClass % 2 + thirdClass % 2))

# print("The second option: The minimum number of desks for purchase ", ((firstClass + 1) // 2 +
#       (secondClass + 1) // 2 + (thirdClass + 1) // 2))

# print("The third option: The minimum number of desks for purchase ", math.ceil(firstClass / 2) +
#       math.ceil(secondClass / 2) + math.ceil(thirdClass / 2))


n = int(input("Enter the number of classes: "))
sum = 0
for i in range(n):
    numberStudents = int(input(f"Enter the number of students {i+1} class: "))
    sum += numberStudents // 2 + numberStudents % 2
print(sum)
