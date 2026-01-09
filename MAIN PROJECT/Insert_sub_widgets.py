import json
import sys
import re

from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QPixmap, QIntValidator, QIcon, QCursor
from PyQt6.QtWidgets import QWidget, QLabel, QApplication, QMessageBox, QFileDialog, QPushButton, QLineEdit, QDialog, \
    QCalendarWidget, QVBoxLayout, QComboBox, QRadioButton, QHBoxLayout, QGroupBox, QTableWidgetItem, QTableWidget, \
    QButtonGroup, QHeaderView, QTextEdit

from DATABASE import RunQuery
from PyQt6.QtGui import QColor
from INSERT import *

# Inside display_data method
custom_color = QColor(169, 242, 255)
insert_person_family_id = -1


# #################################################################################################
# ########################################  INSERT WIDGETS  #######################################
# #################################################################################################

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


# ################################################
# ###############  PERSON CALENDER WIDGET  ##############
# ################################################

class Insert_person_CalendarDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Select Date")

        self.insert_person_dateofbirth_calendar = QCalendarWidget()
        self.insert_person_dateofbirth_calendar.setGridVisible(True)

        self.insert_person_dateofbirth_calender_button = QPushButton("OK", self)
        self.insert_person_dateofbirth_calender_button.setObjectName("insert_person_dateofbirth_calender_button")
        self.insert_person_dateofbirth_calender_button.setGeometry(50, 130, 200, 30)
        self.insert_person_dateofbirth_calender_button.clicked.connect(self.check_date)

        layout = QVBoxLayout()
        layout.addWidget(self.insert_person_dateofbirth_calendar)
        layout.addWidget(self.insert_person_dateofbirth_calender_button)
        self.setLayout(layout)

    def check_date(self):
        if not self.insert_person_dateofbirth_calendar.selectedDate().isValid():
            QMessageBox.warning(self, "Warning", "Please select a valid date.")
        else:
            self.accept()


# ################################################
# ###############  FAMILY PERSONS  ##############
# ################################################

class Insert_person_See_Family_detail_Window(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("FAMILY DETAILS")
        self.setObjectName("Insert_person_See_Family_detail_Window")
        self.setGeometry(500, 150, 470, 500)
        self.setFixedSize(470, 500)

        with open("./style.css", "r") as f:
            self.setStyleSheet(f.read())

        self.insert_person_see_families_label = QLabel("FAMILY DETAILS", self)
        self.insert_person_see_families_label.setGeometry(170, 30, 200, 50)
        self.insert_person_see_families_label.setObjectName("insert_person_see_families_label")

        self.insert_person_see_family_detail_table = QTableWidget(self)
        self.insert_person_see_family_detail_table.setObjectName("insert_person_see_family_detail_table")
        self.insert_person_see_family_detail_table.setGeometry(5, 80, 460, 300)
        self.insert_person_see_family_detail_table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)

        self.insert_person_see_family_id_back_button = QPushButton("Back", self)
        self.insert_person_see_family_id_back_button.setObjectName("insert_person_see_family_id_back_button")
        self.insert_person_see_family_id_back_button.setGeometry(120, 430, 100, 30)
        self.insert_person_see_family_id_back_button.clicked.connect(
            self.insert_person_family_detail_back_button_clicked)

        self.insert_person_see_family_id_close_button = QPushButton("Close", self)
        self.insert_person_see_family_id_close_button.setObjectName("insert_person_see_family_id_close_button")
        self.insert_person_see_family_id_close_button.setGeometry(250, 430, 100, 30)
        self.insert_person_see_family_id_close_button.clicked.connect(self.insert_person_family_detail_close_clicked)
        self.load_data()

    def insert_person_family_detail_back_button_clicked(self):
        self.Insert_person_See_Family_ID_Window = Insert_person_See_Family_ID_Window()
        self.hide()
        self.Insert_person_See_Family_ID_Window.show()

    def insert_person_family_detail_close_clicked(self):
        self.hide()

    def load_data(self):
        try:
            global insert_person_family_id
            query = str(
                "SELECT f_name, l_name, gender, age FROM person WHERE family_id = " + str(insert_person_family_id))
            json_data = RunQuery(query)

            data = json_data
            self.display_data(data)
        except Exception as e:
            QMessageBox.warning(self, "Server Error", str(e))

    def display_data(self, data):
        num_rows = len(data)
        num_cols = len(data[0])

        self.insert_person_see_family_detail_table.setRowCount(num_rows)
        self.insert_person_see_family_detail_table.setColumnCount(num_cols)  # Add one more column for the button
        headers = ["First Name", "Last Name", "Gender", "Age"]  # Custom headers
        self.insert_person_see_family_detail_table.setHorizontalHeaderLabels(headers)

        self.insert_person_see_family_detail_table.setColumnWidth(0, 100)
        self.insert_person_see_family_detail_table.setColumnWidth(1, 100)
        self.insert_person_see_family_detail_table.setColumnWidth(2, 100)
        self.insert_person_see_family_detail_table.setColumnWidth(3, 100)
        # self.insert_person_see_families_table.setColumnWidth(4, 100)

        for row, row_data in enumerate(data):
            for col, value in enumerate(row_data.values()):
                item = QTableWidgetItem(str(value))
                self.insert_person_see_family_detail_table.setItem(row, col, item)

            if row % 2 == 0:
                self.insert_person_see_family_detail_table.item(row, 0).setBackground(custom_color)
                self.insert_person_see_family_detail_table.item(row, 1).setBackground(custom_color)
                self.insert_person_see_family_detail_table.item(row, 2).setBackground(custom_color)
                self.insert_person_see_family_detail_table.item(row, 3).setBackground(custom_color)
            else:
                self.insert_person_see_family_detail_table.item(row, 0).setBackground(Qt.GlobalColor.white)
                self.insert_person_see_family_detail_table.item(row, 1).setBackground(Qt.GlobalColor.white)
                self.insert_person_see_family_detail_table.item(row, 2).setBackground(Qt.GlobalColor.white)
                self.insert_person_see_family_detail_table.item(row, 3).setBackground(Qt.GlobalColor.white)


# ################################################
# ###############  FAMILY DETAILS  ##############
# ################################################

class Insert_person_See_Family_ID_Window(QWidget):

    def __init__(self):
        super().__init__()
        self.setObjectName("Insert_person_See_Family_ID_Window")
        self.setWindowTitle("FAMILIES")
        self.setGeometry(500, 150, 370, 400)
        self.setFixedSize(370, 400)

        with open("./style.css", "r") as f:
            self.setStyleSheet(f.read())

        self.insert_person_see_families_label = QLabel("FAMILIES", self)
        self.insert_person_see_families_label.setGeometry(200, 30, 100, 50)
        self.insert_person_see_families_label.setObjectName("insert_person_see_families_label")

        self.insert_person_see_families_table = QTableWidget()
        self.insert_person_see_families_table.setObjectName("insert_person_see_families_table")

        self.insert_person_see_families_table.setGeometry(50, 80, 250, 300)
        self.insert_person_see_families_table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.insert_person_see_families_label)
        self.layout.addWidget(self.insert_person_see_families_table)

        self.load_data()

    def load_data(self):
        try:

            query = "SELECT family_id, COUNT(*) AS total_members FROM person GROUP BY family_id;"
            json_data = RunQuery(query)

            data = json_data
            self.display_data(data)
        except Exception as e:
            QMessageBox.warning(self, "Server Error", str(e))

    def display_data(self, data):
        num_rows = len(data)
        num_cols = len(data[0])

        self.insert_person_see_families_table.setRowCount(num_rows)
        self.insert_person_see_families_table.setColumnCount(num_cols + 1)  # Add one more column for the button
        headers = ["Family ID", "Total Members", "Action"]  # Custom headers
        self.insert_person_see_families_table.setHorizontalHeaderLabels(headers)

        self.insert_person_see_families_table.setColumnWidth(1, 100)
        self.insert_person_see_families_table.setColumnWidth(2, 100)
        self.insert_person_see_families_table.setColumnWidth(3, 100)

        for row, row_data in enumerate(data):
            for col, value in enumerate(row_data.values()):
                item = QTableWidgetItem(str(value))
                self.insert_person_see_families_table.setItem(row, col, item)

            # Add button to the last column
            insert_person_family_detail_show_button = QPushButton("Show Details")
            insert_person_family_detail_show_button.setObjectName("insert_person_family_detail_show_button")
            insert_person_family_detail_show_button.clicked.connect(
                lambda _, family_id=row_data['family_id']: self.insert_person_family_detail_show_data(family_id))
            self.insert_person_see_families_table.setCellWidget(row, num_cols, insert_person_family_detail_show_button)

            if row % 2 == 0:
                self.insert_person_see_families_table.item(row, 0).setBackground(custom_color)
                self.insert_person_see_families_table.item(row, 1).setBackground(custom_color)
            else:
                self.insert_person_see_families_table.item(row, 0).setBackground(Qt.GlobalColor.white)
                self.insert_person_see_families_table.item(row, 1).setBackground(Qt.GlobalColor.white)

    def insert_person_family_detail_show_data(self, family_id):
        global insert_person_family_id
        insert_person_family_id = family_id
        self.Insert_person_See_Family_detail_Window = Insert_person_See_Family_detail_Window()
        self.hide()
        self.Insert_person_See_Family_detail_Window.show()


