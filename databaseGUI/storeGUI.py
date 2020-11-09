# Created by: PyQt5 UI code generator 5.15.1


from PyQt5 import QtCore, QtGui, QtWidgets
import sys, time, threading

OMEGALUL = 5
ui = None

class Ui_MasterWindow(object):
    def setupUi(self, MasterWindow):
        MasterWindow.setObjectName("MasterWindow")
        MasterWindow.resize(942, 750)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MasterWindow.sizePolicy().hasHeightForWidth())
        MasterWindow.setSizePolicy(sizePolicy)
        MasterWindow.setMinimumSize(QtCore.QSize(942, 750))
        MasterWindow.setMaximumSize(QtCore.QSize(942, 750))
        MasterWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MasterWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Title = QtWidgets.QLabel(self.centralwidget)
        self.Title.setGeometry(QtCore.QRect(270, 0, 401, 61))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.Title.setFont(font)
        self.Title.setObjectName("Title")
        self.store1Label = QtWidgets.QLabel(self.centralwidget)
        self.store1Label.setGeometry(QtCore.QRect(270, 190, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.store1Label.setFont(font)
        self.store1Label.setObjectName("store1Label")
        self.store2Label = QtWidgets.QLabel(self.centralwidget)
        self.store2Label.setGeometry(QtCore.QRect(580, 190, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.store2Label.setFont(font)
        self.store2Label.setObjectName("store2Label")
        self.store1Frame = QtWidgets.QFrame(self.centralwidget)
        self.store1Frame.setGeometry(QtCore.QRect(190, 220, 251, 411))
        self.store1Frame.setAutoFillBackground(True)
        self.store1Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.store1Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.store1Frame.setObjectName("store1Frame")
        self.store1ProgressBar = QtWidgets.QProgressBar(self.store1Frame)
        self.store1ProgressBar.setGeometry(QtCore.QRect(20, 160, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.store1ProgressBar.setFont(font)
        self.store1ProgressBar.setProperty("value", 24)
        self.store1ProgressBar.setObjectName("store1ProgressBar")
        self.store1_cap_label = QtWidgets.QLabel(self.store1Frame)
        self.store1_cap_label.setGeometry(QtCore.QRect(20, 10, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.store1_cap_label.setFont(font)
        self.store1_cap_label.setObjectName("store1_cap_label")
        self.store1Count = QtWidgets.QLineEdit(self.store1Frame)
        self.store1Count.setGeometry(QtCore.QRect(12, 60, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.store1Count.setFont(font)
        self.store1Count.setObjectName("store1Count")
        self.store1_totalCustomers = QtWidgets.QLineEdit(self.store1Frame)
        self.store1_totalCustomers.setGeometry(QtCore.QRect(10, 350, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.store1_totalCustomers.setFont(font)
        self.store1_totalCustomers.setObjectName("store1_totalCustomers")
        self.label_2 = QtWidgets.QLabel(self.store1Frame)
        self.label_2.setGeometry(QtCore.QRect(190, 10, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.store1_totalCustomers_2 = QtWidgets.QLineEdit(self.store1Frame)
        self.store1_totalCustomers_2.setGeometry(QtCore.QRect(10, 220, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.store1_totalCustomers_2.setFont(font)
        self.store1_totalCustomers_2.setObjectName("store1_totalCustomers_2")
        self.store1_totalCustomers_3 = QtWidgets.QLineEdit(self.store1Frame)
        self.store1_totalCustomers_3.setGeometry(QtCore.QRect(10, 260, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.store1_totalCustomers_3.setFont(font)
        self.store1_totalCustomers_3.setObjectName("store1_totalCustomers_3")
        self.store2Frame = QtWidgets.QFrame(self.centralwidget)
        self.store2Frame.setGeometry(QtCore.QRect(500, 220, 251, 411))
        self.store2Frame.setAutoFillBackground(True)
        self.store2Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.store2Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.store2Frame.setObjectName("store2Frame")
        self.store2ProgressBar = QtWidgets.QProgressBar(self.store2Frame)
        self.store2ProgressBar.setGeometry(QtCore.QRect(20, 160, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.store2ProgressBar.setFont(font)
        self.store2ProgressBar.setProperty("value", 24)
        self.store2ProgressBar.setObjectName("store2ProgressBar")
        self.store2_cap_label = QtWidgets.QLabel(self.store2Frame)
        self.store2_cap_label.setGeometry(QtCore.QRect(20, 10, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.store2_cap_label.setFont(font)
        self.store2_cap_label.setObjectName("store2_cap_label")
        self.store2Count = QtWidgets.QLineEdit(self.store2Frame)
        self.store2Count.setGeometry(QtCore.QRect(12, 60, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.store2Count.setFont(font)
        self.store2Count.setObjectName("store2Count")
        self.store2_customerPeak = QtWidgets.QLineEdit(self.store2Frame)
        self.store2_customerPeak.setGeometry(QtCore.QRect(10, 350, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.store2_customerPeak.setFont(font)
        self.store2_customerPeak.setObjectName("store2_customerPeak")
        self.label_3 = QtWidgets.QLabel(self.store2Frame)
        self.label_3.setGeometry(QtCore.QRect(190, 10, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.store2_humidity = QtWidgets.QLineEdit(self.store2Frame)
        self.store2_humidity.setGeometry(QtCore.QRect(10, 220, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.store2_humidity.setFont(font)
        self.store2_humidity.setObjectName("store2_humidity")
        self.store2_temp = QtWidgets.QLineEdit(self.store2Frame)
        self.store2_temp.setGeometry(QtCore.QRect(10, 260, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.store2_temp.setFont(font)
        self.store2_temp.setObjectName("store2_temp")
        MasterWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MasterWindow)
        self.menuBar.setEnabled(True)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 942, 21))
        self.menuBar.setAutoFillBackground(False)
        self.menuBar.setDefaultUp(False)
        self.menuBar.setNativeMenuBar(True)
        self.menuBar.setObjectName("menuBar")
        MasterWindow.setMenuBar(self.menuBar)
        self.statusbar = QtWidgets.QStatusBar(MasterWindow)
        self.statusbar.setObjectName("statusbar")
        MasterWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MasterWindow)
        QtCore.QMetaObject.connectSlotsByName(MasterWindow)




    def retranslateUi(self, MasterWindow):
        _translate = QtCore.QCoreApplication.translate
        MasterWindow.setWindowTitle(_translate("MasterWindow", "Store Observer GUI"))
        self.Title.setText(_translate("MasterWindow", "Store Master Observer"))
        self.store1Label.setText(_translate("MasterWindow", "Store 1"))
        self.store2Label.setText(_translate("MasterWindow", "Store 2"))
        self.store1_cap_label.setText(_translate("MasterWindow", "Store Capacity:"))
        self.store1Count.setText(_translate("MasterWindow", "Current count: [number]"))
        self.store1_totalCustomers.setText(_translate("MasterWindow", "Customer Peak:          []"))
        self.label_2.setText(_translate("MasterWindow", "25"))
        self.store1_totalCustomers_2.setText(_translate("MasterWindow", "Recent Humidity:        []"))
        self.store1_totalCustomers_3.setText(_translate("MasterWindow", "Recent Temperature:  []"))
        self.store2_cap_label.setText(_translate("MasterWindow", "Store Capacity:"))
        self.store2Count.setText(_translate("MasterWindow", "Current count: [number]"))
        self.store2_customerPeak.setText(_translate("MasterWindow", "Customer Peak:          []"))
        self.label_3.setText(_translate("MasterWindow", "25"))
        self.store2_humidity.setText(_translate("MasterWindow", "Recent Humidity:        []"))
        self.store2_temp.setText(_translate("MasterWindow", "Recent Temperature:  []"))


    def updateGUI(MasterWindow):
        MasterWindow.store1ProgressBar.setProperty("value", OMEGALUL)




def GUI():
    global ui
    app = QtWidgets.QApplication(sys.argv)
    MasterWindow = QtWidgets.QMainWindow()
    ui = Ui_MasterWindow()
    ui.setupUi(MasterWindow)
    MasterWindow.show()
    sys.exit(app.exec_())
    #app.exec_()

def polling():
    global OMEGALUL
    global ui

    while True:     #Database polling goes in here, this is just test example
        for i in range (0,2):
            time.sleep(2)
            OMEGALUL += 1

        ui.updateGUI()
        

if __name__ == "__main__":
    poll = threading.Thread(target=polling)
    poll.daemon = True
    poll.start()
    GUI()

    
