'''
3. Усовершенствовать родительский класс таким образом, чтобы получить доступ к защищенным переменным.
Результат выполнения заданий 1 и 2 должен быть идентичным.
'''


class ItemDiscount:

    def __init__(self):
        self.__product_name = 'apple'
        self.__price = 100

    @property
    def get_product_name(self):
        return self.__product_name

    @property
    def get_price(self):
        return self.__price


class ItemDiscountReport(ItemDiscount):

    def get_parent_data(self):
        return f'Product name: {self.get_product_name}, price: {self.get_price}'


report = ItemDiscountReport()
print(report.get_parent_data())
