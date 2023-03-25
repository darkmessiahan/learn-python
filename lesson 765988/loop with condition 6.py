""" ам дано целое число n. Нужно определить, что число является палиндромом (слева направо и справа налево читается одинаково). Примеры палиндромов: 121, 1331, 222, 2, 11, 56165.
В случае если число является палиндромом выведите True, в ином случае False.
Для тех кто уже прошел уроки по строкам: Сможете решить эту задачу в целых числах без приведения к строке?
Sample Input 1:
1331
Sample Output 1:
True"""
def isPalindrome(num):

    # `n` сохраняет данное целое число
    n = num

    # `rev` хранит обратную сторону заданного целого числа.
    rev = 0

    while n:

        # сохранит последнюю цифру n в переменной r
        #, например, если `n` равно 1234, то `r` будет равно 4
        r = n % 10

        # добавить `r` к `rev` вместо своего места
        # например, если `rev = 65` и `r = 4`, то новый `rev` будет 654
        rev = rev * 10 + r

        # удалить последнюю цифру из `n`
        #, например, если `n` равно 1234, то новое `n` будет 123.
        n = n // 10

    # это выражение вернет 1, если заданное число равно
    # его реверс; в противном случае он вернет 0
    return num == rev


if __name__ == '__main__':

    n = int(input())
    if n < 0 :
        print(False)
    elif isPalindrome(n):
        print(True)
    else:
        print(False)