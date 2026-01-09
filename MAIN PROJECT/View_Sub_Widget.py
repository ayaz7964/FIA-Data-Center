import sys

from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QTableWidget, QTableWidgetItem, QRadioButton, QPushButton, \
    QMessageBox, \
    QLineEdit, QAbstractItemView, QApplication, QHBoxLayout, QSizePolicy, QGraphicsDropShadowEffect
from PyQt6.QtCore import Qt, pyqtSignal, QSize
from PyQt6.QtGui import QFont, QIcon, QCursor

from PyQt6.QtWidgets import QWidget, QLabel, QGridLayout
from DATABASE import RunQuery


class Search_person_main_Widget(QWidget):
    dataReturned = pyqtSignal(object)
    def __init__(self, person_id):
        super().__init__()
        self.setObjectName("Search_person_main_Widget")
        self.person_id = person_id
        self.data = self.getData(person_id)

        self.person_view_main_Widget = QWidget(self)
        self.person_view_main_Widget.setObjectName("person_view_main_Widget")
        self.person_view_main_Widget.setGeometry(50, 80, 850, 380)

        self.person_view_sub_widget_1 = QWidget(self.person_view_main_Widget)
        self.person_view_sub_widget_1.setObjectName("person_view_sub_widget_1")
        self.person_view_sub_widget_1.setGeometry(30, 10, 400, 350)

        self.person_view_sub_widget_2 = QWidget(self.person_view_main_Widget)
        self.person_view_sub_widget_2.setObjectName("person_view_sub_widget_2")
        self.person_view_sub_widget_2.setGeometry(420, 10, 400, 350)

        self.View_person_Label = QLabel("Personal Details", self)
        self.View_person_Label.setObjectName("View_person_Label")
        self.View_person_Label.setGeometry(350, 10, 350, 50)

        self.person_f_name_label_1 = QLabel("First Name", self.person_view_sub_widget_1)
        self.person_f_name_label_1.setObjectName("person_f_name_label_1")
        self.person_f_name_label_1.setGeometry(20, 20, 150, 50)

        self.person_l_name_label_1 = QLabel("Last Name", self.person_view_sub_widget_2)
        self.person_l_name_label_1.setObjectName("person_l_name_label_1")
        self.person_l_name_label_1.setGeometry(20, 20, 150, 50)

        self.person_dob_label_1 = QLabel("Date of Birth", self.person_view_sub_widget_1)
        self.person_dob_label_1.setObjectName("person_dob_label_1")
        self.person_dob_label_1.setGeometry(20, 70, 150, 50)

        self.person_age_label_1 = QLabel("Age", self.person_view_sub_widget_2)
        self.person_age_label_1.setObjectName("person_age_label_1")
        self.person_age_label_1.setGeometry(20, 70, 150, 50)

        self.person_pob_label_1 = QLabel("Place of Birth", self.person_view_sub_widget_1)
        self.person_pob_label_1.setObjectName("person_pob_label_1")
        self.person_pob_label_1.setGeometry(20, 120, 150, 50)

        self.person_gender_label_1 = QLabel("Gender", self.person_view_sub_widget_2)
        self.person_gender_label_1.setObjectName("person_gender_label_1")
        self.person_gender_label_1.setGeometry(20, 120, 150, 50)

        self.person_nationality_label_1 = QLabel("Nationality", self.person_view_sub_widget_1)
        self.person_nationality_label_1.setObjectName("person_nationality_label_1")
        self.person_nationality_label_1.setGeometry(20, 170, 150, 50)

        self.person_cnic_label_1 = QLabel("CNIC Number", self.person_view_sub_widget_2)
        self.person_cnic_label_1.setObjectName("person_cnic_label_1")
        self.person_cnic_label_1.setGeometry(20, 170, 150, 50)

        self.person_religion_label_1 = QLabel("Religion", self.person_view_sub_widget_1)
        self.person_religion_label_1.setObjectName("person_religion_label_1")
        self.person_religion_label_1.setGeometry(20, 220, 150, 50)

        self.person_family_id_label_1 = QLabel("Family ID", self.person_view_sub_widget_2)
        self.person_family_id_label_1.setObjectName("person_family_id_label_1")
        self.person_family_id_label_1.setGeometry(20, 220, 150, 50)

        # ################################################################################################
        # ################################################################################################
        # ################################################################################################

        self.person_f_name_label_2 = QLabel(self.person_view_sub_widget_1)
        self.person_f_name_label_2.setObjectName("person_f_name_label_2")
        self.person_f_name_label_2.setGeometry(200, 20, 200, 50)
        self.person_f_name_label_2.setText(str(self.data[0]["f_name"]))

        self.person_l_name_label_2 = QLabel(self.person_view_sub_widget_2)
        self.person_l_name_label_2.setObjectName("person_l_name_label_2")
        self.person_l_name_label_2.setGeometry(200, 20, 200, 50)
        self.person_l_name_label_2.setText(str(self.data[0]["l_name"]))

        self.person_dob_label_2 = QLabel(self.person_view_sub_widget_1)
        self.person_dob_label_2.setObjectName("person_dob_label_2")
        self.person_dob_label_2.setGeometry(200, 70, 200, 50)
        self.person_dob_label_2.setText(str(self.data[0]["date_of_birth"]))

        self.person_age_label_2 = QLabel(self.person_view_sub_widget_2)
        self.person_age_label_2.setObjectName("person_age_label_2")
        self.person_age_label_2.setGeometry(200, 70, 200, 50)
        self.person_age_label_2.setText(str(self.data[0]["age"]))

        self.person_pob_label_2 = QLabel(self.person_view_sub_widget_1)
        self.person_pob_label_2.setObjectName("person_pob_label_2")
        self.person_pob_label_2.setGeometry(200, 120, 200, 50)
        self.person_pob_label_2.setText(str(self.data[0]["place_of_birth"]))

        self.person_gender_label_2 = QLabel(self.person_view_sub_widget_2)
        self.person_gender_label_2.setObjectName("person_gender_label_2")
        self.person_gender_label_2.setGeometry(200, 120, 200, 50)
        self.person_gender_label_2.setText(str(self.data[0]["gender"]))

        self.person_nationality_label_2 = QLabel(self.person_view_sub_widget_1)
        self.person_nationality_label_2.setObjectName("person_nationality_label_2")
        self.person_nationality_label_2.setGeometry(200, 170, 200, 50)
        self.person_nationality_label_2.setText(str(self.data[0]["nationality"]))

        self.person_cnic_label_2 = QLabel(self.person_view_sub_widget_2)
        self.person_cnic_label_2.setObjectName("person_cnic_label_2")
        self.person_cnic_label_2.setGeometry(200, 170, 200, 50)
        self.person_cnic_label_2.setText(str(self.data[0]["cnic_number"]))

        self.person_nationality_label_2 = QLabel(self.person_view_sub_widget_1)
        self.person_nationality_label_2.setObjectName("person_nationality_label_2")
        self.person_nationality_label_2.setGeometry(200, 220, 200, 50)
        self.person_nationality_label_2.setText(str(self.data[0]["religion"]))

        self.person_family_id_label_2 = QLabel(self.person_view_sub_widget_2)
        self.person_family_id_label_2.setObjectName("person_family_id_label_2")
        self.person_family_id_label_2.setGeometry(200, 220, 200, 50)
        self.person_family_id_label_2.setText(str(self.data[0]["Family_id"]))

        self.person_view_Delete_btn = QPushButton("DELETE", self.person_view_sub_widget_1)
        self.person_view_Delete_btn.setObjectName("person_view_Delete_btn")
        self.person_view_Delete_btn.setGeometry(225, 300, 150, 35)
        self.person_view_Delete_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.person_view_Delete_btn.clicked.connect(self.delete_person)


        with open("test.css") as style:
            self.setStyleSheet(style.read())

    def delete_person(self):
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Confirmation")
        msg_box.setText("Are you sure you want to Delete?")
        msg_box.setStandardButtons(QMessageBox.StandardButton.Cancel | QMessageBox.StandardButton.Ok)
        msg_box.setDefaultButton(QMessageBox.StandardButton.Cancel)

        # Change button text
        ok_button = msg_box.button(QMessageBox.StandardButton.Ok)
        ok_button.setText("Delete")

        result = msg_box.exec()
        if result == QMessageBox.StandardButton.Ok:
            self.dataReturned.emit("Delete")
        else:
            pass

    def getData(self, person_id):
        query = f"Select * from person where person_id = {person_id}"
        return RunQuery(query)


