# 1. Напишите программу, которая принимает на вход вещественное
# число и показывает сумму его цифр.

print('Введите число')
a = int(input())
print(sum(map(int,str(a))))