# ################################################
# ###############  PERSON WIDGET  ##############
# ################################################

class insert_person_widget(QWidget):

    def __init__(self):
        super().__init__()
        self.setGeometry(200, 50, 800, 550)

        self.insert_person_label = QLabel("PERSONAL DETAILS", self)
        self.insert_person_label.setObjectName("insert_person_label")
        self.insert_person_label.setGeometry(280, 40, 250, 50)

        self.insert_person_first_name_lineedit = QLineEdit(self)
        self.insert_person_first_name_lineedit.setObjectName("insert_person_first_name_lineedit")
        self.insert_person_first_name_lineedit.setGeometry(160, 130, 200, 30)
        self.insert_person_first_name_lineedit.setPlaceholderText("First Name")

        self.insert_person_last_name_lineedit = QLineEdit(self)
        self.insert_person_last_name_lineedit.setObjectName("insert_person_last_name_lineedit")
        self.insert_person_last_name_lineedit.setGeometry(440, 130, 200, 30)
        self.insert_person_last_name_lineedit.setPlaceholderText("Last Name")

        # ################# INSERT DATE OF BIRTH ##############################

        self.insert_person_dateofbirth_button = QPushButton("DATE OF BIRTH", self)
        self.insert_person_dateofbirth_button.setObjectName("insert_person_dateofbirth_button")
        self.insert_person_dateofbirth_button.setGeometry(160, 180, 200, 30)
        self.insert_person_dateofbirth_button.clicked.connect(self.show_insert_person_dateofbirth_calendar_dialog)

        self.insert_person_placeofbirth_lineedit = QLineEdit(self)
        self.insert_person_placeofbirth_lineedit.setObjectName("insert_person_placeofbirth_lineedit")
        self.insert_person_placeofbirth_lineedit.setGeometry(440, 180, 200, 30)
        self.insert_person_placeofbirth_lineedit.setPlaceholderText("Place of Birth")

        # ################# INSERT GENDER ##############################

        self.insert_person_gender_group = QGroupBox("Gender:", self)
        self.insert_person_gender_group.setObjectName("insert_person_gender_group")
        self.insert_person_gender_group.setGeometry(160, 230, 480, 50)
        self.insert_person_male_radio = QRadioButton("Male")
        self.insert_person_female_radio = QRadioButton("Female")
        self.insert_person_other_radio = QRadioButton("Other")
        self.insert_person_gender_layout = QHBoxLayout()
        self.insert_person_gender_layout.addWidget(self.insert_person_male_radio)
        self.insert_person_gender_layout.addWidget(self.insert_person_female_radio)
        self.insert_person_gender_layout.addWidget(self.insert_person_other_radio)
        self.insert_person_gender_group.setLayout(self.insert_person_gender_layout)

        self.insert_person_nationality_lineedit = QLineEdit(self)
        self.insert_person_nationality_lineedit.setObjectName("insert_person_nationality_lineedit")
        self.insert_person_nationality_lineedit.setGeometry(160, 300, 200, 30)
        self.insert_person_nationality_lineedit.setPlaceholderText("Nationality")

        self.insert_person_cnicno_lineedit = QLineEdit(self)
        self.insert_person_cnicno_lineedit.setObjectName("insert_person_cnicno_lineedit")
        self.insert_person_cnicno_lineedit.setGeometry(440, 300, 200, 30)
        self.insert_person_cnicno_lineedit.setPlaceholderText("CNIC NO")

        self.insert_person_religion_lineedit = QLineEdit(self)
        self.insert_person_religion_lineedit.setObjectName("insert_person_religion_lineedit")
        self.insert_person_religion_lineedit.setGeometry(160, 350, 200, 30)
        self.insert_person_religion_lineedit.setPlaceholderText("Religion")

        self.insert_person_family_id_lineedit = QLineEdit(self)
        self.insert_person_family_id_lineedit.setObjectName("insert_person_family_id_lineedit")
        self.insert_person_family_id_lineedit.setGeometry(440, 350, 90, 30)
        self.insert_person_family_id_lineedit.setPlaceholderText("Family ID")
        self.insert_person_family_id_lineedit.setValidator(QIntValidator())

        self.insert_person_see_family_id_button = QPushButton("See Families", self)
        self.insert_person_see_family_id_button.setObjectName("insert_person_see_family_id_button")
        self.insert_person_see_family_id_button.setGeometry(550, 350, 90, 30)
        self.insert_person_see_family_id_button.clicked.connect(self.insert_person_see_family_id_button_clicked)

        with open("./style.css", "r") as f:
            self.setStyleSheet(f.read())

    def clear_all(self):
        self.insert_person_first_name_lineedit.setText("")
        self.insert_person_last_name_lineedit.setText("")
        self.insert_person_dateofbirth_button.setText("DATE OF BIRTH")
        self.insert_person_placeofbirth_lineedit.setText("")
        self.insert_person_male_radio.setChecked(False)
        self.insert_person_female_radio.setChecked(False)
        self.insert_person_other_radio.setChecked(False)
        self.insert_person_nationality_lineedit.setText("")
        self.insert_person_cnicno_lineedit.setText("")
        self.insert_person_religion_lineedit.setText("")
        self.insert_person_family_id_lineedit.setText("")

    def show_insert_person_dateofbirth_calendar_dialog(self):
        insert_person_dateofbirth_dialog = Insert_person_CalendarDialog(self)
        if insert_person_dateofbirth_dialog.exec() == QDialog.DialogCode.Accepted:
            self.set_calendar_date(self.insert_person_dateofbirth_button,
                                   insert_person_dateofbirth_dialog.insert_person_dateofbirth_calendar)

    def insert_person_see_family_id_button_clicked(self):
        self.insert_person_see_family_id_window = Insert_person_See_Family_ID_Window()
        self.insert_person_see_family_id_window.show()

    def set_calendar_date(self, line_edit, calendar):
        date = calendar.selectedDate()
        self.insert_person_dateofbirth_button.setText(date.toString("yyyy-MM-dd"))


# ################################################
# ###############  CONTACT WIDGET  ###############
# ################################################