class View_Contact_Widget(QWidget):
    def __init__(self, person_id):
        super().__init__()

        self.person_id = person_id

        self.setObjectName("Contact_Widget")
        self.setFixedSize(950, 500)

        self.Search_contact_Label = QLabel("Contact Details", self)
        self.Search_contact_Label.setObjectName("Search_contact_Label")
        self.Search_contact_Label.setGeometry(380, 20, 350, 50)

        self.contact_view_sub_widget_1 = QWidget(self)
        self.contact_view_sub_widget_1.setObjectName("contact_view_sub_widget_1")
        self.contact_view_sub_widget_1.setGeometry(50, 90, 400, 370)

        self.contact_view_sub_widget_2 = QWidget(self)
        self.contact_view_sub_widget_2.setObjectName("contact_view_sub_widget_2")
        self.contact_view_sub_widget_2.setGeometry(500, 90, 400, 370)

        self.contact_ph_no_label = QLabel("Phone Numbers", self.contact_view_sub_widget_1)
        self.contact_ph_no_label.setObjectName("contact_ph_no_label")
        self.contact_ph_no_label.setGeometry(100, 5, 200, 50)
        self.contact_ph_no_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.contact_email_label = QLabel("Emails", self.contact_view_sub_widget_2)
        self.contact_email_label.setObjectName("contact_email_label")
        self.contact_email_label.setGeometry(100, 5, 200, 50)
        self.contact_email_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.contact_email_table = QTableWidget(self.contact_view_sub_widget_2)
        self.contact_email_table.setObjectName("contact_email_table")
        self.contact_email_table.setGeometry(35, 60, 330, 290)
        self.contact_email_table.setColumnCount(2)
        self.contact_email_table.setHorizontalHeaderLabels([
            "Email Address",
            "Delete"
        ])
        self.contact_email_table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.contact_email_table.horizontalHeader().setStyleSheet(
            "QHeaderView::section{font-weight: bold; font-size: 15px;}")
        self.contact_email_table.verticalHeader().setStyleSheet(
            "QHeaderView::section{font-weight: bold; font-size: 15px;}")

        self.contact_email_table.setColumnWidth(0, 220)
        self.contact_email_table.setColumnWidth(1, 65)
        self.contact_email_table.horizontalHeader().setStretchLastSection(True)
        self.contact_email_table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.contact_email_table.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)

        self.contact_ph_no_table = QTableWidget(self.contact_view_sub_widget_1)
        self.contact_ph_no_table.setObjectName("contact_ph_no_table")
        self.contact_ph_no_table.setGeometry(35, 60, 330, 290)
        self.contact_ph_no_table.setColumnCount(2)
        self.contact_ph_no_table.setHorizontalHeaderLabels([
            "Phone Number",
            "Delete"
        ])
        self.contact_ph_no_table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.contact_ph_no_table.horizontalHeader().setStyleSheet(
            "QHeaderView::section{font-weight: bold; font-size: 15px;}")
        self.contact_ph_no_table.verticalHeader().setStyleSheet(
            "QHeaderView::section{font-weight: bold; font-size: 15px;}")

        self.contact_ph_no_table.setColumnWidth(0, 220)
        self.contact_ph_no_table.setColumnWidth(1, 65)
        self.contact_ph_no_table.horizontalHeader().setStretchLastSection(True)
        self.contact_ph_no_table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.contact_ph_no_table.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)

        self.contact_load_data()
        with open("./test.css", "r") as f:
            self.setStyleSheet(f.read())

    def contact_load_data(self):
        try:
            query = f"SELECT phone_number FROM phone_numbers WHERE person_id = {self.person_id}"
            phone_no = RunQuery(query)
            self.contact_phone_no_display_data(phone_no)

            query = f"SELECT email_address FROM emails WHERE person_id = {self.person_id}"
            email = RunQuery(query)
            self.contact_email_display_data(email)
        except Exception as e:
            QMessageBox.warning(self, "Server Error", str(e))

    def contact_phone_no_display_data(self, data):
        num_rows = len(data)
        self.contact_ph_no_table.setRowCount(num_rows)

        for row, row_data in enumerate(data):
            for col, value in enumerate(row_data.values()):
                # self.contact_ph_no_table.insertRow(row)
                self.contact_ph_no_table.setItem(row, 0, QTableWidgetItem(value))

                delete_button_layout = QHBoxLayout()
                delete_button_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

                self.insert_phone_delete_button = QPushButton("X")
                self.insert_phone_delete_button.setFixedSize(25, 25)
                self.insert_phone_delete_button.setGeometry(0, 0, 25, 25)
                self.insert_phone_delete_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
                self.insert_phone_delete_button.setIconSize(QSize(20, 20))  # Set icon size
                self.insert_phone_delete_button.setObjectName("insert_phone_delete_button")
                self.insert_phone_delete_button.clicked.connect(lambda _, row=row: self.delete_contact_phone(data[row]['phone_number']))

                delete_button_layout.addWidget(self.insert_phone_delete_button)
                cell_widget = QWidget()
                cell_widget.setLayout(delete_button_layout)
                self.contact_ph_no_table.setCellWidget(row, 1, cell_widget)

        self.contact_ph_no_table.resizeRowsToContents()


    def contact_email_display_data(self, data):
        num_rows = len(data)
        self.contact_email_table.setRowCount(num_rows)

        for row, row_data in enumerate(data):
            for col, value in enumerate(row_data.values()):
                self.contact_email_table.setItem(row, 0, QTableWidgetItem(value))

                delete_button_layout = QHBoxLayout()
                delete_button_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

                self.insert_phone_delete_button = QPushButton("X")
                self.insert_phone_delete_button.setFixedSize(25, 25)
                self.insert_phone_delete_button.setGeometry(0, 0, 25, 25)
                self.insert_phone_delete_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
                self.insert_phone_delete_button.setIconSize(QSize(20, 20))  # Set icon size
                self.insert_phone_delete_button.setObjectName("insert_phone_delete_button")
                self.insert_phone_delete_button.clicked.connect(lambda _, row=row: self.delete_contact_email(data[row]['email_address']))

                delete_button_layout.addWidget(self.insert_phone_delete_button)
                cell_widget = QWidget()
                cell_widget.setLayout(delete_button_layout)
                self.contact_email_table.setCellWidget(row, 1, cell_widget)

        self.contact_email_table.resizeRowsToContents()


    def delete_contact_phone(self, data):
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Confirmation")
        msg_box.setText("Are you sure you want to Delete?")
        msg_box.setStandardButtons(QMessageBox.StandardButton.Cancel | QMessageBox.StandardButton.Ok)
        msg_box.setDefaultButton(QMessageBox.StandardButton.Cancel)

        # Change button text
        ok_button = msg_box.button(QMessageBox.StandardButton.Ok)
        ok_button.setText("Delete")

        result = msg_box.exec()
        if result == QMessageBox.StandardButton.Ok:
            query = f"DELETE FROM phone_numbers WHERE phone_number = '{data}'"
            RunQuery(query)
            self.contact_load_data()
        else:
            pass

    def delete_contact_email(self, data):
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Confirmation")
        msg_box.setText("Are you sure you want to Delete?")
        msg_box.setStandardButtons(QMessageBox.StandardButton.Cancel | QMessageBox.StandardButton.Ok)
        msg_box.setDefaultButton(QMessageBox.StandardButton.Cancel)

        # Change button text
        ok_button = msg_box.button(QMessageBox.StandardButton.Ok)
        ok_button.setText("Delete")

        result = msg_box.exec()
        if result == QMessageBox.StandardButton.Ok:
            query = f"DELETE FROM emails WHERE email_address = '{data}'"
            RunQuery(query)
            self.contact_load_data()
        else:
            pass


