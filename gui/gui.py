# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 576)

        self.mainWindow = MainWindow

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(10, 500, 511, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.labelLogo = QtWidgets.QLabel(self.centralwidget)
        self.labelLogo.setGeometry(QtCore.QRect(10, 10, 481, 451))
        self.labelLogo.setText("")
        self.labelLogo.setObjectName("labelLogo")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(570, 100, 211, 51))
        self.pushButton.setObjectName("pushButton")
        self.labelFileName = QtWidgets.QLabel(self.centralwidget)
        self.labelFileName.setGeometry(QtCore.QRect(570, 20, 211, 51))
        self.labelFileName.setObjectName("labelFileName")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuPlik = QtWidgets.QMenu(self.menubar)
        self.menuPlik.setObjectName("menuPlik")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionZa_aduj = QtWidgets.QAction(MainWindow)
        self.actionZa_aduj.setObjectName("actionZa_aduj")
        self.menuPlik.addAction(self.actionZa_aduj)
        self.menubar.addAction(self.menuPlik.menuAction())

        self.attachEvents()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Przetwórz"))
        self.labelFileName.setText(_translate("MainWindow", "TextLabel"))
        self.menuPlik.setTitle(_translate("MainWindow", "Plik"))
        self.actionZa_aduj.setText(_translate("MainWindow", "Załaduj"))

    def attachEvents(self):
        self.actionZa_aduj.triggered.connect(self.browse)

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


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
