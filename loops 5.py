""" Вашей программе на вход поступает натуральное число n. Вам нужно сделать из чисел обратную пирамидку, например для числа 5 вывод будет следующим:

5 4 3 2 1
5 4 3 2
5 4 3
5 4
5
Sample Input 1: """
A = int(input())
B = -1 * A
x = ""
for i in range(0,A):
    for c in range(A, i, -1):
        R =  c
        x = x + str(R) + " "
    i -= 1
    print(x)
    x = ''
