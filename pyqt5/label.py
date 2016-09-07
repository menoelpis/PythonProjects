import sys
from PyQt5 import QtWidgets, QtGui

def window():
  app = QtWidgets.QApplication(sys.argv)
  w = QtWidgets.QWidget()
  l1 = QtWidgets.QLabel(w)
  l2 = QtWidgets.QLabel(w)
  l1.setText('Hello World')
  l2.setPixmap(QtGui.QPixmap('globe.png'))
  w.setWindowTitle('PyQt5 Lesson 2')
  w.setGeometry(100, 100, 300, 300)
  l1.move(110, 20)
  l2.move(20, 40)
  w.show()
  sys.exit(app.exec_())


window()