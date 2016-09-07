import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from PyQt5.QtGui import QIcon 
from PyQt5.QtCore import pyqtSlot

class App(QWidget):
  def __init__(self):
    super().__init__()
    self.initUI()

  def initUI(self):

    answer  = QMessageBox.question(self, 'Beverage', 'Do you lik coffee?', QMessageBox.Yes | QMessageBox.No | QMessageBox.Help, QMessageBox.Yes)
    if answer == QMessageBox.Yes:
      print('yes')
    else:
      print('no')
    #self.show()

if __name__ == '__main__':
  app = QApplication(sys.argv)
  ex = App()
  sys.exit(app.exec_())