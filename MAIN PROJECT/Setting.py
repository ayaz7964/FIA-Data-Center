import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QButtonGroup, QLabel, QStackedWidget
from PyQt6.QtGui import QIcon, QMouseEvent
from PyQt6.QtCore import QSize, Qt


class Setting_Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Setting")
        self.setWindowIcon(QIcon("./Images/Settings-white.png"))
        self.setGeometry(550, 150, 500, 400)
        self.setFixedSize(500, 400)

        self.setting_user_label = QLabel("USER SETTING", self)
        self.setting_user_label.setObjectName("setting_user_label")
        self.setting_user_label.setGeometry(200, 50, 200, 50)

        with open("./style.css", "r") as f:
            self.setStyleSheet(f.read())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Setting_Window()
    window.show()
    sys.exit(app.exec())
