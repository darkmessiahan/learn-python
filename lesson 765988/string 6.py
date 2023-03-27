""" Дана строка s. Найдите в ней подстроку, где наибольшее количество подряд идущих одинаковых символов. Выведите символ и длину последовательности. Если таких несколько – выведите последнюю.
Ввод:
s – строка
Вывод:
res – символ последовательности
acc – длина самой большой последовательности
Sample Input:
aaabbccccaaaab
Sample Output:
a
4"""
s = input()
itog = ''
li = ["", 0]
li[0] = ""
li[1] = 0
count_cur = 0
char_cur = s[0]
for char in s:
    if char == char_cur:
        count_cur += 1
    else:
        itog += char_cur + str(count_cur)
        char_cur = char
        count_cur = 1
    if li[1] <= count_cur:
        li[0] = char_cur
        li[1] = count_cur

itog += char_cur + str(count_cur)
print(li[0])
print(li[1])