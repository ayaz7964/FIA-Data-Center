from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QVBoxLayout, QGridLayout, \
    QButtonGroup, \
    QMessageBox, QRadioButton, QHBoxLayout, QGroupBox, QSizePolicy, QStackedWidget
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon, QPixmap, QPalette, QColor
from PyQt6 import QtGui
import sys

from Search_sub_widgets import *


class SearchWidget(QWidget):
    dataReturned = pyqtSignal(object)

    def __init__(self):
        super().__init__()
        self.setObjectName("Search_Widget")
        self.setFixedSize(1000, 750)
        self.setStyleSheet("""
                    background-color: white;
                    color: black;
                """)

        self.search_stacked_widget = QStackedWidget(self)
        self.search_stacked_widget.setObjectName("search_stacked_widget")
        self.search_stacked_widget.setGeometry(150, 70, 700, 450)

        self.search_person_widget = Search_person_main_Widget()
        self.search_person_widget.dataReturned.connect(self.handle_data)
        self.search_person_widget.setObjectName("search_person_widget")

        self.search_contact_widget = Search_Contact_main_Widget()
        self.search_contact_widget.dataReturned.connect(self.handle_data)
        self.search_contact_widget.setObjectName("search_contact_widget")

        self.serach_address_widget = Serach_Address_main_Widget()
        self.serach_address_widget.dataReturned.connect(self.handle_data)
        self.serach_address_widget.setObjectName("serach_address_widget")

        self.search_education_widget = Search_Education_main_Widget()
        self.search_education_widget.dataReturned.connect(self.handle_data)
        self.search_education_widget.setObjectName("search_education_widget")

        self.search_property_widget = Search_Property_main_Widget()
        self.search_property_widget.dataReturned.connect(self.handle_data)
        self.search_property_widget.setObjectName("search_property_widget")

        self.search_employeement_widget = Search_Employeement_main_Widget()
        self.search_employeement_widget.dataReturned.connect(self.handle_data)
        self.search_employeement_widget.setObjectName("search_employeement_widget")

        self.search_vehicle_widget = Search_Vehicle_main_Widget()
        self.search_vehicle_widget.dataReturned.connect(self.handle_data)
        self.search_vehicle_widget.setObjectName("search_vehicle_widget")

        self.search_jailRecord_widget = Search_JailRecord_main_Widget()
        self.search_jailRecord_widget.dataReturned.connect(self.handle_data)
        self.search_jailRecord_widget.setObjectName("search_jailRecipe_widget")

        self.search_stacked_widget.addWidget(self.search_person_widget)
        self.search_stacked_widget.addWidget(self.search_contact_widget)
        self.search_stacked_widget.addWidget(self.serach_address_widget)
        self.search_stacked_widget.addWidget(self.search_education_widget)
        self.search_stacked_widget.addWidget(self.search_property_widget)
        self.search_stacked_widget.addWidget(self.search_employeement_widget)
        self.search_stacked_widget.addWidget(self.search_vehicle_widget)
        self.search_stacked_widget.addWidget(self.search_jailRecord_widget)

        self.search_person_btn = QPushButton("Person ", self)
        self.search_person_btn.setObjectName("Search_Person")
        self.search_person_btn.setGeometry(100, 600, 100, 30)
        self.search_person_btn.clicked.connect(self.search_person_btn_clicked)

        self.search_contact_btn = QPushButton("Contact  ", self)
        self.search_contact_btn.setObjectName("Search_contact")
        self.search_contact_btn.setGeometry(200, 600, 100, 30)
        self.search_contact_btn.clicked.connect(self.search_contact_btn_clicked)

        self.search_address_btn = QPushButton("Address ", self)
        self.search_address_btn.setObjectName("search_address")
        self.search_address_btn.setGeometry(300, 600, 100, 30)
        self.search_address_btn.clicked.connect(self.search_address_btn_clicked)

        self.search_education_btn = QPushButton("Education ", self)
        self.search_education_btn.setObjectName("Search_education")
        self.search_education_btn.setGeometry(400, 600, 100, 30)
        self.search_education_btn.clicked.connect(self.search_education_btn_clicked)

        self.search_property_btn = QPushButton("Property ", self)
        self.search_property_btn.setObjectName("Search_property")
        self.search_property_btn.setGeometry(500, 600, 100, 30)
        self.search_property_btn.clicked.connect(self.search_property_btn_clicked)

        self.search_employment_btn = QPushButton("Employment ", self)
        self.search_employment_btn.setObjectName("Search_employment")
        self.search_employment_btn.setGeometry(600, 600, 100, 30)
        self.search_employment_btn.clicked.connect(self.search_employment_btn_clicked)

        self.search_vehicle_btn = QPushButton("Vehicle ", self)
        self.search_vehicle_btn.setObjectName("Search_vehicle")
        self.search_vehicle_btn.setGeometry(700, 600, 100, 30)
        self.search_vehicle_btn.clicked.connect(self.search_vehicle_btn_clicked)

        self.search_jailRecord_btn = QPushButton("Jail Record ", self)
        self.search_jailRecord_btn.setObjectName("Search_jailRecord")
        self.search_jailRecord_btn.setGeometry(800, 600, 100, 30)
        self.search_jailRecord_btn.clicked.connect(self.search_jailRecord_btn_clicked)

        with open("style.css") as style:
            self.setStyleSheet(style.read())

    def handle_data(self, result):
        self.dataReturned.emit(result)

    def search_person_btn_clicked(self):
        self.search_stacked_widget.setCurrentIndex(0)

    def search_contact_btn_clicked(self):
        self.search_stacked_widget.setCurrentIndex(1)

    def search_address_btn_clicked(self):
        self.search_stacked_widget.setCurrentIndex(2)

    def search_education_btn_clicked(self):
        self.search_stacked_widget.setCurrentIndex(3)

    def search_property_btn_clicked(self):
        self.search_stacked_widget.setCurrentIndex(4)

    def search_employment_btn_clicked(self):
        self.search_stacked_widget.setCurrentIndex(5)

    def search_vehicle_btn_clicked(self):
        self.search_stacked_widget.setCurrentIndex(6)

    def search_jailRecord_btn_clicked(self):
        self.search_stacked_widget.setCurrentIndex(7)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SearchWidget()
    window.show()
    sys.exit(app.exec())
