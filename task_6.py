'''
6. Проверить на практике возможности полиморфизма. Необходимо разделить дочерний класс ItemDiscountReport на
два класса. Инициализировать классы необязательно. Внутри каждого поместить функцию get_info, которая в первом
классе будет отвечать за вывод названия товара, а вторая — его цены. Далее реализовать выполнение каждой из функции
тремя способами.
'''


class ItemDiscount:

    __product_name = 'apple'
    __price = 100

    def __init__(self):
        pass

    @property
    def get_product_name(self):
        return self.__product_name

    @property
    def get_price(self):
        return self.__price

    @classmethod
    def set_product_name(cls, new_name):
        cls.__product_name = new_name

    @classmethod
    def set_price(cls, new_price):
        cls.__price = new_price

    @property
    def get_data(self):
        return f'Product name: {self.get_product_name}, price: {self.get_price}'


class ItemDiscountReportFirst(ItemDiscount):
    def __init__(self):
        super(ItemDiscountReportFirst, self).__init__()

    def get_info(self):
        return self.get_product_name


class ItemDiscountReportSecond(ItemDiscount):
    def __init__(self):
        super(ItemDiscountReportSecond, self).__init__()

    def get_info(self):
        return self.get_price


first_report = ItemDiscountReportFirst()
print(f'Product name: {first_report.get_info()}')
second_report = ItemDiscountReportSecond()
print(f'Product price: {second_report.get_info()}')
