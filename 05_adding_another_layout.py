import sys

from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
    QFrame,
    QPushButton,
)
from PyQt6.QtCore import Qt


class Window(QMainWindow):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        self.setGeometry(100, 100, 1600, 900)
        self.setWindowTitle("PyQt6 - Layouts Example")
        self._add_labels()
        self._add_buttons()
        self._create_layout()

    def _add_buttons(self):
        self.button = QPushButton()
        self.button.setText("Hello World")
        self.button.clicked.connect(lambda _: self.button.setText("Clicked"))
        self.button_2 = QPushButton()
        self.button_2.setText("Hello World 2")
        self.button_2.clicked.connect(lambda _: self.button_2.setText("Clicked"))

    def _add_labels(self):
        self.label = QLabel(self)
        self.label.setText("Hello World")
        self.label_2 = QLabel(self)
        self.label_2.setText("Hello World 2")

    def _create_layout(self):
        # Add a main frame as a widget
        self.main_frame = QFrame()
        # Add an overall layout to the main frame
        self.main_layout = QHBoxLayout()
        # Add a left and right frame to the main layout, so we can modify layouts respective of each side
        self.left_frame = QFrame()
        self.right_frame = QFrame()
        self.main_layout.addWidget(self.left_frame)
        self.main_layout.addWidget(self.right_frame)

        # Add a vertical box layout to the left frame
        self.vertical_box = QVBoxLayout()
        # self.vertical_box.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.vertical_box.addWidget(self.label)
        self.vertical_box.addWidget(self.label_2)
        self.left_frame.setLayout(self.vertical_box)

        # Add a Horizontal box layout to the right frame
        self.horizontal_box = QHBoxLayout()
        self.horizontal_box.addWidget(self.button)
        self.horizontal_box.addWidget(self.button_2)
        self.right_frame.setLayout(self.horizontal_box)

        # Add the layout to the main frame, and set the main frame as the Central Widget
        self.main_frame.setLayout(self.main_layout)
        self.setCentralWidget(self.main_frame)


def main():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
