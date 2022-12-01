# 5. Реализуйте алгоритм перемешивания списка.

from random import randrange
print('Введите размерность списка')
n = int(input())
a = [randrange(-n, n) for i in range(n)]
print(a)
