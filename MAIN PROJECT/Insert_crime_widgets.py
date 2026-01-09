from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QVBoxLayout, QGridLayout, \
    QButtonGroup, \
    QMessageBox, QRadioButton, QHBoxLayout, QGroupBox, QSizePolicy, QStackedWidget, QTableWidgetItem, QTableWidget, \
    QComboBox, QTextEdit, QCalendarWidget, QDialog
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon, QPixmap, QCursor, QColor, QIntValidator
from PyQt6 import QtGui
import sys

from INSERT import *
from DATABASE import *

custom_color = QColor(169, 242, 255)


# ################################################
# ###############  CALENDER WIDGET  ##############
# ################################################

class Insert_address_date_CalendarDialog(QDialog):
    def __init__(self, button, parent=None):
        super().__init__(parent)
        self.button = button

        self.setWindowTitle("Select Date")

        self.calendar = QCalendarWidget()
        self.calendar.setGridVisible(True)

        self.ok_button = QPushButton("OK", self)
        self.ok_button.clicked.connect(self.set_date_and_accept)

        layout = QVBoxLayout()
        layout.addWidget(self.calendar)
        layout.addWidget(self.ok_button)
        self.setLayout(layout)

    def set_date_and_accept(self):
        if not self.calendar.selectedDate().isValid():
            QMessageBox.warning(self, "Warning", "Please select a valid date.")
        else:
            self.button.setText(self.calendar.selectedDate().toString("yyyy-MM-dd"))
            self.accept()


class Insert_crime_Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("Insert_crime_Widget")
        self.setGeometry(200, 50, 1000, 750)

        self.insert_Stacked_Widgets = QStackedWidget(self)
        self.insert_Stacked_Widgets.setGeometry(100, 50, 800, 550)
        self.insert_Stacked_Widgets.setObjectName("insert_Stacked_Widgets")

        self.insert_crime_record_btn = QPushButton("Insert Crime Record", self)
        self.insert_crime_record_btn.setObjectName("insert_crime_record_btn")
        self.insert_crime_record_btn.setGeometry(325, 650, 150, 40)
        self.insert_crime_record_btn.clicked.connect(self.show_insert_crime_record_widget)

        self.insert_jail_record_btn = QPushButton("Insert Jail Record", self)
        self.insert_jail_record_btn.setObjectName("insert_jail_record_btn")
        self.insert_jail_record_btn.setGeometry(525, 650, 150, 40)
        self.insert_jail_record_btn.clicked.connect(self.show_insert_jail_record_widget)

        self.insert_crime_record_widget = insert_crime_record_widget()

        self.insert_jail_record_widget = insert_jail_record_widget()

        self.insert_Stacked_Widgets.addWidget(self.insert_crime_record_widget)
        self.insert_Stacked_Widgets.addWidget(self.insert_jail_record_widget)

        with open("style.css", "r") as f:
            self.setStyleSheet(f.read())

    def show_insert_crime_record_widget(self):
        self.insert_Stacked_Widgets.setCurrentIndex(0)

    def show_insert_jail_record_widget(self):
        self.insert_Stacked_Widgets.setCurrentIndex(1)


# ################################################
# #############  CRIME RECORD WIDGET  #############
# ################################################

