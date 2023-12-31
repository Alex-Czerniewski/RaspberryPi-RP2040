# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bits.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(781, 500)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 140, 451, 71))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.btn_enter = QtWidgets.QPushButton(self.groupBox)
        self.btn_enter.setGeometry(QtCore.QRect(340, 35, 101, 25))
        self.btn_enter.setFlat(False)
        self.btn_enter.setObjectName("btn_enter")
        self.ledit_freq = QtWidgets.QLineEdit(self.groupBox)
        self.ledit_freq.setGeometry(QtCore.QRect(160, 35, 131, 25))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.ledit_freq.setFont(font)
        self.ledit_freq.setObjectName("ledit_freq")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 30, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 370, 451, 101))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.cbox_bit128 = QtWidgets.QCheckBox(self.groupBox_2)
        self.cbox_bit128.setGeometry(QtCore.QRect(190, 63, 91, 28))
        self.cbox_bit128.setObjectName("cbox_bit128")
        self.cbox_bit64 = QtWidgets.QCheckBox(self.groupBox_2)
        self.cbox_bit64.setGeometry(QtCore.QRect(100, 63, 81, 28))
        self.cbox_bit64.setObjectName("cbox_bit64")
        self.cbox_bit4 = QtWidgets.QCheckBox(self.groupBox_2)
        self.cbox_bit4.setGeometry(QtCore.QRect(190, 30, 71, 28))
        self.cbox_bit4.setObjectName("cbox_bit4")
        self.cbox_bit32 = QtWidgets.QCheckBox(self.groupBox_2)
        self.cbox_bit32.setGeometry(QtCore.QRect(10, 63, 81, 28))
        self.cbox_bit32.setObjectName("cbox_bit32")
        self.cbox_bit2 = QtWidgets.QCheckBox(self.groupBox_2)
        self.cbox_bit2.setGeometry(QtCore.QRect(100, 30, 71, 28))
        self.cbox_bit2.setObjectName("cbox_bit2")
        self.cbox_bit8 = QtWidgets.QCheckBox(self.groupBox_2)
        self.cbox_bit8.setGeometry(QtCore.QRect(280, 30, 71, 28))
        self.cbox_bit8.setObjectName("cbox_bit8")
        self.cbox_bit256 = QtWidgets.QCheckBox(self.groupBox_2)
        self.cbox_bit256.setGeometry(QtCore.QRect(280, 63, 91, 28))
        self.cbox_bit256.setObjectName("cbox_bit256")
        self.cbox_bit16 = QtWidgets.QCheckBox(self.groupBox_2)
        self.cbox_bit16.setGeometry(QtCore.QRect(370, 30, 81, 28))
        self.cbox_bit16.setObjectName("cbox_bit16")
        self.cbox_bit1 = QtWidgets.QCheckBox(self.groupBox_2)
        self.cbox_bit1.setGeometry(QtCore.QRect(10, 30, 71, 28))
        self.cbox_bit1.setObjectName("cbox_bit1")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(460, 0, 20, 541))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(480, 30, 291, 91))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName("groupBox_4")
        self.label_3 = QtWidgets.QLabel(self.groupBox_4)
        self.label_3.setGeometry(QtCore.QRect(10, 30, 68, 22))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox_4)
        self.label_4.setGeometry(QtCore.QRect(10, 60, 68, 22))
        self.label_4.setObjectName("label_4")
        self.ledit_IP = QtWidgets.QLineEdit(self.groupBox_4)
        self.ledit_IP.setGeometry(QtCore.QRect(50, 30, 121, 21))
        self.ledit_IP.setObjectName("ledit_IP")
        self.ledit_PORT = QtWidgets.QLineEdit(self.groupBox_4)
        self.ledit_PORT.setGeometry(QtCore.QRect(50, 60, 121, 21))
        self.ledit_PORT.setObjectName("ledit_PORT")
        self.btn_Connect = QtWidgets.QPushButton(self.groupBox_4)
        self.btn_Connect.setGeometry(QtCore.QRect(190, 55, 91, 25))
        self.btn_Connect.setObjectName("btn_Connect")
        self.groupBox_6 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_6.setGeometry(QtCore.QRect(480, 130, 291, 80))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox_6.setFont(font)
        self.groupBox_6.setObjectName("groupBox_6")
        self.label_6 = QtWidgets.QLabel(self.groupBox_6)
        self.label_6.setGeometry(QtCore.QRect(10, 40, 81, 22))
        self.label_6.setObjectName("label_6")
        self.ledit_Span = QtWidgets.QLineEdit(self.groupBox_6)
        self.ledit_Span.setGeometry(QtCore.QRect(100, 42, 91, 21))
        self.ledit_Span.setText("")
        self.ledit_Span.setObjectName("ledit_Span")
        self.btn_SAspan = QtWidgets.QPushButton(self.groupBox_6)
        self.btn_SAspan.setGeometry(QtCore.QRect(210, 40, 71, 25))
        self.btn_SAspan.setObjectName("btn_SAspan")
        self.groupBox_7 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_7.setGeometry(QtCore.QRect(480, 340, 291, 80))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox_7.setFont(font)
        self.groupBox_7.setObjectName("groupBox_7")
        self.label_7 = QtWidgets.QLabel(self.groupBox_7)
        self.label_7.setGeometry(QtCore.QRect(10, 40, 81, 22))
        self.label_7.setObjectName("label_7")
        self.ledit_CTRF = QtWidgets.QLineEdit(self.groupBox_7)
        self.ledit_CTRF.setGeometry(QtCore.QRect(100, 42, 91, 21))
        self.ledit_CTRF.setText("")
        self.ledit_CTRF.setObjectName("ledit_CTRF")
        self.btn_SActrf = QtWidgets.QPushButton(self.groupBox_7)
        self.btn_SActrf.setGeometry(QtCore.QRect(210, 40, 71, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_SActrf.setFont(font)
        self.btn_SActrf.setObjectName("btn_SActrf")
        self.txtedit_DSA = QtWidgets.QTextEdit(self.centralwidget)
        self.txtedit_DSA.setGeometry(QtCore.QRect(480, 430, 291, 41))
        self.txtedit_DSA.setObjectName("txtedit_DSA")
        self.groupBox_5 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_5.setGeometry(QtCore.QRect(480, 230, 291, 91))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox_5.setFont(font)
        self.groupBox_5.setObjectName("groupBox_5")
        self.label_5 = QtWidgets.QLabel(self.groupBox_5)
        self.label_5.setGeometry(QtCore.QRect(10, 30, 68, 22))
        self.label_5.setObjectName("label_5")
        self.ledit_Directory = QtWidgets.QLineEdit(self.groupBox_5)
        self.ledit_Directory.setGeometry(QtCore.QRect(60, 30, 221, 23))
        self.ledit_Directory.setObjectName("ledit_Directory")
        self.ledit_FileName = QtWidgets.QLineEdit(self.groupBox_5)
        self.ledit_FileName.setGeometry(QtCore.QRect(60, 60, 221, 23))
        self.ledit_FileName.setObjectName("ledit_FileName")
        self.label_8 = QtWidgets.QLabel(self.groupBox_5)
        self.label_8.setGeometry(QtCore.QRect(10, 60, 68, 22))
        self.label_8.setObjectName("label_8")
        self.groupBox_8 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_8.setGeometry(QtCore.QRect(10, 210, 451, 161))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox_8.setFont(font)
        self.groupBox_8.setObjectName("groupBox_8")
        self.label_37 = QtWidgets.QLabel(self.groupBox_8)
        self.label_37.setGeometry(QtCore.QRect(220, 40, 67, 17))
        self.label_37.setObjectName("label_37")
        self.label_43 = QtWidgets.QLabel(self.groupBox_8)
        self.label_43.setGeometry(QtCore.QRect(10, 36, 91, 17))
        self.label_43.setObjectName("label_43")
        self.ledit_minf = QtWidgets.QLineEdit(self.groupBox_8)
        self.ledit_minf.setGeometry(QtCore.QRect(100, 34, 113, 23))
        self.ledit_minf.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ledit_minf.setObjectName("ledit_minf")
        self.label_40 = QtWidgets.QLabel(self.groupBox_8)
        self.label_40.setGeometry(QtCore.QRect(220, 70, 67, 17))
        self.label_40.setObjectName("label_40")
        self.label_38 = QtWidgets.QLabel(self.groupBox_8)
        self.label_38.setGeometry(QtCore.QRect(10, 68, 91, 17))
        self.label_38.setObjectName("label_38")
        self.ledit_maxf = QtWidgets.QLineEdit(self.groupBox_8)
        self.ledit_maxf.setGeometry(QtCore.QRect(100, 64, 113, 23))
        self.ledit_maxf.setObjectName("ledit_maxf")
        self.label_35 = QtWidgets.QLabel(self.groupBox_8)
        self.label_35.setGeometry(QtCore.QRect(10, 100, 91, 17))
        self.label_35.setObjectName("label_35")
        self.label_41 = QtWidgets.QLabel(self.groupBox_8)
        self.label_41.setGeometry(QtCore.QRect(220, 102, 67, 17))
        self.label_41.setObjectName("label_41")
        self.ledit_stepS = QtWidgets.QLineEdit(self.groupBox_8)
        self.ledit_stepS.setGeometry(QtCore.QRect(100, 97, 113, 23))
        self.ledit_stepS.setObjectName("ledit_stepS")
        self.btn_sweep = QtWidgets.QPushButton(self.groupBox_8)
        self.btn_sweep.setGeometry(QtCore.QRect(350, 130, 81, 23))
        self.btn_sweep.setObjectName("btn_sweep")
        self.label_36 = QtWidgets.QLabel(self.groupBox_8)
        self.label_36.setGeometry(QtCore.QRect(10, 130, 91, 17))
        self.label_36.setObjectName("label_36")
        self.ledit_dwellT = QtWidgets.QLineEdit(self.groupBox_8)
        self.ledit_dwellT.setGeometry(QtCore.QRect(100, 127, 113, 23))
        self.ledit_dwellT.setObjectName("ledit_dwellT")
        self.label_44 = QtWidgets.QLabel(self.groupBox_8)
        self.label_44.setGeometry(QtCore.QRect(220, 132, 67, 17))
        self.label_44.setObjectName("label_44")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 20, 451, 81))
        self.groupBox_3.setObjectName("groupBox_3")
        self.rbtn_SpurNB = QtWidgets.QRadioButton(self.groupBox_3)
        self.rbtn_SpurNB.setGeometry(QtCore.QRect(20, 40, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.rbtn_SpurNB.setFont(font)
        self.rbtn_SpurNB.setObjectName("rbtn_SpurNB")
        self.rbtn_SpurWB = QtWidgets.QRadioButton(self.groupBox_3)
        self.rbtn_SpurWB.setGeometry(QtCore.QRect(110, 40, 81, 28))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.rbtn_SpurWB.setFont(font)
        self.rbtn_SpurWB.setObjectName("rbtn_SpurWB")
        self.cbox_Div64 = QtWidgets.QCheckBox(self.groupBox_3)
        self.cbox_Div64.setGeometry(QtCore.QRect(290, 40, 71, 28))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.cbox_Div64.setFont(font)
        self.cbox_Div64.setObjectName("cbox_Div64")
        self.btn_reset = QtWidgets.QPushButton(self.groupBox_3)
        self.btn_reset.setGeometry(QtCore.QRect(370, 40, 71, 25))
        self.btn_reset.setAutoDefault(False)
        self.btn_reset.setFlat(False)
        self.btn_reset.setObjectName("btn_reset")
        self.rbtn_Sweep = QtWidgets.QRadioButton(self.groupBox_3)
        self.rbtn_Sweep.setGeometry(QtCore.QRect(200, 40, 81, 28))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.rbtn_Sweep.setFont(font)
        self.rbtn_Sweep.setObjectName("rbtn_Sweep")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "VCO"))
        self.groupBox.setTitle(_translate("MainWindow", "Set Frequency"))
        self.btn_enter.setText(_translate("MainWindow", "Enter"))
        self.btn_enter.setShortcut(_translate("MainWindow", "Return"))
        self.label.setText(_translate("MainWindow", "Frequency"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Bits"))
        self.cbox_bit128.setText(_translate("MainWindow", "128 MHz"))
        self.cbox_bit64.setText(_translate("MainWindow", "64 MHz"))
        self.cbox_bit4.setText(_translate("MainWindow", "4 MHz"))
        self.cbox_bit32.setText(_translate("MainWindow", "32 MHz"))
        self.cbox_bit2.setText(_translate("MainWindow", "2 MHz"))
        self.cbox_bit8.setText(_translate("MainWindow", "8 MHz"))
        self.cbox_bit256.setText(_translate("MainWindow", "256 MHz"))
        self.cbox_bit16.setText(_translate("MainWindow", "16 MHz"))
        self.cbox_bit1.setText(_translate("MainWindow", "1 MHz"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Connect to DSA832E"))
        self.label_3.setText(_translate("MainWindow", "IP:"))
        self.label_4.setText(_translate("MainWindow", "Port:"))
        self.ledit_IP.setText(_translate("MainWindow", "192.168.0.11"))
        self.ledit_PORT.setText(_translate("MainWindow", "5555"))
        self.btn_Connect.setText(_translate("MainWindow", "Connect"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Set Span"))
        self.label_6.setText(_translate("MainWindow", "Span:"))
        self.btn_SAspan.setText(_translate("MainWindow", "Send"))
        self.groupBox_7.setTitle(_translate("MainWindow", "Set Center Frequency"))
        self.label_7.setText(_translate("MainWindow", "Ctr Freq:"))
        self.btn_SActrf.setText(_translate("MainWindow", "Send"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Write To XLSX File"))
        self.label_5.setText(_translate("MainWindow", "Dir."))
        self.ledit_Directory.setText(_translate("MainWindow", "/home/pi/AlexTest/"))
        self.ledit_FileName.setText(_translate("MainWindow", "test2"))
        self.label_8.setText(_translate("MainWindow", "Name"))
        self.groupBox_8.setTitle(_translate("MainWindow", "Sweep Parameters"))
        self.label_37.setText(_translate("MainWindow", "MHz"))
        self.label_43.setText(_translate("MainWindow", "Min. Freq:"))
        self.ledit_minf.setText(_translate("MainWindow", "944"))
        self.label_40.setText(_translate("MainWindow", "MHz"))
        self.label_38.setText(_translate("MainWindow", "Max Freq:"))
        self.ledit_maxf.setText(_translate("MainWindow", "1220"))
        self.label_35.setText(_translate("MainWindow", "Step Size:"))
        self.label_41.setText(_translate("MainWindow", "MHz"))
        self.ledit_stepS.setText(_translate("MainWindow", "1"))
        self.btn_sweep.setText(_translate("MainWindow", "Sweep"))
        self.label_36.setText(_translate("MainWindow", "Dwell Time:"))
        self.ledit_dwellT.setText(_translate("MainWindow", "3"))
        self.label_44.setText(_translate("MainWindow", "Sec."))
        self.groupBox_3.setTitle(_translate("MainWindow", "GroupBox"))
        self.rbtn_SpurNB.setText(_translate("MainWindow", "Spur NB"))
        self.rbtn_SpurWB.setText(_translate("MainWindow", "Spur WB"))
        self.cbox_Div64.setText(_translate("MainWindow", "Div 64"))
        self.btn_reset.setToolTip(_translate("MainWindow", "This will reset the switches back to red/off"))
        self.btn_reset.setWhatsThis(_translate("MainWindow", "This will reset the switches back to red/off"))
        self.btn_reset.setText(_translate("MainWindow", "Reset "))
        self.btn_reset.setShortcut(_translate("MainWindow", "Ctrl+R"))
        self.rbtn_Sweep.setText(_translate("MainWindow", "Sweep"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
