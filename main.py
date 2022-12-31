import sys

from PyQt5.QtSql import QSqlQuery, QSqlDatabase
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QPushButton,
                             QHBoxLayout, QListWidget, QLineEdit, QTextEdit,
                             QListWidgetItem, QLabel, QMessageBox)

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QGridLayout, QWidget, QCheckBox, QSystemTrayIcon, \
    QSpacerItem, QSizePolicy, QMenu, QAction, QStyle, qApp

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *

from PyQt5.QtGui import *

from PyQt5.QtCore import QDate, QTime, QDateTime, Qt
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(420, 520)
        MainWindow.setStyleSheet("background-color: rgb(162, 165, 100);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tasks_list = QtWidgets.QListWidget(self.centralwidget)
        self.tasks_list.setGeometry(QtCore.QRect(10, 25, 281, 100))
        self.tasks_list.setObjectName("listWidget")
        self.categories_list = QtWidgets.QListWidget(self.centralwidget)
        self.categories_list.setGeometry(QtCore.QRect(10, 220, 401, 100))
        self.categories_list.setObjectName("listWidget_2")
        self.category_name = QtWidgets.QLineEdit(self.centralwidget)
        self.category_name.setGeometry(QtCore.QRect(260, 330, 150, 20))
        self.category_name.setObjectName("lineEdit")
        self.task_name = QtWidgets.QLineEdit(self.centralwidget)
        self.task_name.setGeometry(QtCore.QRect(260, 360, 150, 20))
        self.task_name.setObjectName("lineEdit_2")
        self.task_description = QtWidgets.QTextEdit(self.centralwidget)
        self.task_description.setGeometry(QtCore.QRect(260, 400, 150, 100))
        self.task_description.setObjectName("textEdit")
        self.button_edit_task = QtWidgets.QPushButton(self.centralwidget)
        self.button_edit_task.setGeometry(QtCore.QRect(10, 440, 120, 23))
        self.button_edit_task.setObjectName("button_edit_task")
        self.button_add_task = QtWidgets.QPushButton(self.centralwidget)
        self.button_add_task.setGeometry(QtCore.QRect(10, 400, 120, 23))
        self.button_add_task.setObjectName("button_add_task")
        self.button_delete_task = QtWidgets.QPushButton(self.centralwidget)
        self.button_delete_task.setGeometry(QtCore.QRect(10, 480, 120, 23))
        self.button_delete_task.setObjectName("button_delete_task")
        self.button_all_tasks = QtWidgets.QPushButton(self.centralwidget)
        self.button_all_tasks.setGeometry(QtCore.QRect(10, 170, 120, 23))
        self.button_all_tasks.setObjectName("button_all_tasks")
        self.button_edit_category = QtWidgets.QPushButton(self.centralwidget)
        self.button_edit_category.setGeometry(QtCore.QRect(130, 440, 120, 23))
        self.button_edit_category.setObjectName("button_edit_category")
        self.button_done_tasks = QtWidgets.QPushButton(self.centralwidget)
        self.button_done_tasks.setGeometry(QtCore.QRect(290, 170, 120, 23))
        self.button_done_tasks.setObjectName("button_done_tasks")
        self.button_add_category = QtWidgets.QPushButton(self.centralwidget)
        self.button_add_category.setGeometry(QtCore.QRect(130, 400, 120, 23))
        self.button_add_category.setObjectName("button_add_category")
        self.button_delete_category = QtWidgets.QPushButton(self.centralwidget)
        self.button_delete_category.setGeometry(QtCore.QRect(130, 480, 120, 23))
        self.button_delete_category.setObjectName("button_delete_category")
        self.button_active_tasks = QtWidgets.QPushButton(self.centralwidget)
        self.button_active_tasks.setGeometry(QtCore.QRect(150, 170, 120, 23))
        self.button_active_tasks.setObjectName("button_active_tasks")
        self.button_high_priority = QtWidgets.QPushButton(self.centralwidget)
        self.button_high_priority.setGeometry(QtCore.QRect(290, 140, 120, 23))
        self.button_high_priority.setObjectName("button_high_priority")
        self.button_normal_priority = QtWidgets.QPushButton(self.centralwidget)
        self.button_normal_priority.setGeometry(QtCore.QRect(150, 140, 120, 23))
        self.button_normal_priority.setObjectName("button_normal_priority")
        self.button_low_priority = QtWidgets.QPushButton(self.centralwidget)
        self.button_low_priority.setGeometry(QtCore.QRect(10, 140, 120, 23))
        self.button_low_priority.setObjectName("button_low_priority")
        self.label = QtWidgets.QLabel('Times font', self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 200, 101, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 6, 81, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(150, 360, 111, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(150, 330, 111, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(260, 380, 111, 16))
        self.label_5.setObjectName("label_5")
        self.dates_list = QtWidgets.QListWidget(self.centralwidget)
        self.dates_list.setGeometry(QtCore.QRect(300, 25, 111, 100))
        self.dates_list.setObjectName("listWidget_3")
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(10, 360, 120, 22))
        self.dateEdit.setObjectName("dateEdit")
        self.date = QtWidgets.QLabel(self.centralwidget)
        self.date.setGeometry(QtCore.QRect(10, 340, 101, 16))
        self.date.setObjectName("label_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        now = QDate.currentDate()
        qdate = QtCore.QDate(now)
        self.dateEdit.setDate(qdate)
        self.dateEdit.setDisplayFormat('dd-MM-yyyy')
        self.dateEdit.setDate(qdate)

        self.label.setFont(QFont('Arial', 8))
        self.label_2.setFont(QFont('Arial', 8))
        self.label_3.setFont(QFont('Arial', 8))
        self.label_4.setFont(QFont('Arial', 8))
        self.label_5.setFont(QFont('Arial', 8))
        self.date.setFont(QFont('Arial', 8))









        self.create_db()
        self.load_tasks()
        self.load_categories()
        self.load_date()

        self.tasks_list.itemClicked.connect(self.task_detail)
        self.categories_list.itemClicked.connect(self.category_detail)

        self.button_add_task.clicked.connect(self.add_task)
        self.button_edit_task.clicked.connect(self.edit_task)
        self.button_delete_task.clicked.connect(self.delete_task)


        self.button_add_category.clicked.connect(self.add_category)
        self.button_edit_category.clicked.connect(self.edit_category)
        self.button_delete_category.clicked.connect(self.delete_category)
        self.button_add_task.clicked.connect(self.add_date)

        #self.tasks_list.Qt..connect(self.update_status)

        self.button_active_tasks.clicked.connect(self.active_task)
        self.button_done_tasks.clicked.connect(self.non_active_task)
        self.button_all_tasks.clicked.connect(self.load_tasks)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowIcon(QIcon(QIcon("Cooman.png")))
        MainWindow.setStyleSheet(' self.setStyleSheet("background-color: yellow;")')
        self.button_edit_task.setText(_translate("MainWindow", "Изменить задачу"))
        self.button_add_task.setText(_translate("MainWindow", "Добавить задачу"))
        self.button_delete_task.setText(_translate("MainWindow", "Удалить задачу"))
        self.button_all_tasks.setText(_translate("MainWindow", "Все задачи"))
        self.button_edit_category.setText(_translate("MainWindow", "Изменить категорию"))
        self.button_done_tasks.setText(_translate("MainWindow", "Выполненные задачи"))
        self.button_add_category.setText(_translate("MainWindow", "Добавить категорию"))
        self.button_delete_category.setText(_translate("MainWindow", "Удалить категорию"))
        self.button_active_tasks.setText(_translate("MainWindow", "Активные задачи"))
        self.button_high_priority.setText(_translate("MainWindow", "Высокий приоритет"))
        self.button_normal_priority.setText(_translate("MainWindow", "Средний приоритет"))
        self.button_low_priority.setText(_translate("MainWindow", "Низкий приоритет"))
        self.label.setText(_translate("MainWindow", "Список категорий:"))
        self.label_2.setText(_translate("MainWindow", "Список задач:"))
        self.label_3.setText(_translate("MainWindow", "Название задачи:"))
        self.label_4.setText(_translate("MainWindow", "Название категории:"))
        self.label_5.setText(_translate("MainWindow", "описание задачи:"))
        self.date.setText(_translate("MainWindow", "Срок выполнения:"))








    def create_db(self):
        query = QSqlQuery()
        query.exec(
            """
            CREATE TABLE IF NOT EXISTS categories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(255) NOT NULL
            );
            """
        )
        query.exec(
            """
            CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(255) NOT NULL,
            description VARCHAR(255) NOT NULL,
            active BOOL NOT NULL DEFAULT TRUE,
            category_id INTEGER,
            FOREIGN KEY (category_id) REFERENCES categories (id)
            );
            """
        )
        query.exec(
            """
            CREATE TABLE IF NOT EXISTS dates (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT
            );
            """
        )

    def load_tasks(self):
        query = QSqlQuery()
        query.exec(
            """SELECT * 
            FROM tasks
            LEFT JOIN categories 
            ON category_id=categories.id;""")
        self.tasks = []
        count = query.record().count()
        while query.next():
            temp = []
            for i in range(count):
                temp.append(query.value(i))
            self.tasks.append(temp)
        print(self.tasks)
        self.tasks_list.clear()
        for task in self.tasks:
            self.tasks_list.addItem(QListWidgetItem(task[1]))

    def load_categories(self):
        query = QSqlQuery()
        query.exec(
            """SELECT * 
            FROM categories;""")
        self.categories = []
        count = query.record().count()
        while query.next():
            temp = []
            for i in range(count):
                temp.append(query.value(i))
            self.categories.append(temp)
        print(self.categories)
        self.categories_list.clear()
        for category in self.categories:
            self.categories_list.addItem(QListWidgetItem(category[1]))

    def load_date(self):
        query = QSqlQuery()
        query.exec(
            """SELECT strftime('%d, %m, %Y')
            FROM dates
            LEFT JOIN tasks
            ON task_id=tasks.id;"""
        )
        self.dates = []
        count = query.record().count()
        while query.next():
            temp = []
            for i in range(count):
                temp.append(query.value(i))
            self.dates.append(temp)
        print(self.dates)
        self.dates_list.clear()
        for date in self.dates:
            self.tasks_list.addItem(QListWidgetItem(date[1]))

    def task_detail(self):
        row = self.tasks_list.currentRow()
        self.task_name.setText(self.tasks[row][1])
        self.task_description.setText(self.tasks[row][2])
        self.category_name.setText(self.tasks[row][6])

    def category_detail(self):
        row = self.categories_list.currentRow()
        self.category_name.setText(self.categories[row][1])

    def add_task(self):
        name = self.task_name.text()
        description = self.task_description.toPlainText()
        row = self.categories_list.currentRow()
        category_id = self.categories[row][0]
        query = QSqlQuery()
        query.exec(
            f"""INSERT INTO tasks (name, description, category_id)                  
            VALUES ('{name}', '{description}', '{category_id}');""")


        self.load_tasks()

    def add_date(self):
        time = self.dateEdit.text()
        #row = self.categories_list.currentRow()

        query = QSqlQuery()
        query.exec(
            f"""INSERT INTO dates (date)
            VALUES ('{time}');"""
        )
        self.load_date()

    def delete_task(self):
        row = self.tasks_list.currentRow()
        task_id = self.tasks[row][0]
        message_box = QMessageBox()
        message_box.setIcon(QMessageBox.Warning)
        message_box.setText(f"Вы точно хотите удалить задачу: {self.tasks[row][1]}?")
        message_box.setWindowTitle("Удалить категорию?")
        message_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        message_box.show()
        result = message_box.exec()
        if result == QMessageBox.Yes:
            query = QSqlQuery()
            query.exec(
                f"""DELETE FROM tasks 
                WHERE id={task_id};"""
            )
            self.load_tasks()

    def edit_task(self):
        row = self.tasks_list.currentRow()
        task_id = self.tasks[row][0]
        name = self.task_name.text()
        description = self.task_description.toPlainText()
        cat_row = self.categories_list.currentRow()
        category_id = self.categories[cat_row][0]
        query = QSqlQuery()
        query.exec(
            f"""UPDATE tasks 
            SET name='{name}', description='{description}', category_id='{category_id}'
            WHERE id={task_id};"""
        )
        self.load_tasks()

    def add_category(self):
        name = self.category_name.text()
        query = QSqlQuery()
        query.exec(
            f"""INSERT INTO categories (name) 
            VALUES ('{name}');"""
        )
        self.load_categories()

    def delete_category(self):
        row = self.categories_list.currentRow()
        category_id = self.categories[row][0]
        message_box = QMessageBox()
        message_box.setIcon(QMessageBox.Warning)
        message_box.setText(f"Вы точно хотите удалить категорию: {self.categories[row][1]}?")
        message_box.setWindowTitle("Удалить категорию?")
        message_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        message_box.show()
        result = message_box.exec()
        if result == QMessageBox.Yes:
            query = QSqlQuery()
            query.exec(
                f"""DELETE FROM categories 
                WHERE id={category_id};"""
            )
            self.load_categories()

    def edit_category(self):
        row = self.categories_list.currentRow()
        category_id = self.categories[row][0]
        name = self.category_name.text()
        query = QSqlQuery()
        query.exec(
            f"""UPDATE categories 
            SET name='{name}'
            WHERE id={category_id};"""
        )
        self.load_categories()

    def active_task(self):
        query = QSqlQuery()
        query.exec(
            """SELECT * 
            FROM tasks
            LEFT JOIN categories 
            ON category_id=categories.id WHERE active == 1;""")
        self.tasks = []
        count = query.record().count()
        while query.next():
            temp = []
            for i in range(count):
                temp.append(query.value(i))
            self.tasks.append(temp)
        print(self.tasks)
        self.tasks_list.clear()
        for task in self.tasks:
            self.tasks_list.addItem(QListWidgetItem(task[1]))

    def non_active_task(self):
        query = QSqlQuery()
        query.exec(
            """SELECT * 
                        FROM tasks 
                                   LEFT JOIN categories    
                                            ON category_id=categories.id WHERE active == 0;""")
        self.tasks = []
        count = query.record().count()
        while query.next():
            temp = []
            for i in range(count):
                temp.append(query.value(i))
            self.tasks.append(temp)
        print(self.tasks)
        self.tasks_list.clear()
        for task in self.tasks:
            self.tasks_list.addItem(QListWidgetItem(task[1]))

    def update_status(self):
        row = self.tasks_list.currentRow()
        task_id = self.tasks[row][0]
        if self.tasks[row][3] == 1:
            message_box = QMessageBox()
            message_box.setIcon(QMessageBox.Warning)
            message_box.setText(f"Вы точно хотите сделать задачу выполненной: {self.tasks[row][1]}?")
            message_box.setWindowTitle("Удалить категорию?")
            message_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            message_box.show()
            result = message_box.exec()
            if result == QMessageBox.Yes:
                query = QSqlQuery()
                query.exec(
                    f"""UPDATE tasks
                    SET active = FALSE
                    WHERE id={task_id};"""
                )
        if self.tasks[row][3] == 0:
            message_box = QMessageBox()
            message_box.setIcon(QMessageBox.Warning)
            message_box.setText(f"Вы точно хотите сделать задачу активной: {self.tasks[row][1]}?")
            message_box.setWindowTitle("Удалить категорию?")
            message_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            message_box.show()
            result = message_box.exec()
            if result == QMessageBox.Yes:
                query = QSqlQuery()
                query.exec(
                    f"""UPDATE tasks
                    SET active = TRUE
                    WHERE id={task_id};"""
                )

if __name__ == "__main__":
    con = QSqlDatabase.addDatabase("QSQLITE")
    con.setDatabaseName("tasks.sqlite")

    if not con.open():
        print("Database Error: %s" % con.lastError().databaseText())
        sys.exit(1)

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    app.setQuitOnLastWindowClosed(False)

    icon = QIcon("icon.png")

    tray = QSystemTrayIcon()
    tray.setIcon(icon)
    tray.setVisible(True)

    menu = QMenu()


    quit = QAction("Quit")
    quit.triggered.connect(app.quit)
    menu.addAction(quit)


    tray.setContextMenu(menu)

    app.exec_()
