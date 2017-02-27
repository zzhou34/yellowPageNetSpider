from PyQt5   .QtWidgets import QApplication,QLabel,QWidget,QHBoxLayout, QPushButton, QLineEdit, QVBoxLayout,QMessageBox
import sys
import spider,gl



class ShowWindow(QWidget):
    def __init__(self):
        super(ShowWindow,self).__init__()
        self.initUI()

    def initUI(self):
        self.inputLabel1=QLabel("Your Root Url:")
        self.inputLabel2=QLabel("Your coordinate:")
        self.inputLabel3=QLabel("Your address:")
        self.inputLabel4=QLabel("Your borough:")
        self.editLine1=QLineEdit()
        self.editLine2=QLineEdit()
        self.editLine3=QLineEdit()
        self.editLine4=QLineEdit()
        self.runButton=QPushButton("Just do it!")



        self.runButton.clicked.connect(self.getData)

        inputLayout1=QHBoxLayout()
        inputLayout1.addWidget(self.inputLabel1)
        inputLayout1.addWidget(self.editLine1)

        inputLayout2=QHBoxLayout()
        inputLayout2.addWidget(self.inputLabel2)
        inputLayout2.addWidget(self.editLine2)

        inputLayout3=QHBoxLayout()
        inputLayout3.addWidget(self.inputLabel3)
        inputLayout3.addWidget(self.editLine3)

        # inputLayout4=QHBoxLayout()
        # inputLayout4.addWidget(self.inputLabel4)
        # inputLayout4.addWidget(self.editLine4)

        inputLayout5=QHBoxLayout()
        inputLayout5.addWidget(self.runButton)

        mainlayout=QVBoxLayout()
        mainlayout.addLayout(inputLayout1)
        mainlayout.addLayout(inputLayout2)
        mainlayout.addLayout(inputLayout3)
        #mainlayout.addLayout(inputLayout4)
        mainlayout.addLayout(inputLayout5)

        self.setLayout(mainlayout)
        self.setWindowTitle('zhouYellowPageSpider')
        self.show()

    def getData(self):
        # text=self.editLine1.text()
        # obj_spider = spider.SpiderMain()
        # obj_spider.craw(text)



        # QMessageBox.information(self, "Print Success",
        #                         "Text: %s" % text)
        # print(text)
        #obj_spider = spider.SpiderMain()
        #print(obj_spider)
        #print(type(obj_spider))
        # print(text)
        # print(type(text))
        #obj_spider.craw(text)




        gl.edit1=self.editLine1.text()
        gl.edit2=self.editLine2.text()
        gl.edit3=self.editLine3.text()
        #gl.edit4 = self.editLine4.text()
        # print(gl.edit1)
        # print(gl.edit2)
        # print(gl.edit3)

        # defense = Defense.Print()
        # defense.print()
        try:
          text=self.editLine1.text()
          obj_spider = spider.SpiderMain()
          obj_spider.craw(text)
          QMessageBox.information(self,"Success","finished")
        except:
          QMessageBox.information(self,"fail","problem unsolved")


if __name__ == '__main__':
  app = QApplication(sys.argv)
  ex = ShowWindow()
  sys.exit(app.exec_())
