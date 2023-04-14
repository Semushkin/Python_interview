'''
2. Инкапсулировать оба параметра (название и цену) товара родительского класса. Убедиться, что при сохранении текущей
логики работы программы будет сгенерирована ошибка выполнения.
'''


class ItemDiscount:

    def __init__(self):
        self.__product_name = 'apple'
        self.__price = 100


class ItemDiscountReport(ItemDiscount):

    def get_parent_data(self):
        return f'Product name: {self.__product_name}, price: {self.__price}'


report = ItemDiscountReport()
print(report.get_parent_data())
