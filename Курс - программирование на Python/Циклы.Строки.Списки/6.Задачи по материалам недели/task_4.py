'''
Напишите программу, на вход которой подаётся прямоугольная матрица в виде последовательности строк, заканчивающихся строкой, содержащей только строку "end" (без кавычек)

Программа должна вывести матрицу того же размера, у которой каждый элемент в позиции i, j равен сумме элементов первой матрицы на позициях (i-1, j), (i+1, j), (i, j-1), (i, j+1). У крайних символов соседний элемент находится с противоположной стороны матрицы.

В случае одной строки/столбца элемент сам себе является соседом по соответствующему направлению.
'''

import copy


def new_elem(a):
    res = []
    for i in range(len(a)):
        temp = [0] * len(a[i])
        for j in range(len(temp)):
            temp[j] = int(a[i-1][j]) + int(a[i+1-len(a)][j]) + int(a[i][j-1]) + int(a[i][j+1-len(temp)])
        res.append(temp)
    return res


a = []
while(True):
    b = [i for i in input().split()]
    if b[0] != 'end':
        a.append(b)
    else:
        break

result = new_elem(a)
for i in range(len(result)):
    for j in range(len(result[i])):
        print(result[i][j], end = ' ')
    print()
