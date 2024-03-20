import sys

from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
    QFrame,
    QPushButton,
    QTextEdit,
)
from PyQt6.QtCore import Qt


class Window(QMainWindow):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        self.setGeometry(100, 100, 1600, 900)
        self.setWindowTitle("PyQt6 - Layouts Example")

        self._create_layout()
        self._add_text_edit_box()

    def _create_layout(self):
        # Add a main frame as a widget
        self.main_frame = QFrame()
        # Add an overall layout to the main frame
        self.main_layout = QVBoxLayout()
        # Add the layout to the main frame, and set the main frame as the Central Widget
        self.main_frame.setLayout(self.main_layout)
        self.setCentralWidget(self.main_frame)

    def _add_text_edit_box(self):
        self.text_box = QTextEdit()
        self.main_layout.addWidget(self.text_box)


def main():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
