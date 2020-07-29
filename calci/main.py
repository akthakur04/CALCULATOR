import math
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Butt:
    def __init__(self,text,result):
        self.b=QPushButton(str(text))
        self.text=text
        self.result=result
        self.b.clicked.connect(lambda: self.inp(self.text))

    def inp(self,v):
        if v == "=":
            res = eval(self.result.text())
            self.result.setText(str(res))
        elif v=="ac":
            self.result.setText("")
        elif v=="√":
           value=float(self.result.text())
           self.result.setText(str(math.sqrt(value)))
        elif v=="DEL":
            current= self.result.text()
            self.result.setText(current[:-1 ])
        else:
            current=self.result.text()
            newv= current+str(v)
            self.result.setText(newv)



class Application(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CALCULATOR")
        self.createapp()
    def createapp(self):
        #grid
        grid=QGridLayout()
        results =QLineEdit()
        buttons=['ac','√','DEL','/',
                 7,8,9,'*',
                 4,5,6,'-',
                 3,2,1,'+',
                 0,'.','=']
        row=1
        col=0
        grid.addWidget(results, 0 , 0, 1, 4)
        for button in buttons:
            if col>3:
                col=0
                row+=1

            buttonObject = Butt(button,results)
            if button == "=":
                grid.addWidget(buttonObject.b,row, col ,1 ,2)
                col+=1
            else:
                grid.addWidget(buttonObject.b, row, col, 1, 1)
            col += 1

        self.setLayout(grid)
        self.show()
if __name__=="__main__":
    app=QApplication(sys.argv)
    window= Application()
    sys.exit(app.exec_())