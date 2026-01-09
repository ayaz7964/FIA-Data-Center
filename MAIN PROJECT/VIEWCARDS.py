import sys
from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
    QMainWindow,
    QGraphicsDropShadowEffect,
    QSizePolicy,
    QGridLayout,
    QScrollArea
)
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtCore import Qt, pyqtSignal
from DATABASE import RunQuery


class data_cards(QMainWindow):
    dataReturned = pyqtSignal(object)

    def __init__(self, person_data):
        super().__init__()
        # self.setWindowTitle("Person Data")
        # self.setGeometry(150, 50, 1000, 750)
        # self.setFixedSize(1000, 750)
        self.setObjectName("view_data_cards")
        self.persons_data = person_data
        # Create main layout
        self.view_data_main_layout = QGridLayout()
        self.view_data_main_layout.setObjectName("view_data_main_layout")

        num_cols = 3  # Number of columns for the grid layout
        row = 0
        col = 0

        for person in self.persons_data:
            self.view_data_card_widget = self.create_card(person)
            self.view_data_main_layout.addWidget(self.view_data_card_widget, row, col)

            col += 1
            if col == num_cols:
                row += 1
                col = 0

        # Create scroll area
        self.view_data_scroll_area = QScrollArea()
        self.view_data_scroll_area.setWidgetResizable(True)
        self.view_data_scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.view_data_scroll_area.setWidget(QWidget())  # Set a widget for scroll area
        self.view_data_scroll_area.setObjectName("view_data_scroll_area")
        self.view_data_scroll_area.widget().setLayout(self.view_data_main_layout)  # Set the main layout to the widget

        # Set scroll area to central widget
        self.view_data_central_widget = QWidget()
        self.view_data_central_widget.setObjectName("view_data_central_widget")
        self.view_data_central_layout = QVBoxLayout()
        self.view_data_central_layout.addWidget(self.view_data_scroll_area)
        self.view_data_central_widget.setLayout(self.view_data_central_layout)
        self.setCentralWidget(self.view_data_central_widget)

        with open("style.css", "r") as f:
            self.setStyleSheet(f.read())

    def create_card(self, person_data):
        # Create card widget and layout
        view_data_card_widget = QWidget()
        view_data_card_widget.setObjectName("view_data_card_widget")
        view_data_card_widget.setFixedSize(300, 350)

        view_data_card_layout = QVBoxLayout(view_data_card_widget)
        view_data_card_layout.setContentsMargins(20, 20, 20, 20)  # Add padding

        # Apply shadow effect
        view_data_card_shadow = QGraphicsDropShadowEffect()
        view_data_card_shadow.setBlurRadius(50)
        view_data_card_shadow.setOffset(2, 2)
        view_data_card_widget.setGraphicsEffect(view_data_card_shadow)

        for key, value in person_data.items():
            if key == "person_id":
                key = "ID"
            elif key == "f_name":
                key = "First Name"
            elif key == "l_name":
                key = "Last Name"
            elif key == "cnic_number":
                key = "CNIC No"
            else:
                key = key.capitalize()

            pair_layout = QHBoxLayout()

            key_label = QLabel(f"{key}:", view_data_card_widget)
            key_label.setObjectName("view_data_card_data_key_labels")
            key_label.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
            pair_layout.addWidget(key_label)

            value_label = QLabel(f"{value}", view_data_card_widget)
            value_label.setObjectName("view_data_card_data_value_labels")
            pair_layout.addWidget(value_label)

            view_data_card_layout.addLayout(pair_layout)

        # Create buttons layout
        self.view_data_buttons_layout = QHBoxLayout()

        self.view_data_view_button = QPushButton("View", view_data_card_widget)
        self.view_data_view_button.setObjectName("view_data_view_button")
        self.view_data_view_button.clicked.connect(lambda: self.view_person(person_data['person_id']))
        self.view_data_buttons_layout.addWidget(self.view_data_view_button)
        self.view_data_view_button.setFixedHeight(25)

        view_data_card_layout.addLayout(self.view_data_buttons_layout)

        # Set size policy for vertical expansion
        view_data_card_widget.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        return view_data_card_widget

    #
    # def delete_person(self, person_id):
    #     # Implement delete functionality here
    #     print(f"Deleting person with ID {person_id}")
    #
    # def update_person(self, person_id):
    #     # Implement update functionality here
    #     print(f"Updating person with ID {person_id}")

    def view_person(self, person_id):
        self.dataReturned.emit(person_id)


if __name__ == "__main__":
    query = "SELECT person_id, f_name, l_name, gender, age, cnic_number, nationality, religion from person"
    persons_data = RunQuery(query)
    app = QApplication(sys.argv)
    main_window = data_cards(persons_data)
    main_window.show()
    sys.exit(app.exec())