class View_Address_main_Widget(QWidget):
    def __init__(self, person_id):
        super().__init__()
        self.person_id = person_id
        self.setObjectName("View_address_main_Widget")
        self.setFixedSize(950, 500)

        self.View_address_Label = QLabel("Address Details", self)
        self.View_address_Label.setObjectName("View_address_Label")
        self.View_address_Label.setGeometry(380, 20, 350, 50)

        self.address_view_sub_widget = QWidget(self)
        self.address_view_sub_widget.setObjectName("address_view_sub_widget")
        self.address_view_sub_widget.setGeometry(25, 90, 900, 370)

        self.address_view_table = QTableWidget(self.address_view_sub_widget)
        self.address_view_table.setObjectName("address_view_table")
        self.address_view_table.setGeometry(25, 40, 850, 290)
        self.address_view_table.setColumnCount(8)
        self.address_view_table.setHorizontalHeaderLabels([
            "Address",
            "City",
            "State",
            "Country",
            "Arrival Date",
            "Departure Date",
            "Status",
            "Delete"
        ])
        self.address_view_table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.address_view_table.horizontalHeader().setStyleSheet(
            "QHeaderView::section{font-weight: bold;}")
        self.address_view_table.verticalHeader().setStyleSheet(
            "QHeaderView::section{font-weight: bold;}")

        self.address_view_table.setColumnWidth(0, 200)
        self.address_view_table.setColumnWidth(1, 90)
        self.address_view_table.setColumnWidth(2, 90)
        self.address_view_table.setColumnWidth(3, 90)
        self.address_view_table.setColumnWidth(4, 88)
        self.address_view_table.setColumnWidth(5, 105)
        self.address_view_table.setColumnWidth(6, 90)
        self.address_view_table.setColumnWidth(7, 55)
        self.address_view_table.horizontalHeader().setStretchLastSection(True)
        self.address_view_table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.address_view_table.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)

        self.address_load_data()
        with open("./test.css", "r") as f:
            self.setStyleSheet(f.read())


    def address_load_data(self):
        try:
            query = f"SELECT address,adr_city, adr_state, adr_country, adr_date_in, adr_date_out ,address_status FROM addresses WHERE person_id = {self.person_id}"
            addresses = RunQuery(query)
            self.address_display_data(addresses)
        except Exception as e:
            QMessageBox.warning(self, "Server Error", str(e))

    def address_display_data(self, data):
        num_rows = len(data)
        self.address_view_table.setRowCount(num_rows)

        for row, row_data in enumerate(data):
            for col, value in enumerate(row_data.values()):
                # self.contact_ph_no_table.insertRow(row)
                item = QTableWidgetItem(str(value))
                if col in [0]:
                    item.setFlags(item.flags() | Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEditable)
                    item.setTextAlignment(Qt.AlignmentFlag.AlignTop)
                self.address_view_table.setItem(row, col, item)
                # self.address_view_table.setItem(row, 0, QTableWidgetItem(value))

                delete_button_layout = QHBoxLayout()
                delete_button_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

                self.insert_phone_delete_button = QPushButton("X")
                self.insert_phone_delete_button.setFixedSize(25, 25)
                self.insert_phone_delete_button.setGeometry(0, 0, 25, 25)
                self.insert_phone_delete_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
                self.insert_phone_delete_button.setIconSize(QSize(20, 20))  # Set icon size
                self.insert_phone_delete_button.setObjectName("insert_phone_delete_button")
                self.insert_phone_delete_button.clicked.connect(lambda _, row=row: self.delete_address(data[row]))

                delete_button_layout.addWidget(self.insert_phone_delete_button)
                cell_widget = QWidget()
                cell_widget.setLayout(delete_button_layout)
                self.address_view_table.setCellWidget(row, 7, cell_widget)

        self.address_view_table.resizeRowsToContents()

    def delete_address(self, data):
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Confirmation")
        msg_box.setText("Are you sure you want to Delete?")
        msg_box.setStandardButtons(QMessageBox.StandardButton.Cancel | QMessageBox.StandardButton.Ok)
        msg_box.setDefaultButton(QMessageBox.StandardButton.Cancel)

        # Change button text
        ok_button = msg_box.button(QMessageBox.StandardButton.Ok)
        ok_button.setText("Delete")

        result = msg_box.exec()
        if result == QMessageBox.StandardButton.Ok:
            query = f"DELETE FROM addresses WHERE address = '{data['address']}' and person_id = {self.person_id} and adr_city = '{data['adr_city']}' and adr_state = '{data['adr_state']}' and adr_country = '{data['adr_country']}' and adr_date_in = '{data['adr_date_in']}' and adr_city = '{data['adr_city']}' and adr_state = '{data['adr_state']}'and adr_date_in = '{data['adr_date_in']}'"
            RunQuery(query)
            self.address_load_data()
        else:
            pass

