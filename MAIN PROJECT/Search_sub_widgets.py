from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QVBoxLayout, QGridLayout, \
    QButtonGroup, \
    QMessageBox, QRadioButton, QHBoxLayout, QGroupBox, QSizePolicy, QStackedWidget
from PyQt6.QtCore import Qt, QSize, pyqtSignal
from PyQt6.QtGui import QIcon, QPixmap, QFont
from PyQt6 import QtGui
from VIEWCARDS import *
import sys


class Search_person_main_Widget(QWidget):
    dataReturned = pyqtSignal(object)

    def __init__(self):
        super().__init__()
        self.setObjectName("Search_person_main_Widget")
        self.setFixedSize(700, 450)

        self.returned_data = None

        self.Search_person_Label = QLabel("Search Personal Details", self)
        self.Search_person_Label.setObjectName("Search_person_Label")
        self.Search_person_Label.setGeometry(175, 30, 400, 50)
        self.Search_person_Label.setFont(QFont("Arial", 16))

        self.First_Name = QRadioButton("First Name", self)
        self.First_Name.setObjectName("First_Name")
        self.First_Name.setGeometry(100, 100, 200, 50)
        self.First_Name.setFont(QFont("Arial", 12))

        self.First_Name_lineedit = QLineEdit(self)
        self.First_Name_lineedit.setObjectName("First_Name_lineedit")
        self.First_Name_lineedit.setGeometry(300, 110, 200, 25)

        self.Last_Name = QRadioButton("Last Name", self)
        self.Last_Name.setObjectName("Last_Name")
        self.Last_Name.setGeometry(100, 150, 200, 50)
        self.Last_Name.setFont(QFont("Arial", 12))

        self.Last_Name_lineedit = QLineEdit(self)
        self.Last_Name_lineedit.setObjectName("Last_Name_lineedit")
        self.Last_Name_lineedit.setGeometry(300, 160, 200, 25)

        self.age_label = QRadioButton("Age", self)
        self.age_label.setObjectName("age_label")
        self.age_label.setGeometry(100, 200, 200, 50)
        self.age_label.setFont(QFont("Arial", 12))

        self.age_lineedit = QLineEdit(self)
        self.age_lineedit.setObjectName("age_lineedit")
        self.age_lineedit.setGeometry(300, 210, 200, 25)

        self.cnic_number = QRadioButton("CNIC Number", self)
        self.cnic_number.setObjectName("cnic_number")
        self.cnic_number.setGeometry(100, 250, 200, 50)
        self.cnic_number.setFont(QFont("Arial", 12))

        self.cnic_number_lineedit = QLineEdit(self)
        self.cnic_number_lineedit.setObjectName("cnic_number_lineedit")
        self.cnic_number_lineedit.setGeometry(300, 260, 200, 25)

        self.family_id = QRadioButton("Family ID ", self)
        self.family_id.setObjectName("family_id")
        self.family_id.setGeometry(100, 300, 200, 50)
        self.family_id.setFont(QFont("Arial", 12))

        self.family_id_lineedit = QLineEdit(self)
        self.family_id_lineedit.setObjectName("family_id_lineedit")
        self.family_id_lineedit.setGeometry(300, 310, 200, 25)

        self.search_button = QPushButton("Search", self)
        self.search_button.setObjectName("search_button")
        self.search_button.setGeometry(400, 400, 200, 30)
        self.search_button.clicked.connect(self.search_person)

        with open("style.css") as style:
            self.setStyleSheet(style.read())

    def search_person(self):
        selected_criteria = None
        line_edit = None

        if self.First_Name.isChecked():
            selected_criteria = "f_name"
            line_edit = self.First_Name_lineedit
        elif self.Last_Name.isChecked():
            selected_criteria = "l_name"
            line_edit = self.Last_Name_lineedit
        elif self.age_label.isChecked():
            selected_criteria = "age"
            line_edit = self.age_lineedit
        elif self.cnic_number.isChecked():
            selected_criteria = "cnic_number"
            line_edit = self.cnic_number_lineedit
        elif self.family_id.isChecked():
            selected_criteria = "family_id"
            line_edit = self.family_id_lineedit

        if not selected_criteria:
            QMessageBox.warning(self, "No Criteria", "Please select a search criteria.")
            return

        search_value = line_edit.text().strip()
        if not search_value:
            QMessageBox.warning(self, "No Value", "Please enter a value for the selected criteria.")
            return

        query = f"SELECT person_id, f_name, l_name, gender, age, cnic_number, nationality, religion FROM person WHERE LOWER({selected_criteria}) = LOWER('{search_value}')"

        result = RunQuery(query)
        if not result:
            QMessageBox.information(self, "Search Result", "No matching records found.")
            return

        QMessageBox.information(self, "Search Result", f"Found {len(result)} matching records.")

        self.dataReturned.emit(result)