class insert_crime_record_widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("insert_crime_record_widget")
        self.setGeometry(200, 50, 800, 550)

        self.insert_crime_label = QLabel("CRIME RECORD", self)
        self.insert_crime_label.setObjectName("insert_crime_label")
        self.insert_crime_label.setGeometry(310, 10, 360, 50)

        self.INSERT_Crime_Record = []

        self.insert_crime_sub_widget = QWidget(self)
        self.insert_crime_sub_widget.setObjectName("insert_crime_sub_widget")
        self.insert_crime_sub_widget.setGeometry(50, 70, 700, 450)

        self.insert_crime_table_widget = QTableWidget(self.insert_crime_sub_widget)
        self.insert_crime_table_widget.setObjectName("insert_crime_table_widget")
        self.insert_crime_table_widget.setGeometry(25, 30, 650, 210)
        self.insert_crime_table_widget.setColumnCount(7)
        self.insert_crime_table_widget.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.insert_crime_table_widget.setHorizontalHeaderLabels([
            "Person ID",
            "Person Name",
            "Crime ID",
            "Crime Name",
            "Crime Date",
            "Status",
            "Delete"
        ])

        self.insert_crime_table_widget.horizontalHeader().setStretchLastSection(True)
        self.insert_crime_table_widget.setColumnWidth(0, 70)
        self.insert_crime_table_widget.setColumnWidth(1, 130)
        self.insert_crime_table_widget.setColumnWidth(2, 70)
        self.insert_crime_table_widget.setColumnWidth(3, 130)
        self.insert_crime_table_widget.setColumnWidth(4, 90)
        self.insert_crime_table_widget.setColumnWidth(5, 80)
        self.insert_crime_table_widget.setColumnWidth(6, 40)
        self.insert_crime_table_widget.verticalHeader().setStyleSheet("QHeaderView::section{font-weight: bold;}")
        self.insert_crime_table_widget.horizontalHeader().setStyleSheet("QHeaderView::section{font-weight: bold;}")
        self.insert_crime_table_widget.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)

        self.insert_person_id_lineedit = QLineEdit(self.insert_crime_sub_widget)
        self.insert_person_id_lineedit.setObjectName("insert_person_id_lineedit")
        self.insert_person_id_lineedit.setGeometry(65, 280, 80, 30)
        self.insert_person_id_lineedit.setPlaceholderText("Person ID")

        self.insert_person_see_button = QPushButton(self.insert_crime_sub_widget)
        self.insert_person_see_button.setObjectName("insert_person_see_button")
        self.insert_person_see_button.setGeometry(170, 280, 160, 30)
        self.insert_person_see_button.setText("See Persons")
        self.insert_person_see_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.insert_person_see_button.clicked.connect(self.show_insert_crime_see_person_table)

        self.insert_crime_id_lineedit = QLineEdit(self.insert_crime_sub_widget)
        self.insert_crime_id_lineedit.setObjectName("insert_crime_id_lineedit")
        self.insert_crime_id_lineedit.setGeometry(370, 280, 80, 30)
        self.insert_crime_id_lineedit.setPlaceholderText("Crime ID")

        self.insert_crime_see_button = QPushButton(self.insert_crime_sub_widget)
        self.insert_crime_see_button.setObjectName("insert_crime_see_button")
        self.insert_crime_see_button.setGeometry(475, 280, 160, 30)
        self.insert_crime_see_button.setText("See Crimes")
        self.insert_crime_see_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.insert_crime_see_button.clicked.connect(self.show_insert_crime_see_crimes_table)

        self.insert_crime_record_date_button = QPushButton(self.insert_crime_sub_widget)
        self.insert_crime_record_date_button.setObjectName("insert_crime_record_date_button")
        self.insert_crime_record_date_button.setGeometry(65, 340, 175, 30)
        self.insert_crime_record_date_button.setText("Date")
        self.insert_crime_record_date_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.insert_crime_record_date_button.clicked.connect(self.show_insert_crime_record_date_calender_dialog)

        self.insert_crime_status_combobox = QComboBox(self.insert_crime_sub_widget)
        self.insert_crime_status_combobox.setObjectName("crime_status_combobox")
        self.insert_crime_status_combobox.setGeometry(270, 340, 160, 30)
        self.insert_crime_status_combobox.addItem("Pending")
        self.insert_crime_status_combobox.addItem("Under Trial")
        self.insert_crime_status_combobox.addItem("Convicted")
        self.insert_crime_status_combobox.addItem("Dismissed")
        self.insert_crime_status_combobox.addItem("Closed Unsolved")

        self.insert_crime_add_button = QPushButton("Add", self.insert_crime_sub_widget)
        self.insert_crime_add_button.setObjectName("insert_crime_add_button")
        self.insert_crime_add_button.setGeometry(460, 340, 175, 30)
        self.insert_crime_add_button.setCursor(Qt.CursorShape.PointingHandCursor)
        self.insert_crime_add_button.clicked.connect(self.add_crime)

        self.insert_crime_insert_button = QPushButton("Insert In Database", self.insert_crime_sub_widget)
        self.insert_crime_insert_button.setObjectName("insert_crime_insert_button")
        self.insert_crime_insert_button.setGeometry(250, 390, 200, 40)
        self.insert_crime_insert_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.insert_crime_insert_button.clicked.connect(self.insert_crime_record)
        self.insert_crime_insert_button.hide()

        with open("./style.css", "r") as f:
            self.setStyleSheet(f.read())

    def insert_crime_record(self):
        try:
            for data in self.INSERT_Crime_Record:
                crime_record = [int(data[0]), int(data[2]), data[4], data[5]]
                Insert_Into_Crime_Record(crime_record)
                # print("Inserting : " + str(crime_record_id) + " : " + str(crime_record))
            QMessageBox.information(self, "Success", "Crime Record Inserted Successfully")
            self.INSERT_Crime_Record.clear()
            self.update_crime_table()
        except Exception as e:
            QMessageBox.warning(self, "Error", str(e))

    def show_insert_crime_see_person_table(self):
        try:
            self.insert_person_see_crimes_table = insert_person_see_crimes_table()
            self.insert_person_see_crimes_table.show()
        except Exception as e:
            QMessageBox.warning(self, "Error", str(e))

    def show_insert_crime_see_crimes_table(self):
        try:
            self.insert_crime_see_crimes_table = insert_crime_see_crimes_table()
            self.insert_crime_see_crimes_table.show()
        except Exception as e:
            QMessageBox.warning(self, "Error", str(e))

    def show_insert_crime_record_date_calender_dialog(self):
        insert_crime_record_date_dialog = Insert_address_date_CalendarDialog(self.insert_crime_record_date_button)
        insert_crime_record_date_dialog.exec()

    def add_crime(self):
        person_id = self.insert_person_id_lineedit.text()
        person_name = self.insert_person_validate_id(person_id)
        crime_id = self.insert_crime_id_lineedit.text()
        crime_name = self.insert_crime_validate_id(crime_id)
        crime_date = self.insert_crime_record_date_button.text()
        crime_status = self.insert_crime_status_combobox.currentText()

        crime_data = [
            person_id,
            person_name,
            crime_id,
            crime_name,
            crime_date,
            crime_status
        ]

        try:
            if crime_data[1] == "":
                QMessageBox.warning(self, "Error", "Person ID is invalid")
            elif crime_data[3] == "":
                QMessageBox.warning(self, "Error", "Crime ID is invalid")
            elif self.validate_crime(crime_data):
                self.INSERT_Crime_Record.append(crime_data)
                self.update_crime_table()
                self.clear_all()
            else:
                QMessageBox.warning(self, "Error", "All fields are required")
        except Exception as e:
            QMessageBox.warning(self, "Error", str(e))

    def insert_person_validate_id(self, person_id):
        try:
            query = f"SELECT f_name,l_name FROM person WHERE person_id = {person_id}"
            json_data = RunQuery(query)
            if not json_data:
                return ""
            name = str(json_data[0]["f_name"] + " " + json_data[0]["l_name"])
            return name
        except Exception as e:
            return ""

    def insert_crime_validate_id(self, crime_id):
        try:
            query = f"SELECT crime_name FROM crimes WHERE crime_id = {crime_id}"
            json_data = RunQuery(query)
            if json_data == []:
                return ""
            name = json_data[0]["crime_name"]
            return name
        except Exception as e:
            return ""

    def clear_all(self):
        self.insert_person_id_lineedit.clear()
        self.insert_crime_id_lineedit.clear()
        self.insert_crime_status_combobox.setCurrentIndex(0)
        self.insert_crime_record_date_button.setText("Date")

    def validate_crime(self, crime_data):
        for data in crime_data:
            if data == "" or data == "Date":
                return False
        return True

    def update_crime_table(self):
        self.insert_crime_table_widget.setRowCount(len(self.INSERT_Crime_Record))
        if len(self.INSERT_Crime_Record) == 0:
            self.insert_crime_insert_button.hide()
        else:
            self.insert_crime_insert_button.show()
        for row, data_entry in enumerate(self.INSERT_Crime_Record):
            for col, value in enumerate(data_entry):
                item = QTableWidgetItem(value)
                self.insert_crime_table_widget.setItem(row, col, item)

            # Add delete button to each row
            self.insert_crime_delete_button = QPushButton("X", self)
            self.insert_crime_delete_button.setFixedSize(30, 30)
            self.insert_crime_delete_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
            self.insert_crime_delete_button.setObjectName("insert_crime_delete_button")
            self.insert_crime_delete_button.clicked.connect(lambda _, row=row: self.delete_crime(row))
            self.insert_crime_table_widget.setCellWidget(row, 6, self.insert_crime_delete_button)

    def delete_crime(self, row):
        del self.INSERT_Crime_Record[row]
        self.update_crime_table()


# ################################################
# #############  SEE Person TABLE  ###############
# ################################################