class insert_contact_widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 50, 800, 550)
        self.setObjectName("insert_contact_widget")

        self.Phone_Numbers = []
        self.Emails = []

        self.insert_contact_Label = QLabel("CONTACT INFORMATION", self)
        self.insert_contact_Label.setObjectName("insert_contact_Label")
        self.insert_contact_Label.setGeometry(260, 15, 300, 50)

        self.insert_contact_ph_no_widget = QWidget(self)
        self.insert_contact_ph_no_widget.setObjectName("insert_contact_ph_no_widget")
        self.insert_contact_ph_no_widget.setGeometry(50, 80, 340, 400)

        self.insert_contact_email_widget = QWidget(self)
        self.insert_contact_email_widget.setObjectName("insert_contact_email_widget")
        self.insert_contact_email_widget.setGeometry(410, 80, 340, 400)

        self.insert_contact_ph_no_label = QLabel("PHONE NUMBERS", self.insert_contact_ph_no_widget)
        self.insert_contact_ph_no_label.setObjectName("insert_contact_ph_no_label")
        self.insert_contact_ph_no_label.setGeometry(90, 5, 300, 50)

        self.inseret_contact_phone_lineedit = QLineEdit(self.insert_contact_ph_no_widget)
        self.inseret_contact_phone_lineedit.setObjectName("inseret_contact_phone_lineedit")
        self.inseret_contact_phone_lineedit.setGeometry(20, 350, 190, 30)
        self.inseret_contact_phone_lineedit.setPlaceholderText("Phone")
        self.inseret_contact_phone_lineedit.setMaxLength(11)

        self.insert_contact_ph_no_table = QTableWidget(self.insert_contact_ph_no_widget)
        self.insert_contact_ph_no_table.setObjectName("insert_contact_ph_no_table")
        self.insert_contact_ph_no_table.setColumnCount(2)  # Two columns for email and delete button
        self.insert_contact_ph_no_table.setHorizontalHeaderLabels(["Phone No", "Delete"])
        self.insert_contact_ph_no_table.horizontalHeader().setStretchLastSection(True)
        self.insert_contact_ph_no_table.setColumnWidth(0, 200)
        self.insert_contact_ph_no_table.setColumnWidth(1, 30)
        self.insert_contact_ph_no_table.setGeometry(20, 60, 300, 270)
        self.insert_contact_ph_no_table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.insert_contact_ph_no_table.verticalHeader().setDefaultSectionSize(42)
        self.insert_contact_ph_no_table.verticalHeader().setStyleSheet("QHeaderView::section{font-weight: bold;}")
        self.insert_contact_ph_no_table.horizontalHeader().setStyleSheet("QHeaderView::section{font-weight: bold;}")

        self.insert_contact_email_label = QLabel("EMAILS", self.insert_contact_email_widget)
        self.insert_contact_email_label.setObjectName("insert_contact_email_label")
        self.insert_contact_email_label.setGeometry(140, 5, 300, 50)

        self.insert_contact_phone_button = QPushButton("Add Phone", self.insert_contact_ph_no_widget)
        self.insert_contact_phone_button.setObjectName("insert_contact_phone_button")
        self.insert_contact_phone_button.setIcon(QIcon("./Images/add.png"))
        self.insert_contact_phone_button.setIconSize(QSize(20, 20))
        self.insert_contact_phone_button.setGeometry(225, 350, 100, 30)
        self.insert_contact_phone_button.clicked.connect(self.insert_contact_phone_button_clicked)

        self.insert_contact_email_lineedit = QLineEdit(self.insert_contact_email_widget)
        self.insert_contact_email_lineedit.setObjectName("insert_contact_email_lineedit")
        self.insert_contact_email_lineedit.setGeometry(20, 350, 190, 30)
        self.insert_contact_email_lineedit.setPlaceholderText("Email")

        self.insert_contact_email_table = QTableWidget(self.insert_contact_email_widget)
        self.insert_contact_email_table.setObjectName("insert_contact_email_table")
        self.insert_contact_email_table.setColumnCount(2)  # Two columns for email and delete button
        self.insert_contact_email_table.setHorizontalHeaderLabels(["Email", "Delete"])
        self.insert_contact_email_table.horizontalHeader().setStretchLastSection(True)
        self.insert_contact_email_table.setColumnWidth(0, 200)
        self.insert_contact_email_table.setColumnWidth(1, 30)
        self.insert_contact_email_table.setGeometry(20, 60, 300, 270)
        self.insert_contact_email_table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.insert_contact_email_table.verticalHeader().setDefaultSectionSize(42)
        self.insert_contact_email_table.verticalHeader().setStyleSheet("QHeaderView::section{font-weight: bold;}")
        self.insert_contact_email_table.horizontalHeader().setStyleSheet("QHeaderView::section{font-weight: bold;}")

        self.insert_contact_email_button = QPushButton("Add Email", self.insert_contact_email_widget)
        self.insert_contact_email_button.setObjectName("insert_contact_email_button")
        self.insert_contact_email_button.setIcon(QIcon("./Images/add.png"))
        self.insert_contact_email_button.setIconSize(QSize(20, 20))
        self.insert_contact_email_button.setGeometry(225, 350, 100, 30)
        self.insert_contact_email_button.clicked.connect(self.insert_contact_email_button_clicked)

        with open("./style.css", "r") as f:
            self.setStyleSheet(f.read())

    def clear_all(self):
        self.inseret_contact_phone_lineedit.setText("")
        self.insert_contact_email_lineedit.setText("")

    def insert_contact_phone_button_clicked(self):
        try:
            phone = self.inseret_contact_phone_lineedit.text()
            if phone and self.validate_phone(phone):
                self.Phone_Numbers.append(phone)
                self.update_insert_phone_list()
            else:
                QMessageBox.warning(self, "Error", "Invalid phone number")
            self.inseret_contact_phone_lineedit.setText("")
        except Exception as e:
            QMessageBox.warning(self, "Error", str(e))

    def update_insert_phone_list(self):
        self.insert_contact_ph_no_table.setRowCount(0)  # Clear existing rows
        for row, ph_no in enumerate(self.Phone_Numbers):
            self.insert_contact_ph_no_table.insertRow(row)
            self.insert_contact_ph_no_table.setItem(row, 0, QTableWidgetItem(ph_no))

            delete_button_layout = QHBoxLayout()
            delete_button_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

            self.insert_phone_delete_button = QPushButton("X")
            self.insert_phone_delete_button.setFixedSize(25, 25)
            self.insert_phone_delete_button.setGeometry(0, 0, 25, 25)
            self.insert_phone_delete_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
            self.insert_phone_delete_button.setIconSize(QSize(20, 20))  # Set icon size
            self.insert_phone_delete_button.setObjectName("insert_phone_delete_button")
            self.insert_phone_delete_button.clicked.connect(lambda _, row=row: self.delete_insert_phone(row))

            delete_button_layout.addWidget(self.insert_phone_delete_button)
            cell_widget = QWidget()
            cell_widget.setLayout(delete_button_layout)
            self.insert_contact_ph_no_table.setCellWidget(row, 1, cell_widget)

    def delete_insert_phone(self, row):
        del self.Phone_Numbers[row]
        self.update_insert_phone_list()

    def validate_phone(self, phone):
        if len(phone) != 11:
            return False
        for i in phone:
            if not i.isdigit():
                return False
        return True

    # ################################################

    def insert_contact_email_button_clicked(self):
        try:
            email = self.insert_contact_email_lineedit.text()
            if email and self.validate_email(email):
                self.Emails.append(email)
                self.update_insert_email_list()
            else:
                QMessageBox.warning(self, "Error", "Invalid Email Address")
            self.insert_contact_email_lineedit.setText("")
        except Exception as e:
            QMessageBox.warning(self, "Error", str(e))

    def update_insert_email_list(self):
        self.insert_contact_email_table.setRowCount(0)  # Clear existing rows
        for row, email in enumerate(self.Emails):
            self.insert_contact_email_table.insertRow(row)
            self.insert_contact_email_table.setItem(row, 0, QTableWidgetItem(email))

            delete_button_layout = QHBoxLayout()
            delete_button_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

            self.insert_email_delete_button = QPushButton("X")
            self.insert_email_delete_button.setFixedSize(25, 25)
            self.insert_email_delete_button.setGeometry(0, 0, 25, 25)
            self.insert_email_delete_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
            self.insert_email_delete_button.setObjectName("insert_email_delete_button")
            self.insert_email_delete_button.clicked.connect(lambda _, row=row: self.delete_insert_email(row))

            delete_button_layout.addWidget(self.insert_email_delete_button)
            cell_widget = QWidget()
            cell_widget.setLayout(delete_button_layout)
            self.insert_contact_email_table.setCellWidget(row, 1, cell_widget)

    def delete_insert_email(self, row):
        del self.Emails[row]
        self.update_insert_email_list()

    def validate_email(self, email):
        # Regular expression for email validation
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

        # Match the email address with the pattern
        if re.match(pattern, email):
            return True
        else:
            return False


# ################################################
# ###############  ADDRESS WIDGET  ###############
# ################################################

