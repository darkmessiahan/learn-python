""" Посчитайте факториал числа n! по формуле ниже:
n!=1∗2∗3∗4∗...∗n
Sample Input:
5
Sample Output:
120
Напишит"""
n = int(input())

factorial = 1
while n > 1:
    factorial *= n
    n -= 1

print(factorial)