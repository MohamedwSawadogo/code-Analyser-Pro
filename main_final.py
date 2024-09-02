from PySide6.QtWidgets import QApplication
from page_test_final import MySideBar
import sys

app = QApplication(sys.argv)

window = MySideBar()
window.stackedWidget.setCurrentIndex(0)
window.show()

app.exec()
