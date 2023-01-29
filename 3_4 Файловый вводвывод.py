'''
Недавно мы считали для каждого слова количество его вхождений в строку. Но на все слова может быть не так интересно смотреть, как, например, на наиболее часто используемые.
Напишите программу, которая считывает текст из файла (в файле может быть больше одной строки) и выводит самое частое слово в этом тексте и через пробел то, сколько раз оно встретилось. Если таких слов несколько, вывести лексикографически первое (можно использовать оператор < для строк).
В качестве ответа укажите вывод программы, а не саму программу.
Слова, написанные в разных регистрах, считаются одинаковыми.
Sample Input:
abc a bCd bC AbC BC BCD bcd ABC
Sample Output:
abc 3
'''
liststring = ""
#Путь к скачанному файлу / Path to downloaded file
with open('G:\Python\ФАйлы\dataset_3363_3.txt') as in_f_obj:
    for list_string in in_f_obj:
        liststring = liststring + list_string.lower()
#Для тестов можно временно указать строку / For tests, you can temporarily specify the line
#list_string = "abc a bCd bC AbC BC BCD bcd ABC".strip().lower().split()
list_string = liststring.split()	
dict_list = {}
for i in list_string:
    if i in dict_list:
        dict_list[i] += 1
    else:
        dict_list[i] = 1  
     
max_ch = max(list_string, key=dict_list.get)  
str_max = max_ch + " "+ str(dict_list[max_ch] )           
#print(str_max)
#Записываем файл с результатом как 	dataset_3363_3_2.txt / Write the file with the result as dataset_3363_3_2.txt
with open('G:\Python\ФАйлы\dataset_3363_3_2.txt', 'w', encoding='utf-8') as out_f_obj:
	out_f_obj.write(str_max)
