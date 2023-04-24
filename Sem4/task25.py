# coding = utf-8
'''Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался. 
Количество повторов добавляется к символам с помощью постфикса формата _n.
Input: a a a b c a a d c d d
Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2'''

text = input("Введите строку: ").split()
dict = {}
for i in text:
    if i in dict:
        print(i+"_"+str(dict[i]), end=" ")
        # print(f"{i}_{dict[i]}", end=" ")
        dict[i] += 1
    else:
        dict[i] = 1
        print(f"{i}", end=" ")
