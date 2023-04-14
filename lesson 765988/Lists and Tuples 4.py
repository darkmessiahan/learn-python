nums = list(map(int, input().split()))  # вводим список чисел
zeros = nums.count(0)  # считаем количество нулей в списке

# удаляем все нули из списка и сохраняем их количество
for i in range(zeros):
    nums.remove(0)

# добавляем нули в конец списка
nums += [0]*zeros
text = ''
for t in nums:
    text = text  + str(t) + " "
# выводим отсортированный список
print(text)