class View_Education_main_Widget(QWidget):
    def __init__(self, person_id):
        super().__init__()
        self.person_id = person_id
        self.setObjectName("View_education_main_Widget")
        self.setFixedSize(950, 500)

        self.View_education_Label = QLabel("Educational Details", self)
        self.View_education_Label.setObjectName("View_address_Label")
        self.View_education_Label.setGeometry(370, 20, 350, 50)

        self.education_view_sub_widget = QWidget(self)
        self.education_view_sub_widget.setObjectName("address_view_sub_widget")
        self.education_view_sub_widget.setGeometry(25, 90, 900, 370)

        self.education_view_table = QTableWidget(self.education_view_sub_widget)
        self.education_view_table.setObjectName("address_view_table")
        self.education_view_table.setGeometry(25, 40, 850, 290)
        self.education_view_table.setColumnCount(7)
        self.education_view_table.setHorizontalHeaderLabels([
            "Deg Name",
            "Reg ID",
            "EDU Institute",
            "Starting Date",
            "Ending Date",
            "Status",
            "Delete"
        ])
        self.education_view_table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.education_view_table.horizontalHeader().setStyleSheet(
            "QHeaderView::section{font-weight: bold;}")
        self.education_view_table.verticalHeader().setStyleSheet(
            "QHeaderView::section{font-weight: bold;}")

        self.education_view_table.setColumnWidth(0, 150)
        self.education_view_table.setColumnWidth(1, 100)
        self.education_view_table.setColumnWidth(2, 200)
        self.education_view_table.setColumnWidth(3, 90)
        self.education_view_table.setColumnWidth(4, 100)
        self.education_view_table.setColumnWidth(5, 90)
        self.education_view_table.setColumnWidth(6, 55)
        self.education_view_table.horizontalHeader().setStretchLastSection(True)
        self.education_view_table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.education_view_table.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)

        self.education_load_data()
        with open("./test.css", "r") as f:
            self.setStyleSheet(f.read())

    def education_load_data(self):
        try:
            query = f"SELECT degree_name, edu_reg_id, edu_institute, edu_date_in, edu_date_out ,Education_status FROM education WHERE person_id = {self.person_id}"
            addresses = RunQuery(query)
            self.address_display_data(addresses)
        except Exception as e:
            QMessageBox.warning(self, "Server Error", str(e))

    def address_display_data(self, data):
        num_rows = len(data)
        self.education_view_table.setRowCount(num_rows)

        for row, row_data in enumerate(data):
            for col, value in enumerate(row_data.values()):
                # self.contact_ph_no_table.insertRow(row)
                item = QTableWidgetItem(str(value))
                if col in [0,2]:
                    item.setFlags(item.flags() | Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEditable)
                self.education_view_table.setItem(row, col, item)
                # self.address_view_table.setItem(row, 0, QTableWidgetItem(value))

                delete_button_layout = QHBoxLayout()
                delete_button_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

                self.insert_phone_delete_button = QPushButton("X")
                self.insert_phone_delete_button.setFixedSize(25, 25)
                self.insert_phone_delete_button.setGeometry(0, 0, 25, 25)
                self.insert_phone_delete_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
                self.insert_phone_delete_button.setIconSize(QSize(20, 20))  # Set icon size
                self.insert_phone_delete_button.setObjectName("insert_phone_delete_button")
                self.insert_phone_delete_button.clicked.connect(lambda _, row=row: self.delete_edu(data[row]))

                delete_button_layout.addWidget(self.insert_phone_delete_button)
                cell_widget = QWidget()
                cell_widget.setLayout(delete_button_layout)
                self.education_view_table.setCellWidget(row, 6, cell_widget)

        self.education_view_table.resizeRowsToContents()

    def delete_edu(self, data):
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Confirmation")
        msg_box.setText("Are you sure you want to Delete?")
        msg_box.setStandardButtons(QMessageBox.StandardButton.Cancel | QMessageBox.StandardButton.Ok)
        msg_box.setDefaultButton(QMessageBox.StandardButton.Cancel)

        # Change button text
        ok_button = msg_box.button(QMessageBox.StandardButton.Ok)
        ok_button.setText("Delete")

        result = msg_box.exec()
        if result == QMessageBox.StandardButton.Ok:
            query = f"DELETE FROM education WHERE degree_name = '{data['degree_name']}' and person_id = {self.person_id} and edu_reg_id = '{data['edu_reg_id']}' and edu_institute = '{data['edu_institute']}' and edu_date_in = '{data['edu_date_in']}' and Education_status = '{data['Education_status']}'"
            RunQuery(query)
            self.education_load_data()
        else:
            pass

