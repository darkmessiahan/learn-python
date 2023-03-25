""" Посчитайте произведение всех целых чисел последовательности, заканчивающейся нулем (ноль в последовательность не включаем). Если чисел в последовательности нет – выведите нейтральное для произведения число 1.

Sample Input 1:

1
2
-1
0
Sample Output 1:

-2 """
c = 1
while (a := int(input())) != 0:
    c = c * a
    if a == 0:
        break

print(c)