class Search_Contact_main_Widget(QWidget):
    dataReturned = pyqtSignal(object)

    def __init__(self):
        super().__init__()
        self.setObjectName("Search_Contact_main_Widget")
        self.setFixedSize(700, 450)

        self.Search_contact_Label = QLabel("Search Contact Details", self)
        self.Search_contact_Label.setObjectName("Search_contact_Label")
        self.Search_contact_Label.setGeometry(175, 30, 400, 50)
        self.setFont(QFont("Arial", 16))

        self.Phone_number = QRadioButton("Phone Number", self)
        self.Phone_number.setObjectName("Phone_number")
        self.Phone_number.setGeometry(100, 100, 200, 50)
        self.setFont(QFont("Arial", 12))

        self.Phone_number_lineedit = QLineEdit(self)
        self.Phone_number_lineedit.setObjectName("Phone_number_lineedit")
        self.Phone_number_lineedit.setGeometry(300, 110, 200, 25)

        self.emails = QRadioButton("Email", self)
        self.emails.setObjectName("emails")
        self.emails.setGeometry(100, 150, 200, 50)
        self.setFont(QFont("Arial", 12))

        self.emails_lineedit = QLineEdit(self)
        self.emails_lineedit.setObjectName("emails_lineedit")
        self.emails_lineedit.setGeometry(300, 160, 200, 25)

        self.search_button = QPushButton("Search", self)
        self.search_button.setObjectName("search_button")
        self.search_button.setGeometry(400, 400, 200, 30)
        self.search_button.clicked.connect(self.search_contact)

        with open("style.css") as style:
            self.setStyleSheet(style.read())

    def search_contact(self):
        # Check if at least one field is selected for search
        if not (self.Phone_number.isChecked() or self.emails.isChecked()):
            QMessageBox.warning(self, "Search Criteria", "Please select at least one field for search.")
            return

        if self.Phone_number.isChecked():
            search_value = self.Phone_number_lineedit.text().strip()
            query = f"SELECT person_id FROM phone_numbers WHERE phone_number = '{search_value}'"
        elif self.emails.isChecked():
            search_value = self.emails_lineedit.text().strip()
            query = f"SELECT person_id FROM emails WHERE LOWER(email_address) = LOWER('{search_value}')"

        result = RunQuery(query)
        if not result:
            QMessageBox.information(self, "Search Result", "No matching records found.")
            return
        QMessageBox.information(self, "Search Result", f"Found {len(result)} matching records.")

        person_ids = [item['person_id'] for item in result]
        person_ids = ', '.join([str(id) for id in person_ids])

        query = f"SELECT person_id, f_name, l_name, gender, age, cnic_number, nationality, religion FROM person WHERE person_id IN ({person_ids})"
        result = RunQuery(query)

        self.dataReturned.emit(result)


