from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        self.resize(QSize(600, 500))
        self.setWindowTitle('app')

def get_main_app(argv=[]):
    app = QApplication(argv)
    win = MainWindow()
    win.show()
    return app, win

if __name__ == '__main__':
    app, _win = get_main_app(sys.argv)
    sys.exit(app.exec_())