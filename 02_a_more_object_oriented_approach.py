import sys

from PyQt6.QtWidgets import QApplication, QMainWindow


class Window(QMainWindow):  # <== Notice the change in type of object
    def __init__(self, parent=None):
        # get the __init__() of the original QWidget object, and execute it.
        super(Window, self).__init__(parent)

        self.setGeometry(100, 100, 1600, 900)


def main():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