class Serach_Address_main_Widget(QWidget):
    dataReturned = pyqtSignal(object)

    def __init__(self):
        super().__init__()
        self.setObjectName("Search_address_main_Widget")
        self.setFixedSize(700, 450)

        # Establish database connection

        self.Search_address_Label = QLabel("Search Address Details", self)
        self.Search_address_Label.setObjectName("Search_address_Label")
        self.Search_address_Label.setGeometry(175, 30, 400, 50)
        self.Search_address_Label.setFont(QFont("Arial", 16))

        # Radio buttons and line edits for search criteria
        self.Address = QRadioButton("Address", self)
        self.Address.setObjectName("Address")
        self.Address.setGeometry(100, 100, 200, 50)
        self.Address.setFont(QFont("Arial", 12))

        self.Address_lineedit = QLineEdit(self)
        self.Address_lineedit.setObjectName("Address_lineedit")
        self.Address_lineedit.setGeometry(300, 110, 200, 25)

        self.City = QRadioButton("City", self)
        self.City.setObjectName("City")
        self.City.setGeometry(100, 150, 200, 50)
        self.City.setFont(QFont("Arial", 12))

        self.City_lineedit = QLineEdit(self)
        self.City_lineedit.setObjectName("City_lineedit")
        self.City_lineedit.setGeometry(300, 160, 200, 25)

        self.State_label = QRadioButton("State", self)
        self.State_label.setObjectName("State_label")
        self.State_label.setGeometry(100, 200, 200, 50)
        self.State_label.setFont(QFont("Arial", 12))

        self.State_lineedit = QLineEdit(self)
        self.State_lineedit.setObjectName("State_lineedit")
        self.State_lineedit.setGeometry(300, 210, 200, 25)

        self.Country = QRadioButton("Country", self)
        self.Country.setObjectName("Country")
        self.Country.setGeometry(100, 250, 200, 50)
        self.Country.setFont(QFont("Arial", 12))

        self.Country_lineedit = QLineEdit(self)
        self.Country_lineedit.setObjectName("Country_lineedit")
        self.Country_lineedit.setGeometry(300, 260, 200, 25)

        # Search button
        self.search_button = QPushButton("Search", self)
        self.search_button.setObjectName("search_button")
        self.search_button.setGeometry(400, 400, 200, 30)
        self.search_button.clicked.connect(self.search_address)

        # Apply style from CSS file
        with open("style.css") as style:
            self.setStyleSheet(style.read())

    def search_address(self):
        # Check if at least one field is selected for search
        if not (
                self.Address.isChecked() or self.City.isChecked() or self.State_label.isChecked() or self.Country.isChecked()):
            QMessageBox.warning(self, "Search Criteria", "Please select at least one field for search.")
            return

        # Perform search in the database
        selected_criteria = None
        search_value = None

        # Determine selected criteria and corresponding search value
        if self.Address.isChecked():
            selected_criteria = "address"
            search_value = self.Address_lineedit.text().strip()
        elif self.City.isChecked():
            selected_criteria = "adr_city"
            search_value = self.City_lineedit.text().strip()
        elif self.State_label.isChecked():
            selected_criteria = "adr_state"
            search_value = self.State_lineedit.text().strip()
        elif self.Country.isChecked():
            selected_criteria = "adr_country"
            search_value = self.Country_lineedit.text().strip()

        query = f"SELECT person_id FROM addresses WHERE LOWER({selected_criteria}) = LOWER('{search_value}')"
        result = RunQuery(query)
        if not result:
            QMessageBox.information(self, "Search Result", "No matching records found.")
            return
        QMessageBox.information(self, "Search Result", f"Found {len(result)} matching records.")

        # person_ids = [record[0] for record in result]
        person_ids = [item['person_id'] for item in result]
        person_ids = ', '.join([str(id) for id in person_ids])

        query = f"SELECT person_id, f_name, l_name, gender, age, cnic_number, nationality, religion FROM person WHERE person_id IN ({person_ids})"
        result = RunQuery(query)

        self.dataReturned.emit(result)