class View_Property_main_Widget(QWidget):
    def __init__(self, person_id):
        super().__init__()
        self.person_id = person_id
        self.setObjectName("View_education_main_Widget")
        self.setFixedSize(950, 500)

        self.View_property_Label = QLabel("Property Details", self)
        self.View_property_Label.setObjectName("View_address_Label")
        self.View_property_Label.setGeometry(380, 20, 350, 50)

        self.education_view_sub_widget = QWidget(self)
        self.education_view_sub_widget.setObjectName("address_view_sub_widget")
        self.education_view_sub_widget.setGeometry(25, 90, 900, 370)

        self.property_view_table = QTableWidget(self.education_view_sub_widget)
        self.property_view_table.setObjectName("address_view_table")
        self.property_view_table.setGeometry(25, 40, 850, 290)
        self.property_view_table.setColumnCount(8)
        self.property_view_table.setHorizontalHeaderLabels([
            "Prop Type",
            "Reg ID",
            "Prop Address",
            "Prop Value",
            "Buy Date",
            "Sell Date",
            "Status",
            "Delete"
        ])
        self.property_view_table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.property_view_table.horizontalHeader().setStyleSheet(
            "QHeaderView::section{font-weight: bold;}")
        self.property_view_table.verticalHeader().setStyleSheet(
            "QHeaderView::section{font-weight: bold;}")

        self.property_view_table.setColumnWidth(0, 100)
        self.property_view_table.setColumnWidth(1, 90)
        self.property_view_table.setColumnWidth(2, 200)
        self.property_view_table.setColumnWidth(3, 90)
        self.property_view_table.setColumnWidth(4, 90)
        self.property_view_table.setColumnWidth(5, 90)
        self.property_view_table.setColumnWidth(6, 90)
        self.property_view_table.setColumnWidth(7, 55)
        self.property_view_table.horizontalHeader().setStretchLastSection(True)
        self.property_view_table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.property_view_table.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)

        self.property_load_data()
        with open("./test.css", "r") as f:
            self.setStyleSheet(f.read())

    def property_load_data(self):
        try:
            query = f"SELECT property_type, property_reg_id, property_address, property_value_amount, buy_date ,sell_date, property_status FROM property WHERE person_id = {self.person_id}"
            Prop = RunQuery(query)
            self.address_display_data(Prop)
        except Exception as e:
            QMessageBox.warning(self, "Server Error", str(e))

    def address_display_data(self, data):
        num_rows = len(data)
        self.property_view_table.setRowCount(num_rows)

        for row, row_data in enumerate(data):
            for col, value in enumerate(row_data.values()):
                # self.contact_ph_no_table.insertRow(row)
                item = QTableWidgetItem(str(value))
                if col in [0, 2]:
                    item.setFlags(item.flags() | Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEditable)
                self.property_view_table.setItem(row, col, item)
                # self.address_view_table.setItem(row, 0, QTableWidgetItem(value))

                delete_button_layout = QHBoxLayout()
                delete_button_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

                self.insert_phone_delete_button = QPushButton("X")
                self.insert_phone_delete_button.setFixedSize(25, 25)
                self.insert_phone_delete_button.setGeometry(0, 0, 25, 25)
                self.insert_phone_delete_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
                self.insert_phone_delete_button.setIconSize(QSize(20, 20))  # Set icon size
                self.insert_phone_delete_button.setObjectName("insert_phone_delete_button")
                self.insert_phone_delete_button.clicked.connect(lambda _, row=row: self.delete_prop(data[row]))

                delete_button_layout.addWidget(self.insert_phone_delete_button)
                cell_widget = QWidget()
                cell_widget.setLayout(delete_button_layout)
                self.property_view_table.setCellWidget(row, 7, cell_widget)

        self.property_view_table.resizeRowsToContents()

    def delete_prop(self, data):
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Confirmation")
        msg_box.setText("Are you sure you want to Delete?")
        msg_box.setStandardButtons(QMessageBox.StandardButton.Cancel | QMessageBox.StandardButton.Ok)
        msg_box.setDefaultButton(QMessageBox.StandardButton.Cancel)

        # Change button text
        ok_button = msg_box.button(QMessageBox.StandardButton.Ok)
        ok_button.setText("Delete")

        result = msg_box.exec()
        if result == QMessageBox.StandardButton.Ok:
            query = f"DELETE FROM property WHERE property_type = '{data['property_type']}' and person_id = {self.person_id} and property_reg_id = '{data['property_reg_id']}' and property_address = '{data['property_address']}' and property_value_amount = '{data['property_value_amount']}' and buy_date = '{data['buy_date']}' and property_status = '{data['property_status']}'"
            RunQuery(query)
            self.property_load_data()
        else:
            pass

