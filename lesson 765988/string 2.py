""" Напишите программу, которая получает на вход строку, и выводит каждый ее символ умноженный на индекс + 1.
Используйте для решения задачи цикл for со счетчиком или for в комбинации с enumerate.
Ввод:
s – строка
Вывод:
Строки, содержащие символы строки s умноженные на индекс+1
Sample Input:
back
Sample Output:
b
aa
ccc
kkkk """
s = input()
for idx, value in enumerate(s):
    sd = idx + 1
    print(sd * value)
