import os
from os import listdir
from os.path import dirname, join, isdir, isfile
from random import randint

'''
1. Написать функцию, реализующую вывод таблицы умножения размерностью AｘB. Первый и второй множитель должны задаваться
в виде аргументов функции. Значения каждой строки таблицы должны быть представлены списком, который формируется в цикле.
После этого осуществляется вызов внешней lambda-функции, которая формирует на основе списка строку. Полученная строка
выводится в главной функции. Элементы строки (элементы таблицы умножения) должны разделяться табуляцией.
'''


calculate = lambda x: f'{x[0]} * {x[1]} = {x[2]}'


def task_1(a, b):
    for row in range(1, a + 1):
        data = []
        for column in range(1, b + 1):
            data.append(row)
            data.append(column)
            data.append(row * column)
            print(calculate(data), end='\t')
            data.clear()
        print('')


'''
2. Дополнить следующую функцию недостающим кодом:
def print_directory_contents(sPath):
"""
Функция принимает имя каталога и распечатывает его содержимое
в виде «путь и имя файла», а также любые другие
файлы во вложенных каталогах.

Эта функция подобна os.walk. Использовать функцию os.walk
нельзя. Данная задача показывает ваше умение работать с 
вложенными структурами.
"""
'''


def task_2():
    path = dirname(__file__)

    def print_directory_contents(path):
        for item in listdir(path):
            obj = join(path, item)
            if isdir(obj):
                print_directory_contents(obj)
            elif isfile(obj):
                print(f'path: {path}; file: {item}')

    print_directory_contents(path)


'''
3. Разработать генератор случайных чисел. В функцию передавать начальное и конечное число генерации (нуль необходимо 
исключить). Заполнить этими данными список и словарь. Ключи словаря должны создаваться 
по шаблону: “elem_<номер_элемента>”. Вывести содержимое созданных списка и словаря.
'''


def task_3(min, max):
    random_list = [randint(min, max) for _ in range(1, 10)]
    random_dict = {f'elem_<{num}>': randint(min, max) for num in range(1, 10)}
    print(random_list)
    print(random_dict)


'''
4. Написать программу «Банковский депозит». Она должна состоять из функции и ее вызова с аргументами. 
Клиент банка делает депозит на определенный срок. В зависимости от суммы и срока вклада определяется процентная 
ставка: 
1000–10000 руб (6 месяцев — 5 % годовых, год — 6 % годовых, 2 года — 5 % годовых). 
10000–100000 руб (6 месяцев — 6 % годовых, год — 7 % годовых, 2 года – 6.5 % годовых). 
100000–1000000 руб (6 месяцев — 7 % годовых, год — 8 % годовых, 2 года — 7.5 % годовых). 
Необходимо написать функцию, в которую будут передаваться параметры: сумма вклада и срок вклада. 
Каждый из трех банковских продуктов должен быть представлен в виде словаря с ключами (begin_sum, end_sum, 6, 12, 24). 
Ключам соответствуют значения начала и конца диапазона суммы вклада и значения процентной ставки для каждого срока. 
В функции необходимо проверять принадлежность суммы вклада к одному из диапазонов и выполнять расчет по нужной 
процентной ставке. Функция возвращает сумму вклада на конец срока.
'''

deposits = [{'begin_sum': 1000, 'end_sum': 10000, 6: 5, 12: 6, 24: 5},
            {'begin_sum': 10000, 'end_sum': 100000, 6: 6, 12: 7, 24: 6.5},
            {'begin_sum': 100000, 'end_sum': 1000000, 6: 7, 12: 8, 24: 7.5}]


def task_4(amount: float, period: int):
    for deposit in deposits:
        if deposit['begin_sum'] <= amount < deposit['end_sum']:
            percent = deposit.get(period)
            if not percent:
                return 'Указан не верный период (должен быть 6, 12 или 24)'
            else:
                percent *= period / 12
                profit = amount * (percent * 0.01) + amount
                return f'Итого к выплате {profit}'
    return 'Нет вклада под указанную сумму'


'''
5. Усовершенствовать программу «Банковский депозит». Третьим аргументом в функцию должна передаваться фиксированная 
ежемесячная сумма пополнения вклада. Необходимо в главной функции реализовать вложенную функцию подсчета процентов для 
пополняемой суммы. Примем, что клиент вносит средства в последний день каждого месяца, кроме первого и последнего. 
Например, при сроке вклада в 6 месяцев пополнение происходит в течение 4 месяцев. Вложенная функция возвращает сумму 
дополнительно внесенных средств (с процентами), а главная функция — общую сумму по вкладу на конец периода.
'''


def task_5(amount: float, period: int, additional_fee: float):

    profit = None

    def additional_percent(amount_add: float):
        result = 0
        try:
            amount_add = float(amount_add)
        except ValueError:
            return None
        for item in range(2, period):
            result += amount_add
            result += result * ((period / 12) * 0.01)
        return result

    for deposit in deposits:
        if deposit['begin_sum'] <= amount < deposit['end_sum']:
            percent = deposit.get(period)
            if not percent:
                return 'Указан не верный период (должен быть 6, 12 или 24)'
            else:
                percent *= period / 12
                profit = amount * (percent * 0.01) + amount

    if profit:
        additional_profit = additional_percent(additional_fee)
        if not additional_profit:
            return 'Ошибка!!! Не верный формат дополнительных взносов'
        profit += additional_percent(additional_fee)
        return f'Итого к выплате на конец периода {profit}'

    return 'Нет вклада под указанную сумму'


if __name__ == '__main__':
    # task_1(2, 5)
    # task_2()
    # task_3(2, 80)
    # print(task_4(3500, 24))
    # print(task_5(1000, 6, 100))
    pass


