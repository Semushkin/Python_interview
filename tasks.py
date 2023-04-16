from os.path import splitext, split
# import os
from os import listdir
from pprint import pprint
from random import randint, choice
import string
# import random

'''
1. Написать программу, которая будет содержать функцию для получения имени файла из полного пути до него.
При вызове функции в качестве аргумента должно передаваться имя файла с расширением.
В функции необходимо реализовать поиск полного пути по имени файла, а затем «выделение» из этого пути имени файла
(без расширения).
'''


def task_1(full_path):
    path, file = split(full_path)
    name, file_extension = splitext(file)
    result = {
        'full_path': full_path,
        'path': path,
        'file': file,
        'file name': name,
        'file_extension': file_extension
    }
    return result


'''
2. Написать программу, которая запрашивает у пользователя ввод числа. На введенное число она отвечает сообщением, 
целое оно или дробное. Если дробное — необходимо далее выполнить сравнение чисел до и после запятой. Если они совпадают, 
программа должна возвращать значение True, иначе False.
'''


def task_2():
    number = input('Введите число: ')
    try:
        float(number)
    except ValueError:
        return 'Ошибка! Введено не число.'
    else:
        if number.isdigit():
            return 'Введено целое число'
        else:
            num_1, num_2 = number.split('.')
            if num_1 == num_2:
                return True
            else:
                return False


'''
3. Создать два списка с различным количеством элементов. В первом должны быть записаны ключи, во втором — значения. 
Необходимо написать функцию, создающую из данных ключей и значений словарь. Если ключу не хватает значения, в словаре 
для него должно сохраняться значение None. Значения, которым не хватило ключей, необходимо отбросить.
'''


def task_3():
    en_alphabet = string.ascii_lowercase
    rand_key = [''.join(choice(en_alphabet) for _ in range(randint(3, 10))) for _ in range(randint(5, 15))]
    rand_value = [randint(1, 100) for _ in range(randint(5, 15))]
    print(f'Keys List (len:{len(rand_key)}): {rand_key}')
    print(f'Value List (len:{len(rand_value)}): {rand_value}')
    result = {}
    for num, i in enumerate(rand_key):
        try:
            result[i] = rand_value[num]
        except IndexError:
            result[i] = None
    print(f'Dict (len:{len(result)}): {result}')


'''
4. Написать программу, в которой реализовать две функции. В первой должен создаваться простой текстовый файл. 
Если файл с таким именем уже существует, выводим соответствующее сообщение. 
Необходимо открыть файл и подготовить два списка: с текстовой и числовой информацией. 
Для создания списков использовать генераторы. Применить к спискам функцию zip(). 
Результат выполнения этой функции должен должен быть обработан и записан в файл таким образом, чтобы каждая строка файла 
содержала текстовое и числовое значение. Вызвать вторую функцию. В нее должна передаваться ссылка на созданный файл. 
Во второй функции необходимо реализовать открытие файла и простой построчный вывод содержимого. Вся программа должна 
запускаться по вызову первой функции.
'''


def task_4(name):

    def create_file(name):
        file_name = name + '.txt'

        files = listdir()
        if file_name in files:
            print('Ошибка! Файл с таким именем уже существует')
            return None

        en_alphabet = string.ascii_lowercase
        rand_text = [''.join(choice(en_alphabet) for _ in range(randint(3, 10))) for _ in range(10)]
        rand_num = [randint(1, 100) for _ in range(10)]
        data = list(zip(rand_text, rand_num))
        print('Запись файла')
        with open(file_name, 'w', encoding='utf-8') as w_file:
            w_file.write('Hello')
            for item in data:
                w_file.writelines(f'{item[0]}, {item[1]}\n')
        reade_file(file_name)

    def reade_file(file_name):
        print('Чтение содержимого файла:')
        with open(file_name, 'r', encoding='utf-8') as r_file:
            for line in r_file:
                print(line, end='')

    create_file(name)

'''
5. Усовершенствовать первую функцию из предыдущего примера. 
Необходимо во втором списке часть строковых значений заменить на значения типа example345 (строка+число). 
Далее — усовершенствовать вторую функцию из предыдущего примера (функцию извлечения данных). 
Дополнительно реализовать поиск определенных подстрок в файле по следующим условиям: вывод первого вхождения, вывод 
всех вхождений. 
Реализовать замену всех найденных подстрок на новое значение и вывод всех подстрок, состоящих из букв и цифр и имеющих 
пробелы только в начале и конце — например, example345.
'''


def task_5(name):

    def create_file(name):
        file_name = name + '.txt'

        files = listdir()
        if file_name in files:
            print('Ошибка! Файл с таким именем уже существует')
            return None

        en_alphabet = string.ascii_lowercase
        rand_text = [''.join(choice(en_alphabet) for _ in range(randint(3, 10))) for _ in range(10)]
        rand_num = [randint(1, 100) for _ in range(10)]
        for _ in range(5):
            rand_item = randint(1, 9)
            rand_num[rand_item] = rand_text[rand_item] + str(rand_num[rand_item])

        data = list(zip(rand_text, rand_num))

        rand_find = choice(data)[randint(0, 1)]

        print('Запись файла')
        with open(file_name, 'w', encoding='utf-8') as w_file:
            w_file.write('Hello')
            for item in data:
                w_file.writelines(f'{item[0]}, {item[1]}\n')
        reade_file(file_name, rand_find)

    def reade_file(file_name, rand_find):
        print('Чтение содержимого файла:')
        with open(file_name, 'r', encoding='utf-8') as r_file:
            for line in r_file:
                print(line, end='')
                if line.find(str(rand_find)) != -1:
                    print(f'Найдено искомое значение {rand_find}')

    create_file(name)


if __name__ == '__main__':
    pprint(task_1(__file__))
    # print(task_2())
    # task_3()
    # task_4('task_4')
    # task_5('task_5')

