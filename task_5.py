'''
5. Реализовать расчет цены товара со скидкой. Величина скидки должна передаваться в качестве аргумента в дочерний класс.
Выполнить перегрузку методов конструктора дочернего класса (метод init, в который должна передаваться
переменная — скидка), и перегрузку метода str дочернего класса. В этом методе должна пересчитываться цена и
возвращаться результат — цена товара со скидкой. Чтобы все работало корректно, не забудьте инициализировать
дочерний и родительский классы (вторая и третья строка после объявления дочернего класса).
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

    def __init__(self, discount: int):
        """
        :param discount: int, percent
        """
        self.discount = discount
        super().__init__()

    def __str__(self):
        new_price = self.get_price - self.get_price * (self.discount/100)
        return str(new_price)

    def get_parent_data(self):
        return f'Product name: {self.get_product_name}, price: {self.get_price}, percent: {self.discount}' \
               f', price with discount:{self}'


Item = ItemDiscount()
report = ItemDiscountReport(10)
print(f'Дочерний класс - {report.get_parent_data()}')
