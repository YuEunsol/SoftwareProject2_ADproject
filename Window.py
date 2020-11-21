import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget,QLayout
from PyQt5.QtWidgets import QGridLayout, QMainWindow
from  PyQt5.QtWidgets import QGridLayout, QApplication
from PyQt5.QtWidgets import QSizePolicy

class MyWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        #윈도우 설정
        self.setWindowTitle("아빠 가계부")
        self.setGeometry(500, 300, 300, 400)
        self.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Preferred)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()