class insert_addresses_widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 50, 800, 550)
        self.setObjectName("insert_addresses_widget")

        self.INSERT_Addresses = []

        self.Address_Label = QLabel("ADDRESSES INFORMATION", self)
        self.Address_Label.setObjectName("insert_address_Label")
        self.Address_Label.setGeometry(250, 15, 330, 50)

        self.insert_address_sub_widget = QWidget(self)
        self.insert_address_sub_widget.setObjectName("insert_address_sub_widget")
        self.insert_address_sub_widget.setGeometry(25, 80, 750, 420)

        self.insert_address_table_widget = QTableWidget(self.insert_address_sub_widget)
        self.insert_address_table_widget.setObjectName("insert_address_table_widget")
        self.insert_address_table_widget.setGeometry(20, 20, 710, 210)
        self.insert_address_table_widget.setColumnCount(8)
        self.insert_address_table_widget.setHorizontalHeaderLabels([
            "Address",
            "City",
            "State",
            "Country",
            "Status",
            "Date In",
            "Date Out",
            "Delete"
        ])

        self.insert_address_table_widget.horizontalHeader().setStretchLastSection(True)
        self.insert_address_table_widget.verticalHeader().setStyleSheet(
            "QHeaderView::section{font-weight: bold;}")
        self.insert_address_table_widget.horizontalHeader().setStyleSheet(
            "QHeaderView::section{font-weight: bold;}")

        self.insert_address_table_widget.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)

        # self.insert_address_table_widget.horizontalHeader().setStretchLastSection(True)
        self.insert_address_table_widget.setColumnWidth(0, 200)
        self.insert_address_table_widget.setColumnWidth(1, 90)
        self.insert_address_table_widget.setColumnWidth(2, 70)
        self.insert_address_table_widget.setColumnWidth(3, 70)
        self.insert_address_table_widget.setColumnWidth(4, 50)
        self.insert_address_table_widget.setColumnWidth(5, 70)
        self.insert_address_table_widget.setColumnWidth(6, 70)
        self.insert_address_table_widget.setColumnWidth(7, 45)

        self.insert_address_addr_lineedit = QLineEdit(self.insert_address_sub_widget)
        self.insert_address_addr_lineedit.setObjectName("insert_address_addr_lineedit")
        self.insert_address_addr_lineedit.setGeometry(50, 250, 390, 30)
        self.insert_address_addr_lineedit.setPlaceholderText("Address")

        self.insert_address_city_lineedit = QLineEdit(self.insert_address_sub_widget)
        self.insert_address_city_lineedit.setObjectName("insert_address_city_lineedit")
        self.insert_address_city_lineedit.setGeometry(468, 250, 180, 30)
        self.insert_address_city_lineedit.setPlaceholderText("City")

        self.insert_address_state_lineedit = QLineEdit(self.insert_address_sub_widget)
        self.insert_address_state_lineedit.setObjectName("insert_address_state_lineedit")
        self.insert_address_state_lineedit.setGeometry(50, 300, 180, 30)
        self.insert_address_state_lineedit.setPlaceholderText("State")

        self.insert_address_country_lineedit = QLineEdit(self.insert_address_sub_widget)
        self.insert_address_country_lineedit.setObjectName("insert_address_country_lineedit")
        self.insert_address_country_lineedit.setGeometry(258, 300, 180, 30)
        self.insert_address_country_lineedit.setPlaceholderText("Country")

        self.insert_address_status_combobox = QComboBox(self.insert_address_sub_widget)
        self.insert_address_status_combobox.setObjectName("insert_address_status_combobox")
        self.insert_address_status_combobox.setGeometry(468, 300, 180, 30)
        self.insert_address_status_combobox.addItem("Living")
        self.insert_address_status_combobox.addItem("Leaved")
        self.insert_address_status_combobox.currentIndexChanged.connect(self.update_address_status)

        self.insert_address_date_in_button = QPushButton(self.insert_address_sub_widget)
        self.insert_address_date_in_button.setObjectName("insert_address_date_in_button")
        self.insert_address_date_in_button.setGeometry(50, 350, 180, 30)
        self.insert_address_date_in_button.setText("Date In")
        self.insert_address_date_in_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.insert_address_date_in_button.clicked.connect(self.show_insert_address_date_in_calendar_dialog)

        self.insert_address_date_out_button = QPushButton(self.insert_address_sub_widget)
        self.insert_address_date_out_button.setObjectName("insert_address_date_out_button")
        self.insert_address_date_out_button.setGeometry(258, 350, 180, 30)
        self.insert_address_date_out_button.setText("Date Out")
        self.insert_address_date_out_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.insert_address_date_out_button.clicked.connect(self.show_insert_address_date_out_calendar_dialog)
        self.insert_address_date_out_button.setEnabled(False)

        self.insert_address_add_button = QPushButton(self.insert_address_sub_widget)
        self.insert_address_add_button.setObjectName("insert_address_add_button")
        self.insert_address_add_button.setText("Add")
        self.insert_address_add_button.setIcon(QIcon("./Images/add.png"))
        self.insert_address_add_button.setIconSize(QSize(20, 20))
        self.insert_address_add_button.setGeometry(468, 350, 180, 30)
        self.insert_address_add_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.insert_address_add_button.clicked.connect(self.insert_address_data)

        with open("./style.css", "r") as f:
            self.setStyleSheet(f.read())

    def update_address_status(self):
        if self.insert_address_status_combobox.currentText() == "Living":
            self.insert_address_date_out_button.setEnabled(False)
            self.insert_address_date_out_button.setText("Date Out")
        else:
            self.insert_address_date_out_button.setEnabled(True)

    def show_insert_address_date_in_calendar_dialog(self):
        insert_address_date_in_dialog = Insert_address_date_CalendarDialog(self.insert_address_date_in_button)
        insert_address_date_in_dialog.exec()

    def show_insert_address_date_out_calendar_dialog(self):
        insert_address_date_out_dialog = Insert_address_date_CalendarDialog(self.insert_address_date_out_button)
        insert_address_date_out_dialog.exec()

    def insert_address_data(self):
        address = self.insert_address_addr_lineedit.text()
        city = self.insert_address_city_lineedit.text()
        state = self.insert_address_state_lineedit.text()
        country = self.insert_address_country_lineedit.text()
        address_status = self.insert_address_status_combobox.currentText()
        date_in = self.insert_address_date_in_button.text()
        date_out = self.insert_address_date_out_button.text()

        if address_status == 'Living':
            date_out = "None"

        addr_data = [
            address,
            city,
            state,
            country,
            address_status,
            date_in,
            date_out
        ]

        try:
            if self.address_validate(addr_data):
                self.INSERT_Addresses.append(addr_data)
                self.update_address_data_list()
                self.clear_all()
            else:
                QMessageBox.warning(self, "Error", "All Fields are required")
        except Exception as e:
            QMessageBox.warning(self, "Error", str(e))

    def address_validate(self, addr_data):
        for data in addr_data:
            if data == "" or data == "Date In" or data == "Date Out":
                return False
        return True

    def clear_all(self):
        self.insert_address_addr_lineedit.clear()
        self.insert_address_city_lineedit.clear()
        self.insert_address_state_lineedit.clear()
        self.insert_address_country_lineedit.clear()
        self.insert_address_date_in_button.setText("Date In")
        self.insert_address_date_out_button.setText("Date Out")
        self.insert_address_status_combobox.setCurrentIndex(0)

    def update_address_data_list(self):
        self.insert_address_table_widget.setRowCount(len(self.INSERT_Addresses))
        for row, data_entry in enumerate(self.INSERT_Addresses):
            for col, value in enumerate(data_entry):
                item = QTableWidgetItem(value)
                self.insert_address_table_widget.setItem(row, col, item)

            # Add delete button to each row
            self.delete_address_button = QPushButton("X")
            self.delete_address_button.setFixedSize(30, 30)
            self.delete_address_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
            self.delete_address_button.setObjectName("delete_address_button")
            self.delete_address_button.clicked.connect(lambda _, row=row: self.delete_address_data(row))
            self.insert_address_table_widget.setCellWidget(row, len(data_entry), self.delete_address_button)

    def delete_address_data(self, row):
        del self.INSERT_Addresses[row]
        self.update_address_data_list()


# ################################################
# ##############  EDUCATION WIDGET  ##############
# ################################################

