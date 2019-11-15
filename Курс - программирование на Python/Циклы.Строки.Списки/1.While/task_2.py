'''
В Институте биоинформатики между информатиками и биологами устраивается соревнование. 
Победителям соревнования достанется большой и вкусный пирог. 
В команде биологов a человек, а в команде информатиков — b человек.

Нужно заранее разрезать пирог таким образом, чтобы можно было раздать кусочки пирога любой команде, 
выигравшей соревнование, при этом каждому участнику этой команды должно достаться одинаковое число кусочков пирога. 
И так как не хочется резать пирог на слишком мелкие кусочки, нужно найти минимальное подходящее число.

Напишите программу, которая помогает найти это число.
Программа должна считывать размеры команд (два положительных целых числа a и b, 
каждое число вводится на отдельной строке) и выводить наименьшее число d, которое делится на оба этих числа без остатка.
'''

a = int(input())
b = int(input())

d = max(a,b)

while d % a != 0 or d % b != 0: #пока  не найдем общий делитель
    d += max(a,b)   #увеличиваем результат d
print(d)
