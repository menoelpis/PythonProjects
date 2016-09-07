import sys
from PyQt5 import QtWidgets

def window():
  app = QtWidgets.QApplication(sys.argv)
  w = QtWidgets.QWidget()
  b = QtWidgets.QPushButton(w)
  l = QtWidgets.QLabel(w)
  b.setText('Push Me!')
  l.setText('Look at Me!')
  b.move(100, 80)
  l.move(100, 120)
  w.setWindowTitle('PyQt5 Lesson 3')
  w.setGeometry(100, 100, 300, 300)
  w.show()
  sys.exit(app.exec_())


window()