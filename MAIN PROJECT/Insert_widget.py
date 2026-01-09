from datetime import date, datetime
from random import randint

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QStackedWidget, QLabel, QFileDialog, \
    QMessageBox
import sys

from Insert_sub_widgets import *

cur_index = 0


class InsertWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.insert_person_data = []
        self.insert_contact_data = []
        self.insert_address_data = []
        self.insert_edu_data = []
        self.insert_emp_data = []
        self.insert_prop_data = []
        self.insert_vehicle_data = []

        self.setObjectName("Insert_Widget")
        self.setGeometry(200, 50, 1000, 750)

        self.insert_Stacked_Widgets = QStackedWidget(self)
        self.insert_Stacked_Widgets.setGeometry(100, 50, 800, 550)
        self.insert_Stacked_Widgets.setObjectName("insert_Stacked_Widgets")

        self.insert_person_Qwidget = insert_person_widget()
        self.insert_person_Qwidget.setObjectName("insert_person_widget")

        self.insert_contact_Qwidget = insert_contact_widget()
        self.insert_contact_Qwidget.setObjectName("insert_contact_Qwidget")

        self.insert_addresses_Qwidget = insert_addresses_widget()
        self.insert_addresses_Qwidget.setObjectName("insert_addresses_widget")

        self.insert_education_Qwidget = insert_education_widget()
        self.insert_education_Qwidget.setObjectName("insert_education_widget")

        self.insert_employment_Qwidget = insert_employment_widget()
        self.insert_employment_Qwidget.setObjectName("insert_employment_widget")

        self.insert_property_Qwidget = insert_property_widget()
        self.insert_property_Qwidget.setObjectName("insert_property_widget")

        self.insert_vehicle_Qwidget = insert_vehicle_widget()
        self.insert_vehicle_Qwidget.setObjectName("insert_vehicle_widget")

        self.insert_Stacked_Widgets.addWidget(self.insert_person_Qwidget)
        self.insert_Stacked_Widgets.addWidget(self.insert_contact_Qwidget)
        self.insert_Stacked_Widgets.addWidget(self.insert_addresses_Qwidget)
        self.insert_Stacked_Widgets.addWidget(self.insert_education_Qwidget)
        self.insert_Stacked_Widgets.addWidget(self.insert_employment_Qwidget)
        self.insert_Stacked_Widgets.addWidget(self.insert_property_Qwidget)
        self.insert_Stacked_Widgets.addWidget(self.insert_vehicle_Qwidget)

        self.insert_previous_button = QPushButton("Previous", self)
        self.insert_previous_button.setGeometry(100, 650, 100, 50)
        self.insert_previous_button.setObjectName("insert_previous_button")
        self.insert_previous_button.clicked.connect(self.previous_button_clicked)

        self.insert_next_button = QPushButton("Next", self)
        self.insert_next_button.setGeometry(800, 650, 100, 50)
        self.insert_next_button.setObjectName("insert_next_button")
        self.insert_next_button.clicked.connect(self.next_button_clicked)

        self.insert_save_button = QPushButton("Save", self)
        self.insert_save_button.setGeometry(450, 650, 100, 50)
        self.insert_save_button.setObjectName("insert_save_button")
        self.insert_save_button.hide()
        self.insert_save_button.clicked.connect(self.save_button_clicked)

        with open("./style.css", "r") as f:
            self.setStyleSheet(f.read())

    def get_insert_person_data(self):
        insert_person_data = []
        f_name = self.insert_person_Qwidget.insert_person_first_name_lineedit.text()
        l_name = self.insert_person_Qwidget.insert_person_last_name_lineedit.text()
        date_of_birth = self.insert_person_Qwidget.insert_person_dateofbirth_button.text()
        place_of_birth = self.insert_person_Qwidget.insert_person_placeofbirth_lineedit.text()
        age = self.calculate_age(str(date_of_birth))
        if self.insert_person_Qwidget.insert_person_male_radio.isChecked():
            gender = "male"
        elif self.insert_person_Qwidget.insert_person_female_radio.isChecked():
            gender = "female"
        else:
            gender = "others"

        nationality = self.insert_person_Qwidget.insert_person_nationality_lineedit.text()
        cnic_no = self.insert_person_Qwidget.insert_person_cnicno_lineedit.text()
        religion = self.insert_person_Qwidget.insert_person_religion_lineedit.text()
        family_id = self.insert_person_Qwidget.insert_person_family_id_lineedit.text()

        insert_person_data = [
            f_name,
            l_name,
            date_of_birth,
            place_of_birth,
            age,
            gender,
            nationality,
            religion,
            cnic_no,
            family_id
        ]

        return insert_person_data

    def get_phone_number(self):
        phone_number = []
        for i in enumerate(phone_number):
            print(i)

    def Check_insert_data(self, data):
        for i in data:
            if i == "" or i == "DATE OF BIRTH":
                return False  # Change this to False
        return True

    def previous_button_clicked(self):
        global cur_index
        if cur_index <= 6:
            self.insert_save_button.hide()
            self.insert_next_button.show()
        if cur_index > 0:
            cur_index -= 1
            self.insert_Stacked_Widgets.setCurrentIndex(cur_index)

    def insert_next_widget(self):
        global cur_index
        if cur_index < 6:
            cur_index += 1
            self.insert_Stacked_Widgets.setCurrentIndex(cur_index)

    def next_button_clicked(self):
        global cur_index
        if cur_index == 0:
            try:
                self.insert_person_data = self.get_insert_person_data()
                if self.Check_insert_data(self.insert_person_data):
                    self.insert_next_widget()
                else:
                    raise Exception("Please fill all the fields")
            except Exception as e:
                QMessageBox.critical(self, "Error1", "Please fill all the fields")
        elif cur_index == 1:
            try:
                self.insert_contact_data = [self.insert_contact_Qwidget.Emails,
                                            self.insert_contact_Qwidget.Phone_Numbers]
                if self.insert_contact_data[0] != [] or self.insert_contact_data[1] != []:
                    self.insert_next_widget()
                else:
                    raise Exception("Please Enter at least one phone number or one email address")
            except Exception as e:
                QMessageBox.critical(self, "Error", str(e))
        elif cur_index == 2:
            try:
                self.insert_address_data = self.insert_addresses_Qwidget.INSERT_Addresses
                if self.insert_address_data:
                    self.insert_next_widget()
                else:
                    raise Exception("Please Enter at least one address")
            except Exception as e:
                QMessageBox.critical(self, "Error", str(e))
        elif cur_index == 3:
            try:
                self.insert_edu_data = self.insert_education_Qwidget.INSERT_Education
                self.insert_next_widget()
            except Exception as e:
                QMessageBox.critical(self, "Error", str(e))
        elif cur_index == 4:
            try:
                self.insert_emp_data = self.insert_employment_Qwidget.INSERT_Employment
                self.insert_next_widget()
            except Exception as e:
                QMessageBox.critical(self, "Error", str(e))
        elif cur_index == 5:
            try:
                self.insert_prop_data = self.insert_property_Qwidget.INSERT_Property
                self.insert_next_widget()
                self.insert_save_button.show()
                self.insert_next_button.hide()
            except Exception as e:
                QMessageBox.critical(self, "Error", str(e))
        elif cur_index == 6:
            try:
                self.insert_vehicle_data = self.insert_vehicle_Qwidget.INSERT_Vehicle
                self.insert_next_widget()
                self.insert_save_button.show()
            except Exception as e:
                QMessageBox.critical(self, "Error", str(e))
        else:
            self.insert_next_widget()

    def save_button_clicked(self):
        try:
            person_data = self.get_insert_person_data()
            Insert_Into_Person(person_data)

            query0 = "SELECT MAX(person_id) AS last_person_id FROM person;"
            json_data = RunQuery(query0)
            person_id = json_data[0]["last_person_id"]
            for i in self.insert_contact_data[1]:
                phone_data = [person_id, i]
                Insert_Into_Phone_Number(phone_data)

            for i in self.insert_contact_data[0]:
                email_data = [person_id, i]
                Insert_Into_Email(email_data)

            for i in self.insert_address_data:
                for j in range(0, len(i)):
                    if i[j] == "None":
                        i[j] = None
                address_data = [person_id, i[0], i[1], i[2], i[3], i[4], i[5], i[6]]
                Insert_Into_Address(address_data)

            for i in self.insert_edu_data:
                for j in range(0, len(i)):
                    if i[j] == "None":
                        i[j] = None
                edu_data = [person_id, i[0], i[2], i[1], i[3], i[4], i[5]]
                Insert_Into_Education(edu_data)

            for i in self.insert_emp_data:
                for j in range(0, len(i)):
                    if i[j] == "None":
                        i[j] = None
                emp_data = [person_id, i[2], i[3], i[4], i[5], i[0], i[6], i[1]]
                Insert_Into_Employment(emp_data)

            for i in self.insert_prop_data:
                for j in range(0, len(i)):
                    if i[j] == "None":
                        i[j] = None
                prop_data = [person_id, i[0], i[1], i[2], i[6], i[3], i[4], i[5]]
                Insert_Into_Property(prop_data)

            self.insert_vehicle_data = self.insert_vehicle_Qwidget.INSERT_Vehicle
            for i in self.insert_vehicle_data:
                for j in range(0, len(i)):
                    if i[j] == "None":
                        i[j] = None
                vehicle_data = [person_id, i[0], i[1], i[2], i[3], i[4]]
                Insert_Into_Vehicle(vehicle_data)

            QMessageBox.information(self, "Success", "Data Inserted Successfully")

            self.clear_all_forms()
            global cur_index
            cur_index = 0
            self.insert_Stacked_Widgets.setCurrentIndex(cur_index)
            self.insert_save_button.hide()
            self.insert_next_button.show()
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def clear_all_forms(self):
        self.insert_person_Qwidget.clear_all()

        self.insert_contact_Qwidget.clear_all()
        self.insert_contact_Qwidget.Emails = []
        self.insert_contact_Qwidget.Phone_Numbers = []
        self.insert_contact_Qwidget.insert_contact_ph_no_table.setRowCount(0)
        self.insert_contact_Qwidget.insert_contact_email_table.setRowCount(0)

        self.insert_addresses_Qwidget.clear_all()
        self.insert_addresses_Qwidget.INSERT_Addresses = []
        self.insert_addresses_Qwidget.insert_address_table_widget.setRowCount(0)

        self.insert_education_Qwidget.clear_all()
        self.insert_education_Qwidget.INSERT_Education = []
        self.insert_education_Qwidget.insert_education_table_widget.setRowCount(0)

        self.insert_employment_Qwidget.clear_all()
        self.insert_employment_Qwidget.INSERT_Employment = []
        self.insert_employment_Qwidget.insert_employment_table_widget.setRowCount(0)

        self.insert_property_Qwidget.clear_all()
        self.insert_property_Qwidget.INSERT_Property = []
        self.insert_property_Qwidget.insert_property_table_widget.setRowCount(0)

        self.insert_vehicle_Qwidget.clear_all()
        self.insert_vehicle_Qwidget.INSERT_Vehicle = []
        self.insert_vehicle_Qwidget.insert_vehicle_table_widget.setRowCount(0)

    def calculate_age(self, date_of_birth_str):
        date_of_birth = datetime.strptime(date_of_birth_str, "%Y-%m-%d")
        current_date = datetime.now()
        age = current_date.year - date_of_birth.year - (
                (current_date.month, current_date.day) < (date_of_birth.month, date_of_birth.day))
        return age


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = InsertWidget()
    window.show()
    sys.exit(app.exec())