class View_Employment_main_Widget(QWidget):
    def __init__(self, person_id):
        super().__init__()
        self.person_id = person_id
        self.setObjectName("View_education_main_Widget")
        self.setFixedSize(950, 500)

        self.View_employment_Label = QLabel("Employment Details", self)
        self.View_employment_Label.setObjectName("View_address_Label")
        self.View_employment_Label.setGeometry(370, 20, 350, 50)

        self.education_view_sub_widget = QWidget(self)
        self.education_view_sub_widget.setObjectName("address_view_sub_widget")
        self.education_view_sub_widget.setGeometry(25, 90, 900, 370)

        self.employment_view_table = QTableWidget(self.education_view_sub_widget)
        self.employment_view_table.setObjectName("address_view_table")
        self.employment_view_table.setGeometry(25, 40, 850, 290)
        self.employment_view_table.setColumnCount(8)
        self.employment_view_table.setHorizontalHeaderLabels([
            "Job Name",
            "Job ID",
            "Company Name",
            "Address",
            "Hire Date",
            "Leave Date",
            "Status",
            "Delete"
        ])
        self.employment_view_table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.employment_view_table.horizontalHeader().setStyleSheet(
            "QHeaderView::section{font-weight: bold;}")
        self.employment_view_table.verticalHeader().setStyleSheet(
            "QHeaderView::section{font-weight: bold;}")

        self.employment_view_table.setColumnWidth(0, 120)
        self.employment_view_table.setColumnWidth(1, 90)
        self.employment_view_table.setColumnWidth(2, 140)
        self.employment_view_table.setColumnWidth(3, 140)
        self.employment_view_table.setColumnWidth(4, 80)
        self.employment_view_table.setColumnWidth(5, 80)
        self.employment_view_table.setColumnWidth(6, 90)
        self.employment_view_table.setColumnWidth(7, 40)
        self.employment_view_table.horizontalHeader().setStretchLastSection(True)
        self.employment_view_table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.employment_view_table.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)

        self.property_load_data()
        with open("./test.css", "r") as f:
            self.setStyleSheet(f.read())

    def property_load_data(self):
        try:
            query = f"SELECT job_name, job_id, employment_company, company_address, hired_date, leave_date, employment_status FROM employment WHERE person_id = {self.person_id}"
            Prop = RunQuery(query)
            self.address_display_data(Prop)
        except Exception as e:
            QMessageBox.warning(self, "Server Error", str(e))

    def address_display_data(self, data):
        num_rows = len(data)
        self.employment_view_table.setRowCount(num_rows)

        for row, row_data in enumerate(data):
            for col, value in enumerate(row_data.values()):
                # self.contact_ph_no_table.insertRow(row)
                item = QTableWidgetItem(str(value))
                if col in [0, 2, 3]:
                    item.setFlags(item.flags() | Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEditable)
                self.employment_view_table.setItem(row, col, item)
                # self.address_view_table.setItem(row, 0, QTableWidgetItem(value))

                delete_button_layout = QHBoxLayout()
                delete_button_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

                self.insert_phone_delete_button = QPushButton("X")
                self.insert_phone_delete_button.setFixedSize(25, 25)
                self.insert_phone_delete_button.setGeometry(0, 0, 25, 25)
                self.insert_phone_delete_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
                self.insert_phone_delete_button.setIconSize(QSize(20, 20))  # Set icon size
                self.insert_phone_delete_button.setObjectName("insert_phone_delete_button")
                self.insert_phone_delete_button.clicked.connect(lambda _, row=row: self.delete_employment(data[row]))

                delete_button_layout.addWidget(self.insert_phone_delete_button)
                cell_widget = QWidget()
                cell_widget.setLayout(delete_button_layout)
                self.employment_view_table.setCellWidget(row, 7, cell_widget)

        self.employment_view_table.resizeRowsToContents()

    def delete_employment(self, data):
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Confirmation")
        msg_box.setText("Are you sure you want to Delete?")
        msg_box.setStandardButtons(QMessageBox.StandardButton.Cancel | QMessageBox.StandardButton.Ok)
        msg_box.setDefaultButton(QMessageBox.StandardButton.Cancel)

        # Change button text
        ok_button = msg_box.button(QMessageBox.StandardButton.Ok)
        ok_button.setText("Delete")

        result = msg_box.exec()
        if result == QMessageBox.StandardButton.Ok:
            query = f"DELETE FROM employment WHERE job_name = '{data['job_name']}' and person_id = {self.person_id} and job_id = '{data['job_id']}' and employment_company = '{data['employment_company']}' and company_address = '{data['company_address']}' and hired_date = '{data['hired_date']}' and employment_status = '{data['employment_status']}'"
            RunQuery(query)
            self.property_load_data()
        else:
            pass