class Search_Education_main_Widget(QWidget):
    dataReturned = pyqtSignal(object)

    def __init__(self):
        super().__init__()
        self.setObjectName("Search_Education_main_Widget")
        self.setFixedSize(700, 450)

        self.Search_Education_Label = QLabel("Search Education Details", self)
        self.Search_Education_Label.setObjectName("Search_Education_Label")
        self.Search_Education_Label.setGeometry(175, 30, 400, 50)
        self.Search_Education_Label.setFont(QFont("Arial", 16))

        # Radio buttons and line edits for search criteria
        self.Degree_Name = QRadioButton("Degree Name", self)
        self.Degree_Name.setObjectName("Degree_Name")
        self.Degree_Name.setGeometry(100, 100, 200, 50)
        self.Degree_Name.setFont(QFont("Arial", 12))

        self.Degree_Name_lineedit = QLineEdit(self)
        self.Degree_Name_lineedit.setObjectName("Degree_Name_lineedit")
        self.Degree_Name_lineedit.setGeometry(300, 110, 200, 25)

        self.Registration_id = QRadioButton("Registration ID", self)
        self.Registration_id.setObjectName("Registration_id")
        self.Registration_id.setGeometry(100, 150, 200, 50)
        self.Registration_id.setFont(QFont("Arial", 12))

        self.Registration_id_lineedit = QLineEdit(self)
        self.Registration_id_lineedit.setObjectName("Registration_id_lineedit")
        self.Registration_id_lineedit.setGeometry(300, 160, 200, 25)

        self.Institute_label = QRadioButton("Institute", self)
        self.Institute_label.setObjectName("Institute_label")
        self.Institute_label.setGeometry(100, 200, 200, 50)
        self.Institute_label.setFont(QFont("Arial", 12))

        self.Institute_lineedit = QLineEdit(self)
        self.Institute_lineedit.setObjectName("Institute_lineedit")
        self.Institute_lineedit.setGeometry(300, 210, 200, 25)

        # Search button
        self.search_button = QPushButton("Search", self)
        self.search_button.setObjectName("search_button")
        self.search_button.setGeometry(400, 400, 200, 30)
        self.search_button.clicked.connect(self.search_education)

        # Apply style from CSS file
        with open("style.css") as style:
            self.setStyleSheet(style.read())

    def search_education(self):
        # Check if at least one field is selected for search
        if not (self.Degree_Name.isChecked() or self.Registration_id.isChecked() or self.Institute_label.isChecked()):
            QMessageBox.warning(self, "Search Criteria", "Please select at least one field for search.")
            return

        if self.Degree_Name.isChecked():
            selected_criteria = "degree_name"
            search_value = self.Degree_Name_lineedit.text().strip()
        elif self.Registration_id.isChecked():
            selected_criteria = "edu_reg_id"
            search_value = self.Registration_id_lineedit.text().strip()
        elif self.Institute_label.isChecked():
            selected_criteria = "edu_institute"
            search_value = self.Institute_lineedit.text().strip()

        query = f"SELECT person_id FROM education WHERE LOWER({selected_criteria}) = LOWER('{search_value}')"
        result = RunQuery(query)
        if not result:
            QMessageBox.information(self, "Search Result", "No matching records found.")
            return
        QMessageBox.information(self, "Search Result", f"Found {len(result)} matching records.")

        # person_ids = [record[0] for record in result]
        person_ids = [item['person_id'] for item in result]
        person_ids = ', '.join([str(id) for id in person_ids])

        query = f"SELECT person_id, f_name, l_name, gender, age, cnic_number, nationality, religion FROM person WHERE person_id IN ({person_ids})"
        result = RunQuery(query)

        self.dataReturned.emit(result)