class insert_education_widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("insert_education_widget")
        self.setGeometry(200, 50, 800, 550)

        self.INSERT_Education = []

        self.Education_Label = QLabel("EDUCATIONAL INFORMATION", self)
        self.Education_Label.setObjectName("insert_Education_Label")
        self.Education_Label.setGeometry(220, 15, 360, 50)

        self.insert_education_sub_widget = QWidget(self)
        self.insert_education_sub_widget.setObjectName("insert_education_sub_widget")
        self.insert_education_sub_widget.setGeometry(50, 80, 700, 420)

        self.insert_education_table_widget = QTableWidget(self.insert_education_sub_widget)
        self.insert_education_table_widget.setObjectName("insert_education_table_widget")
        self.insert_education_table_widget.setGeometry(20, 20, 660, 210)
        self.insert_education_table_widget.setColumnCount(7)
        self.insert_education_table_widget.setHorizontalHeaderLabels([
            "Degree",
            "Institute",
            "Reg ID",
            "Start Date",
            "End Date",
            "Status",
            "Delete"
        ])
        self.insert_education_table_widget.horizontalHeader().setStretchLastSection(True)
        self.insert_education_table_widget.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.insert_education_table_widget.setColumnWidth(0, 125)
        self.insert_education_table_widget.setColumnWidth(1, 160)
        self.insert_education_table_widget.setColumnWidth(2, 80)
        self.insert_education_table_widget.setColumnWidth(3, 70)
        self.insert_education_table_widget.setColumnWidth(4, 70)
        self.insert_education_table_widget.setColumnWidth(5, 70)
        self.insert_education_table_widget.setColumnWidth(6, 40)

        self.insert_education_table_widget.verticalHeader().setStyleSheet("QHeaderView::section{font-weight: bold;}")
        self.insert_education_table_widget.horizontalHeader().setStyleSheet("QHeaderView::section{font-weight: bold;}")

        self.insert_education_deg_lineedit = QLineEdit(self.insert_education_sub_widget)
        self.insert_education_deg_lineedit.setObjectName("insert_education_deg_lineedit")
        self.insert_education_deg_lineedit.setGeometry(50, 250, 180, 30)
        self.insert_education_deg_lineedit.setPlaceholderText("Degree")

        self.insert_education_institute_lineedit = QLineEdit(self.insert_education_sub_widget)
        self.insert_education_institute_lineedit.setObjectName("insert_education_institute_lineedit")
        self.insert_education_institute_lineedit.setGeometry(258, 250, 390, 30)
        self.insert_education_institute_lineedit.setPlaceholderText("Institute")

        self.insert_education_reg_id_lineedit = QLineEdit(self.insert_education_sub_widget)
        self.insert_education_reg_id_lineedit.setObjectName("insert_education_reg_id_lineedit")
        self.insert_education_reg_id_lineedit.setGeometry(50, 300, 180, 30)
        self.insert_education_reg_id_lineedit.setPlaceholderText("Registration ID")

        self.insert_education_start_date_button = QPushButton(self.insert_education_sub_widget)
        self.insert_education_start_date_button.setObjectName("insert_education_start_date_button")
        self.insert_education_start_date_button.setGeometry(258, 300, 180, 30)
        self.insert_education_start_date_button.setText("Start Date")
        self.insert_education_start_date_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.insert_education_start_date_button.clicked.connect(self.show_insert_education_start_date_calendar_dialog)

        self.insert_education_end_date_button = QPushButton(self.insert_education_sub_widget)
        self.insert_education_end_date_button.setObjectName("insert_education_end_date_button")
        self.insert_education_end_date_button.setGeometry(468, 300, 180, 30)
        self.insert_education_end_date_button.setText("End Date")
        self.insert_education_end_date_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.insert_education_end_date_button.clicked.connect(self.show_insert_education_end_date_calendar_dialog)
        self.insert_education_end_date_button.setEnabled(True)

        self.insert_education_status_combobox = QComboBox(self.insert_education_sub_widget)
        self.insert_education_status_combobox.setObjectName("insert_education_status_combobox")
        self.insert_education_status_combobox.setGeometry(50, 350, 180, 30)
        self.insert_education_status_combobox.addItem("Completed")
        self.insert_education_status_combobox.addItem("In Progress")
        self.insert_education_status_combobox.addItem("Withdrawn")
        self.insert_education_status_combobox.addItem("Expelled")
        self.insert_education_status_combobox.setCurrentIndex(0)
        self.insert_education_status_combobox.currentIndexChanged.connect(self.update_education_status)

        self.insert_education_add_button = QPushButton(self.insert_education_sub_widget)
        self.insert_education_add_button.setObjectName("insert_education_add_button")
        self.insert_education_add_button.setText("Add")
        self.insert_education_add_button.setIcon(QIcon("./Images/add.png"))
        self.insert_education_add_button.setIconSize(QSize(20, 20))
        self.insert_education_add_button.setGeometry(468, 350, 180, 30)
        self.insert_education_add_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.insert_education_add_button.clicked.connect(self.insert_education_data)

        with open("./style.css", "r") as f:
            self.setStyleSheet(f.read())

    def update_education_status(self):
        if self.insert_education_status_combobox.currentText() == "In Progress":
            self.insert_education_end_date_button.setEnabled(False)
            self.insert_education_end_date_button.setText("End Date")
        else:
            self.insert_education_end_date_button.setEnabled(True)

    def show_insert_education_end_date_calendar_dialog(self):
        insert_edu_date_end_dialog = Insert_address_date_CalendarDialog(self.insert_education_end_date_button)
        insert_edu_date_end_dialog.exec()

    def show_insert_education_start_date_calendar_dialog(self):
        insert_edu_date_end_dialog = Insert_address_date_CalendarDialog(self.insert_education_start_date_button)
        insert_edu_date_end_dialog.exec()

    def insert_education_data(self):
        degree = self.insert_education_deg_lineedit.text()
        institute = self.insert_education_institute_lineedit.text()
        reg_id = self.insert_education_reg_id_lineedit.text()
        start_date = self.insert_education_start_date_button.text()
        end_date = self.insert_education_end_date_button.text()
        status = self.insert_education_status_combobox.currentText()

        if end_date == "End Date":
            end_date = "None"

        edu_data = [
            degree,
            institute,
            reg_id,
            start_date,
            end_date,
            status
        ]

        try:
            if self.edu_validate(edu_data):
                self.INSERT_Education.append(edu_data)
                self.update_edu_data_list()
                self.clear_all()
            else:
                QMessageBox.warning(self, "Error", "All Fields are required")
        except Exception as e:
            QMessageBox.warning(self, "Error", str(e))

    def clear_all(self):
        self.insert_education_deg_lineedit.clear()
        self.insert_education_institute_lineedit.clear()
        self.insert_education_reg_id_lineedit.clear()
        self.insert_education_start_date_button.setText("Start Date")
        self.insert_education_end_date_button.setText("End Date")
        self.insert_education_status_combobox.setCurrentIndex(0)

    def edu_validate(self, edu_data):
        for data in edu_data:
            if data == "" or data == "Start Date" or data == "End Date":
                return False  # False
        return True

    def update_edu_data_list(self):
        self.insert_education_table_widget.setRowCount(len(self.INSERT_Education))
        for row, data_entry in enumerate(self.INSERT_Education):
            for col, value in enumerate(data_entry):
                item = QTableWidgetItem(value)
                self.insert_education_table_widget.setItem(row, col, item)

            # Add delete button to each row
            self.delete_edu_button = QPushButton("X")
            self.delete_edu_button.setFixedSize(30, 30)
            self.delete_edu_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
            self.delete_edu_button.setObjectName("delete_edu_button")
            self.delete_edu_button.clicked.connect(lambda _, row=row: self.delete_edu_data(row))
            self.insert_education_table_widget.setCellWidget(row, len(data_entry), self.delete_edu_button)

    def delete_edu_data(self, row):
        del self.INSERT_Education[row]
        self.update_edu_data_list()


# ################################################
# #############  EMPLOYMENT WIDGET  #############
# ################################################

