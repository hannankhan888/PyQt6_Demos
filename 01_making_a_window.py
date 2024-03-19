import sys

from PyQt5.QtWidgets import QApplication, QLabel, QWidget


def main():
    app = QApplication(sys.argv)
    w = QWidget()
    w.setGeometry(100, 100, 1600, 900)
    w.setWindowTitle("PyQt6 - Hello World Example")
    w.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
