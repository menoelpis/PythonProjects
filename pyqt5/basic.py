import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':

  app = QApplication(sys.argv)

  w = QWidget()
  w.resize(250, 150)
  w.move(100, 100)
  w.setWindowTitle('Example PyQT5 Application')
  w.show()

  sys.exit(app.exec_())