class Search_Property_main_Widget(QWidget):
    dataReturned = pyqtSignal(object)

    def __init__(self):
        super().__init__()
        self.setObjectName("Search_Property_main_Widget")
        self.setFixedSize(700, 450)

        # Establish database connection

        self.Search_Property_Label = QLabel("Search Property Details", self)
        self.Search_Property_Label.setObjectName("Search_Property_Label")
        self.Search_Property_Label.setGeometry(175, 30, 400, 50)
        self.Search_Property_Label.setFont(QFont("Arial", 16))

        # Radio buttons and line edits for search criteria
        self.Property_Type = QRadioButton("Property Type", self)
        self.Property_Type.setObjectName("Property_Type")
        self.Property_Type.setGeometry(100, 100, 200, 50)
        self.Property_Type.setFont(QFont("Arial", 12))

        self.Property_Type_lineedit = QLineEdit(self)
        self.Property_Type_lineedit.setObjectName("Property_Type_lineedit")
        self.Property_Type_lineedit.setGeometry(300, 110, 200, 25)

        self.address = QRadioButton("Address", self)
        self.address.setObjectName("address")
        self.address.setGeometry(100, 150, 200, 50)
        self.address.setFont(QFont("Arial", 12))

        self.address_lineedit = QLineEdit(self)
        self.address_lineedit.setObjectName("address_lineedit")
        self.address_lineedit.setGeometry(300, 160, 200, 25)

        self.Registration_Id_label = QRadioButton("Registration ID", self)
        self.Registration_Id_label.setObjectName("Registration_Id_label")
        self.Registration_Id_label.setGeometry(100, 200, 200, 50)
        self.Registration_Id_label.setFont(QFont("Arial", 12))

        self.Registration_Id_lineedit = QLineEdit(self)
        self.Registration_Id_lineedit.setObjectName("Registration_Id_lineedit")
        self.Registration_Id_lineedit.setGeometry(300, 210, 200, 25)

        # Search button
        self.search_button = QPushButton("Search", self)
        self.search_button.setObjectName("search_button")
        self.search_button.setGeometry(400, 400, 200, 30)
        self.search_button.clicked.connect(self.search_property)

        # Apply style from CSS file
        with open("style.css") as style:
            self.setStyleSheet(style.read())

    def search_property(self):
        # Check if at least one field is selected for search
        if not (self.Property_Type.isChecked() or self.address.isChecked() or self.Registration_Id_label.isChecked()):
            QMessageBox.warning(self, "Search Criteria", "Please select at least one field for search.")
            return

        if self.Property_Type.isChecked():
            selected_criteria = "property_type"
            search_value = self.Property_Type_lineedit.text().strip()
        elif self.address.isChecked():
            selected_criteria = "property_address"
            search_value = self.address_lineedit.text().strip()
        elif self.Registration_Id_label.isChecked():
            selected_criteria = "property_reg_id"
            search_value = self.Registration_Id_lineedit.text().strip()

        query = f"SELECT person_id FROM property WHERE LOWER({selected_criteria}) = LOWER('{search_value}')"
        result = RunQuery(query)
        if not result:
            QMessageBox.information(self, "Search Result", "No matching records found.")
            return
        QMessageBox.information(self, "Search Result", f"Found {len(result)} matching records.")

        # person_ids = [record[0] for record in result]
        person_ids = [item['person_id'] for item in result]
        person_ids = ', '.join([str(id) for id in person_ids])

        query = f"SELECT person_id, f_name, l_name, gender, age, cnic_number, nationality, religion FROM person WHERE person_id IN ({person_ids})"
        result = RunQuery(query)

        self.dataReturned.emit(result)


