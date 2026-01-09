from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QVBoxLayout, QGridLayout, \
    QButtonGroup, \
    QMessageBox, QRadioButton, QHBoxLayout, QGroupBox, QSizePolicy, QStackedWidget
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6 import QtGui
import sys

import Setting
import json
from Insert_crime_widgets import *
from Insert_widget import InsertWidget
from VIEWCARDS import data_cards
import Login_Setting
from Search_widget import SearchWidget
from View_Data import *

Name = None
Data = []


def load_config():
    with open("config.json", "r") as f:
        return json.load(f)


config = load_config()


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.config = None
        self.Login_Setting_window = None
        self.setWindowTitle("Login")
        self.setWindowIcon(QIcon("./Images/User.png"))
        self.setGeometry(300, 100, 800, 600)
        self.setFixedSize(900, 700)

        # Define a method to close the setting window

        # Create a background label
        self.background_label = QLabel(self)
        self.background_label.setGeometry(0, 0, 900, 700)

        # Load and set the background image
        pixmap = QPixmap("./Images/Back.jpg")
        pixmap = pixmap.scaled(self.size(), Qt.AspectRatioMode.KeepAspectRatio)
        self.background_label.setPixmap(pixmap)
        self.background_label.setScaledContents(True)

        self.login_widget = QWidget(self.background_label)
        self.login_widget.setGeometry(250, 175, 400, 350)
        self.login_widget.setObjectName("Login_widget")

        self.Login_label = QLabel("LOGIN", self.login_widget)
        self.Login_label.setObjectName("Login_label")
        self.Login_label.setGeometry(160, 50, 120, 30)

        self.Uname_label = QLabel("Username", self.login_widget)
        self.Uname_label.setGeometry(40, 120, 120, 30)
        self.Uname_label.setObjectName("Uname_label")

        self.username_lineedit = QLineEdit(self.login_widget)
        self.username_lineedit.setGeometry(160, 120, 200, 30)
        self.username_lineedit.setObjectName("username_lineedit")

        self.password_label = QLabel("Password", self.login_widget)
        self.password_label.setGeometry(40, 170, 120, 30)
        self.password_label.setObjectName("password_label")

        self.password_lineedit = QLineEdit(self.login_widget)
        self.password_lineedit.setGeometry(160, 170, 200, 30)
        self.password_lineedit.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_lineedit.setObjectName("password_lineedit")

        self.login_button = QPushButton("   Login", self.login_widget)
        self.login_button.setGeometry(120, 250, 230, 40)
        self.login_button.setObjectName("login_button")
        self.login_button.clicked.connect(self.login_Pressed)
        Login_icon = QIcon("./Images/Login.png")
        self.login_button.setIcon(Login_icon)
        self.login_button.setIconSize(Login_icon.actualSize(QSize(25, 25)))

        self.setting_login = QPushButton(self.login_widget)
        self.setting_login.setGeometry(60, 250, 40, 40)
        self.setting_login.setObjectName("setting_login")
        Login_setting_icon = QIcon("./Images/Settings.png")
        self.setting_login.setIcon(Login_setting_icon)
        self.setting_login.setIconSize(Login_setting_icon.actualSize(QSize(25, 25)))
        self.setting_login.clicked.connect(self.Login_Setting_Clicked)

        # Set style sheet
        with open("style.css", "r") as f:
            self.setStyleSheet(f.read())

    def closeEvent(self, event):
        QApplication.quit()

    def Login_Setting_Clicked(self):
        try:
            self.config = load_config()
            self.Login_Setting_window = Login_Setting.Login_Setting_Window()
            self.Login_Setting_window.show()
        except Exception as e:
            QMessageBox.warning(self, "Server Error", str(e))

    def login_Pressed(self):
        # Retrieve username and password from line edits
        username = self.username_lineedit.text()
        password = self.password_lineedit.text()
        self.username_lineedit.setText("")
        self.password_lineedit.setText("")

        try:
            # Construct query
            query = f"SELECT * FROM users WHERE user_uname = '{username}' AND password = '{password}'"

            # Send query to server
            response = RunQuery(query)

            if response:
                person_id = response[0]["person_id"]
                data = RunQuery(f"SELECT * FROM person WHERE person_id = {person_id}")
                username = data[0]["f_name"]
                self.hide()
                QMessageBox.information(self, "Login Successful", "Welcome " + username + "!")
                self.main_panel = windows(person_id)
                self.main_panel.show()
            else:
                QMessageBox.warning(self, "Login Error", "Invalid username or password")
        except Exception as e:
            QMessageBox.warning(self, "Server Error", str(e))


class DashboardWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.dasboard_data = self.get_dashboard_data()

        self.dashboard_widget = QWidget(self)
        self.dashboard_widget.setGeometry(100, 50, 800, 650)
        self.dashboard_widget.setObjectName("Dashboard_Widget")

        self.Dashboard_Label = QLabel("DASHBOARD", self.dashboard_widget)
        self.Dashboard_Label.setObjectName("Dashboard_Label")
        self.Dashboard_Label.setGeometry(300, 40, 200, 50)
        self.Dashboard_Label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        view_data_card_shadow_1 = QGraphicsDropShadowEffect()
        view_data_card_shadow_1.setBlurRadius(100)
        view_data_card_shadow_1.setOffset(1, 1)

        view_data_card_shadow_2 = QGraphicsDropShadowEffect()
        view_data_card_shadow_2.setBlurRadius(100)
        view_data_card_shadow_2.setOffset(1, 1)

        view_data_card_shadow_3 = QGraphicsDropShadowEffect()
        view_data_card_shadow_3.setBlurRadius(100)
        view_data_card_shadow_3.setOffset(1, 1)

        view_data_card_shadow_4 = QGraphicsDropShadowEffect()
        view_data_card_shadow_4.setBlurRadius(100)
        view_data_card_shadow_4.setOffset(1, 1)

        view_data_card_shadow_5 = QGraphicsDropShadowEffect()
        view_data_card_shadow_5.setBlurRadius(100)
        view_data_card_shadow_5.setOffset(1, 1)

        view_data_card_shadow_6 = QGraphicsDropShadowEffect()
        view_data_card_shadow_6.setBlurRadius(100)
        view_data_card_shadow_6.setOffset(1, 1)

        self.person_card_widget = QWidget(self.dashboard_widget)
        self.person_card_widget.setGeometry(50, 150, 200, 200)
        self.person_card_widget.setObjectName("person_card_widget")
        self.person_card_widget.setFixedSize(200, 200)
        self.person_card_label = QLabel("Person", self.person_card_widget)
        self.person_card_label.setObjectName("person_card_label")
        self.person_card_label.setGeometry(50, 10, 100, 50)
        self.person_card_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.person_card_icon = QLabel(self.person_card_widget)
        self.person_card_icon.setObjectName("person_card_icon")
        self.person_card_icon.setGeometry(50, 50, 100, 100)
        person_icon = QPixmap("./Images/person.png")
        self.person_card_icon.setPixmap(person_icon)
        self.person_card_icon.setScaledContents(True)
        self.person_card_icon.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.person_total_number = QLabel(str(self.dasboard_data[0]), self.person_card_widget)
        self.person_total_number.setObjectName("person_total_number")
        self.person_total_number.setGeometry(50, 150, 100, 50)
        self.person_total_number.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.person_card_widget.setGraphicsEffect(view_data_card_shadow_1)

        self.phone_no_card_widget = QWidget(self.dashboard_widget)
        self.phone_no_card_widget.setGeometry(300, 150, 200, 200)
        self.phone_no_card_widget.setObjectName("person_card_widget")
        self.phone_no_card_widget.setFixedSize(200, 200)
        self.phone_no_card_label = QLabel("Contacts", self.phone_no_card_widget)
        self.phone_no_card_label.setObjectName("person_card_label")
        self.phone_no_card_label.setGeometry(50, 10, 100, 50)
        self.phone_no_card_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.phone_no_card_icon = QLabel(self.phone_no_card_widget)
        self.phone_no_card_icon.setObjectName("person_card_icon")
        self.phone_no_card_icon.setGeometry(50, 50, 100, 100)
        phone_no_icon = QPixmap("./Images/contact.png")
        self.phone_no_card_icon.setPixmap(phone_no_icon)
        self.phone_no_card_icon.setScaledContents(True)
        self.phone_no_card_icon.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.phone_no_total_number = QLabel(str(self.dasboard_data[1] + self.dasboard_data[2]),
                                            self.phone_no_card_widget)
        self.phone_no_total_number.setObjectName("person_total_number")
        self.phone_no_total_number.setGeometry(50, 150, 100, 50)
        self.phone_no_total_number.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.phone_no_card_widget.setGraphicsEffect(view_data_card_shadow_2)

        self.address_card_widget = QWidget(self.dashboard_widget)
        self.address_card_widget.setGeometry(550, 150, 200, 200)
        self.address_card_widget.setObjectName("person_card_widget")
        self.address_card_widget.setFixedSize(200, 200)
        self.address_card_label = QLabel("Addresses", self.address_card_widget)
        self.address_card_label.setObjectName("person_card_label")
        self.address_card_label.setGeometry(50, 10, 100, 50)
        self.address_card_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.address_card_icon = QLabel(self.address_card_widget)
        self.address_card_icon.setObjectName("person_card_icon")
        self.address_card_icon.setGeometry(50, 50, 100, 100)
        address_icon = QPixmap("./Images/Address.png")
        self.address_card_icon.setPixmap(address_icon)
        self.address_card_icon.setScaledContents(True)
        self.address_card_icon.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.address_total_number = QLabel(str(self.dasboard_data[3]), self.address_card_widget)
        self.address_total_number.setObjectName("person_total_number")
        self.address_total_number.setGeometry(50, 150, 100, 50)
        self.address_total_number.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.address_card_widget.setGraphicsEffect(view_data_card_shadow_3)

        self.vehicles_card_widget = QWidget(self.dashboard_widget)
        self.vehicles_card_widget.setGeometry(50, 400, 200, 200)
        self.vehicles_card_widget.setObjectName("person_card_widget")
        self.vehicles_card_widget.setFixedSize(200, 200)
        self.vehicles_card_label = QLabel("Vehicles", self.vehicles_card_widget)
        self.vehicles_card_label.setObjectName("person_card_label")
        self.vehicles_card_label.setGeometry(0, 10, 200, 50)
        self.vehicles_card_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.vehicles_card_icon = QLabel(self.vehicles_card_widget)
        self.vehicles_card_icon.setObjectName("person_card_icon")
        self.vehicles_card_icon.setGeometry(50, 50, 100, 100)
        vehicles_icon = QPixmap("./Images/vehicle.png")
        self.vehicles_card_icon.setPixmap(vehicles_icon)
        self.vehicles_card_icon.setScaledContents(True)
        self.vehicles_card_icon.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.vehicles_total_number = QLabel(str(self.dasboard_data[4]), self.vehicles_card_widget)
        self.vehicles_total_number.setObjectName("person_total_number")
        self.vehicles_total_number.setGeometry(50, 150, 100, 50)
        self.vehicles_total_number.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.vehicles_card_widget.setGraphicsEffect(view_data_card_shadow_4)

        self.crimes_card_widget = QWidget(self.dashboard_widget)
        self.crimes_card_widget.setGeometry(300, 400, 200, 200)
        self.crimes_card_widget.setObjectName("person_card_widget")
        self.crimes_card_widget.setFixedSize(200, 200)
        self.crimes_card_label = QLabel("Crime Records", self.crimes_card_widget)
        self.crimes_card_label.setObjectName("person_card_label")
        self.crimes_card_label.setGeometry(0, 10, 200, 50)
        self.crimes_card_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.crimes_card_icon = QLabel(self.crimes_card_widget)
        self.crimes_card_icon.setObjectName("person_card_icon")
        self.crimes_card_icon.setGeometry(50, 50, 100, 100)
        crimes_icon = QPixmap("./Images/Crime1.png")
        self.crimes_card_icon.setPixmap(crimes_icon)
        self.crimes_card_icon.setScaledContents(True)
        self.crimes_card_icon.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.crimes_total_number = QLabel(str(self.dasboard_data[5]), self.crimes_card_widget)
        self.crimes_total_number.setObjectName("person_total_number")
        self.crimes_total_number.setGeometry(50, 150, 100, 50)
        self.crimes_total_number.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.crimes_card_widget.setGraphicsEffect(view_data_card_shadow_5)

        self.jail_rec_card_widget = QWidget(self.dashboard_widget)
        self.jail_rec_card_widget.setGeometry(550, 400, 200, 200)
        self.jail_rec_card_widget.setObjectName("person_card_widget")
        self.jail_rec_card_widget.setFixedSize(200, 200)
        self.jail_rec_card_label = QLabel("Jail Records", self.jail_rec_card_widget)
        self.jail_rec_card_label.setObjectName("person_card_label")
        self.jail_rec_card_label.setGeometry(0, 10, 200, 50)
        self.jail_rec_card_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.jail_rec_card_icon = QLabel(self.jail_rec_card_widget)
        self.jail_rec_card_icon.setObjectName("person_card_icon")
        self.jail_rec_card_icon.setGeometry(50, 50, 100, 100)
        jail_rec_icon = QPixmap("./Images/jail.png")
        self.jail_rec_card_icon.setPixmap(jail_rec_icon)
        self.jail_rec_card_icon.setScaledContents(True)
        self.jail_rec_card_icon.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.jail_rec_total_number = QLabel(str(self.dasboard_data[6]), self.jail_rec_card_widget)
        self.jail_rec_total_number.setObjectName("person_total_number")
        self.jail_rec_total_number.setGeometry(50, 150, 100, 50)
        self.jail_rec_total_number.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.jail_rec_card_widget.setGraphicsEffect(view_data_card_shadow_6)

        with open("style.css", "r") as f:
            self.setStyleSheet(f.read())

    def get_dashboard_data(self):
        try:
            query = "SELECT COUNT(*) FROM person"
            person = RunQuery(query)
            person = person[0]["COUNT(*)"]

            query = "SELECT COUNT(*) FROM phone_numbers"
            phone_numbers = RunQuery(query)
            phone_numbers = phone_numbers[0]["COUNT(*)"]

            query = "SELECT COUNT(*) FROM emails"
            email = RunQuery(query)
            email = email[0]["COUNT(*)"]

            query = "SELECT COUNT(*) FROM addresses"
            address = RunQuery(query)
            address = address[0]["COUNT(*)"]

            query = "SELECT COUNT(*) FROM vehicles"
            vehicle = RunQuery(query)
            vehicle = vehicle[0]["COUNT(*)"]

            query = "SELECT COUNT(*) FROM crimerecord"
            crime_record = RunQuery(query)
            crime_record = crime_record[0]["COUNT(*)"]

            query = "SELECT COUNT(*) FROM jail_record"
            jail_record = RunQuery(query)
            jail_record = jail_record[0]["COUNT(*)"]

            data = []
            data.append(person)
            data.append(phone_numbers)
            data.append(email)
            data.append(address)
            data.append(vehicle)
            data.append(crime_record)
            data.append(jail_record)

            return data

        except Exception as e:
            print(e)
            return None


class AboutWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("About_Widget")
        self.Dashboard_Label = QLabel("ABOUT", self)
        self.Dashboard_Label.setObjectName("About_Label")
        self.Dashboard_Label.setGeometry(300, 300, 200, 50)


class windows(QWidget):

    def __init__(self, person_id):
        super().__init__()

        self.view_person_id = None

        self.View_data_cards = None
        self.View_data = None
        self.person_id = person_id
        self.username = self.get_username(person_id)
        self.setWindowTitle("FIA DATABASE")
        self.setWindowIcon(QIcon("./Images/User.png"))
        self.setGeometry(200, 50, 1200, 750)
        self.setFixedSize(1200, 750)

        self.sidebar = QWidget(self)
        self.sidebar.setObjectName("sidebar")
        self.sidebar.setGeometry(0, 0, 200, 750)

        self.Logo = QLabel(self.sidebar)
        self.Logo.setObjectName("Main_Logo")
        self.Logo.setGeometry(30, 30, 50, 50)
        icon = QPixmap("./Images/User.png")
        self.Logo.setPixmap(icon)
        self.Logo.setScaledContents(True)

        self.Name_Bar = QLabel(self.sidebar)
        self.Name_Bar.setObjectName("Name_Bar")
        self.Name_Bar.setGeometry(90, 35, 165, 40)
        self.Name_Bar.setText(self.username)

        self.Dashboard_btn = QPushButton(self.sidebar)
        self.Dashboard_btn.setObjectName("Dashboard_btn")
        self.Dashboard_btn.setText("Dashboard")
        self.Dashboard_btn.setGeometry(35, 150, 165, 40)
        dash_icon = QIcon("./Images/Dashboard.png")
        self.Dashboard_btn.setIcon(dash_icon)
        self.Dashboard_btn.setIconSize(dash_icon.actualSize(QSize(25, 25)))
        self.Dashboard_btn.clicked.connect(self.Dashboard_Clicked)

        self.Search_btn = QPushButton(self.sidebar)
        self.Search_btn.setObjectName("Search_btn")
        self.Search_btn.setText("Search")
        self.Search_btn.setGeometry(35, 225, 165, 40)
        search_icon = QIcon("./Images/Search_bl.png")
        self.Search_btn.setIcon(search_icon)
        self.Search_btn.setIconSize(search_icon.actualSize(QSize(25, 25)))
        self.Search_btn.clicked.connect(self.Search_Clicked)

        self.Insert_btn = QPushButton(self.sidebar)
        self.Insert_btn.setObjectName("Insert_btn")
        self.Insert_btn.setText("Insert Person")
        self.Insert_btn.setGeometry(35, 300, 165, 40)
        self.Insert_icon = QIcon("./Images/person_insert.png")
        self.Insert_btn.setIcon(self.Insert_icon)
        self.Insert_btn.setIconSize(self.Insert_icon.actualSize(QSize(25, 25)))
        self.Insert_btn.clicked.connect(self.Insert_Clicked)

        self.Insert_crime_btn = QPushButton(self.sidebar)
        self.Insert_crime_btn.setObjectName("Insert_crime_btn")
        self.Insert_crime_btn.setText("Insert Crime")
        self.Insert_crime_btn.setGeometry(35, 375, 165, 40)
        self.Insert_crime_icon = QIcon("./Images/crime.png")
        self.Insert_crime_btn.setIcon(self.Insert_crime_icon)
        self.Insert_crime_btn.setIconSize(self.Insert_crime_icon.actualSize(QSize(25, 25)))
        self.Insert_crime_btn.clicked.connect(self.Insert_crime_Clicked)

        # self.About_btn = QPushButton(self.sidebar)
        # self.About_btn.setObjectName("About_btn")
        # self.About_btn.setText("About Us")
        # self.About_btn.setGeometry(35, 450, 165, 40)
        # about_icon = QIcon("./Images/About.png")
        # self.About_btn.setIcon(about_icon)
        # self.About_btn.setIconSize(about_icon.actualSize(QSize(25, 25)))
        # self.About_btn.clicked.connect(self.About_Clicked)

        self.Menu_Button_Group = QButtonGroup()
        self.Menu_Button_Group.addButton(self.Dashboard_btn)
        self.Menu_Button_Group.addButton(self.Search_btn)
        self.Menu_Button_Group.addButton(self.Insert_btn)
        self.Menu_Button_Group.addButton(self.Insert_crime_btn)
        # self.Menu_Button_Group.addButton(self.About_btn)
        self.Menu_Button_Group.buttonClicked.connect(self.Menu_button_clicked)

        self.Logout_btn = QPushButton(self.sidebar)
        self.Logout_btn.setObjectName("Logout_btn")
        self.Logout_btn.setText("Logout")
        self.Logout_btn.setGeometry(40, 640, 120, 40)
        Logout_icon = QIcon("./Images/Shutdown-white.png")
        self.Logout_btn.setIcon(Logout_icon)
        self.Logout_btn.setIconSize(Logout_icon.actualSize(QSize(25, 25)))
        self.Logout_btn.clicked.connect(self.logout_btn_clicked)

        # self.Setting_btn = QPushButton(self.sidebar)
        # self.Setting_btn.setObjectName("Setting_btn")
        # self.Setting_btn.setGeometry(150, 640, 40, 40)
        # Setting_icon = QIcon("./Images/Settings.png")
        # self.Setting_btn.setIcon(Setting_icon)
        # self.Setting_btn.setIconSize(Setting_icon.actualSize(QSize(25, 25)))
        # self.Setting_btn.clicked.connect(self.Setting_Clicked)

        self.Stacked_Main_Widgets = QStackedWidget(self)
        self.Stacked_Main_Widgets.setGeometry(200, 0, 1000, 750)
        self.Stacked_Main_Widgets.setObjectName("Stacked_Main_Widgets")

        self.Dashboard_Widget = DashboardWidget()
        self.Search_Widget = SearchWidget()
        self.Search_Widget.dataReturned.connect(self.handle_data)
        self.Insert_Widget = InsertWidget()
        self.Insert_crime_Widget = Insert_crime_Widget()
        self.About_Widget = AboutWidget()

        self.Stacked_Main_Widgets.addWidget(self.Dashboard_Widget)
        self.Stacked_Main_Widgets.addWidget(self.Search_Widget)
        self.Stacked_Main_Widgets.addWidget(self.Insert_Widget)
        self.Stacked_Main_Widgets.addWidget(self.Insert_crime_Widget)
        self.Stacked_Main_Widgets.addWidget(self.About_Widget)
        self.Stacked_Main_Widgets.setCurrentWidget(self.Dashboard_Widget)

        with open("style.css", "r") as f:
            self.setStyleSheet(f.read())

    def get_username(self, person_id):
        try:
            query = f"SELECT f_name FROM person WHERE person_id = {person_id}"
            response = RunQuery(query)
            return str(response[0]["f_name"])
        except Exception as e:
            print(e)
            return "Unknown"

    def logout_btn_clicked(self):
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Confirmation")
        msg_box.setText("Are you sure you want to logout?")
        msg_box.setStandardButtons(QMessageBox.StandardButton.Cancel | QMessageBox.StandardButton.Ok)
        msg_box.setDefaultButton(QMessageBox.StandardButton.Cancel)

        # Change button text
        ok_button = msg_box.button(QMessageBox.StandardButton.Ok)
        ok_button.setText("Logout")

        result = msg_box.exec()
        if result == QMessageBox.StandardButton.Ok:
            self.close()
            self.new_window = LoginWindow()
            self.new_window.show()
        else:
            pass

    def handle_data(self, data):
        try:
            if self.View_data_cards is not None:
                self.Stacked_Main_Widgets.removeWidget(self.View_data_cards)
            self.View_data_cards = data_cards(data)
            self.Stacked_Main_Widgets.addWidget(self.View_data_cards)
            self.Stacked_Main_Widgets.setCurrentWidget(self.View_data_cards)
            self.View_data_cards.dataReturned.connect(self.show_view_window)
        except Exception as e:
            QMessageBox.warning(self, "Error display", str(e))

    def handle_view_data(self, data):
        try:
            print("Person ID:", self.view_person_id)
            if data == "Delete":
                if self.View_data is not None:
                    if self.view_person_id == self.person_id:
                        QMessageBox.warning(self, "Error", "You cannot delete your own record")
                        return
                    query = f"DELETE FROM person WHERE person_id = {self.view_person_id}"
                    RunQuery(query)
                    self.view_person_id = None
                    QMessageBox.information(self, "Delete", "Record deleted successfully")
                    self.Stacked_Main_Widgets.removeWidget(self.View_data)
                    self.Stacked_Main_Widgets.setCurrentWidget(self.Search_Widget)
        except Exception as e:
            QMessageBox.warning(self, "Error display", str(e))

    def show_view_window(self, person_id):
        try:
            if self.View_data is not None:
                self.Stacked_Main_Widgets.removeWidget(self.View_data)
            self.View_data = ViewWidget(person_id)
            self.Stacked_Main_Widgets.addWidget(self.View_data)
            self.Stacked_Main_Widgets.setCurrentWidget(self.View_data)
            self.view_person_id = person_id
            self.View_data.dataReturned.connect(self.handle_view_data)
        except Exception as e:
            QMessageBox.warning(self, "Error display", str(e))

    def Dashboard_Clicked(self):
        self.Stacked_Main_Widgets.removeWidget(self.Dashboard_Widget)
        self.Dashboard_Widget = DashboardWidget()
        self.Stacked_Main_Widgets.addWidget(self.Dashboard_Widget)
        self.Stacked_Main_Widgets.setCurrentWidget(self.Dashboard_Widget)

    def Search_Clicked(self):
        self.Stacked_Main_Widgets.setCurrentWidget(self.Search_Widget)

    def Insert_Clicked(self):
        self.Stacked_Main_Widgets.setCurrentWidget(self.Insert_Widget)

    def Insert_crime_Clicked(self):
        self.Stacked_Main_Widgets.setCurrentWidget(self.Insert_crime_Widget)

    def About_Clicked(self):
        self.Stacked_Main_Widgets.setCurrentWidget(self.About_Widget)

    def Setting_Clicked(self):
        self.new_window = Setting.Setting_Window()
        self.new_window.show()

    def Menu_button_clicked(self, button):
        for btn in self.Menu_Button_Group.buttons():
            if btn is not button:
                btn.setChecked(False)
                btn.setStyleSheet("background-color: #ffffff; color: #0051ff;")
            else:
                btn.setChecked(True)
                btn.setStyleSheet("background-color: #a9f2ff; color: #001fc3;")


if __name__ == '__main__':
    try:
        app = QApplication(sys.argv)
        window = LoginWindow()
        # window = windows(5)
        window.show()
        sys.exit(app.exec())
    except Exception as e:
        QMessageBox.critical(None, "Error", str(e))
