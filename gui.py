import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QHBoxLayout, QLabel, QLineEdit, QPushButton, \
    QFileDialog, QTableView, QAction, QVBoxLayout
from PyQt5.QtSql import QSqlTableModel, QSqlDatabase, QSqlRelation, QSqlRelationalTableModel, QSqlRelationalDelegate

'''
1. Создать главное окно программы, реализовать для него меню с шестью пунктами, верхний и центральный виджеты. 
    Каждый из пунктов должен соответствовать одной из шести таблиц. SQL-запросы их создания были написаны в практическом 
    задании к предыдущему уроку. Например, это могут быть пункты меню «Категории товаров», «Единицы измерения товаров», 
    «Должности» и так далее. Сделать так, чтобы пользователь не мог выбирать пункты меню (метод setEnabled()).
'''
'''    
2. Создать верхний виджет программы с фреймом, в котором расположить три виджета:
    a) надпись — путь к базе данных;
    b) текстовое поле для отображения пути к БД — сделать его недоступным для редактирования;
    c) кнопка, открывающая диалог выбора файла sqlite-базы данных.
'''
'''    
3. В центральном виджете программы реализовать виджет с табличным компонентом-представлением (QTableView) и двумя 
    кнопками (для добавления и удаления записи таблицы БД). В компоненте-представлении будут отображаться модели данных, 
    соответствующие каждой из таблиц. Пользователь сможет добавлять и удалять записи.
'''
'''
4. К кнопке, открывающей диалог выбора файла sqlite-базы данных, привязать обработчик нажатия. Он должен открывать окно 
    диалога для выбора файла БД (класс QFileDialog). При этом полный путь до базы данных должен сохраняться в текстовом 
    поле верхнего виджета программы. Должно устанавливаться соединение с базой данных — для этого используйте фрагмент 
    кода из практического задания с предыдущего урока. Сделать доступными меню главного окна программы.
'''
'''    
5. Для каждого из пунктов меню реализовать обработчики нажатия. Их код реализовать в отдельном модуле, который должен 
    импортироваться в главное окно программы. В каждый из обработчиков поместить фрагменты программного кода (из 
    практического задания предыдущего урока), отвечающие за создание соответствующих таблиц БД. В обработчике должны 
    создаваться соответствующие модели-таблицы (модели на основе таблиц БД). Для этого применяется PyQt-класс 
    QSqlTableModel.
'''
'''    
6. К каждой из кнопок добавления и удаления записей привязать обработчики этих событий. В компоненте-представлении 
    QTableView должны отображаться изменения — таблицы с добавленными записями или без удаленных.
'''


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.width()
        self.setWindowTitle('Main Window')

        self.main_widget = QWidget(self)
        self.vertical_layout = QVBoxLayout()
        self.main_widget.setLayout(self.vertical_layout)
        self.setCentralWidget(self.main_widget)

        self.menu()
        self.top_widget()
        self.central_widget()
        self.vertical_layout.addStretch(1)
        self.db_path = ''
        self.database_connect()

        self.show()

    def database_connect(self):
        database = QSqlDatabase.addDatabase('QSQLITE')
        database.setDatabaseName(self.db_path)
        database.open()

        self.model_type = QSqlRelationalTableModel(db=database)

        self.category_list()

    def menu(self):

        self.select_category_action = QAction('Категории товаров', self)
        self.select_unit_action = QAction('Еденици измерения товаров', self)
        self.select_position_action = QAction('Должности', self)
        self.select_goods_action = QAction('Товары', self)
        self.select_emoloyees_action = QAction('Сотрудники', self)
        self.select_vendor_action = QAction('Поставщики', self)


        self.toolbar = self.addToolBar('MainBar')
        self.toolbar.addAction(self.select_category_action)
        self.toolbar.addAction(self.select_unit_action)
        self.toolbar.addAction(self.select_position_action)
        self.toolbar.addAction(self.select_goods_action)
        self.toolbar.addAction(self.select_emoloyees_action)
        self.toolbar.addAction(self.select_vendor_action)

        self.select_category_action.triggered.connect(self.category_list)
        self.select_unit_action.triggered.connect(self.unit_list)
        self.select_position_action.triggered.connect(self.position_list)
        self.select_goods_action.triggered.connect(self.goods_list)
        self.select_emoloyees_action.triggered.connect(self.employees_list)
        self.select_vendor_action.triggered.connect(self.vendors_list)

    def top_widget(self):
        self.db_path_label = QLabel('Путь к базе данных', self)

        self.text_db_path = QLineEdit(self)
        self.text_db_path.setReadOnly(True)

        def get_file_dialog():
            self.db_path = QFileDialog.getOpenFileName(self)[0]
            self.database_connect()
            self.text_db_path.insert(self.db_path)
            print(self.db_path)

        self.db_path_button = QPushButton('Обзор', self)
        self.db_path_button.setFixedSize(60, 30)
        self.db_path_button.clicked.connect(get_file_dialog)

        self.vertical_layout.addWidget(self.db_path_label)
        self.vertical_layout.addWidget(self.text_db_path)
        self.vertical_layout.addWidget(self.db_path_button)

    def central_widget(self):

        self.label_tables = QLabel('Таблица', self)
        self.label_tables.setEnabled(False)

        self.btn_add_item = QPushButton('Добавить запись', self)
        self.btn_add_item.clicked.connect(self.add_row)

        self.btn_delete_item = QPushButton('Удалить запись', self)
        self.btn_delete_item.clicked.connect(self.delete_item)

        self.btn_save_items = QPushButton('Сохранить', self)
        self.btn_save_items.clicked.connect(self.save_row)

        self.table = QTableView(self)

        self.horizontal_Layout = QHBoxLayout()
        self.horizontal_Layout.addWidget(self.btn_add_item)
        self.horizontal_Layout.addWidget(self.btn_delete_item)
        self.horizontal_Layout.addWidget(self.btn_save_items)
        self.vertical_layout.addLayout(self.horizontal_Layout)
        self.vertical_layout.addWidget(self.label_tables)
        self.vertical_layout.addWidget(self.table)

    def category_list(self):
        self.model_type.setTable('Categories')
        self.table_options()

    def unit_list(self):
        self.model_type.setTable('Units')
        self.table_options()

    def position_list(self):
        self.model_type.setTable('Positions')
        self.table_options()

    def goods_list(self):
        self.model_type.setTable('Goods')
        self.model_type.setRelation(2, QSqlRelation('Units', 'unit', 'unit'))
        self.model_type.setRelation(3, QSqlRelation('Categories', 'id', 'name'))
        self.table_options()

    def employees_list(self):
        self.model_type.setTable('Employees')
        self.model_type.setRelation(2, QSqlRelation('Positions', 'position', 'position'))
        self.table_options()

    def vendors_list(self):
        self.model_type.setTable('Vendors')
        self.table_options()

    def add_row(self):
        self.model_type.insertRow(self.model_type.rowCount())

    def save_row(self):
        self.model_type.submitAll()

    def table_options(self):
        self.model_type.setEditStrategy(QSqlTableModel.OnManualSubmit)
        self.model_type.select()
        self.table.setModel(self.model_type)
        self.table.setItemDelegate(QSqlRelationalDelegate(self.table))
        self.table.resizeRowsToContents()
        self.table.resizeColumnsToContents()
        # self.btn_add_item.disconnect()

    def delete_item(self):
        selected_row = self.table.currentIndex().row()
        if selected_row != -1:
            self.model_type.removeRow(selected_row)
            self.save_row()
            # self.category_list()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    program = MainWindow()

    sys.exit(app.exec_())
