import sys

# from PyQt5.QtCore import
from PyQt5.QtWidgets import QApplication, QLabel, QWidget


def main():
    app = QApplication(sys.argv)
    w = QWidget()
    label = QLabel(w)
    label.setText("Hello World")
    w.setGeometry(100, 100, 1600, 900)
    label.move(800, 450)
    w.setWindowTitle("PyQt6 - Hello World Example")
    w.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()