class insert_employment_widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("insert_employment_widget")
        self.setGeometry(200, 50, 800, 550)

        self.INSERT_Employment = []

        self.Employment_Label = QLabel("EMPLOYMENT INFORMATION", self)
        self.Employment_Label.setObjectName("insert_Employment_Label")
        self.Employment_Label.setGeometry(220, 15, 360, 50)

        self.insert_employment_sub_widget = QWidget(self)
        self.insert_employment_sub_widget.setObjectName("insert_employment_sub_widget")
        self.insert_employment_sub_widget.setGeometry(25, 80, 750, 420)

        self.insert_employment_table_widget = QTableWidget(self.insert_employment_sub_widget)
        self.insert_employment_table_widget.setObjectName("insert_employment_table_widget")
        self.insert_employment_table_widget.setGeometry(20, 20, 710, 210)
        self.insert_employment_table_widget.setColumnCount(8)
        self.insert_employment_table_widget.setHorizontalHeaderLabels([
            "Job Name",
            "Job ID",
            "Company",
            "Company Address",
            "Hire Date",
            "Leaving Date",
            "Status",
            "Delete"
        ])
        self.insert_employment_table_widget.horizontalHeader().setStretchLastSection(True)
        self.insert_employment_table_widget.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.insert_employment_table_widget.setColumnWidth(0, 70)
        self.insert_employment_table_widget.setColumnWidth(1, 90)
        self.insert_employment_table_widget.setColumnWidth(2, 125)
        self.insert_employment_table_widget.setColumnWidth(3, 130)
        self.insert_employment_table_widget.setColumnWidth(4, 70)
        self.insert_employment_table_widget.setColumnWidth(5, 80)
        self.insert_employment_table_widget.setColumnWidth(6, 70)
        self.insert_employment_table_widget.setColumnWidth(7, 35)

        self.insert_employment_table_widget.verticalHeader().setStyleSheet("QHeaderView::section{font-weight: bold;}")
        self.insert_employment_table_widget.horizontalHeader().setStyleSheet("QHeaderView::section{font-weight: bold;}")

        self.insert_employment_job_name_lineedit = QLineEdit(self.insert_employment_sub_widget)
        self.insert_employment_job_name_lineedit.setObjectName("insert_employment_job_name_lineedit")
        self.insert_employment_job_name_lineedit.setGeometry(75, 250, 180, 30)
        self.insert_employment_job_name_lineedit.setPlaceholderText("Job Name")

        self.insert_employment_job_id_lineedit = QLineEdit(self.insert_employment_sub_widget)
        self.insert_employment_job_id_lineedit.setObjectName("insert_employment_job_id_lineedit")
        self.insert_employment_job_id_lineedit.setGeometry(283, 250, 180, 30)
        self.insert_employment_job_id_lineedit.setPlaceholderText("Job ID")

        self.insert_employment_Company_lineedit = QLineEdit(self.insert_employment_sub_widget)
        self.insert_employment_Company_lineedit.setObjectName("insert_employment_Company_lineedit")
        self.insert_employment_Company_lineedit.setGeometry(493, 250, 180, 30)
        self.insert_employment_Company_lineedit.setPlaceholderText("Company")

        self.insert_employment_company_address_lineedit = QLineEdit(self.insert_employment_sub_widget)
        self.insert_employment_company_address_lineedit.setObjectName("insert_employment_company_address_lineedit")
        self.insert_employment_company_address_lineedit.setGeometry(75, 300, 390, 30)
        self.insert_employment_company_address_lineedit.setPlaceholderText("Company Address")

        self.insert_employment_status_combobox = QComboBox(self.insert_employment_sub_widget)
        self.insert_employment_status_combobox.setObjectName("insert_employment_status_combobox")
        self.insert_employment_status_combobox.setGeometry(493, 300, 180, 30)
        self.insert_employment_status_combobox.addItem("Current")
        self.insert_employment_status_combobox.addItem("Past")
        self.insert_employment_status_combobox.addItem("On leave")
        self.insert_employment_status_combobox.addItem("Terminated")
        self.insert_employment_status_combobox.addItem("Resigned")
        self.insert_employment_status_combobox.addItem("Retired")
        self.insert_employment_status_combobox.addItem("Suspended")
        self.insert_employment_status_combobox.addItem("Contract Ended")
        self.insert_employment_status_combobox.setCurrentIndex(0)
        self.insert_employment_status_combobox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.insert_employment_status_combobox.currentIndexChanged.connect(self.update_employment_status)

        self.insert_employment_start_date_button = QPushButton(self.insert_employment_sub_widget)
        self.insert_employment_start_date_button.setObjectName("insert_employment_start_date_button")
        self.insert_employment_start_date_button.setGeometry(75, 350, 180, 30)
        self.insert_employment_start_date_button.setText("Hire Date")
        self.insert_employment_start_date_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.insert_employment_start_date_button.clicked.connect(self.show_insert_employment_start_date_calendar_dialog)

        self.insert_employment_leaving_date_button = QPushButton(self.insert_employment_sub_widget)
        self.insert_employment_leaving_date_button.setObjectName("insert_employment_leaving_date_button")
        self.insert_employment_leaving_date_button.setGeometry(283, 350, 180, 30)
        self.insert_employment_leaving_date_button.setText("Leaving Date")
        self.insert_employment_leaving_date_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.insert_employment_leaving_date_button.clicked.connect(self.show_insert_employment_end_date_calendar_dialog)
        self.insert_employment_leaving_date_button.setEnabled(False)

        self.insert_employment_add_button = QPushButton(self.insert_employment_sub_widget)
        self.insert_employment_add_button.setObjectName("insert_employment_add_button")
        self.insert_employment_add_button.setText("Add")
        self.insert_employment_add_button.setIcon(QIcon("./Images/add.png"))
        self.insert_employment_add_button.setIconSize(QSize(20, 20))
        self.insert_employment_add_button.setGeometry(493, 350, 180, 30)
        self.insert_employment_add_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.insert_employment_add_button.clicked.connect(self.insert_employment_data)

        with open("./style.css", "r") as f:
            self.setStyleSheet(f.read())

    def update_employment_status(self):
        if self.insert_employment_status_combobox.currentText() == "Current":
            self.insert_employment_leaving_date_button.setEnabled(False)
            self.insert_employment_leaving_date_button.setText("Leaving Date")
        else:
            self.insert_employment_leaving_date_button.setEnabled(True)

    def show_insert_employment_end_date_calendar_dialog(self):
        insert_emp_date_end_dialog = Insert_address_date_CalendarDialog(self.insert_employment_leaving_date_button)
        insert_emp_date_end_dialog.exec()

    def show_insert_employment_start_date_calendar_dialog(self):
        insert_emp_date_end_dialog = Insert_address_date_CalendarDialog(self.insert_employment_start_date_button)
        insert_emp_date_end_dialog.exec()

    def insert_employment_data(self):
        job_name = self.insert_employment_job_name_lineedit.text()
        job_id = self.insert_employment_job_id_lineedit.text()
        company = self.insert_employment_Company_lineedit.text()
        company_address = self.insert_employment_company_address_lineedit.text()
        hire_date = self.insert_employment_start_date_button.text()
        leaving_date = self.insert_employment_leaving_date_button.text()
        status = self.insert_employment_status_combobox.currentText()

        if leaving_date == "Leaving Date":
            leaving_date = "None"

        emp_data = [
            job_name,
            job_id,
            company,
            company_address,
            hire_date,
            leaving_date,
            status
        ]

        try:
            if self.emp_validate(emp_data):
                self.INSERT_Employment.append(emp_data)
                self.update_emp_data_list()
                self.clear_all()
            else:
                QMessageBox.warning(self, "Error", "All Fields are required")
        except Exception as e:
            QMessageBox.warning(self, "Error", str(e))

    def clear_all(self):
        self.insert_employment_job_name_lineedit.clear()
        self.insert_employment_job_id_lineedit.clear()
        self.insert_employment_Company_lineedit.clear()
        self.insert_employment_company_address_lineedit.clear()
        self.insert_employment_start_date_button.setText("Hire Date")
        self.insert_employment_leaving_date_button.setText("Leaving Date")
        self.insert_employment_status_combobox.setCurrentIndex(0)

    def emp_validate(self, emp_data):
        for data in emp_data:
            if data == "" or data == "Hire Date" or data == "Leaving Date":
                return False
        return True

    def update_emp_data_list(self):
        self.insert_employment_table_widget.setRowCount(len(self.INSERT_Employment))
        for row, data_entry in enumerate(self.INSERT_Employment):
            for col, value in enumerate(data_entry):
                item = QTableWidgetItem(value)
                self.insert_employment_table_widget.setItem(row, col, item)

            # Add delete button to each row
            self.delete_emp_button = QPushButton("X")
            self.delete_emp_button.setFixedSize(30, 30)
            self.delete_emp_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
            self.delete_emp_button.setObjectName("delete_emp_button")
            self.delete_emp_button.clicked.connect(lambda _, row=row: self.delete_emp_data(row))
            self.insert_employment_table_widget.setCellWidget(row, len(data_entry), self.delete_emp_button)

    def delete_emp_data(self, row):
        del self.INSERT_Employment[row]
        self.update_emp_data_list()

    def get_employment_data(self):
        return self.INSERT_Employment


