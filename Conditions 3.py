""" ; ; Задача на программирование
Напишите программу, которая получает на вход целое число n и выводит 5 строк содержащих True или False с ответами на эти вопросы:
1) Является ли число четным?
2) Число является положительным?
3) Число находится в промежутке от -5 включительно до 5 включительно?
4) Число делится на 3 и 4, но не делится на 7?
5) Является ли число трехзначным?
Sample Input 1:
5
Sample Output 1:
False
True
True
False
False """
#Является ли число четным?
num = int(input())
if num % 2 == 0:
    print(True)
else:
    print(False)
#Число является положительным?
if num  > 0:
    print(True)
else:
    print(False)
#Число находится в промежутке от -5 включительно до 5 включительно?
if num >= -5 and num <= 5:
    print(True)
else:
    print(False)
#Число делится на 3 и 4, но не делится на 7?
if num % 3 == 0 and num % 4 == 0 and not num % 7 == 0:
    print(True)
else:
    print(False)
#Является ли число трехзначным?
if  len(str(abs(num))) == 3:
    print(True)
else:
    print(False)