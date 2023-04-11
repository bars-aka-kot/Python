''' Шахматный конь ходит буквой "Г" - на две клетки по вертикали в любом направлении и на одну клетку по горизонтали, или наоборот.
# Даны две различные клетки шахматной доски, определите, может ли конь попасть с первой клетки на вторую одним ходом.
# В случае, если хотя бы одно из введенных чисел не лежит в диапазоне от 1 до 8, выведите строку "Ошибка!".'''

currentPosition = [int(x) for x in input(
    'Введите текущую позицию коня: ').split()]
desiredPosition = [int(x) for x in input(
    'Введите позицию, куда передвинуть коня: ').split()]
if 0 < currentPosition[0] <= 8 and 0 < currentPosition[1] <= 8 and 0 < desiredPosition[0] <= 8 and 0 < desiredPosition[1] <= 8:
    if currentPosition[0] == desiredPosition[0] and currentPosition[1] == desiredPosition[1]:
        print("Ошибка введеных координат")
    else:
        possibleXPositions = [currentPosition[0] - 2, currentPosition[0] -
                              1, currentPosition[0] + 1, currentPosition[0] + 2]
        possibleYPositions = [currentPosition[1] - 2, currentPosition[1] -
                              1, currentPosition[1] + 1, currentPosition[1] + 2]
        if desiredPosition[0] in possibleXPositions and desiredPosition[1] in possibleYPositions:
            print('можно передвинуть')
        else:
            print("нельзя передвинуть")
else:
    print("Ошибка введеных координат")

# возможное решение
# if abs(x2-x1) == 2 and abs(y2-y1)==1:
#     print("yes")
# elif abs(x2-x1) == 1 and abs(y2-y1)==2:
#     print("yes")
# else: print("no")