# ################################################
# ###############  PROPERTY WIDGET  ##############
# ################################################

class insert_property_widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("insert_property_widget")
        self.setGeometry(200, 50, 800, 550)

        self.insert_Property_Label = QLabel("PROPERTY INFORMATION", self)
        self.insert_Property_Label.setObjectName("insert_Property_Label")
        self.insert_Property_Label.setGeometry(250, 15, 360, 50)

        self.INSERT_Property = []

        self.insert_property_sub_widget = QWidget(self)
        self.insert_property_sub_widget.setObjectName("insert_property_sub_widget")
        self.insert_property_sub_widget.setGeometry(25, 80, 750, 420)

        self.insert_property_table_widget = QTableWidget(self.insert_property_sub_widget)
        self.insert_property_table_widget.setObjectName("insert_property_table_widget")
        self.insert_property_table_widget.setGeometry(20, 20, 710, 210)
        self.insert_property_table_widget.setColumnCount(8)
        self.insert_property_table_widget.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.insert_property_table_widget.setHorizontalHeaderLabels([
            "Property Type",
            "Address",
            "Reg ID",
            "Buy Date",
            "Selling Date",
            "Status",
            "Value Price",
            "Delete"
        ])

        self.insert_property_table_widget.horizontalHeader().setStretchLastSection(True)
        self.insert_property_table_widget.setColumnWidth(0, 100)
        self.insert_property_table_widget.setColumnWidth(1, 130)
        self.insert_property_table_widget.setColumnWidth(2, 80)
        self.insert_property_table_widget.setColumnWidth(3, 80)
        self.insert_property_table_widget.setColumnWidth(4, 80)
        self.insert_property_table_widget.setColumnWidth(5, 80)
        self.insert_property_table_widget.setColumnWidth(6, 80)
        self.insert_property_table_widget.setColumnWidth(7, 40)
        self.insert_property_table_widget.verticalHeader().setStyleSheet("QHeaderView::section{font-weight: bold;}")
        self.insert_property_table_widget.horizontalHeader().setStyleSheet("QHeaderView::section{font-weight: bold;}")

        self.insert_property_type_lineedit = QLineEdit(self.insert_property_sub_widget)
        self.insert_property_type_lineedit.setObjectName("insert_property_type_lineedit")
        self.insert_property_type_lineedit.setGeometry(75, 250, 180, 30)
        self.insert_property_type_lineedit.setPlaceholderText("Property Type")

        self.insert_property_address_lineedit = QLineEdit(self.insert_property_sub_widget)
        self.insert_property_address_lineedit.setObjectName("insert_property_address_lineedit")
        self.insert_property_address_lineedit.setGeometry(283, 250, 390, 30)
        self.insert_property_address_lineedit.setPlaceholderText("Address")

        self.insert_property_reg_id_lineedit = QLineEdit(self.insert_property_sub_widget)
        self.insert_property_reg_id_lineedit.setObjectName("insert_property_reg_id_lineedit")
        self.insert_property_reg_id_lineedit.setGeometry(75, 300, 180, 30)
        self.insert_property_reg_id_lineedit.setPlaceholderText("Registration ID")

        self.insert_property_buy_date_button = QPushButton(self.insert_property_sub_widget)
        self.insert_property_buy_date_button.setObjectName("insert_property_buy_date_button")
        self.insert_property_buy_date_button.setGeometry(283, 300, 180, 30)
        self.insert_property_buy_date_button.setText("Buy Date")
        self.insert_property_buy_date_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.insert_property_buy_date_button.clicked.connect(self.show_insert_property_buy_date_calendar_dialog)

        self.insert_property_sell_date_button = QPushButton(self.insert_property_sub_widget)
        self.insert_property_sell_date_button.setObjectName("insert_property_sell_date_button")
        self.insert_property_sell_date_button.setGeometry(493, 300, 180, 30)
        self.insert_property_sell_date_button.setText("Selling Date")
        self.insert_property_sell_date_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.insert_property_sell_date_button.clicked.connect(self.show_insert_property_sell_date_calendar_dialog)
        self.insert_property_sell_date_button.setDisabled(True)

        self.insert_property_status_combobox = QComboBox(self.insert_property_sub_widget)
        self.insert_property_status_combobox.setObjectName("insert_property_status_combobox")
        self.insert_property_status_combobox.setGeometry(75, 350, 180, 30)
        self.insert_property_status_combobox.addItem("Owned")
        self.insert_property_status_combobox.addItem("Sold")
        self.insert_property_status_combobox.currentIndexChanged.connect(self.update_property_status)

        self.insert_property_value_price_lineedit = QLineEdit(self.insert_property_sub_widget)
        self.insert_property_value_price_lineedit.setObjectName("insert_property_value_price_lineedit")
        self.insert_property_value_price_lineedit.setGeometry(283, 350, 180, 30)
        self.insert_property_value_price_lineedit.setPlaceholderText("Value Price")
        self.insert_property_value_price_lineedit.setValidator(QIntValidator())

        self.insert_property_add_button = QPushButton("Add", self.insert_property_sub_widget)
        self.insert_property_add_button.setObjectName("insert_property_add_button")
        self.insert_property_add_button.setGeometry(493, 350, 180, 30)
        self.insert_property_add_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.insert_property_add_button.clicked.connect(self.add_property)

        with open("./style.css", "r") as f:
            self.setStyleSheet(f.read())

    def update_property_status(self):
        if self.insert_property_status_combobox.currentText() == "Owned":
            self.insert_property_sell_date_button.setDisabled(True)
            self.insert_property_sell_date_button.setText("Selling Date")
        else:
            self.insert_property_sell_date_button.setEnabled(True)

    def show_insert_property_buy_date_calendar_dialog(self):
        insert_property_buy_date_end_dialog = Insert_address_date_CalendarDialog(self.insert_property_buy_date_button)
        insert_property_buy_date_end_dialog.exec()

    def show_insert_property_sell_date_calendar_dialog(self):
        insert_property_sell_date_end_dialog = Insert_address_date_CalendarDialog(self.insert_property_sell_date_button)
        insert_property_sell_date_end_dialog.exec()

    def add_property(self):
        property_type = self.insert_property_type_lineedit.text()
        address = self.insert_property_address_lineedit.text()
        reg_id = self.insert_property_reg_id_lineedit.text()
        buy_date = self.insert_property_buy_date_button.text()
        sell_date = self.insert_property_sell_date_button.text()
        status = self.insert_property_status_combobox.currentText()
        value_price = self.insert_property_value_price_lineedit.text()

        if sell_date == "Selling Date":
            sell_date = "None"

        property_data = [
            property_type,
            address,
            reg_id,
            buy_date,
            sell_date,
            status,
            value_price
        ]

        try:
            if self.validate_property(property_data):
                self.INSERT_Property.append(property_data)
                self.update_property_table()
                self.clear_all()
            else:
                QMessageBox.warning(self, "Error", "All fields are required")
        except Exception as e:
            QMessageBox.warning(self, "Error", str(e))

    def clear_all(self):
        self.insert_property_type_lineedit.clear()
        self.insert_property_address_lineedit.clear()
        self.insert_property_reg_id_lineedit.clear()
        self.insert_property_buy_date_button.setText("Buy Date")
        self.insert_property_sell_date_button.setText("Selling Date")
        self.insert_property_status_combobox.setCurrentIndex(0)
        self.insert_property_value_price_lineedit.clear()

    def validate_property(self, property_data):
        for data in property_data:
            if data == "" or data == "Buy Date":
                return False
        return True

    def update_property_table(self):
        self.insert_property_table_widget.setRowCount(len(self.INSERT_Property))
        for row, data_entry in enumerate(self.INSERT_Property):
            for col, value in enumerate(data_entry):
                item = QTableWidgetItem(value)
                self.insert_property_table_widget.setItem(row, col, item)

            # Add delete button to each row
            self.insert_property_delete_button = QPushButton("X")
            self.insert_property_delete_button.setFixedSize(30, 30)
            self.insert_property_delete_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
            self.insert_property_delete_button.setObjectName("insert_property_delete_button")
            self.insert_property_delete_button.clicked.connect(lambda _, row=row: self.delete_property(row))
            self.insert_property_table_widget.setCellWidget(row, len(data_entry), self.insert_property_delete_button)

    def delete_property(self, row):
        del self.INSERT_Property[row]
        self.update_property_table()

    def get_property_data(self):
        return self.INSERT_Property


