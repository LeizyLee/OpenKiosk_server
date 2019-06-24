import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import threading

form_class = uic.loadUiType("./qtDesinger/servergui.ui")[0]


class MyWindow(QMainWindow, form_class, threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.daemon = True
        self.start()
        super().__init__()
        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywind = MyWindow()
    mywind.show()
    sys.exit(app.exec_())