class Search_Employeement_main_Widget(QWidget):
    dataReturned = pyqtSignal(object)
    def __init__(self):
        super().__init__()
        self.setObjectName("Search_Employment_main_Widget")
        self.setFixedSize(700, 450)

        # Establish database connection

        self.Search_Employment_Label = QLabel("Search Employment Details", self)
        self.Search_Employment_Label.setObjectName("Search_Employment_Label")
        self.Search_Employment_Label.setGeometry(175, 30, 400, 50)
        self.Search_Employment_Label.setFont(QFont("Arial", 16))

        # Radio buttons and line edits for search criteria
        self.Company_Name = QRadioButton("Company Name", self)
        self.Company_Name.setObjectName("Company_Name")
        self.Company_Name.setGeometry(100, 100, 200, 50)
        self.Company_Name.setFont(QFont("Arial", 12))

        self.Company_Name_lineedit = QLineEdit(self)
        self.Company_Name_lineedit.setObjectName("Company_Name_lineedit")
        self.Company_Name_lineedit.setGeometry(300, 110, 200, 25)

        self.Address = QRadioButton("Address", self)
        self.Address.setObjectName("Address")
        self.Address.setGeometry(100, 150, 200, 50)
        self.Address.setFont(QFont("Arial", 12))

        self.Address_lineedit = QLineEdit(self)
        self.Address_lineedit.setObjectName("Address_lineedit")
        self.Address_lineedit.setGeometry(300, 160, 200, 25)

        self.Job_Name_label = QRadioButton("Job Name", self)
        self.Job_Name_label.setObjectName("Job_Name_label")
        self.Job_Name_label.setGeometry(100, 200, 200, 50)
        self.Job_Name_label.setFont(QFont("Arial", 12))

        self.Job_Name_lineedit = QLineEdit(self)
        self.Job_Name_lineedit.setObjectName("Job_Name_lineedit")
        self.Job_Name_lineedit.setGeometry(300, 210, 200, 25)

        self.Job_ID = QRadioButton("Job ID", self)
        self.Job_ID.setObjectName("Job_ID")
        self.Job_ID.setGeometry(100, 250, 200, 50)
        self.Job_ID.setFont(QFont("Arial", 12))

        self.Job_ID_lineedit = QLineEdit(self)
        self.Job_ID_lineedit.setObjectName("Job_ID_lineedit")
        self.Job_ID_lineedit.setGeometry(300, 260, 200, 25)

        # Search button
        self.search_button = QPushButton("Search", self)
        self.search_button.setObjectName("search_button")
        self.search_button.setGeometry(400, 400, 200, 30)
        self.search_button.clicked.connect(self.search_employment)

        # Apply style from CSS file
        with open("style.css") as style:
            self.setStyleSheet(style.read())

    def search_employment(self):
        # Check if at least one field is selected for search
        if not (
                self.Company_Name.isChecked() or self.Address.isChecked() or self.Job_Name_label.isChecked() or self.Job_ID.isChecked()):
            QMessageBox.warning(self, "Search Criteria", "Please select at least one field for search.")
            return

        if self.Company_Name.isChecked():
            selected_criteria = "employment_company"
            search_value = self.Company_Name_lineedit.text().strip()
        elif self.Address.isChecked():
            selected_criteria = "company_address"
            search_value = self.Address_lineedit.text().strip()
        elif self.Job_Name_label.isChecked():
            selected_criteria = "job_name"
            search_value = self.Job_Name_lineedit.text().strip()
        elif self.Job_ID.isChecked():
            selected_criteria = "job_id"
            search_value = self.Job_ID_lineedit.text().strip()

        query = f"SELECT person_id FROM employment WHERE LOWER({selected_criteria}) = LOWER('{search_value}')"
        result = RunQuery(query)
        if not result:
            QMessageBox.information(self, "Search Result", "No matching records found.")
            return
        QMessageBox.information(self, "Search Result", f"Found {len(result)} matching records.")

        # person_ids = [record[0] for record in result]
        person_ids = [item['person_id'] for item in result]
        person_ids = ', '.join([str(id) for id in person_ids])

        query = f"SELECT person_id, f_name, l_name, gender, age, cnic_number, nationality, religion FROM person WHERE person_id IN ({person_ids})"
        result = RunQuery(query)

        self.dataReturned.emit(result)