# ################################################
# ##############  VEHICLES WIDGET  ##############
# ################################################

class insert_vehicle_widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("insert_vehicle_widget")
        self.setGeometry(200, 50, 800, 550)

        self.insert_vehicle_label = QLabel("VEHICLE INFORMATION", self)
        self.insert_vehicle_label.setObjectName("insert_vehicle_label")
        self.insert_vehicle_label.setGeometry(260, 15, 360, 50)

        self.INSERT_Vehicle = []

        self.insert_vehicle_sub_widget = QWidget(self)
        self.insert_vehicle_sub_widget.setObjectName("insert_vehicle_sub_widget")
        self.insert_vehicle_sub_widget.setGeometry(75, 80, 650, 420)

        self.insert_vehicle_table_widget = QTableWidget(self.insert_vehicle_sub_widget)
        self.insert_vehicle_table_widget.setObjectName("insert_vehicle_table_widget")
        self.insert_vehicle_table_widget.setGeometry(45, 30, 560, 210)
        self.insert_vehicle_table_widget.setColumnCount(6)
        self.insert_vehicle_table_widget.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.insert_vehicle_table_widget.setHorizontalHeaderLabels([
            "Maker",
            "Name",
            "Year",
            "Color",
            "Reg Number",
            "Delete"
        ])

        self.insert_vehicle_table_widget.horizontalHeader().setStretchLastSection(True)
        self.insert_vehicle_table_widget.setColumnWidth(0, 100)
        self.insert_vehicle_table_widget.setColumnWidth(1, 130)
        self.insert_vehicle_table_widget.setColumnWidth(2, 80)
        self.insert_vehicle_table_widget.setColumnWidth(3, 80)
        self.insert_vehicle_table_widget.setColumnWidth(4, 90)
        self.insert_vehicle_table_widget.setColumnWidth(5, 40)
        self.insert_vehicle_table_widget.verticalHeader().setStyleSheet("QHeaderView::section{font-weight: bold;}")
        self.insert_vehicle_table_widget.horizontalHeader().setStyleSheet("QHeaderView::section{font-weight: bold;}")

        self.insert_vehicle_maker_lineedit = QLineEdit(self.insert_vehicle_sub_widget)
        self.insert_vehicle_maker_lineedit.setObjectName("insert_vehicle_maker_lineedit")
        self.insert_vehicle_maker_lineedit.setGeometry(50, 280, 180, 30)
        self.insert_vehicle_maker_lineedit.setPlaceholderText("Vehicle Maker")

        self.insert_vehicle_name_lineedit = QLineEdit(self.insert_vehicle_sub_widget)
        self.insert_vehicle_name_lineedit.setObjectName("insert_vehicle_name_lineedit")
        self.insert_vehicle_name_lineedit.setGeometry(260, 280, 180, 30)
        self.insert_vehicle_name_lineedit.setPlaceholderText("Vehicle Name")

        self.insert_vehicle_year_Button = QPushButton(self.insert_vehicle_sub_widget)
        self.insert_vehicle_year_Button.setObjectName("insert_vehicle_year_button")
        self.insert_vehicle_year_Button.setGeometry(470, 280, 125, 30)
        self.insert_vehicle_year_Button.setText("Registration Date")
        self.insert_vehicle_year_Button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.insert_vehicle_year_Button.clicked.connect(self.show_insert_vehicle_reg_date_calendar_dialog)

        self.insert_vehicle_color_lineedit = QLineEdit(self.insert_vehicle_sub_widget)
        self.insert_vehicle_color_lineedit.setObjectName("insert_vehicle_color_lineedit")
        self.insert_vehicle_color_lineedit.setGeometry(50, 330, 180, 30)
        self.insert_vehicle_color_lineedit.setPlaceholderText("Color")

        self.insert_vehicle_reg_number_lineedit = QLineEdit(self.insert_vehicle_sub_widget)
        self.insert_vehicle_reg_number_lineedit.setObjectName("insert_vehicle_reg_number_lineedit")
        self.insert_vehicle_reg_number_lineedit.setGeometry(260, 330, 125, 30)
        self.insert_vehicle_reg_number_lineedit.setPlaceholderText("Reg Number")

        self.insert_vehicle_add_button = QPushButton("Add", self.insert_vehicle_sub_widget)
        self.insert_vehicle_add_button.setObjectName("insert_vehicle_add_button")
        self.insert_vehicle_add_button.setGeometry(420, 330, 180, 30)
        self.insert_vehicle_add_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.insert_vehicle_add_button.clicked.connect(self.add_vehicle)

        with open("./style.css", "r") as f:
            self.setStyleSheet(f.read())

    def show_insert_vehicle_reg_date_calendar_dialog(self):
        insert_vehicle_reg_date_end_dialog = Insert_address_date_CalendarDialog(self.insert_vehicle_year_Button)
        insert_vehicle_reg_date_end_dialog.exec()

    def add_vehicle(self):
        maker = self.insert_vehicle_maker_lineedit.text()
        name = self.insert_vehicle_name_lineedit.text()
        year = self.insert_vehicle_year_Button.text()
        color = self.insert_vehicle_color_lineedit.text()
        reg_number = self.insert_vehicle_reg_number_lineedit.text()

        vehicle_data = [
            maker,
            name,
            year,
            color,
            reg_number
        ]

        try:
            if self.validate_vehicle(vehicle_data):
                self.INSERT_Vehicle.append(vehicle_data)
                self.update_vehicle_table()
                self.clear_all()
            else:
                QMessageBox.warning(self, "Error", "All fields are required")
        except Exception as e:
            QMessageBox.warning(self, "Error", str(e))

    def clear_all(self):
        self.insert_vehicle_maker_lineedit.clear()
        self.insert_vehicle_name_lineedit.clear()
        self.insert_vehicle_year_Button.setText("Registration Date")
        self.insert_vehicle_color_lineedit.clear()
        self.insert_vehicle_reg_number_lineedit.clear()

    def validate_vehicle(self, vehicle_data):
        for data in vehicle_data:
            if data == "":
                return False
        return True

    def update_vehicle_table(self):
        self.insert_vehicle_table_widget.setRowCount(len(self.INSERT_Vehicle))
        for row, data_entry in enumerate(self.INSERT_Vehicle):
            for col, value in enumerate(data_entry):
                item = QTableWidgetItem(value)
                self.insert_vehicle_table_widget.setItem(row, col, item)

            # Add delete button to each row
            self.insert_vehicle_delete_button = QPushButton("X")
            self.insert_vehicle_delete_button.setFixedSize(30, 30)
            self.insert_vehicle_delete_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
            self.insert_vehicle_delete_button.setObjectName("insert_vehicle_delete_button")
            self.insert_vehicle_delete_button.clicked.connect(lambda _, row=row: self.delete_vehicle(row))
            self.insert_vehicle_table_widget.setCellWidget(row, len(data_entry), self.insert_vehicle_delete_button)

    def delete_vehicle(self, row):
        del self.INSERT_Vehicle[row]
        self.update_vehicle_table()

    def get_vehicle_data(self):
        return self.INSERT_Vehicle


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = insert_addresses_widget()
    window.show()
    sys.exit(app.exec())
