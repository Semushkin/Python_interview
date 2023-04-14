'''
1. Проверить механизм наследования в Python. Для этого создать два класса. Первый — родительский (ItemDiscount),
должен содержать статическую информацию о товаре: название и цену. Второй — дочерний (ItemDiscountReport), должен
содержать функцию (get_parent_data), отвечающую за отображение информации о товаре в одной строке. Проверить работу
программы, создав экземпляр (объект) родительского класса.
'''


class ItemDiscount:

    def __init__(self):
        self.product_name = 'apple'
        self.price = 100


class ItemDiscountReport(ItemDiscount):

    def get_parent_data(self):
        return f'Product name: {self.product_name}, price: {self.price}'


report = ItemDiscountReport()
print(report.get_parent_data())
