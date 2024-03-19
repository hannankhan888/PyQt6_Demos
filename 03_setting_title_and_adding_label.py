import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel


class Window(QMainWindow):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        self.setGeometry(100, 100, 1600, 900)
        self.setWindowTitle("PyQt6 - Hello World Example")
        self._add_label()

    def _add_label(self):
        self.label = QLabel(self)
        self.label.setText("Hello World")
        self.label.move(800, 450)


def main():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
