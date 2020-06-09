# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import tagger
import os.path


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(973, 336)

        self.mainWindow = MainWindow

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 961, 231))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(
            self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.textBrowser = QtWidgets.QTextBrowser(self.horizontalLayoutWidget)
        self.textBrowser.setObjectName("textBrowser")
        self.horizontalLayout.addWidget(self.textBrowser)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(
            QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setObjectName("verticalLayout")
        self.button_nature = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.button_nature.setObjectName("button_nature")
        self.verticalLayout.addWidget(self.button_nature)
        self.button_plot = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.button_plot.setObjectName("button_plot")
        self.verticalLayout.addWidget(self.button_plot)
        self.button_others = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.button_others.setObjectName("button_others")
        self.verticalLayout.addWidget(self.button_others)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.horizontalLayout.setStretch(0, 8)
        self.horizontalLayout.setStretch(1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 973, 21))
        self.menubar.setObjectName("menubar")
        self.menuLoad_file = QtWidgets.QMenu(self.menubar)
        self.menuLoad_file.setObjectName("menuLoad_file")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionLoad = QtWidgets.QAction(MainWindow)
        self.actionLoad.setObjectName("actionLoad")
        self.menuLoad_file.addAction(self.actionLoad)
        self.menubar.addAction(self.menuLoad_file.menuAction())

        self.attachEvents()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.button_nature.setText(_translate("MainWindow", "Przyroda"))
        self.button_plot.setText(_translate("MainWindow", "Fabuła"))
        self.button_others.setText(_translate("MainWindow", "Inne"))
        self.menuLoad_file.setTitle(_translate("MainWindow", "File"))
        self.actionLoad.setText(_translate("MainWindow", "Load"))

    def attachEvents(self):
        self.actionLoad.triggered.connect(self.browse)

        self.button_nature.clicked.connect(self.tagAsNature)
        self.button_plot.clicked.connect(self.tagAsPlot)
        self.button_others.clicked.connect(self.tagAsOther)

    def browse(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        self.inputFile = QtWidgets.QFileDialog.getOpenFileName(
            self.mainWindow, "QFileDialog.getOpenFileName()", "", options=options)
        if self.inputFile:
            self.inputFile = str(self.inputFile[0])
            self.lines = tagger.readFile(self.inputFile)

            fname = "./data_tagged/" + self.inputFile.split("/")[-1]
            if os.path.isfile(fname):
                with open(fname, "r") as f:
                    self.firstIndex = len(f.readlines())
            else:
                self.firstIndex = 0
            self.textBrowser.setText(self.lines[self.firstIndex])

    def tag(self, tag):
        with open("./data_tagged/" + self.inputFile.split("/")[-1], "a") as f:
            f.write(tagger.tagSentence(self.textBrowser.toPlainText(), tag))
        self.firstIndex += 1
        self.textBrowser.setText(self.lines[self.firstIndex])

    def tagAsNature(self):
        self.tag("N")

    def tagAsPlot(self):
        self.tag("P")

    def tagAsOther(self):
        self.tag("O")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