class View_Vehicles_main_Widget(QWidget):
    def __init__(self, person_id):
        super().__init__()
        self.person_id = person_id
        self.setObjectName("View_education_main_Widget")
        self.setFixedSize(950, 500)

        self.View_vehicles_Label = QLabel("Vehicles Details", self)
        self.View_vehicles_Label.setObjectName("View_address_Label")
        self.View_vehicles_Label.setGeometry(370, 20, 350, 50)

        self.education_view_sub_widget = QWidget(self)
        self.education_view_sub_widget.setObjectName("address_view_sub_widget")
        self.education_view_sub_widget.setGeometry(75, 90, 800, 370)

        self.vehicles_view_table = QTableWidget(self.education_view_sub_widget)
        self.vehicles_view_table.setObjectName("address_view_table")
        self.vehicles_view_table.setGeometry(50, 40, 700, 290)
        self.vehicles_view_table.setColumnCount(6)
        self.vehicles_view_table.setHorizontalHeaderLabels([
            "Vehicle Maker",
            "Vehicle Model",
            "Reg Year",
            "Vehicle Color",
            "Reg Number",
            "Delete"
        ])
        self.vehicles_view_table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.vehicles_view_table.horizontalHeader().setStyleSheet(
            "QHeaderView::section{font-weight: bold;}")
        self.vehicles_view_table.verticalHeader().setStyleSheet(
            "QHeaderView::section{font-weight: bold;}")

        self.vehicles_view_table.setColumnWidth(0, 120)
        self.vehicles_view_table.setColumnWidth(1, 120)
        self.vehicles_view_table.setColumnWidth(2, 120)
        self.vehicles_view_table.setColumnWidth(3, 120)
        self.vehicles_view_table.setColumnWidth(4, 120)
        self.vehicles_view_table.setColumnWidth(5, 50)
        self.vehicles_view_table.horizontalHeader().setStretchLastSection(True)
        self.vehicles_view_table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.vehicles_view_table.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)

        self.property_load_data()
        with open("./test.css", "r") as f:
            self.setStyleSheet(f.read())

    def property_load_data(self):
        try:
            query = f"SELECT vehicle_maker, vehicle_model, year(vehicle_year) as reg_year, vehicle_color, vehicle_reg_number FROM vehicles WHERE person_id = {self.person_id}"
            vehicles = RunQuery(query)
            self.address_display_data(vehicles)
        except Exception as e:
            QMessageBox.warning(self, "Server Error", str(e))

    def address_display_data(self, data):
        num_rows = len(data)
        self.vehicles_view_table.setRowCount(num_rows)

        for row, row_data in enumerate(data):
            for col, value in enumerate(row_data.values()):
                # self.contact_ph_no_table.insertRow(row)
                item = QTableWidgetItem(str(value))
                self.vehicles_view_table.setItem(row, col, item)

                delete_button_layout = QHBoxLayout()
                delete_button_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

                self.insert_phone_delete_button = QPushButton("X")
                self.insert_phone_delete_button.setFixedSize(25, 25)
                self.insert_phone_delete_button.setGeometry(0, 0, 25, 25)
                self.insert_phone_delete_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
                self.insert_phone_delete_button.setIconSize(QSize(20, 20))  # Set icon size
                self.insert_phone_delete_button.setObjectName("insert_phone_delete_button")
                self.insert_phone_delete_button.clicked.connect(lambda _, row=row: self.delete_vehicle(data[row]))

                delete_button_layout.addWidget(self.insert_phone_delete_button)
                cell_widget = QWidget()
                cell_widget.setLayout(delete_button_layout)
                self.vehicles_view_table.setCellWidget(row, 5, cell_widget)

        self.vehicles_view_table.resizeRowsToContents()

    def delete_vehicle(self, data):
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Confirmation")
        msg_box.setText("Are you sure you want to Delete?")
        msg_box.setStandardButtons(QMessageBox.StandardButton.Cancel | QMessageBox.StandardButton.Ok)
        msg_box.setDefaultButton(QMessageBox.StandardButton.Cancel)

        # Change button text
        ok_button = msg_box.button(QMessageBox.StandardButton.Ok)
        ok_button.setText("Delete")

        result = msg_box.exec()
        if result == QMessageBox.StandardButton.Ok:
            query = f"DELETE FROM vehicles WHERE vehicle_maker = '{data['vehicle_maker']}' and person_id = {self.person_id} and vehicle_model = '{data['vehicle_model']}' and year(vehicle_year) = '{data['reg_year']}' and vehicle_reg_number = '{data['vehicle_reg_number']}'"
            RunQuery(query)
            self.property_load_data()
        else:
            pass


class View_CrimeRecord_main_Widget(QWidget):
    def __init__(self, person_id):
        super().__init__()
        self.person_id = person_id
        self.setObjectName("View_education_main_Widget")
        self.setFixedSize(950, 500)

        self.View_crime_Label = QLabel("Crime Record", self)
        self.View_crime_Label.setObjectName("View_address_Label")
        self.View_crime_Label.setGeometry(370, 20, 350, 50)

        self.education_view_sub_widget = QWidget(self)
        self.education_view_sub_widget.setObjectName("address_view_sub_widget")
        self.education_view_sub_widget.setGeometry(25, 90, 900, 370)

        self.crime_view_table = QTableWidget(self.education_view_sub_widget)
        self.crime_view_table.setObjectName("address_view_table")
        self.crime_view_table.setGeometry(25, 40, 850, 290)
        self.crime_view_table.setColumnCount(8)
        self.crime_view_table.setHorizontalHeaderLabels([
            "Crime ID",
            "Crime Name",
            "Crime Details",
            "Crime Date",
            "Status",
            "Punishment",
            "Fine",
            "Delete"
        ])
        self.crime_view_table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.crime_view_table.horizontalHeader().setStyleSheet(
            "QHeaderView::section{font-weight: bold;}")
        self.crime_view_table.verticalHeader().setStyleSheet(
            "QHeaderView::section{font-weight: bold;}")

        self.crime_view_table.setColumnWidth(0, 80)
        self.crime_view_table.setColumnWidth(1, 90)
        self.crime_view_table.setColumnWidth(2, 200)
        self.crime_view_table.setColumnWidth(3, 90)
        self.crime_view_table.setColumnWidth(4, 100)
        self.crime_view_table.setColumnWidth(5, 90)
        self.crime_view_table.setColumnWidth(6, 90)
        self.crime_view_table.setColumnWidth(7, 40)
        self.crime_view_table.horizontalHeader().setStretchLastSection(True)
        self.crime_view_table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.crime_view_table.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)

        self.Crime_load_data()
        with open("./test.css", "r") as f:
            self.setStyleSheet(f.read())

    def Crime_load_data(self):
        try:
            query = f"select cr.crime_id, c.crime_name, c.crime_details, cr.crime_date, cr.crime_status, c.punishment, c.fine from crimerecord cr inner join crimes c on cr.crime_id = c.crime_id WHERE cr.person_id = {self.person_id}"
            Prop = RunQuery(query)
            self.address_display_data(Prop)
        except Exception as e:
            QMessageBox.warning(self, "Server Error", str(e))

    def address_display_data(self, data):
        num_rows = len(data)
        self.crime_view_table.setRowCount(num_rows)

        for row, row_data in enumerate(data):
            for col, value in enumerate(row_data.values()):
                # self.contact_ph_no_table.insertRow(row)
                item = QTableWidgetItem(str(value))
                if col in [1,2, 4]:
                    item.setFlags(item.flags() | Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEditable)
                self.crime_view_table.setItem(row, col, item)
                # self.address_view_table.setItem(row, 0, QTableWidgetItem(value))

                delete_button_layout = QHBoxLayout()
                delete_button_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

                self.insert_phone_delete_button = QPushButton("X")
                self.insert_phone_delete_button.setFixedSize(25, 25)
                self.insert_phone_delete_button.setGeometry(0, 0, 25, 25)
                self.insert_phone_delete_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
                self.insert_phone_delete_button.setIconSize(QSize(20, 20))  # Set icon size
                self.insert_phone_delete_button.setObjectName("insert_phone_delete_button")
                self.insert_phone_delete_button.clicked.connect(lambda _, row=row: self.delete_crime(data[row]))

                delete_button_layout.addWidget(self.insert_phone_delete_button)
                cell_widget = QWidget()
                cell_widget.setLayout(delete_button_layout)
                self.crime_view_table.setCellWidget(row, 7, cell_widget)

        self.crime_view_table.resizeRowsToContents()

    def delete_crime(self, data):
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Confirmation")
        msg_box.setText("Are you sure you want to Delete?")
        msg_box.setStandardButtons(QMessageBox.StandardButton.Cancel | QMessageBox.StandardButton.Ok)
        msg_box.setDefaultButton(QMessageBox.StandardButton.Cancel)

        # Change button text
        ok_button = msg_box.button(QMessageBox.StandardButton.Ok)
        ok_button.setText("Delete")

        result = msg_box.exec()
        if result == QMessageBox.StandardButton.Ok:
            query = f"DELETE FROM crimerecord WHERE crime_id = '{data['crime_id']}' and person_id = {self.person_id} and crime_date = '{data['crime_date']}'"
            RunQuery(query)
            self.Crime_load_data()
        else:
            pass