class insert_person_see_crimes_table(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Persons Table")
        self.setObjectName("insert_crime_see_crimes_table_window")
        self.setGeometry(500, 150, 800, 600)
        self.setFixedSize(800, 600)

        self.insert_see_persons_label = QLabel("PERSONS", self)
        self.insert_see_persons_label.setObjectName("insert_see_persons_label")
        self.insert_see_persons_label.setGeometry(340, 10, 150, 50)
        self.insert_see_persons_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.insert_see_persons_table = QTableWidget(self)
        self.insert_see_persons_table.setObjectName("insert_see_persons_table")
        self.insert_see_persons_table.setGeometry(25, 70, 750, 400)
        self.insert_see_persons_table.setColumnCount(6)
        self.insert_see_persons_table.setHorizontalHeaderLabels([
            "Person ID",
            "First Name",
            "Last Name",
            "DOB",
            "Gender",
            "CNIC"
        ])
        self.insert_see_persons_table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.insert_see_persons_table.verticalHeader().hide()
        self.insert_see_persons_table.horizontalHeader().setStyleSheet("QHeaderView::section{font-weight: bold;}")
        self.insert_see_persons_table.horizontalHeader().setStretchLastSection(True)
        self.insert_see_persons_table.setColumnWidth(0, 80)
        self.insert_see_persons_table.setColumnWidth(1, 130)
        self.insert_see_persons_table.setColumnWidth(2, 130)
        self.insert_see_persons_table.setColumnWidth(3, 130)
        self.insert_see_persons_table.setColumnWidth(4, 130)
        self.insert_see_persons_table.setColumnWidth(5, 130)
        self.insert_see_persons_table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.insert_see_persons_table.setSelectionMode(QTableWidget.SelectionMode.SingleSelection)
        self.insert_see_persons_table.setShowGrid(False)

        self.insert_see_persons_close_button = QPushButton("Close", self)
        self.insert_see_persons_close_button.setObjectName("insert_see_persons_close_button")
        self.insert_see_persons_close_button.setGeometry(350, 500, 100, 40)
        self.insert_see_persons_close_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.insert_see_persons_close_button.clicked.connect(self.close)

        self.person_load_data()
        with open("./style.css", "r") as f:
            self.setStyleSheet(f.read())

    def person_load_data(self):
        try:
            query = "SELECT person_id, f_name, l_name, date_of_birth, gender, cnic_number FROM person"
            json_data = RunQuery(query)
            person_data = json_data
            self.person_display_data(person_data)
        except Exception as e:
            QMessageBox.warning(self, "Server Error", str(e))

    def person_display_data(self, person_data):
        num_rows = len(person_data)
        self.insert_see_persons_table.setRowCount(num_rows)

        for row, row_data in enumerate(person_data):
            for col, value in enumerate(row_data.values()):
                item = QTableWidgetItem(str(value))
                if col in [1, 2]:
                    item.setFlags(item.flags() | Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEditable)
                    item.setTextAlignment(Qt.AlignmentFlag.AlignTop)
                self.insert_see_persons_table.setItem(row, col, item)

            if row % 2 == 0:
                self.insert_see_persons_table.item(row, 0).setBackground(custom_color)
                self.insert_see_persons_table.item(row, 1).setBackground(custom_color)
                self.insert_see_persons_table.item(row, 2).setBackground(custom_color)
                self.insert_see_persons_table.item(row, 3).setBackground(custom_color)
                self.insert_see_persons_table.item(row, 4).setBackground(custom_color)
                self.insert_see_persons_table.item(row, 5).setBackground(custom_color)
            else:
                self.insert_see_persons_table.item(row, 0).setBackground(Qt.GlobalColor.white)
                self.insert_see_persons_table.item(row, 1).setBackground(Qt.GlobalColor.white)
                self.insert_see_persons_table.item(row, 2).setBackground(Qt.GlobalColor.white)
                self.insert_see_persons_table.item(row, 3).setBackground(Qt.GlobalColor.white)
                self.insert_see_persons_table.item(row, 4).setBackground(Qt.GlobalColor.white)
                self.insert_see_persons_table.item(row, 5).setBackground(Qt.GlobalColor.white)

        self.insert_see_persons_table.resizeRowsToContents()


class insert_crime_see_crimes_table(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Crimes Table")
        self.setObjectName("insert_crime_see_crimes_table_window")
        self.setGeometry(500, 150, 800, 600)
        self.setFixedSize(800, 600)

        self.insert_see_crime_label = QLabel("CRIMES", self)
        self.insert_see_crime_label.setObjectName("insert_see_crime_label")
        self.insert_see_crime_label.setGeometry(350, 10, 100, 50)
        self.insert_see_crime_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.insert_see_crime_table = QTableWidget(self)
        self.insert_see_crime_table.setObjectName("insert_see_crime_table")
        self.insert_see_crime_table.setGeometry(25, 70, 750, 400)
        self.insert_see_crime_table.setColumnCount(5)
        self.insert_see_crime_table.setHorizontalHeaderLabels([
            "Crime ID",
            "Crime Name",
            "Crime Details",
            "Punishment",
            "Fine"
        ])
        self.insert_see_crime_table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.insert_see_crime_table.verticalHeader().hide()
        self.insert_see_crime_table.horizontalHeader().setStyleSheet(
            "QHeaderView::section{font-weight: bold; font-size: 15px;}")

        self.insert_see_crime_table.horizontalHeader().setStretchLastSection(True)
        self.insert_see_crime_table.setColumnWidth(0, 80)
        self.insert_see_crime_table.setColumnWidth(1, 130)
        self.insert_see_crime_table.setColumnWidth(2, 250)
        self.insert_see_crime_table.setColumnWidth(3, 170)
        self.insert_see_crime_table.setColumnWidth(4, 80)
        self.insert_see_crime_table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)

        self.insert_see_crime_add_new_button = QPushButton("Add New", self)
        self.insert_see_crime_add_new_button.setObjectName("insert_see_crime_add_new_button")
        self.insert_see_crime_add_new_button.setGeometry(285, 500, 100, 40)
        self.insert_see_crime_add_new_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.insert_see_crime_add_new_button.clicked.connect(self.add_new_crime)

        self.insert_see_crime_delete_close = QPushButton("Close", self)
        self.insert_see_crime_delete_close.setObjectName("insert_see_crime_close")
        self.insert_see_crime_delete_close.setGeometry(415, 500, 100, 40)
        self.insert_see_crime_delete_close.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.insert_see_crime_delete_close.clicked.connect(self.close)

        self.crimes_load_data()
        with open("./style.css", "r") as f:
            self.setStyleSheet(f.read())

    def add_new_crime(self):
        self.insert_crime_window = insert_add_crime()
        self.insert_crime_window.show()
        self.close()

    def crimes_load_data(self):
        try:
            query = "SELECT * FROM crimes"
            json_data = RunQuery(query)
            data = json_data
            self.crimes_display_data(data)
        except Exception as e:
            QMessageBox.warning(self, "Server Error", str(e))

    def crimes_display_data(self, data):
        num_rows = len(data)
        self.insert_see_crime_table.setRowCount(num_rows)

        for row, row_data in enumerate(data):
            for col, value in enumerate(row_data.values()):
                item = QTableWidgetItem(str(value))
                if col in [1, 2]:
                    item.setFlags(item.flags() | Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEditable)
                    item.setTextAlignment(Qt.AlignmentFlag.AlignTop)
                self.insert_see_crime_table.setItem(row, col, item)

            if row % 2 == 0:
                self.insert_see_crime_table.item(row, 0).setBackground(custom_color)
                self.insert_see_crime_table.item(row, 1).setBackground(custom_color)
                self.insert_see_crime_table.item(row, 2).setBackground(custom_color)
                self.insert_see_crime_table.item(row, 3).setBackground(custom_color)
                self.insert_see_crime_table.item(row, 4).setBackground(custom_color)
            else:
                self.insert_see_crime_table.item(row, 0).setBackground(Qt.GlobalColor.white)
                self.insert_see_crime_table.item(row, 1).setBackground(Qt.GlobalColor.white)
                self.insert_see_crime_table.item(row, 2).setBackground(Qt.GlobalColor.white)
                self.insert_see_crime_table.item(row, 3).setBackground(Qt.GlobalColor.white)
                self.insert_see_crime_table.item(row, 4).setBackground(Qt.GlobalColor.white)

        self.insert_see_crime_table.resizeRowsToContents()


class insert_add_crime(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add Crime")
        self.setObjectName("insert_add_crime_window")
        self.setGeometry(500, 150, 500, 550)
        self.setFixedSize(500, 550)

        self.insert_add_crime_label = QLabel("ADD CRIME", self)
        self.insert_add_crime_label.setObjectName("insert_add_crime_label")
        self.insert_add_crime_label.setGeometry(175, 10, 150, 50)
        self.insert_add_crime_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.add_new_crime_name = QLineEdit(self)
        self.add_new_crime_name.setObjectName("add_new_crime_name")
        self.add_new_crime_name.setGeometry(50, 90, 400, 30)
        self.add_new_crime_name.setPlaceholderText("Crime Name")

        self.add_new_crime_details = QTextEdit(self)
        self.add_new_crime_details.setObjectName("add_new_crime_details")
        self.add_new_crime_details.setGeometry(50, 140, 400, 150)
        self.add_new_crime_details.setPlaceholderText("Crime Details")

        self.add_new_crime_punishment = QTextEdit(self)
        self.add_new_crime_punishment.setObjectName("add_new_crime_punishment")
        self.add_new_crime_punishment.setGeometry(50, 310, 400, 70)
        self.add_new_crime_punishment.setPlaceholderText("Punishment")

        self.add_new_crime_fine = QLineEdit(self)
        self.add_new_crime_fine.setObjectName("add_new_crime_fine")
        self.add_new_crime_fine.setGeometry(50, 400, 400, 30)
        self.add_new_crime_fine.setPlaceholderText("Fine")
        self.add_new_crime_fine.setValidator(QIntValidator())

        self.add_new_crime_add_button = QPushButton("Add", self)
        self.add_new_crime_add_button.setObjectName("add_new_crime_add_button")
        self.add_new_crime_add_button.setGeometry(130, 470, 100, 30)
        self.add_new_crime_add_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.add_new_crime_add_button.clicked.connect(self.add_new_crime_add_button_clicked)

        self.add_new_crime_close_button = QPushButton("Close", self)
        self.add_new_crime_close_button.setObjectName("add_new_crime_close_button")
        self.add_new_crime_close_button.setGeometry(270, 470, 100, 30)
        self.add_new_crime_close_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.add_new_crime_close_button.clicked.connect(self.add_new_crime_close_button_clicked)

        with open("./style.css", "r") as f:
            self.setStyleSheet(f.read())

    def add_new_crime_close_button_clicked(self):
        self.see_crimes_table = insert_crime_see_crimes_table()
        self.see_crimes_table.show()
        self.close()

    def add_new_crime_add_button_clicked(self):
        try:
            name = self.add_new_crime_name.text()
            details = self.add_new_crime_details.toPlainText()
            punishment = self.add_new_crime_punishment.toPlainText()
            fine = self.add_new_crime_fine.text()

            data = [name, details, punishment, fine]
            if not self.validate_new_crime(data):
                QMessageBox.warning(self, "Error", "All fields are required")
            else:
                try:
                    Insert_Into_Crimes(data)
                except Exception as e:
                    QMessageBox.warning(self, "Server Error", str(e))
                QMessageBox.information(self, "Success", "Crime Added Successfully")
                self.see_crimes_table = insert_crime_see_crimes_table()
                self.see_crimes_table.show()
                self.close()
        except Exception as e:
            QMessageBox.warning(self, "Server Error", str(e))

    def validate_new_crime(self, data):
        for d in data:
            if d == "":
                return False
        return True


# ################################################
# #############  JAIL RECORD WIDGET  #############
# ################################################

class insert_jail_record_widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("insert_jail_record_widget")
        self.setGeometry(200, 50, 800, 550)
        self.INSERT_jail_Record = []

        self.insert_jail_label = QLabel("JAIL RECORD", self)
        self.insert_jail_label.setObjectName("insert_jail_label")
        self.insert_jail_label.setGeometry(310, 10, 360, 50)

        self.insert_jail_sub_widget = QWidget(self)
        self.insert_jail_sub_widget.setObjectName("insert_jail_sub_widget")
        self.insert_jail_sub_widget.setGeometry(70, 80, 650, 450)

        self.insert_jail_table_widget = QTableWidget(self.insert_jail_sub_widget)
        self.insert_jail_table_widget.setObjectName("insert_jail_table_widget")
        self.insert_jail_table_widget.setGeometry(25, 30, 600, 210)
        self.insert_jail_table_widget.setColumnCount(7)
        self.insert_jail_table_widget.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.insert_jail_table_widget.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.insert_jail_table_widget.setSelectionMode(QTableWidget.SelectionMode.SingleSelection)
        self.insert_jail_table_widget.setHorizontalHeaderLabels([
            "Person ID",
            "Crime ID",
            "Jail ID",
            "Date IN",
            "Date OUT",
            "Status",
            "Delete"
        ])

        self.insert_jail_table_widget.horizontalHeader().setStretchLastSection(True)
        self.insert_jail_table_widget.setColumnWidth(0, 70)
        self.insert_jail_table_widget.setColumnWidth(1, 130)
        self.insert_jail_table_widget.setColumnWidth(2, 70)
        self.insert_jail_table_widget.setColumnWidth(3, 85)
        self.insert_jail_table_widget.setColumnWidth(4, 85)
        self.insert_jail_table_widget.setColumnWidth(5, 90)
        self.insert_jail_table_widget.setColumnWidth(6, 40)
        self.insert_jail_table_widget.verticalHeader().setStyleSheet("QHeaderView::section{font-weight: bold;}")
        self.insert_jail_table_widget.horizontalHeader().setStyleSheet("QHeaderView::section{font-weight: bold;}")

        self.insert_jail__person_id_lineedit = QLineEdit(self.insert_jail_sub_widget)
        self.insert_jail__person_id_lineedit.setObjectName("insert_jail__person_id_lineedit")
        self.insert_jail__person_id_lineedit.setGeometry(22, 280, 80, 30)
        self.insert_jail__person_id_lineedit.setPlaceholderText("Person ID")

        self.insert_jail_person_see_btn = QPushButton(self.insert_jail_sub_widget)
        self.insert_jail_person_see_btn.setObjectName("insert_jail_person_see_btn")
        self.insert_jail_person_see_btn.setGeometry(110, 280, 100, 30)
        self.insert_jail_person_see_btn.setText("See Persons")
        self.insert_jail_person_see_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.insert_jail_person_see_btn.clicked.connect(self.show_insert_jail_see_person_table)

        self.insert_jail_crime_id_lineedit = QLineEdit(self.insert_jail_sub_widget)
        self.insert_jail_crime_id_lineedit.setObjectName("insert_jail_crime_id_lineedit")
        self.insert_jail_crime_id_lineedit.setGeometry(230, 280, 75, 30)
        self.insert_jail_crime_id_lineedit.setPlaceholderText("Crime ID")

        self.insert_jail_crimes_see_btn = QPushButton(self.insert_jail_sub_widget)
        self.insert_jail_crimes_see_btn.setObjectName("insert_jail_crimes_see_btn")
        self.insert_jail_crimes_see_btn.setGeometry(315, 280, 100, 30)
        self.insert_jail_crimes_see_btn.setText("See Crimes")
        self.insert_jail_crimes_see_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.insert_jail_crimes_see_btn.clicked.connect(self.show_insert_jail_see_crimes_table)

        self.insert_jail_jail_id_lineedit = QLineEdit(self.insert_jail_sub_widget)
        self.insert_jail_jail_id_lineedit.setObjectName("insert_jail_jail_id_lineedit")
        self.insert_jail_jail_id_lineedit.setGeometry(435, 280, 75, 30)
        self.insert_jail_jail_id_lineedit.setPlaceholderText("Jail ID")

        self.insert_jail_jails_see_btn = QPushButton(self.insert_jail_sub_widget)
        self.insert_jail_jails_see_btn.setObjectName("insert_jail_jails_see_btn")
        self.insert_jail_jails_see_btn.setGeometry(520, 280, 105, 30)
        self.insert_jail_jails_see_btn.setText("See Jails")
        self.insert_jail_jails_see_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.insert_jail_jails_see_btn.clicked.connect(self.show_insert_jail_see_jails_table)

        self.insert_jail_record_date_in_button = QPushButton(self.insert_jail_sub_widget)
        self.insert_jail_record_date_in_button.setObjectName("insert_jail_record_date_in_button")
        self.insert_jail_record_date_in_button.setGeometry(25, 340, 120, 30)
        self.insert_jail_record_date_in_button.setText("Date IN")
        self.insert_jail_record_date_in_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.insert_jail_record_date_in_button.clicked.connect(self.show_insert_jail_record_date_in_calender_dialog)

        self.insert_jail_record_date_out_button = QPushButton(self.insert_jail_sub_widget)
        self.insert_jail_record_date_out_button.setObjectName("insert_jail_record_date_out_button")
        self.insert_jail_record_date_out_button.setGeometry(170, 340, 120, 30)
        self.insert_jail_record_date_out_button.setText("Date OUT")
        self.insert_jail_record_date_out_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.insert_jail_record_date_out_button.clicked.connect(self.show_insert_jail_record_date_out_calender_dialog)
        self.insert_jail_record_date_out_button.setDisabled(True)

        self.insert_jail_status_combobox = QComboBox(self.insert_jail_sub_widget)
        self.insert_jail_status_combobox.setObjectName("jail_status_combobox")
        self.insert_jail_status_combobox.setGeometry(315, 340, 155, 30)
        self.insert_jail_status_combobox.addItem("In Custody")
        self.insert_jail_status_combobox.addItem("Released")
        self.insert_jail_status_combobox.addItem("On Bail")
        self.insert_jail_status_combobox.addItem("Serving Sentence")
        self.insert_jail_status_combobox.addItem("Escaped")
        self.insert_jail_status_combobox.addItem("Deceased")
        self.insert_jail_status_combobox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.insert_jail_status_combobox.setCurrentIndex(0)
        self.insert_jail_status_combobox.currentIndexChanged.connect(self.jail_status_changed)

        self.insert_jail_add_button = QPushButton("Add", self.insert_jail_sub_widget)
        self.insert_jail_add_button.setObjectName("insert_jail_add_button")
        self.insert_jail_add_button.setGeometry(495, 340, 130, 30)
        self.insert_jail_add_button.setCursor(Qt.CursorShape.PointingHandCursor)
        self.insert_jail_add_button.clicked.connect(self.add_jail_data)

        self.insert_jail_insert_button = QPushButton("Insert In Database", self.insert_jail_sub_widget)
        self.insert_jail_insert_button.setObjectName("insert_crime_insert_button")
        self.insert_jail_insert_button.setGeometry(250, 390, 200, 40)
        self.insert_jail_insert_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.insert_jail_insert_button.clicked.connect(self.insert_jail_record)
        self.insert_jail_insert_button.hide()

        with open("./style.css", "r") as f:
            self.setStyleSheet(f.read())

    def insert_jail_record(self):
        try:
            for data in self.INSERT_jail_Record:
                if data[4] == "NULL":
                    data[4] = None

                jail_record = [int(data[2]), int(data[0]), int(data[1]), data[3], data[4], data[5]]
                Insert_Into_Jail_Record(jail_record)
            QMessageBox.information(self, "Success", "Jail Record Inserted Successfully")
            self.INSERT_jail_Record.clear()
            self.update_jail_table()
        except Exception as e:
            QMessageBox.warning(self, "Error", str(e))
    def jail_status_changed(self):
        status = self.insert_jail_status_combobox.currentText()
        if status == "Released" or status == "Deceased" or status == "Escaped" or status == "On Bail":
            self.insert_jail_record_date_out_button.setDisabled(False)
        else:
            self.insert_jail_record_date_out_button.setDisabled(True)
            self.insert_jail_record_date_out_button.setText("Date OUT")

    def show_insert_jail_record_date_in_calender_dialog(self):
        insert_jail_record_date_dialog = Insert_address_date_CalendarDialog(self.insert_jail_record_date_in_button)
        insert_jail_record_date_dialog.exec()

    def show_insert_jail_record_date_out_calender_dialog(self):
        insert_jail_record_date_dialog = Insert_address_date_CalendarDialog(self.insert_jail_record_date_out_button)
        insert_jail_record_date_dialog.exec()

    def show_insert_jail_see_person_table(self):
        try:
            self.insert_person_see_jail_table = insert_person_see_jail_table()
            self.insert_person_see_jail_table.show()
        except Exception as e:
            QMessageBox.warning(self, "Error", str(e))

    def show_insert_jail_see_crimes_table(self):
        try:
            self.p_id = self.insert_jail__person_id_lineedit.text()
            if self.p_id == "":
                QMessageBox.warning(self, "Error", "Person ID is required")
                return
            query = f"SELECT p.person_id,p.f_name,p.l_name,cr.crime_record_id,c.crime_name,cr.crime_date,cr.crime_status FROM person p INNER JOIN crimerecord cr inner join crimes c ON p.person_id = cr.person_id and cr.crime_id = c.crime_id WHERE p.person_id = {self.p_id};"
            json_data = RunQuery(query)
            if not json_data:
                QMessageBox.warning(self, "Error", "No Crimes Found")
                return
            self.insert_Crimes_see_jail_table = insert_Crimes_see_jail_table(json_data)
            self.insert_Crimes_see_jail_table.show()
        except Exception as e:
            QMessageBox.warning(self, "Error", str(e))

    def show_insert_jail_see_jails_table(self):
        try:
            self.insert_jail_see_jails_table = insert_jail_see_jails_table()
            self.insert_jail_see_jails_table.show()
        except Exception as e:
            QMessageBox.warning(self, "Error", str(e))

    def validate_jail(self, jail_data):
        for row in jail_data:
            if row == "" or row == "Date OUT" or row == "Date IN":
                return False
        return True

    def add_jail_data(self):
        person_id = self.insert_jail__person_id_lineedit.text()
        crime_id = self.insert_jail_crime_id_lineedit.text()
        jail_id = self.insert_jail_jail_id_lineedit.text()
        date_in = self.insert_jail_record_date_in_button.text()
        date_out = self.insert_jail_record_date_out_button.text()
        status = self.insert_jail_status_combobox.currentText()

        if status == "In Custody" or status == "Serving Sentence" :
            date_out = "NULL"

        jail_data = [
            person_id,
            crime_id,
            jail_id,
            date_in,
            date_out,
            status
        ]

        try:
            if self.validate_jail(jail_data):
                data = RunQuery(f"SELECT p.person_id,cr.crime_id, FROM person p INNER JOIN crimerecord cr inner join crimes c ON p.person_id = cr.person_id and cr.crime_id = c.crime_id WHERE p.person_id = {jail_data[0]};")
                if not data:
                    QMessageBox.warning(self, "Error", "Person ID is invalid")
                else:
                    self.insert_jail_insert_button.show()
                    self.INSERT_jail_Record.append(jail_data)
                    self.update_jail_table()
                    self.clear_all()
            else:
                QMessageBox.warning(self, "Error", "All fields are required")
        except Exception as e:
            QMessageBox.warning(self, "Error1", str(e))

    def clear_all(self):
        self.insert_jail__person_id_lineedit.clear()
        self.insert_jail_crime_id_lineedit.clear()
        self.insert_jail_jail_id_lineedit.clear()
        self.insert_jail_record_date_in_button.setText("Date IN")
        self.insert_jail_record_date_out_button.setText("Date OUT")
        self.insert_jail_status_combobox.setCurrentIndex(0)

    def update_jail_table(self):
        if len(self.INSERT_jail_Record) == 0:
            self.insert_jail_insert_button.hide()
        else:
            self.insert_jail_insert_button.show()

        self.insert_jail_table_widget.setRowCount(len(self.INSERT_jail_Record))
        for row, data_entry in enumerate(self.INSERT_jail_Record):
            for col, value in enumerate(data_entry):
                item = QTableWidgetItem(value)
                self.insert_jail_table_widget.setItem(row, col, item)

            # Add delete button to each row
            self.insert_jail_delete_button = QPushButton("X", self)
            self.insert_jail_delete_button.setFixedSize(30, 30)
            self.insert_jail_delete_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
            self.insert_jail_delete_button.setObjectName("insert_jail_delete_button")
            self.insert_jail_delete_button.clicked.connect(lambda _, row=row: self.delete_jail(row))
            self.insert_jail_table_widget.setCellWidget(row, 6, self.insert_jail_delete_button)

    def delete_jail(self, row):
        del self.INSERT_jail_Record[row]
        self.update_jail_table()


class insert_jail_see_jails_table(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Crimes Table")
        self.setObjectName("insert_crime_see_crimes_table_window")
        self.setGeometry(500, 150, 600, 600)
        self.setFixedSize(600, 600)

        self.insert_see_crime_label = QLabel("JAILS", self)
        self.insert_see_crime_label.setObjectName("insert_see_crime_label")
        self.insert_see_crime_label.setGeometry(250, 10, 100, 50)
        self.insert_see_crime_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.insert_see_crime_table = QTableWidget(self)
        self.insert_see_crime_table.setObjectName("insert_see_crime_table")
        self.insert_see_crime_table.setGeometry(25, 70, 550, 400)
        self.insert_see_crime_table.setColumnCount(4)
        self.insert_see_crime_table.setHorizontalHeaderLabels([
            "Jail ID",
            "Jail Name",
            "Jail Location",
            "Total Prisoners"
        ])
        self.insert_see_crime_table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.insert_see_crime_table.verticalHeader().hide()
        self.insert_see_crime_table.horizontalHeader().setStyleSheet(
            "QHeaderView::section{font-weight: bold; font-size: 15px;}")

        self.insert_see_crime_table.horizontalHeader().setStretchLastSection(True)
        self.insert_see_crime_table.setColumnWidth(0, 100)
        self.insert_see_crime_table.setColumnWidth(1, 190)
        self.insert_see_crime_table.setColumnWidth(2, 150)
        self.insert_see_crime_table.setColumnWidth(3, 70)
        self.insert_see_crime_table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)

        self.insert_see_crime_add_new_button = QPushButton("Add New", self)
        self.insert_see_crime_add_new_button.setObjectName("insert_see_crime_add_new_button")
        self.insert_see_crime_add_new_button.setGeometry(185, 500, 100, 40)
        self.insert_see_crime_add_new_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.insert_see_crime_add_new_button.clicked.connect(self.add_see_crime_add_new_button_clicked)

        self.insert_see_crime_delete_close = QPushButton("Close", self)
        self.insert_see_crime_delete_close.setObjectName("insert_see_crime_close")
        self.insert_see_crime_delete_close.setGeometry(315, 500, 100, 40)
        self.insert_see_crime_delete_close.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.insert_see_crime_delete_close.clicked.connect(self.close)

        self.crimes_load_data()
        with open("./style.css", "r") as f:
            self.setStyleSheet(f.read())

    def add_see_crime_add_new_button_clicked(self):
        self.insert_add_jail_window = insert_add_jail()
        self.insert_add_jail_window.show()
        self.close()

    def crimes_load_data(self):
        try:
            query = "SELECT jd.jail_id, jd.jail_name, jd.jail_location, COUNT(jr.jail_id) AS total_prisoners FROM jail_details jd LEFT JOIN jail_record jr ON jd.jail_id = jr.jail_id GROUP BY jd.jail_id, jd.jail_name, jd.jail_location;"
            json_data = RunQuery(query)
            data = json_data
            self.crimes_display_data(data)
        except Exception as e:
            QMessageBox.warning(self, "Server Error", str(e))

    def crimes_display_data(self, data):
        num_rows = len(data)
        self.insert_see_crime_table.setRowCount(num_rows)

        for row, row_data in enumerate(data):
            for col, value in enumerate(row_data.values()):
                item = QTableWidgetItem(str(value))
                if col in [1, 2]:
                    item.setFlags(item.flags() | Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEditable)
                    item.setTextAlignment(Qt.AlignmentFlag.AlignTop)
                self.insert_see_crime_table.setItem(row, col, item)

            if row % 2 == 0:
                self.insert_see_crime_table.item(row, 0).setBackground(custom_color)
                self.insert_see_crime_table.item(row, 1).setBackground(custom_color)
                self.insert_see_crime_table.item(row, 2).setBackground(custom_color)
                self.insert_see_crime_table.item(row, 3).setBackground(custom_color)
            else:
                self.insert_see_crime_table.item(row, 0).setBackground(Qt.GlobalColor.white)
                self.insert_see_crime_table.item(row, 1).setBackground(Qt.GlobalColor.white)
                self.insert_see_crime_table.item(row, 2).setBackground(Qt.GlobalColor.white)
                self.insert_see_crime_table.item(row, 3).setBackground(Qt.GlobalColor.white)

        self.insert_see_crime_table.resizeRowsToContents()


class insert_add_jail(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add JAIL")
        self.setObjectName("insert_add_crime_window")
        self.setGeometry(500, 150, 500, 300)
        self.setFixedSize(500, 300)

        self.insert_add_crime_label = QLabel("ADD JAIL", self)
        self.insert_add_crime_label.setObjectName("insert_add_crime_label")
        self.insert_add_crime_label.setGeometry(175, 10, 150, 50)
        self.insert_add_crime_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.add_new_crime_name = QLineEdit(self)
        self.add_new_crime_name.setObjectName("add_new_crime_name")
        self.add_new_crime_name.setGeometry(50, 90, 400, 30)
        self.add_new_crime_name.setPlaceholderText("Jail Name")

        self.add_new_crime_fine = QLineEdit(self)
        self.add_new_crime_fine.setObjectName("add_new_crime_fine")
        self.add_new_crime_fine.setGeometry(50, 150, 400, 30)
        self.add_new_crime_fine.setPlaceholderText("Jail Location")

        self.add_new_crime_add_button = QPushButton("Add", self)
        self.add_new_crime_add_button.setObjectName("add_new_crime_add_button")
        self.add_new_crime_add_button.setGeometry(130, 230, 100, 30)
        self.add_new_crime_add_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.add_new_crime_add_button.clicked.connect(self.add_new_crime_add_button_clicked)

        self.add_new_crime_close_button = QPushButton("Close", self)
        self.add_new_crime_close_button.setObjectName("add_new_crime_close_button")
        self.add_new_crime_close_button.setGeometry(270, 230, 100, 30)
        self.add_new_crime_close_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.add_new_crime_close_button.clicked.connect(self.add_new_crime_close_button_clicked)

        with open("./style.css", "r") as f:
            self.setStyleSheet(f.read())

    def add_new_crime_close_button_clicked(self):
        self.see_crimes_table = insert_jail_see_jails_table()
        self.see_crimes_table.show()
        self.close()

    def add_new_crime_add_button_clicked(self):
        try:
            name = self.add_new_crime_name.text()
            location = self.add_new_crime_fine.text()

            data = [name, location]
            if not self.validate_new_crime(data):
                QMessageBox.warning(self, "Error", "All fields are required")
            else:
                try:
                    Insert_Into_Jail_Details(data)
                except Exception as e:
                    QMessageBox.warning(self, "Server Error", str(e))
                QMessageBox.information(self, "Success", "Jail Added Successfully")
                self.see_crimes_table = insert_jail_see_jails_table()
                self.see_crimes_table.show()
                self.close()
        except Exception as e:
            QMessageBox.warning(self, "Server Error", str(e))

    def validate_new_crime(self, data):
        for d in data:
            if d == "":
                return False
        return True


class insert_Crimes_see_jail_table(QWidget):
    def __init__(self, crime_data):
        super().__init__()
        self.crime_data = crime_data
        self.setWindowTitle("CRIME Table")
        self.setObjectName("insert_crime_see_crimes_table_window")
        self.setGeometry(500, 150, 800, 600)
        self.setFixedSize(800, 600)

        self.insert_see_persons_label = QLabel("PERSONS", self)
        self.insert_see_persons_label.setObjectName("insert_see_persons_label")
        self.insert_see_persons_label.setGeometry(340, 10, 150, 50)
        self.insert_see_persons_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.insert_see_persons_table = QTableWidget(self)
        self.insert_see_persons_table.setObjectName("insert_see_persons_table")
        self.insert_see_persons_table.setGeometry(25, 70, 750, 400)
        self.insert_see_persons_table.setColumnCount(7)
        self.insert_see_persons_table.setHorizontalHeaderLabels([
            "Person ID",
            "First Name",
            "Last Name",
            "Crime Record ID",
            "Crime Name",
            "Crime Date",
            "Crime Status"
        ])
        self.insert_see_persons_table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        # self.insert_see_persons_table.verticalHeader().hide()
        self.insert_see_persons_table.horizontalHeader().setStyleSheet("QHeaderView::section{font-weight: bold;}")
        self.insert_see_persons_table.horizontalHeader().setStretchLastSection(True)
        self.insert_see_persons_table.setColumnWidth(0, 80)
        self.insert_see_persons_table.setColumnWidth(1, 100)
        self.insert_see_persons_table.setColumnWidth(2, 100)
        self.insert_see_persons_table.setColumnWidth(3, 100)
        self.insert_see_persons_table.setColumnWidth(4, 100)
        self.insert_see_persons_table.setColumnWidth(5, 100)
        self.insert_see_persons_table.setColumnWidth(6, 100)
        self.insert_see_persons_table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.insert_see_persons_table.setSelectionMode(QTableWidget.SelectionMode.SingleSelection)
        self.insert_see_persons_table.setShowGrid(False)

        self.insert_see_persons_close_button = QPushButton("Close", self)
        self.insert_see_persons_close_button.setObjectName("insert_see_persons_close_button")
        self.insert_see_persons_close_button.setGeometry(350, 500, 100, 40)
        self.insert_see_persons_close_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.insert_see_persons_close_button.clicked.connect(self.close)

        self.person_display_data(self.crime_data)
        with open("./style.css", "r") as f:
            self.setStyleSheet(f.read())

    def person_display_data(self, person_data):
        num_rows = len(person_data)
        self.insert_see_persons_table.setRowCount(num_rows)

        for row, row_data in enumerate(person_data):
            for col, value in enumerate(row_data.values()):
                item = QTableWidgetItem(str(value))
                if col in [1, 2]:
                    item.setFlags(item.flags() | Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEditable)
                    item.setTextAlignment(Qt.AlignmentFlag.AlignTop)
                self.insert_see_persons_table.setItem(row, col, item)

            if row % 2 == 0:
                self.insert_see_persons_table.item(row, 0).setBackground(custom_color)
                self.insert_see_persons_table.item(row, 1).setBackground(custom_color)
                self.insert_see_persons_table.item(row, 2).setBackground(custom_color)
                self.insert_see_persons_table.item(row, 3).setBackground(custom_color)
                self.insert_see_persons_table.item(row, 4).setBackground(custom_color)
                self.insert_see_persons_table.item(row, 5).setBackground(custom_color)
                self.insert_see_persons_table.item(row, 6).setBackground(custom_color)
            else:
                self.insert_see_persons_table.item(row, 0).setBackground(Qt.GlobalColor.white)
                self.insert_see_persons_table.item(row, 1).setBackground(Qt.GlobalColor.white)
                self.insert_see_persons_table.item(row, 2).setBackground(Qt.GlobalColor.white)
                self.insert_see_persons_table.item(row, 3).setBackground(Qt.GlobalColor.white)
                self.insert_see_persons_table.item(row, 4).setBackground(Qt.GlobalColor.white)
                self.insert_see_persons_table.item(row, 5).setBackground(Qt.GlobalColor.white)
                self.insert_see_persons_table.item(row, 6).setBackground(Qt.GlobalColor.white)

        self.insert_see_persons_table.resizeRowsToContents()


class insert_person_see_jail_table(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Persons Table")
        self.setObjectName("insert_crime_see_crimes_table_window")
        self.setGeometry(500, 150, 800, 600)
        self.setFixedSize(800, 600)

        self.insert_see_persons_label = QLabel("PERSONS", self)
        self.insert_see_persons_label.setObjectName("insert_see_persons_label")
        self.insert_see_persons_label.setGeometry(340, 10, 150, 50)
        self.insert_see_persons_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.insert_see_persons_table = QTableWidget(self)
        self.insert_see_persons_table.setObjectName("insert_see_persons_table")
        self.insert_see_persons_table.setGeometry(25, 70, 750, 400)
        self.insert_see_persons_table.setColumnCount(7)
        self.insert_see_persons_table.setHorizontalHeaderLabels([
            "Person ID",
            "First Name",
            "Last Name",
            "DOB",
            "Gender",
            "CNIC",
            "Crimes"
        ])
        self.insert_see_persons_table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        # self.insert_see_persons_table.verticalHeader().hide()
        self.insert_see_persons_table.horizontalHeader().setStyleSheet("QHeaderView::section{font-weight: bold;}")
        self.insert_see_persons_table.horizontalHeader().setStretchLastSection(True)
        self.insert_see_persons_table.setColumnWidth(0, 80)
        self.insert_see_persons_table.setColumnWidth(1, 110)
        self.insert_see_persons_table.setColumnWidth(2, 110)
        self.insert_see_persons_table.setColumnWidth(3, 110)
        self.insert_see_persons_table.setColumnWidth(4, 110)
        self.insert_see_persons_table.setColumnWidth(5, 130)
        self.insert_see_persons_table.setColumnWidth(6, 60)
        self.insert_see_persons_table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.insert_see_persons_table.setSelectionMode(QTableWidget.SelectionMode.SingleSelection)
        self.insert_see_persons_table.setShowGrid(False)

        self.insert_see_persons_close_button = QPushButton("Close", self)
        self.insert_see_persons_close_button.setObjectName("insert_see_persons_close_button")
        self.insert_see_persons_close_button.setGeometry(350, 500, 100, 40)
        self.insert_see_persons_close_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.insert_see_persons_close_button.clicked.connect(self.close)

        self.person_load_data()
        with open("./style.css", "r") as f:
            self.setStyleSheet(f.read())

    def person_load_data(self):
        try:
            query = "SELECT p.person_id, p.f_name, p.l_name, p.date_of_birth, p.gender, p.cnic_number, COUNT(c.crime_id) AS num_crime_records FROM person p INNER JOIN crimerecord c ON p.person_id = c.person_id GROUP BY p.person_id;"
            json_data = RunQuery(query)
            person_data = json_data
            self.person_display_data(person_data)
        except Exception as e:
            QMessageBox.warning(self, "Server Error", str(e))

    def person_display_data(self, person_data):
        num_rows = len(person_data)
        self.insert_see_persons_table.setRowCount(num_rows)

        for row, row_data in enumerate(person_data):
            for col, value in enumerate(row_data.values()):
                item = QTableWidgetItem(str(value))
                if col in [1, 2]:
                    item.setFlags(item.flags() | Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEditable)
                    item.setTextAlignment(Qt.AlignmentFlag.AlignTop)
                self.insert_see_persons_table.setItem(row, col, item)

            if row % 2 == 0:
                self.insert_see_persons_table.item(row, 0).setBackground(custom_color)
                self.insert_see_persons_table.item(row, 1).setBackground(custom_color)
                self.insert_see_persons_table.item(row, 2).setBackground(custom_color)
                self.insert_see_persons_table.item(row, 3).setBackground(custom_color)
                self.insert_see_persons_table.item(row, 4).setBackground(custom_color)
                self.insert_see_persons_table.item(row, 5).setBackground(custom_color)
                self.insert_see_persons_table.item(row, 6).setBackground(custom_color)
            else:
                self.insert_see_persons_table.item(row, 0).setBackground(Qt.GlobalColor.white)
                self.insert_see_persons_table.item(row, 1).setBackground(Qt.GlobalColor.white)
                self.insert_see_persons_table.item(row, 2).setBackground(Qt.GlobalColor.white)
                self.insert_see_persons_table.item(row, 3).setBackground(Qt.GlobalColor.white)
                self.insert_see_persons_table.item(row, 4).setBackground(Qt.GlobalColor.white)
                self.insert_see_persons_table.item(row, 5).setBackground(Qt.GlobalColor.white)
                self.insert_see_persons_table.item(row, 6).setBackground(Qt.GlobalColor.white)

        self.insert_see_persons_table.resizeRowsToContents()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = insert_crime_see_crimes_table()
    window.show()
    sys.exit(app.exec())
