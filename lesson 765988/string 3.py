""" Выведите полученную строку в обратном порядке без первого символа.
Ввод:
s – строка
Вывод:
res – строка в обратном порядке без первого символа
Sample Input:
backend
Sample Output:
dnekca  """
x = input()
x = x[::-1]
x = x[0:len(x) - 1]
print(x)