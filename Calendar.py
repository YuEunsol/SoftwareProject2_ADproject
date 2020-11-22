import sys

from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout,
                             QCalendarWidget)

class CalendarWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.CalendarUI()

    def CalendarUI(self):
        cal = QCalendarWidget(self)
        cal.setGridVisible(True)
        vbox = QVBoxLayout()
        vbox.addWidget(cal)
        self.setLayout(vbox)
        self.show()




if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = CalendarWidget()
    sys.exit(app.exec_())