"""Представим, что вы программируете hr-сервис по работе с вакансиями. Обычно в языках программирования есть множество различных фреймворков, и каждый из них относится к определенному языку программирования и специальности. Напишите программу, которая по названию фреймворка будет определять язык и профессию человека.
Flask, Django, Fast-API – Python(<framework>),Backend-dev
Angular, React, Vue – JavaScript/TypeScript(<framework>),Frontend-dev
Flutter, React Native – JavaScript(<framework>),Cross-Mobile-dev
Pandas, skit-learn, keras – Python(<framework>),Data-Scientist
В случае если фреймворк еще не известен – выведете "модель еще не обучена"
Ввод:
s – строка с названием фреймворка
Вывод:
Через запятую – lang(framework), profession
Sample Input 1:
Fast-API
Sample Output 1:
Python(Fast-API),Backend-dev"""
m = input()
match m:
    case "Flask" | "Django" | "Fast-API":
        print("Python("+ m + "),Backend-dev")
    case "Angular" | "React" | "Vue":
        print("JavaScript/TypeScript("+ m + "),Frontend-dev")
    case "Flutter" | "ReactNative" | "Vue":
        print("JavaScript("+ m + "),Cross-Mobile-dev")
    case "Pandas" | "skit-learn" | "keras ":
        print("Python("+ m + "),Data-Scientist")
    case _:
        print("модель еще не обучена")