class View_JailRecord_main_Widget(QWidget):
    def __init__(self, person_id):
        super().__init__()
        self.person_id = person_id
        self.setObjectName("View_education_main_Widget")
        self.setFixedSize(950, 500)

        self.View_crime_Label = QLabel("Jail Record", self)
        self.View_crime_Label.setObjectName("View_address_Label")
        self.View_crime_Label.setGeometry(370, 20, 350, 50)

        self.education_view_sub_widget = QWidget(self)
        self.education_view_sub_widget.setObjectName("address_view_sub_widget")
        self.education_view_sub_widget.setGeometry(75, 90, 800, 370)

        self.crime_view_table = QTableWidget(self.education_view_sub_widget)
        self.crime_view_table.setObjectName("address_view_table")
        self.crime_view_table.setGeometry(25, 40, 750, 290)
        self.crime_view_table.setColumnCount(6)
        self.crime_view_table.setHorizontalHeaderLabels([
            "Jail Name",
            "Location",
            "Jailed Date",
            "Release Date",
            "Status",
            "Delete"
        ])
        self.crime_view_table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.crime_view_table.horizontalHeader().setStyleSheet(
            "QHeaderView::section{font-weight: bold;}")
        self.crime_view_table.verticalHeader().setStyleSheet(
            "QHeaderView::section{font-weight: bold;}")

        self.crime_view_table.setColumnWidth(0, 170)
        self.crime_view_table.setColumnWidth(1, 150)
        self.crime_view_table.setColumnWidth(2, 100)
        self.crime_view_table.setColumnWidth(3, 100)
        self.crime_view_table.setColumnWidth(4, 100)
        self.crime_view_table.setColumnWidth(5, 50)
        self.crime_view_table.horizontalHeader().setStretchLastSection(True)
        self.crime_view_table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.crime_view_table.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)

        self.Crime_load_data()
        with open("./test.css", "r") as f:
            self.setStyleSheet(f.read())

    def Crime_load_data(self):
        try:
            query = f"select jr.jail_record_id, jd.jail_name, jd.jail_location , jr.jailed_date_in, jr.jailed_date_out, jr.jailed_status from jail_record jr inner join jail_details jd on jr.jail_id = jd.jail_id WHERE jr.person_id = {self.person_id}"
            Prop = RunQuery(query)
            self.address_display_data(Prop)
        except Exception as e:
            QMessageBox.warning(self, "Server Error", str(e))

    def address_display_data(self, data):
        num_rows = len(data)
        self.crime_view_table.setRowCount(num_rows)

        for row, row_data in enumerate(data):
            for col, value in enumerate(row_data.values()):
                if col == 0:  # Skip the first column (jail record ID)
                    continue
                item = QTableWidgetItem(str(value))
                if col in [1, 3, 4]:  # Make specific columns selectable and editable
                    item.setFlags(item.flags() | Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEditable)
                self.crime_view_table.setItem(row, col - 1, item)


                delete_button_layout = QHBoxLayout()
                delete_button_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

                self.insert_phone_delete_button = QPushButton("X")
                self.insert_phone_delete_button.setFixedSize(25, 25)
                self.insert_phone_delete_button.setGeometry(0, 0, 25, 25)
                self.insert_phone_delete_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
                self.insert_phone_delete_button.setIconSize(QSize(20, 20))  # Set icon size
                self.insert_phone_delete_button.setObjectName("insert_phone_delete_button")
                self.insert_phone_delete_button.clicked.connect(lambda _, row=row: self.delete_jail(data[row]))

                delete_button_layout.addWidget(self.insert_phone_delete_button)
                cell_widget = QWidget()
                cell_widget.setLayout(delete_button_layout)
                self.crime_view_table.setCellWidget(row, 5, cell_widget)

        self.crime_view_table.resizeRowsToContents()

    def delete_jail(self, data):
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Confirmation")
        msg_box.setText("Are you sure you want to Delete?")
        msg_box.setStandardButtons(QMessageBox.StandardButton.Cancel | QMessageBox.StandardButton.Ok)
        msg_box.setDefaultButton(QMessageBox.StandardButton.Cancel)

        # Change button text
        ok_button = msg_box.button(QMessageBox.StandardButton.Ok)
        ok_button.setText("Delete")

        result = msg_box.exec()
        if result == QMessageBox.StandardButton.Ok:
            query = f"DELETE FROM jail_record WHERE person_id = {self.person_id} and jail_record_id = {data['jail_record_id']}; "
            RunQuery(query)
            self.Crime_load_data()
        else:
            pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = View_JailRecord_main_Widget(2)
    window.show()
    sys.exit(app.exec())
