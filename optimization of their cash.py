"""  Семья решила заняться оптимизацией своих денежных расходов и придумала следующую схему:

10 % доходов идут на отпуск
30 % доходов на пропитание и еду
5 % на коммунальные платежи
15 % на выходной досуг
остальные 40% идут в накопления
Если вдруг нужный процент не получается сделать, тогда копейка перекидывается в накопления. Например:

Сумма доходов равна 50 001.25 , 10 % от этой суммы это 5000.125 рублей. Пол копейки как валюты не существует, поэтому эта половинка переходит в накопления.

Напишите для семьи программу, которая будет принимать на вход месячный доход мужа и жены и расчитывать сколько им нужно отложить на каждую категорию.

Ваша программа принимает два числа типа float. Целая часть – рубли, а дробная – копейки.

В качестве результата работы выведите количество рублей и копеек для каждой из категорий в таком формате:

Отпуск: 10 руб. 5 коп.
Пропитание и еда: 30 руб. 15 коп.
Коммунальные платежи: 5 руб. 0 коп.
Досуг: 10 руб. 11 коп.
Накопления: 50 руб. 3 коп.  """
import math
def RubKop(total):
    vacationrub =  total // 100
    vacationkop = total % 100 // 1 * 0.01
    return vacationrub, vacationkop

def RubKopOkr(total):
    vacationrub = math.modf(total)[1]
    #vacationkop = math.modf(total%1 * 100)[1] * 0.01
    vacationkop =  round(math.modf(total)[0], 2)
    return vacationrub, vacationkop

def razdel(total_income, percent):
    vacation = total_income * percent
    vacation = vacation
    vacationrub, vacationkop = RubKop(vacation)
    vacation = vacationrub + vacationkop
    vacationkop = round(vacationkop * 100)
    vacationrub = round(vacationrub)
    return  vacationrub, vacationkop, vacation

husbands_income = float(input()) * 100
wifes_income   = float(input()) * 100
#accumulation = 0
total_income = husbands_income + wifes_income
total_income = total_income

vacationRub, vacationKop, vacation = razdel(total_income, 0.1)
#accumulation = accumulation + ost

sustenance_and_foodRub, sustenance_and_foodKop, sustenance_and_food  = razdel(total_income, 0.3)

communal_paymentsRub, communal_paymentsKop, communal_payments  = razdel(total_income,  0.05)

weekend_leisureRub, weekend_leisureKop, weekend_leisure  = razdel(total_income,  0.15)

total_income = total_income * 0.01
accumulation = total_income - vacation  - sustenance_and_food - communal_payments - weekend_leisure
accumulationRub, accumulationKop = RubKopOkr(accumulation)
accumulationKop = round(accumulationKop * 100)
accumulationRub = round(accumulationRub )
print("Отпуск:" , vacationRub, "руб.", vacationKop, "коп.")
print("Пропитание и еда:" , sustenance_and_foodRub, "руб.", sustenance_and_foodKop, "коп.")
print("Коммунальные платежи:" , communal_paymentsRub, "руб.", communal_paymentsKop, "коп.")
print("Досуг:" , weekend_leisureRub, "руб.", weekend_leisureKop, "коп.")
print("Накопления:" , accumulationRub, "руб.",accumulationKop, "коп.")