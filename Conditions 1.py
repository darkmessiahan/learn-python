""" Задача на программирование
Ваша программа принимает целое число n. Напишите программу, определяющую что число находится в интервале от 5 включительно до 10 строго или от 101 строго до 200 включительно или иными словами
∈[5,10)∪(101,200]n∈[5,10)∪(101,200]. В качестве ответа выведите True если находится и False если не находится.
Sample Input 1:
5
Sample Output 1:
True """

num = int(input())
if num >= 5 and num < 10 or num > 101 and num <= 200:
    print(True)
else:
    print(False)
#print(int(-1*x), int(x-1))