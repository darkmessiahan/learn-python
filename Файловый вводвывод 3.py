"""
Имеется файл с данными по успеваемости абитуриентов. Он представляет из себя набор строк, где в каждой строке записана следующая информация:
Фамилия;Оценка_по_математике;Оценка_по_физике;Оценка_по_русскому_языку
Поля внутри строки разделены точкой с запятой, оценки — целые числа.
Напишите программу, которая считывает исходный файл с подобной структурой и для каждого абитуриента записывает его среднюю оценку по трём предметам на отдельной строке, соответствующей этому абитуриенту, в файл с ответом.
Также вычислите средние баллы по математике, физике и русскому языку по всем абитуриентам и добавьте полученные значения, разделённые пробелом, последней строкой в файл с ответом.
В качестве ответа на задание прикрепите полученный файл со средними оценками по каждому ученику и одной строкой со средними оценками по трём предметам.
Примечание. Для разбиения строки на части по символу ';' можно использовать метод split следующим образом:
print('First;Second-1 Second-2;Third'.split(';'))
# ['First', 'Second-1 Second-2', 'Third']

Sample Input:

Петров;85;92;78
Сидоров;100;88;94
Иванов;58;72;85
Sample Output:

85.0
94.0
71.666666667
81.0 84.0 85.666666667
"""
MathScore = []
PhysicsScore = []
RussianScore = []
stringtotal  = ''
with open('G:\Python\ФАйлы\dataset_3363_4.txt') as in_f_obj:
    for list_string in in_f_obj:
        SdudentScoire = list_string.strip().split(";")
        MedScore =  (int(SdudentScoire[1]) + int(SdudentScoire[2]) + int(SdudentScoire[3]) ) / 3
        stringtotal = stringtotal + str(MedScore) + '\n'
        MathScore.append(int(SdudentScoire[1]))
        PhysicsScore.append(int(SdudentScoire[2]))
        RussianScore.append(int(SdudentScoire[3]))

MedMathSovre = sum(MathScore) / len(MathScore)
#stringtotal = stringtotal + str(MedMathSovre) + '\n'
MedPhysicsScore = sum(PhysicsScore) / len(PhysicsScore)
#stringtotal = stringtotal + str(MedPhysicsScore) + '\n'
MedPRussianScore = sum(RussianScore) / len(RussianScore)
stringtotal = stringtotal + str(MedMathSovre) + " " + str(MedPhysicsScore) + " " + str(MedPRussianScore) 


	
with open('G:\Python\ФАйлы\dataset_3363_4_2.txt', 'w', encoding='utf-8') as out_f_obj:
	out_f_obj.write(stringtotal)