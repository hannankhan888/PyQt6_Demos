import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QFrame
from PyQt6.QtCore import Qt


class Window(QMainWindow):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        self.setGeometry(100, 100, 1600, 900)
        self.setWindowTitle("PyQt6 - Layouts Example")
        self._add_labels()
        self._create_layout()

    def _add_labels(self):
        self.label = QLabel(self)
        self.label.setText("Hello World")
        self.label_2 = QLabel(self)
        self.label_2.setText("Hello World 2")

    def _create_layout(self):
        # Add a main frame as a widget
        self.main_frame = QFrame()

        # Add a vertical box layout
        self.vertical_box = QVBoxLayout()
        # self.vertical_box.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.vertical_box.addWidget(self.label)
        self.vertical_box.addWidget(self.label_2)

        # Add the layout to the main frame, and set the main frame as the Central Widget
        self.main_frame.setLayout(self.vertical_box)
        self.setCentralWidget(self.main_frame)


def main():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