class Search_Vehicle_main_Widget(QWidget):
    dataReturned = pyqtSignal(object)
    def __init__(self):
        super().__init__()
        self.setObjectName("Search_Vehicle_main_Widget")
        self.setFixedSize(700, 450)

        self.Search_Vehicle_Label = QLabel("Search Vehicle Details", self)
        self.Search_Vehicle_Label.setObjectName("Search_Vehicle_Label")
        self.Search_Vehicle_Label.setGeometry(175, 30, 400, 50)
        self.Search_Vehicle_Label.setFont(QFont("Arial", 16))

        # Radio buttons and line edits for search criteria
        self.Vehicle_Maker = QRadioButton("Vehicle Maker", self)
        self.Vehicle_Maker.setObjectName("Vehicle_Maker")
        self.Vehicle_Maker.setGeometry(100, 100, 200, 50)
        self.Vehicle_Maker.setFont(QFont("Arial", 12))

        self.Vehicle_Maker_lineedit = QLineEdit(self)
        self.Vehicle_Maker_lineedit.setObjectName("Vehicle_Maker_lineedit")
        self.Vehicle_Maker_lineedit.setGeometry(300, 110, 200, 25)

        self.Vehicle_Model = QRadioButton("Vehicle Model", self)
        self.Vehicle_Model.setObjectName("Vehicle_Model")
        self.Vehicle_Model.setGeometry(100, 150, 200, 50)
        self.Vehicle_Model.setFont(QFont("Arial", 12))

        self.Vehicle_Model_lineedit = QLineEdit(self)
        self.Vehicle_Model_lineedit.setObjectName("Vehicle_Model_lineedit")
        self.Vehicle_Model_lineedit.setGeometry(300, 160, 200, 25)

        self.Registration_Date = QRadioButton("Registration Year", self)
        self.Registration_Date.setObjectName("Registration_Date")
        self.Registration_Date.setGeometry(100, 200, 200, 50)
        self.Registration_Date.setFont(QFont("Arial", 12))

        self.Registration_Date_lineedit = QLineEdit(self)
        self.Registration_Date_lineedit.setObjectName("Registration_Date_lineedit")
        self.Registration_Date_lineedit.setGeometry(300, 210, 200, 25)

        self.Vehicle_Color = QRadioButton("Vehicle Color", self)
        self.Vehicle_Color.setObjectName("Vehicle_Color")
        self.Vehicle_Color.setGeometry(100, 250, 200, 50)
        self.Vehicle_Color.setFont(QFont("Arial", 12))

        self.Vehicle_Color_lineedit = QLineEdit(self)
        self.Vehicle_Color_lineedit.setObjectName("Vehicle_Color_lineedit")
        self.Vehicle_Color_lineedit.setGeometry(300, 260, 200, 25)

        self.Vehicle_registration = QRadioButton("Registration ID", self)
        self.Vehicle_registration.setObjectName("Vehicle_Color")
        self.Vehicle_registration.setGeometry(100, 300, 200, 50)
        self.Vehicle_registration.setFont(QFont("Arial", 12))

        self.Vehicle_registration_lineedit = QLineEdit(self)
        self.Vehicle_registration_lineedit.setObjectName("Vehicle_Color_lineedit")
        self.Vehicle_registration_lineedit.setGeometry(300, 310, 200, 25)


        # Search button
        self.search_button = QPushButton("Search", self)
        self.search_button.setObjectName("search_button")
        self.search_button.setGeometry(400, 400, 200, 30)
        self.search_button.clicked.connect(self.search_vehicle)

        # Apply style from CSS file
        with open("style.css") as style:
            self.setStyleSheet(style.read())

    def search_vehicle(self):
        # Check if at least one field is selected for search
        if not (self.Vehicle_Maker.isChecked() or self.Vehicle_Model.isChecked() or
                self.Registration_Date.isChecked() or self.Vehicle_Color.isChecked() or self.Vehicle_registration.isChecked()):
            QMessageBox.warning(self, "Search Criteria", "Please select at least one field for search.")
            return

        if self.Vehicle_Maker.isChecked():
            selected_criteria = "vehicle_maker"
            search_value = self.Vehicle_Maker_lineedit.text().strip()
        elif self.Vehicle_Model.isChecked():
            selected_criteria = "vehicle_model"
            search_value = self.Vehicle_Model_lineedit.text().strip()
        elif self.Registration_Date.isChecked():
            selected_criteria = "YEAR(vehicle_year)"
            search_value = self.Registration_Date_lineedit.text().strip()
        elif self.Vehicle_Color.isChecked():
            selected_criteria = "vehicle_color"
            search_value = self.Vehicle_Color_lineedit.text().strip()
        elif self.Vehicle_registration.isChecked():
            selected_criteria = "vehicle_reg_number"
            search_value = self.Vehicle_registration_lineedit.text().strip()

        query = f"SELECT person_id FROM vehicles WHERE LOWER({selected_criteria}) = LOWER('{search_value}')"
        result = RunQuery(query)
        if not result:
            QMessageBox.information(self, "Search Result", "No matching records found.")
            return
        QMessageBox.information(self, "Search Result", f"Found {len(result)} matching records.")

        # person_ids = [record[0] for record in result]
        person_ids = [item['person_id'] for item in result]
        person_ids = ', '.join([str(id) for id in person_ids])

        query = f"SELECT person_id, f_name, l_name, gender, age, cnic_number, nationality, religion FROM person WHERE person_id IN ({person_ids})"
        result = RunQuery(query)

        self.dataReturned.emit(result)


