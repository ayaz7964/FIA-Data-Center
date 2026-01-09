import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QButtonGroup, QLabel, QStackedWidget, \
    QLineEdit
from PyQt6.QtGui import QIcon, QMouseEvent
from PyQt6.QtCore import QSize, Qt

import json


def load_config():
    with open("config.json", "r") as f:
        return json.load(f)


def save_config(config):
    with open("config.json", "w") as f:
        json.dump(config, f, indent=4)


class Login_Setting_Window(QWidget):
    def __init__(self):
        super().__init__()
        self.config = load_config()
        self.setWindowTitle("Setting")
        self.setObjectName("Login_Setting_Window")
        self.setWindowIcon(QIcon("./Images/Settings-white.png"))
        self.setGeometry(600, 200, 400, 350)
        self.setFixedSize(400, 350)

        self.login_setting_label = QLabel("SERVER SETTING", self)
        self.login_setting_label.setObjectName("login_setting_label")
        self.login_setting_label.setGeometry(110, 30, 200, 30)

        self.login_host_label = QLabel("Host", self)
        self.login_host_label.setGeometry(50, 100, 100, 30)
        self.login_host_label.setObjectName("login_host_label")

        self.login_host_lineedit = QLineEdit(self)
        self.login_host_lineedit.setText(str(self.config["IP"]))
        self.login_host_lineedit.setGeometry(170, 100, 180, 30)
        self.login_host_lineedit.setObjectName("login_host_lineedit")
        self.login_host_lineedit.setDisabled(True)

        self.login_port_label = QLabel("Port GET", self)
        self.login_port_label.setGeometry(50, 150, 100, 30)
        self.login_port_label.setObjectName("login_port_label")

        self.login_port_lineedit = QLineEdit(self)
        self.login_port_lineedit.setText(str(self.config["PORT-1"]))
        self.login_port_lineedit.setGeometry(170, 150, 180, 30)
        self.login_port_lineedit.setObjectName("login_port_lineedit")
        self.login_port_lineedit.setDisabled(True)

        self.login_port_2_label = QLabel("Port INSERT", self)
        self.login_port_2_label.setGeometry(47, 200, 100, 30)
        self.login_port_2_label.setObjectName("login_port_label")

        self.login_port_2_lineedit = QLineEdit(self)
        self.login_port_2_lineedit.setText(str(self.config["PORT-2"]))
        self.login_port_2_lineedit.setGeometry(170, 200, 180, 30)
        self.login_port_2_lineedit.setObjectName("login_port_lineedit")
        self.login_port_2_lineedit.setDisabled(True)

        self.login_setting_change_button = QPushButton("Change", self)
        self.login_setting_change_button.setGeometry(50, 270, 140, 30)
        self.login_setting_change_button.setObjectName("login_setting_change_button")
        self.login_setting_change_button.clicked.connect(self.login_setting_change_button_clicked)

        self.login_setting_save_button = QPushButton("Save", self)
        self.login_setting_save_button.setGeometry(210, 270, 140, 30)
        self.login_setting_save_button.setObjectName("login_setting_save_button")
        self.login_setting_save_button.clicked.connect(self.login_setting_save_button_clicked)

        # Set style sheet
        with open("style.css", "r") as f:
            self.setStyleSheet(f.read())

    def login_setting_change_button_clicked(self):
        self.login_host_lineedit.setDisabled(False)
        self.login_port_lineedit.setDisabled(False)
        self.login_port_2_lineedit.setDisabled(False)
        self.login_setting_change_button.setText("Cancel")
        self.login_setting_change_button.clicked.connect(self.login_setting_change_button_cancel)

    def login_setting_change_button_cancel(self):
        self.login_host_lineedit.setText(str(self.config["IP"]))
        self.login_port_lineedit.setText(str(self.config["PORT-1"]))
        self.login_port_2_lineedit.setText(str(self.config["PORT-2"]))
        self.login_host_lineedit.setDisabled(True)
        self.login_port_lineedit.setDisabled(True)
        self.login_port_2_lineedit.setDisabled(True)
        self.login_setting_change_button.setText("Change")
        self.login_setting_change_button.clicked.connect(self.login_setting_change_button_clicked)

    def login_setting_save_button_clicked(self):
        IP = self.login_host_lineedit.text()
        PORT_1 = int(self.login_port_lineedit.text())
        PORT_2 = int(self.login_port_2_lineedit.text())
        self.config["IP"] = IP
        self.config["PORT-1"] = PORT_1
        self.config["PORT-2"] = PORT_2
        save_config(self.config)
        self.login_host_lineedit.setText(str(self.config["IP"]))
        self.login_port_lineedit.setText(str(self.config["PORT-1"]))
        self.login_port_2_lineedit.setText(str(self.config["PORT-2"]))
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Login_Setting_Window()
    window.show()
    sys.exit(app.exec())
