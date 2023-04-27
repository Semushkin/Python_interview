import sqlite3
from os.path import dirname
from pprint import pprint

'''
На данном этапе работы с проектом выполним первую часть практического задания: подготовим фрагменты программного кода,
отвечающие за создание таблиц базы данных. В седьмом уроке отображение этих таблиц реализуем в специальных виджетах.
Ниже приведено описание необходимых блоков программного кода.
'''
'''
1. Создать файл базы данных:
    С помощью одного из менеджеров баз данных (например, SQLiteStudio) создать пустой файл SQLite-базы данных.
'''
'''
2. Создать подключение к базе данных:
    Выполнить импорт модуля с Python DB-API для реализации взаимодействия с СУБД SQLite. Создать подключение к базе
    данных, путь к которой записан в переменную db_path. Создать объект-курсор для выполнения операций с данными.
'''
'''
3. Создать вспомогательные таблицы:
    Категории товаров. Написать запрос создания таблицы categories (с проверкой ее существования).
    Таблица должна содержать два поля:
        category_name (категория),
        category_description (описание).
    Все поля должны быть не пустыми. Поле category должно быть первичным ключом.Единицы измерения товаров.

    Написать запрос создания таблицы units с проверкой ее существования.
    Таблица должна содержать одно поле — unit (единица измерения). Оно должно быть не пустым и выступать первичным ключом.

    Должности. Написать запрос создания таблицы positions (с проверкой ее существования).
    Таблица должна содержать одно поле — position (должность). Оно должно быть не пустым и выступать первичным ключом.
'''
'''
### 4. Создать основные таблицы
    Товары:
        Написать запрос создания таблицы goods с проверкой ее существования.
        Таблица должна содержать четыре поля:
            good_id (номер товара — первичный ключ),
            good_name (название товара),
            good_unit (единица измерения товара — внешний ключ на таблицу units),
            good_cat (категория товара — внешний ключ на таблицу categories).
    Сотрудники:
        Написать запрос создания таблицы employees с проверкой ее существования.
        Таблица должна содержать три поля:
            employee_id (номер сотрудника — первичный ключ),
            employee_fio (ФИО сотрудника),
            employee_position (должность сотрудника — внешний ключ на таблицу positions).
    Поставщики:
        Написать запрос создания таблицы vendors с проверкой ее существования.
        Таблица должна содержать шесть полей:
            vendor_id (номер поставщика — первичный ключ),
            vendor_name (название поставщика),
            vendor_ownerchipform (форма собственности поставщика),
            vendor_address (адрес поставщика),
            vendor_phone (телефон поставщика),
            vendor_email (email поставщика).
'''

FILENAME = 'db.sqlite'
db_path = dirname(__file__) + '/' + FILENAME


def task_1():
    conn = sqlite3.connect('db.sqlite')
    conn.close()


def task_2(db_path):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    conn.close()


def task_3(db_path):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS categories ('
                'category_id INTEGER PRIMARY KEY, '
                'category_name STRING NOT NULL, '
                'category_description STRING NOT NULL)')

    cur.execute('CREATE TABLE IF NOT EXISTS units (unit STRING PRIMARY KEY NOT NULL)')

    cur.execute('CREATE TABLE IF NOT EXISTS positions (position STRING PRIMARY KEY NOT NULL)')
    conn.commit()
    conn.close()


def task_4(db_path):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    cur.execute('CREATE TABLE IF NOT EXISTS goods ('
                'good_id INTEGER PRIMARY KEY, '
                'good_name STRING, '
                'good_unit STRING, '
                'good_cat INTEGER, '
                'FOREIGN KEY (good_unit) REFERENCES units (unit) , '
                'FOREIGN KEY (good_cat) REFERENCES categories (category_id))')

    cur.execute('CREATE TABLE IF NOT EXISTS employees ('
                'employee_id INTEGER PRIMARY KEY, '
                'employee_fio STRING, '
                'employee_position STRING, '
                'FOREIGN KEY (employee_position) REFERENCES positions (position))')

    cur.execute('CREATE TABLE IF NOT EXISTS vendors ('
                'vendor_id INTEGER PRIMARY KEY, '
                'vendor_name STRING, '
                'vendor_ownerchipform STRING, '
                'vendor_address STRING, '
                'vendor_phone STRING, '
                'vendor_email STRING)')

    conn.commit()
    conn.close()


def show_all_table(db_path):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute('SELECT * FROM sqlite_master WHERE type="table"')
    for item in cur.fetchall():
        print(item)
    conn.close()


if __name__ == '__main__':
    task_1()
    task_2(db_path)
    task_3(db_path)
    task_4(db_path)

    show_all_table(db_path)
