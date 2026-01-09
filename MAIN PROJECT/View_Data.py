from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QVBoxLayout, QGridLayout, \
    QButtonGroup, \
    QMessageBox, QRadioButton, QHBoxLayout, QGroupBox, QSizePolicy, QStackedWidget
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6 import QtGui
import sys

from View_Sub_Widget import *


class ViewWidget(QWidget):
    dataReturned = pyqtSignal(object)

    def __init__(self, person_id):
        super().__init__()
        self.setObjectName("View_Widget")
        self.setFixedSize(1000, 750)

        self.person_id = person_id

        self.View_stacked_widget = QStackedWidget(self)
        self.View_stacked_widget.setObjectName("View_stacked_widget")
        self.View_stacked_widget.setGeometry(25, 70, 950, 500)

        self.View_person_widget = Search_person_main_Widget(self.person_id)
        self.View_person_widget.dataReturned.connect(self.handle_data)
        self.View_person_widget.setObjectName("View_person_widget")

        self.search_contact_widget = View_Contact_Widget(self.person_id)
        self.search_contact_widget.setObjectName("search_contact_widget")
        #
        self.View_address_widget = View_Address_main_Widget(self.person_id)
        self.View_address_widget.setObjectName("View_address_widget")
        #
        self.view_education_widget = View_Education_main_Widget(self.person_id)
        self.view_education_widget.setObjectName("View_education_widget")
        #
        self.View_property_widget = View_Property_main_Widget(self.person_id)
        self.View_property_widget.setObjectName("View_property_widget")
        #
        self.View_employeement_widget = View_Employment_main_Widget(self.person_id)
        self.View_employeement_widget.setObjectName("View_employeement_widget")
        #
        self.View_vehicle_widget = View_Vehicles_main_Widget(self.person_id)
        self.View_vehicle_widget.setObjectName("View_vehicle_widget")
        #
        self.View_CrimeRecord_widget = View_CrimeRecord_main_Widget(self.person_id)
        self.View_CrimeRecord_widget.setObjectName("View_jailRecipe_widget")

        self.View_jailRecord_widget = View_JailRecord_main_Widget(self.person_id)
        self.View_jailRecord_widget.setObjectName("View_jailRecipe_widget")

        self.View_stacked_widget.addWidget(self.View_person_widget)

        self.View_stacked_widget.addWidget(self.View_address_widget)
        self.View_stacked_widget.addWidget(self.view_education_widget)

        self.View_stacked_widget.addWidget(self.View_employeement_widget)
        self.View_stacked_widget.addWidget(self.View_property_widget)
        self.View_stacked_widget.addWidget(self.View_vehicle_widget)
        self.View_stacked_widget.addWidget(self.View_CrimeRecord_widget)
        self.View_stacked_widget.addWidget(self.search_contact_widget)
        self.View_stacked_widget.addWidget(self.View_jailRecord_widget)

        self.search_person_btn = QPushButton("Person ", self)
        self.search_person_btn.setObjectName("Search_Person")
        self.search_person_btn.setGeometry(50, 600, 100, 30)
        self.search_person_btn.clicked.connect(self.search_person_btn_clicked)

        self.search_contact_btn = QPushButton("Contact  ", self)
        self.search_contact_btn.setObjectName("Search_contact")
        self.search_contact_btn.setGeometry(150, 600, 100, 30)
        self.search_contact_btn.clicked.connect(self.search_contact_btn_clicked)

        self.search_address_btn = QPushButton("Address ", self)
        self.search_address_btn.setObjectName("search_address")
        self.search_address_btn.setGeometry(250, 600, 100, 30)
        self.search_address_btn.clicked.connect(self.search_address_btn_clicked)

        self.search_education_btn = QPushButton("Education ", self)
        self.search_education_btn.setObjectName("Search_education")
        self.search_education_btn.setGeometry(350, 600, 100, 30)
        self.search_education_btn.clicked.connect(self.search_education_btn_clicked)

        self.View_property_btn = QPushButton("Property ", self)
        self.View_property_btn.setObjectName("Search_property")
        self.View_property_btn.setGeometry(450, 600, 100, 30)
        self.View_property_btn.clicked.connect(self.View_property_btn_clicked)

        self.search_employment_btn = QPushButton("Employment ", self)
        self.search_employment_btn.setObjectName("Search_employment")
        self.search_employment_btn.setGeometry(550, 600, 100, 30)
        self.search_employment_btn.clicked.connect(self.View_employment_btn_clicked)

        self.View_vehicle_btn = QPushButton("Vehicle ", self)
        self.View_vehicle_btn.setObjectName("Search_vehicle")
        self.View_vehicle_btn.setGeometry(650, 600, 100, 30)
        self.View_vehicle_btn.clicked.connect(self.View_vehicle_btn_clicked)

        self.search_jailRecord_btn = QPushButton("Crime Record ", self)
        self.search_jailRecord_btn.setObjectName("Search_CrimeRecord")
        self.search_jailRecord_btn.setGeometry(750, 600, 100, 30)
        self.search_jailRecord_btn.clicked.connect(self.View_CrimeRecord_btn_clicked)

        self.search_jailRecord_btn = QPushButton("Jail Record ", self)
        self.search_jailRecord_btn.setObjectName("Search_jailRecord")
        self.search_jailRecord_btn.setGeometry(850, 600, 100, 30)
        self.search_jailRecord_btn.clicked.connect(self.View_jailRecord_btn_clicked)

        with open("style.css") as style:
            self.setStyleSheet(style.read())

    def handle_data(self, data):
        if data == "Delete":
            self.dataReturned.emit("Delete")

    def search_person_btn_clicked(self):
        self.View_stacked_widget.setCurrentIndex(0)

    def search_contact_btn_clicked(self):
        self.View_stacked_widget.setCurrentIndex(7)

    def search_address_btn_clicked(self):
        self.View_stacked_widget.setCurrentIndex(1)

    #
    def search_education_btn_clicked(self):
        self.View_stacked_widget.setCurrentIndex(2)

    #
    def View_property_btn_clicked(self):
        self.View_stacked_widget.setCurrentIndex(4)

    #
    def View_employment_btn_clicked(self):
        self.View_stacked_widget.setCurrentIndex(3)

    #
    def View_vehicle_btn_clicked(self):
        self.View_stacked_widget.setCurrentIndex(5)

    def View_CrimeRecord_btn_clicked(self):
        self.View_stacked_widget.setCurrentIndex(6)
    #
    def View_jailRecord_btn_clicked(self):
        self.View_stacked_widget.setCurrentWidget(self.View_jailRecord_widget)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ViewWidget(2)
    window.show()
    sys.exit(app.exec())
