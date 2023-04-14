'''
4. Реализовать возможность переустановки значения цены товара. Необходимо, чтобы и родительский, и дочерний классы
получили новое значение цены. Следует проверить это, вызвав соответствующий метод родительского класса и функцию
дочернего (функция, отвечающая за отображение информации о товаре в одной строке).
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


class ItemDiscountReport(ItemDiscount):

    def get_parent_data(self):
        return f'Product name: {self.get_product_name}, price: {self.get_price}'


item = ItemDiscount()
report = ItemDiscountReport()
print('До изминения')
print(f'Родительский класс - product_name: {item.get_data}')
print(f'Дочерний класс - {report.get_parent_data()}')

item.set_product_name('Cherry')
item.set_price(200)
print('После изминения')
print(f'Родительский класс - product_name: {item.get_data}')
print(f'Дочерний класс - {report.get_parent_data()}')

