import sys
from PyQt5.QtWidgets import *


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initui()

    def initui(self):
        label= QLabel("NAME l:")
        namei = QLineEdit()
        button = QPushButton("SET NAME: ")
        button.clicked.connect(self.action)
        horizontal= QHBoxLayout()

        horizontal.addWidget(label)
        horizontal.addWidget(namei)

        vertical=QVBoxLayout()
        vertical.addStretch(1)
        vertical.addLayout(horizontal)
        vertical.addWidget(button)

        self.setLayout(vertical)
        self.setWindowTitle("qline")
        self.show()
    def action(self):
        print("thi is clicked")

if __name__=="__main__":
    app=QApplication(sys.argv)
    window= MainWindow()
    sys.exit(app.exec_())