class Search_JailRecord_main_Widget(QWidget):
    dataReturned = pyqtSignal(object)
    def __init__(self):
        super().__init__()
        self.setObjectName("Search_JailRecord_main_Widget")
        self.setFixedSize(700, 450)

        self.Search_JailRecord_Label = QLabel("Search Criminal Details", self)
        self.Search_JailRecord_Label.setObjectName("Search_JailRecord_Label")
        self.Search_JailRecord_Label.setGeometry(175, 30, 400, 50)
        self.setFont(QFont("Arial", 16))

        self.jail_location = QRadioButton("Jail location", self)
        self.jail_location.setObjectName("jail_location")
        self.jail_location.setGeometry(100, 100, 200, 50)
        self.jail_location.setFont(QFont("Arial", 12))

        self.jail_location_lineedit = QLineEdit(self)
        self.jail_location_lineedit.setObjectName("jail_location_lineedit")
        self.jail_location_lineedit.setGeometry(300, 110, 200, 25)

        self.Jail_Name = QRadioButton("Jail Name", self)
        self.Jail_Name.setObjectName("Jail_Name")
        self.Jail_Name.setGeometry(100, 150, 200, 50)
        self.setFont(QFont("Arial", 12))

        self.Jail_Name_lineedit = QLineEdit(self)
        self.Jail_Name_lineedit.setObjectName("Jail_Name_lineedit")
        self.Jail_Name_lineedit.setGeometry(300, 160, 200, 25)

        self.crime_Name = QRadioButton("Crime Name", self)
        self.crime_Name.setObjectName("Crime_Name")
        self.crime_Name.setGeometry(100, 200, 200, 50)
        self.setFont(QFont("Arial", 12))

        self.crime_Name_lineedit = QLineEdit(self)
        self.crime_Name_lineedit.setObjectName("crime_Name_lineedit")
        self.crime_Name_lineedit.setGeometry(300, 210, 200, 25)

        self.search_button = QPushButton("Search", self)
        self.search_button.setObjectName("search_button")
        self.search_button.setGeometry(400, 400, 200, 30)
        self.search_button.clicked.connect(self.search_jailrecord)

        with open("style.css") as style:
            self.setStyleSheet(style.read())

    def search_jailrecord(self):
        # Check if at least one field is selected for search
        if not (self.jail_location.isChecked() or self.Jail_Name.isChecked() or self.crime_Name.isChecked()):
            QMessageBox.warning(self, "Search Criteria", "Please select at least one field for search.")
            return

        if self.jail_location.isChecked():
            search_value = self.jail_location_lineedit.text().strip()
            query = f"select p.person_id from person p inner join jail_record jr inner join jail_details jd on p.person_id = jr.person_id and jr.jail_id = jd.jail_id where LOWER(jd.jail_location) = LOWER('{search_value}') "
        elif self.Jail_Name.isChecked():
            search_value = self.Jail_Name_lineedit.text().strip()
            query = f"select p.person_id from person p inner join jail_record jr inner join jail_details jd on p.person_id = jr.person_id and jr.jail_id = jd.jail_id where LOWER(jd.jail_name) = LOWER('{search_value}') "
        elif self.crime_Name.isChecked():
            search_value = self.crime_Name_lineedit.text().strip()
            query = f"select p.person_id from person p inner join crimerecord cr inner join crimes c on p.person_id = cr.person_id and cr.crime_id = c.crime_id where LOWER(crime_name) = LOWER('{search_value}')"

        result = RunQuery(query)
        if not result:
            QMessageBox.information(self, "Search Result", "No matching records found.")
            return
        QMessageBox.information(self, "Search Result", f"Found {len(result)} matching records.")

        # person_ids = [record[0] for record in result]
        person_ids = [item['person_id'] for item in result]
        person_ids = ', '.join([str(id) for id in person_ids])

        query = f"SELECT person_id, f_name, l_name, gender, age, cnic_number, nationality, religion FROM person WHERE person_id IN ({person_ids})"
        result = RunQuery(query)

        self.dataReturned.emit(result)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Search_Contact_main_Widget()
    window.show()
    sys.exit(app.exec())
