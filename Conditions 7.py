"""Вам нужно написать программу, которая получает на вход целое число n и определяет какой день недели будет через n дней. Отсчет ведется от понедельника.
Вам нужно вывести какой день недели будет через n дней. В качестве ответа выведите один из этих вариантов:
пн
вт
ср
чт
пт
сб
вс
Например если на вход пришло n = 10, тогда нужно вывести чт.
Sample Input 1:
1
Sample Output 1:
вт"""
q = int(input())% 7
#q -= 1
days = ['пн', 'вт', 'ср', 'чт', 'пт', 'сб', 'вс']
print(days[q])