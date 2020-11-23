# Created in part by: PyQt5 UI code generator 5.15.1
# Team DADA SYSC3010 Group Project

from PyQt5 import QtCore, QtGui, QtWidgets
import sys, time, threading, datetime
from datetime import datetime
from databasepoll import database_retrieve
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot

############# GLOBAL VARIABLES ##################################
CAP1 = 25
CAP2 = 25
DELAY = 0.1 #GUI update interval, in minutes
#################################################################

# GUI Class
class Ui_MasterWindow(QObject):

    updateSignal = pyqtSignal(int, int, int, int, int, int, int, int, str)
    
    def __init__(self):
        QObject.__init__(self)

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
        self.store1ProgressBar.setGeometry(QtCore.QRect(20, 120, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.store1ProgressBar.setFont(font)
        self.store1ProgressBar.setProperty("value", 0)
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
        self.store1Count.setReadOnly(True)
        self.store1Count.setObjectName("store1Count")
        self.store1_totalCustomers = QtWidgets.QLineEdit(self.store1Frame)
        self.store1_totalCustomers.setGeometry(QtCore.QRect(10, 350, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.store1_totalCustomers.setFont(font)
        self.store1_totalCustomers.setReadOnly(True)
        self.store1_totalCustomers.setObjectName("store1_totalCustomers")
        self.label_2 = QtWidgets.QLabel(self.store1Frame)
        self.label_2.setGeometry(QtCore.QRect(200, 10, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.store1_totalCustomers_2 = QtWidgets.QLineEdit(self.store1Frame)
        self.store1_totalCustomers_2.setGeometry(QtCore.QRect(10, 220, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.store1_totalCustomers_2.setFont(font)
        self.store1_totalCustomers_2.setReadOnly(True)
        self.store1_totalCustomers_2.setObjectName("store1_totalCustomers_2")
        self.store1_totalCustomers_3 = QtWidgets.QLineEdit(self.store1Frame)
        self.store1_totalCustomers_3.setGeometry(QtCore.QRect(10, 260, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.store1_totalCustomers_3.setFont(font)
        self.store1_totalCustomers_3.setReadOnly(True)
        self.store1_totalCustomers_3.setObjectName("store1_totalCustomers_3")
        self.store2Frame = QtWidgets.QFrame(self.centralwidget)
        self.store2Frame.setGeometry(QtCore.QRect(500, 220, 251, 411))
        self.store2Frame.setAutoFillBackground(True)
        self.store2Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.store2Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.store2Frame.setObjectName("store2Frame")
        self.store2ProgressBar = QtWidgets.QProgressBar(self.store2Frame)
        self.store2ProgressBar.setGeometry(QtCore.QRect(20, 120, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.store2ProgressBar.setFont(font)
        self.store2ProgressBar.setProperty("value", 0)
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
        self.store2Count.setReadOnly(True)
        self.store2Count.setObjectName("store2Count")
        self.store2_customerPeak = QtWidgets.QLineEdit(self.store2Frame)
        self.store2_customerPeak.setGeometry(QtCore.QRect(10, 350, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.store2_customerPeak.setFont(font)
        self.store2_customerPeak.setReadOnly(True)
        self.store2_customerPeak.setObjectName("store2_customerPeak")
        self.label_3 = QtWidgets.QLabel(self.store2Frame)
        self.label_3.setGeometry(QtCore.QRect(200, 10, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.store2_humidity = QtWidgets.QLineEdit(self.store2Frame)
        self.store2_humidity.setGeometry(QtCore.QRect(10, 220, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.store2_humidity.setFont(font)
        self.store2_humidity.setReadOnly(True)
        self.store2_humidity.setObjectName("store2_humidity")
        self.store2_temp = QtWidgets.QLineEdit(self.store2Frame)
        self.store2_temp.setGeometry(QtCore.QRect(10, 260, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.store2_temp.setFont(font)
        self.store2_temp.setReadOnly(True)
        self.store2_temp.setObjectName("store2_temp")
        self.labeldate = QtWidgets.QLabel(self.centralwidget)
        self.labeldate.setGeometry(QtCore.QRect(360, 120, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(False)
        self.labeldate.setFont(font)
        self.labeldate.setAutoFillBackground(True)
        self.labeldate.setObjectName("label")
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

        #Signal for updating GUI
        self.updateSignal.connect(self.updateGUI)

    def retranslateUi(self, MasterWindow):
        _translate = QtCore.QCoreApplication.translate
        MasterWindow.setWindowTitle(_translate("MasterWindow", "Store Observer GUI"))
        self.Title.setText(_translate("MasterWindow", "Store Master Observer"))
        self.store1Label.setText(_translate("MasterWindow", "Store 1"))
        self.store2Label.setText(_translate("MasterWindow", "Store 2"))
        self.store1_cap_label.setText(_translate("MasterWindow", "Store Capacity:"))
        self.store1Count.setText(_translate("MasterWindow", "Current count:           0"))
        self.store1_totalCustomers.setText(_translate("MasterWindow", "Customer Peak:          0"))
        self.label_2.setText(_translate("MasterWindow", "25"))
        self.store1_totalCustomers_2.setText(_translate("MasterWindow", "Recent Humidity:        0"))
        self.store1_totalCustomers_3.setText(_translate("MasterWindow", "Recent Temperature:  0"))
        self.store2_cap_label.setText(_translate("MasterWindow", "Store Capacity:"))
        self.store2Count.setText(_translate("MasterWindow", "Current count:           0"))
        self.store2_customerPeak.setText(_translate("MasterWindow", "Customer Peak:          0"))
        self.label_3.setText(_translate("MasterWindow", "25"))
        self.store2_humidity.setText(_translate("MasterWindow", "Recent Humidity:        0"))
        self.store2_temp.setText(_translate("MasterWindow", "Recent Temperature:  0"))
        self.labeldate.setText(_translate("MasterWindow", "Last updated: N/A"))


    @pyqtSlot(int, int, int, int, int, int, int, int, str)
    def updateGUI(MasterWindow, count1, temp1, hum1, peak1, count2, temp2, hum2, peak2, time):
        global CAP1, CAP2
        _translate = QtCore.QCoreApplication.translate

        
        MasterWindow.labeldate.setText(_translate("MasterWindow", "Last updated: " +str(time)))

        #PROGRESS BAR UPDATES
        if count1 >= CAP1:
            MasterWindow.store1ProgressBar.setProperty("value", 100)
            MasterWindow.store1ProgressBar.setStyleSheet("QProgressBar::chunk "
                  "{"
                    "background-color: red;"
                  "}")
        elif count1 >= 0:
            MasterWindow.store1ProgressBar.setProperty("value", (count1/CAP1)*100)
            MasterWindow.store1ProgressBar.setStyleSheet("QProgressBar::chunk "
                "{"
                   "background-color: lightgreen;"
                 "}")

        if count2 >= CAP2:
            MasterWindow.store2ProgressBar.setProperty("value", 100)
            MasterWindow.store1ProgressBar.setStyleSheet("QProgressBar::chunk "
                  "{"
                    "background-color: red;"
                  "}")
        elif count2 >= 0:
            MasterWindow.store2ProgressBar.setProperty("value", (count2/CAP2)*100)
            MasterWindow.store2ProgressBar.setStyleSheet("QProgressBar::chunk "
                  "{"
                    "background-color: lightgreen;"
                  "}")

        # HUMIDITY UPDATE
        if hum1 >= 0 and hum1 <= 100:
            MasterWindow.store1_totalCustomers_2.setText(_translate("MasterWindow", "Recent Humidity(%):  " +str(hum1)))

        if hum1 >= 0 and hum1 <= 100:
            MasterWindow.store2_humidity.setText(_translate("MasterWindow", "Recent Humidity(%):  " +str(hum2)))

        MasterWindow.store1_totalCustomers_3.setText(_translate("MasterWindow", "Recent Temp(°C):      " +str(temp1)))
        MasterWindow.store2_temp.setText(_translate("MasterWindow", "Recent Temp(°C):      " + str(temp2)))

        #PEAK UPDATES
        if peak1 >=0:
            MasterWindow.store1_totalCustomers.setText(_translate("MasterWindow", "Customer Peak:         " +str(peak1)))
            
        if peak2 >=0:
            MasterWindow.store2_customerPeak.setText(_translate("MasterWindow", "Customer Peak:         " +str(peak2)))

        #CURRENT COUNT UPDATES
        if count1 >= 0:
            MasterWindow.store1Count.setText(_translate("MasterWindow", "Current count:           " +str(count1)))
        if count2 >= 0:
            MasterWindow.store2Count.setText(_translate("MasterWindow", "Current count:           " +str(count2)))
######################### END OF GUI CLASS #####################################################

def polling():
    global ui, DELAY

    time.sleep(5)   #Give 5 seconds to start up GUI to avoid errors
    now = datetime.now()
    
    while True:     #Database polling and GUI updating takes place here

        #found in databasepoll.py
        store1_data, store2_data = database_retrieve()
        current_time = now.strftime("%H:%M")

        ui.updateSignal.emit(store1_data[0], store1_data[1], store1_data[2], store1_data[3],\
                             store2_data[0], store2_data[1], store2_data[2], store2_data[3], current_time)

        time.sleep(DELAY*60) #Interval between updates

if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    MasterWindow = QtWidgets.QMainWindow()
    ui = Ui_MasterWindow()
    ui.setupUi(MasterWindow)

    #Create thread for polling database
    poll = threading.Thread(target=polling)
    poll.daemon = True
    poll.start()
    
    MasterWindow.show()
    sys.exit(app.exec_())

