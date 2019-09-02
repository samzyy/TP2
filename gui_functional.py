# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import sys
import glob
import serial
import time
from PyQt5 import QtCore, QtGui, QtWidgets

def serial_ports():

    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result

class Ui_MainWindow(object):

    fitzpatrick_score = 0
    fitzpatrick_type = 0
    fitzpatrick_genetic_1_score = 0
    fitzpatrick_genetic_2_score = 0
    fitzpatrick_genetic_3_score = 0
    fitzpatrick_genetic_4_score = 0
    fitzpatrick_sensitivity_1_score = 0
    fitzpatrick_sensitivity_2_score = 0
    fitzpatrick_sensitivity_3_score = 0
    fitzpatrick_sensitivity_4_score = 0
    fitzpatrick_exposure_1_score = 0
    fitzpatrick_exposure_2_score = 0

    MED = 0
    connected = 0
    fitzpatrick_type_set = 0

    available_ports = serial_ports()
    number_ports = len(available_ports)
    ser = None
    connected_port = ""

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1111, 823)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(20, 40, 221, 31))
        self.comboBox.setObjectName("comboBox")
        if len(self.available_ports) == 0:
            self.comboBox.addItem("")
        else:
            for i in range(len(self.available_ports)):
                self.comboBox.addItem("")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(70, 80, 103, 31))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 3000, 20))
        self.label.setAutoFillBackground(False)
        self.label.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setScaledContents(False)
        self.label.setObjectName("label")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(20, 120, 221, 391))
        self.listWidget.setAutoFillBackground(False)
        self.listWidget.setFrameShape(QtWidgets.QFrame.Box)
        self.listWidget.setViewMode(QtWidgets.QListView.ListMode)
        self.listWidget.setObjectName("listWidget")
        self.listWidget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.listWidget.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setEnabled(False)
        self.frame.setGeometry(QtCore.QRect(10, 30, 241, 491))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(270, 30, 821, 51))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.comboBox_2 = QtWidgets.QComboBox(self.frame_2)
        self.comboBox_2.setGeometry(QtCore.QRect(10, 10, 241, 31))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label_12 = QtWidgets.QLabel(self.frame_2)
        self.label_12.setGeometry(QtCore.QRect(260, 5, 551, 41))
        self.label_12.setWordWrap(True)
        self.label_12.setObjectName("label_12")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(270, 90, 281, 421))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_4 = QtWidgets.QLabel(self.frame_3)
        self.label_4.setGeometry(QtCore.QRect(10, 260, 241, 41))
        self.label_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.comboBox_5 = QtWidgets.QComboBox(self.frame_3)
        self.comboBox_5.setGeometry(QtCore.QRect(10, 310, 241, 22))
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_6 = QtWidgets.QComboBox(self.frame_3)
        self.comboBox_6.setGeometry(QtCore.QRect(10, 390, 241, 22))
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.label_5 = QtWidgets.QLabel(self.frame_3)
        self.label_5.setGeometry(QtCore.QRect(10, 340, 241, 41))
        self.label_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 251, 41))
        self.label_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        self.label_3.setGeometry(QtCore.QRect(10, 170, 241, 41))
        self.label_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.comboBox_4 = QtWidgets.QComboBox(self.frame_3)
        self.comboBox_4.setGeometry(QtCore.QRect(10, 230, 241, 22))
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_3 = QtWidgets.QComboBox(self.frame_3)
        self.comboBox_3.setGeometry(QtCore.QRect(10, 130, 241, 22))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.label_6 = QtWidgets.QLabel(self.frame_3)
        self.label_6.setGeometry(QtCore.QRect(10, 0, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_6.setObjectName("label_6")
        self.label_17 = QtWidgets.QLabel(self.frame_3)
        self.label_17.setGeometry(QtCore.QRect(10, 30, 121, 21))
        self.label_17.setObjectName("label_17")
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setEnabled(True)
        self.frame_4.setGeometry(QtCore.QRect(550, 90, 281, 421))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.label_7 = QtWidgets.QLabel(self.frame_4)
        self.label_7.setGeometry(QtCore.QRect(10, 260, 241, 41))
        self.label_7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_7.setWordWrap(True)
        self.label_7.setObjectName("label_7")
        self.comboBox_7 = QtWidgets.QComboBox(self.frame_4)
        self.comboBox_7.setGeometry(QtCore.QRect(10, 310, 241, 22))
        self.comboBox_7.setObjectName("comboBox_7")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_8 = QtWidgets.QComboBox(self.frame_4)
        self.comboBox_8.setGeometry(QtCore.QRect(10, 390, 241, 22))
        self.comboBox_8.setObjectName("comboBox_8")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.label_8 = QtWidgets.QLabel(self.frame_4)
        self.label_8.setGeometry(QtCore.QRect(10, 340, 241, 41))
        self.label_8.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_8.setWordWrap(True)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.frame_4)
        self.label_9.setGeometry(QtCore.QRect(10, 70, 251, 51))
        self.label_9.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_9.setWordWrap(True)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.frame_4)
        self.label_10.setGeometry(QtCore.QRect(10, 170, 241, 41))
        self.label_10.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_10.setWordWrap(True)
        self.label_10.setObjectName("label_10")
        self.comboBox_9 = QtWidgets.QComboBox(self.frame_4)
        self.comboBox_9.setGeometry(QtCore.QRect(10, 230, 241, 22))
        self.comboBox_9.setObjectName("comboBox_9")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_10 = QtWidgets.QComboBox(self.frame_4)
        self.comboBox_10.setGeometry(QtCore.QRect(10, 130, 241, 22))
        self.comboBox_10.setObjectName("comboBox_10")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.label_11 = QtWidgets.QLabel(self.frame_4)
        self.label_11.setGeometry(QtCore.QRect(10, 0, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_11.setObjectName("label_11")
        self.label_18 = QtWidgets.QLabel(self.frame_4)
        self.label_18.setGeometry(QtCore.QRect(10, 30, 231, 21))
        self.label_18.setObjectName("label_18")
        self.frame_5 = QtWidgets.QFrame(self.centralwidget)
        self.frame_5.setGeometry(QtCore.QRect(830, 90, 261, 421))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.label_14 = QtWidgets.QLabel(self.frame_5)
        self.label_14.setGeometry(QtCore.QRect(10, 70, 251, 41))
        self.label_14.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_14.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.frame_5)
        self.label_15.setGeometry(QtCore.QRect(10, 170, 241, 51))
        self.label_15.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_15.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_15.setWordWrap(True)
        self.label_15.setObjectName("label_15")
        self.comboBox_13 = QtWidgets.QComboBox(self.frame_5)
        self.comboBox_13.setGeometry(QtCore.QRect(10, 230, 241, 22))
        self.comboBox_13.setObjectName("comboBox_13")
        self.comboBox_13.addItem("")
        self.comboBox_13.addItem("")
        self.comboBox_13.addItem("")
        self.comboBox_13.addItem("")
        self.comboBox_13.addItem("")
        self.comboBox_14 = QtWidgets.QComboBox(self.frame_5)
        self.comboBox_14.setGeometry(QtCore.QRect(10, 130, 241, 22))
        self.comboBox_14.setObjectName("comboBox_14")
        self.comboBox_14.addItem("")
        self.comboBox_14.addItem("")
        self.comboBox_14.addItem("")
        self.comboBox_14.addItem("")
        self.comboBox_14.addItem("")
        self.label_16 = QtWidgets.QLabel(self.frame_5)
        self.label_16.setGeometry(QtCore.QRect(10, 0, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_16.setFont(font)
        self.label_16.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_16.setObjectName("label_16")
        self.label_19 = QtWidgets.QLabel(self.frame_5)
        self.label_19.setGeometry(QtCore.QRect(10, 30, 231, 21))
        self.label_19.setObjectName("label_19")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 371, 181, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(270, 540, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_13.setFont(font)
        self.label_13.setTextFormat(QtCore.Qt.AutoText)
        self.label_13.setObjectName("label_13")
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(270, 580, 500, 22))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalSlider.setMinimum(0)
        self.horizontalSlider.setMaximum(440)
        self.horizontalSlider.setSingleStep(1)
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(330, 540, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(890, 560, 141, 51))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setEnabled(False)
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(40, 520, 201, 41))
        self.label_21.setObjectName("label_21")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(50, 560, 141, 51))
        self.pushButton_4.setObjectName("pushButton_4")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 640, 1071, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.listWidget_2 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_2.setGeometry(QtCore.QRect(20, 670, 1071, 121))
        self.listWidget_2.setAutoFillBackground(False)
        self.listWidget_2.setFrameShape(QtWidgets.QFrame.Box)
        self.listWidget_2.setViewMode(QtWidgets.QListView.ListMode)
        self.listWidget_2.setObjectName("listWidget_2")
        self.listWidget_2.addItem("TERMINAL OUTPUT\n")
        self.listWidget_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.listWidget_2.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.frame.raise_()
        self.frame_4.raise_()
        self.frame_3.raise_()
        self.frame_2.raise_()
        self.comboBox.raise_()
        self.pushButton.raise_()
        self.label.raise_()
        self.listWidget.raise_()
        self.listWidget_2.raise_()
        self.frame_5.raise_()
        self.label_13.raise_()
        self.horizontalSlider.raise_()
        self.label_20.raise_()
        self.pushButton_3.raise_()
        self.label_21.raise_()
        self.pushButton_4.raise_()
        self.lineEdit.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1111, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.timer = QtCore.QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.timeout_operations)
        self.timer.start()

        self.comboBox_2.activated.connect(self.manual_set_fitzpatrick)
        self.comboBox_3.activated.connect(self.fitzpatrick_genetic_1)
        self.comboBox_4.activated.connect(self.fitzpatrick_genetic_2)
        self.comboBox_5.activated.connect(self.fitzpatrick_genetic_3)
        self.comboBox_6.activated.connect(self.fitzpatrick_genetic_4)
        self.comboBox_10.activated.connect(self.fitzpatrick_sensitivity_1)
        self.comboBox_9.activated.connect(self.fitzpatrick_sensitivity_2)
        self.comboBox_7.activated.connect(self.fitzpatrick_sensitivity_3)
        self.comboBox_8.activated.connect(self.fitzpatrick_sensitivity_4)
        self.comboBox_14.activated.connect(self.fitzpatrick_exposure_1)
        self.comboBox_13.activated.connect(self.fitzpatrick_exposure_2)

        self.pushButton.clicked.connect(self.connect_port)
        self.pushButton_2.clicked.connect(self.set_fitzpatrick)

        self.horizontalSlider.valueChanged.connect(self.slider_med)

        self.lineEdit.returnPressed.connect(self.input_terminal)

    def timeout_operations(self):
        self.label_21.setText(QtCore.QDateTime.currentDateTime().toString())
        self.available_ports = serial_ports()
        if len(self.available_ports) != self.number_ports:
            self.number_ports = len(self.available_ports)
            self.comboBox.clear()
            if self.number_ports == 0:
                self.comboBox.addItem("No serial port found")
            else:
                for i in range(self.number_ports):
                    self.comboBox.addItem(self.available_ports[i])
        if self.connected == 1:
            disconnected_port = 1
            for i in range(self.number_ports):
                if self.available_ports[i] == self.connected_port:
                    disconnected_port = 0
                    break
            if disconnected_port:
                self.ser = None
                self.listWidget_2.addItem("[" + QtCore.QDateTime.currentDateTime().time().toString() + "] " + \
                "Device disconnected.\n")
                self.listWidget_2.scrollToBottom()
                self.connected = 0
                self.pushButton.setText("Connect")
                self.label.setText("Status: Not connected. Please select the serial port and click connect.");
                self.pushButton_3.setEnabled(False)


    def fitzpatrick_genetic_1(self):
        if self.comboBox_3.currentIndex() == 0:
            self.fitzpatrick_genetic_1_score = 0
        elif self.comboBox_3.currentIndex() == 1:
            self.fitzpatrick_genetic_1_score = 1
        elif self.comboBox_3.currentIndex() == 2:
            self.fitzpatrick_genetic_1_score = 2
        elif self.comboBox_3.currentIndex() == 3:
            self.fitzpatrick_genetic_1_score = 3
        else:
            self.fitzpatrick_genetic_1_score = 4

    def fitzpatrick_genetic_2(self):
        if self.comboBox_4.currentIndex() == 0:
            self.fitzpatrick_genetic_2_score = 0
        elif self.comboBox_4.currentIndex() == 1:
            self.fitzpatrick_genetic_2_score = 1
        elif self.comboBox_4.currentIndex() == 2:
            self.fitzpatrick_genetic_2_score = 2
        elif self.comboBox_4.currentIndex() == 3:
            self.fitzpatrick_genetic_2_score = 3
        else:
            self.fitzpatrick_genetic_2_score = 4

    def fitzpatrick_genetic_3(self):
        if self.comboBox_5.currentIndex() == 0:
            self.fitzpatrick_genetic_3_score = 0
        elif self.comboBox_5.currentIndex() == 1:
            self.fitzpatrick_genetic_3_score = 1
        elif self.comboBox_5.currentIndex() == 2:
            self.fitzpatrick_genetic_3_score = 2
        elif self.comboBox_5.currentIndex() == 3:
            self.fitzpatrick_genetic_3_score = 3
        else:
            self.fitzpatrick_genetic_3_score = 4

    def fitzpatrick_genetic_4(self):
        if self.comboBox_6.currentIndex() == 0:
            self.fitzpatrick_genetic_4_score = 0
        elif self.comboBox_6.currentIndex() == 1:
            self.fitzpatrick_genetic_4_score = 1
        elif self.comboBox_6.currentIndex() == 2:
            self.fitzpatrick_genetic_4_score = 2
        elif self.comboBox_6.currentIndex() == 3:
            self.fitzpatrick_genetic_4_score = 3
        else:
            self.fitzpatrick_genetic_4_score = 4

    def fitzpatrick_sensitivity_1(self):
        if self.comboBox_10.currentIndex() == 0:
            self.fitzpatrick_sensitivity_1_score = 0
        elif self.comboBox_10.currentIndex() == 1:
            self.fitzpatrick_sensitivity_1_score = 1
        elif self.comboBox_10.currentIndex() == 2:
            self.fitzpatrick_sensitivity_1_score = 2
        elif self.comboBox_10.currentIndex() == 3:
            self.fitzpatrick_sensitivity_1_score = 3
        else:
            self.fitzpatrick_sensitivity_1_score = 4

    def fitzpatrick_sensitivity_2(self):
        if self.comboBox_9.currentIndex() == 0:
            self.fitzpatrick_sensitivity_2_score = 0
        elif self.comboBox_9.currentIndex() == 1:
            self.fitzpatrick_sensitivity_2_score = 1
        elif self.comboBox_9.currentIndex() == 2:
            self.fitzpatrick_sensitivity_2_score = 2
        elif self.comboBox_9.currentIndex() == 3:
            self.fitzpatrick_sensitivity_2_score = 3
        else:
            self.fitzpatrick_sensitivity_2_score = 4

    def fitzpatrick_sensitivity_3(self):
        if self.comboBox_7.currentIndex() == 0:
            self.fitzpatrick_sensitivity_3_score = 0
        elif self.comboBox_7.currentIndex() == 1:
            self.fitzpatrick_sensitivity_3_score = 1
        elif self.comboBox_7.currentIndex() == 2:
            self.fitzpatrick_sensitivity_3_score = 2
        elif self.comboBox_7.currentIndex() == 3:
            self.fitzpatrick_sensitivity_3_score = 3
        else:
            self.fitzpatrick_sensitivity_3_score = 4

    def fitzpatrick_sensitivity_4(self):
        if self.comboBox_8.currentIndex() == 0:
            self.fitzpatrick_sensitivity_4_score = 0
        elif self.comboBox_8.currentIndex() == 1:
            self.fitzpatrick_sensitivity_4_score = 1
        elif self.comboBox_8.currentIndex() == 2:
            self.fitzpatrick_sensitivity_4_score = 2
        elif self.comboBox_8.currentIndex() == 3:
            self.fitzpatrick_sensitivity_4_score = 3
        else:
            self.fitzpatrick_sensitivity_4_score = 4

    def fitzpatrick_exposure_1(self):
        if self.comboBox_14.currentIndex() == 0:
            self.fitzpatrick_exposure_1_score = 0
        elif self.comboBox_14.currentIndex() == 1:
            self.fitzpatrick_exposure_1_score = 1
        elif self.comboBox_14.currentIndex() == 2:
            self.fitzpatrick_exposure_1_score = 2
        elif self.comboBox_14.currentIndex() == 3:
            self.fitzpatrick_exposure_1_score = 3
        else:
            self.fitzpatrick_exposure_1_score = 4

    def fitzpatrick_exposure_2(self):
        if self.comboBox_13.currentIndex() == 0:
            self.fitzpatrick_exposure_2_score = 0
        elif self.comboBox_13.currentIndex() == 1:
            self.fitzpatrick_exposure_2_score = 1
        elif self.comboBox_13.currentIndex() == 2:
            self.fitzpatrick_exposure_2_score = 2
        elif self.comboBox_13.currentIndex() == 3:
            self.fitzpatrick_exposure_2_score = 3
        else:
            self.fitzpatrick_exposure_2_score = 4

    def fitzpatrick_type_0(self):
        self.fitzpatrick_type = 0
        self.MED = 0
        self.label_12.setText("Note: Fitzpatrick skin type currently not set. "
        "Please select from the dropdown box or take the quiz below.")
        self.label_20.setText("{} SED".format(self.MED))
        self.horizontalSlider.setValue(self.MED)
        self.pushButton_3.setEnabled(False)
        self.fitzpatrick_type_set = 0

    def fitzpatrick_type_1(self):
        self.fitzpatrick_type = 1
        self.MED = 150
        self.comboBox_2.setCurrentText("Fitzpatrick Skin Type I")
        self.label_12.setText("Note: Fitzpatrick Skin Type I set.")
        self.label_20.setText("{} SED".format(self.MED))
        self.horizontalSlider.setValue(self.MED)
        self.fitzpatrick_type_set = 1
        if self.connected:
            self.pushButton_3.setEnabled(True)
        else:
            self.pushButton_3.setEnabled(False)

    def fitzpatrick_type_2(self):
        self.fitzpatrick_type = 2
        self.MED = 220
        self.comboBox_2.setCurrentText("Fitzpatrick Skin Type II")
        self.label_12.setText("Note: Fitzpatrick Skin Type II set.")
        self.label_20.setText("{} SED".format(self.MED))
        self.horizontalSlider.setValue(self.MED)
        self.fitzpatrick_type_set = 1
        if self.connected:
            self.pushButton_3.setEnabled(True)
        else:
            self.pushButton_3.setEnabled(False)

    def fitzpatrick_type_3(self):
        self.fitzpatrick_type = 3
        self.MED = 290
        self.comboBox_2.setCurrentText("Fitzpatrick Skin Type III")
        self.label_12.setText("Note: Fitzpatrick Skin Type III set.")
        self.label_20.setText("{} SED".format(self.MED))
        self.horizontalSlider.setValue(self.MED)
        self.fitzpatrick_type_set = 1
        if self.connected:
            self.pushButton_3.setEnabled(True)
        else:
            self.pushButton_3.setEnabled(False)

    def fitzpatrick_type_4(self):
        self.fitzpatrick_type = 4
        self.MED = 370
        self.comboBox_2.setCurrentText("Fitzpatrick Skin Type IV")
        self.label_12.setText("Note: Fitzpatrick Skin Type IV set.")
        self.label_20.setText("{} SED".format(self.MED))
        self.horizontalSlider.setValue(self.MED)
        self.fitzpatrick_type_set = 1
        if self.connected:
            self.pushButton_3.setEnabled(True)
        else:
            self.pushButton_3.setEnabled(False)

    def fitzpatrick_type_5(self):
        self.fitzpatrick_type = 5
        self.MED = 440
        self.comboBox_2.setCurrentText("Fitzpatrick Skin Type V")
        self.label_12.setText("Note: Fitzpatrick Skin Type V set.")
        self.label_20.setText("{} SED".format(self.MED))
        self.horizontalSlider.setValue(self.MED)
        self.fitzpatrick_type_set = 1
        if self.connected:
            self.pushButton_3.setEnabled(True)
        else:
            self.pushButton_3.setEnabled(False)

    def fitzpatrick_type_6(self):
        self.fitzpatrick_type = 6
        self.MED = 440
        self.comboBox_2.setCurrentText("Fitzpatrick Skin Type VI")
        self.label_12.setText("Note: Fitzpatrick Skin Type VI set.")
        self.label_20.setText("{} SED".format(self.MED))
        self.horizontalSlider.setValue(self.MED)
        self.fitzpatrick_type_set = 1
        if self.connected:
            self.pushButton_3.setEnabled(True)
        else:
            self.pushButton_3.setEnabled(False)

    def set_fitzpatrick(self):
        self.fitzpatrick_score = (self.fitzpatrick_genetic_1_score +
        self.fitzpatrick_genetic_2_score + self.fitzpatrick_genetic_3_score +
        self.fitzpatrick_genetic_4_score + self.fitzpatrick_sensitivity_1_score +
        self.fitzpatrick_sensitivity_2_score  + self.fitzpatrick_sensitivity_3_score +
        self.fitzpatrick_sensitivity_4_score +self.fitzpatrick_exposure_1_score +
        self.fitzpatrick_exposure_2_score)
        print("genetic1:", self.fitzpatrick_genetic_1_score)
        print("genetic2:", self.fitzpatrick_genetic_2_score)
        print("genetic3:", self.fitzpatrick_genetic_3_score)
        print("genetic4:", self.fitzpatrick_genetic_4_score)
        print("sensitivity1:", self.fitzpatrick_sensitivity_1_score)
        print("sensitivity2:", self.fitzpatrick_sensitivity_2_score)
        print("sensitivity3:", self.fitzpatrick_sensitivity_3_score)
        print("sensitivity4:", self.fitzpatrick_sensitivity_4_score)
        print("exposure1:", self.fitzpatrick_exposure_1_score)
        print("exposure2:", self.fitzpatrick_exposure_2_score)
        print("fitzpatrick score:", self.fitzpatrick_score, "\n")
        if self.fitzpatrick_score >= 0 and self.fitzpatrick_score <= 6:
            self.fitzpatrick_type_1()
        elif self.fitzpatrick_score >= 7 and self.fitzpatrick_score <= 13:
            self.fitzpatrick_type_2()
        elif self.fitzpatrick_score >= 14 and self.fitzpatrick_score <= 20:
            self.fitzpatrick_type_3()
        elif self.fitzpatrick_score >= 21 and self.fitzpatrick_score <= 27:
            self.fitzpatrick_type_4()
        elif self.fitzpatrick_score >= 28 and self.fitzpatrick_score <= 34:
            self.fitzpatrick_type_5()
        else:
            self.fitzpatrick_type_6()

    def manual_set_fitzpatrick(self):
        if self.comboBox_2.currentIndex() == 0:
            self.fitzpatrick_type_0()
        elif self.comboBox_2.currentIndex() == 1:
            self.fitzpatrick_type_1()
        elif self.comboBox_2.currentIndex() == 2:
            self.fitzpatrick_type_2()
        elif self.comboBox_2.currentIndex() == 3:
            self.fitzpatrick_type_3()
        elif self.comboBox_2.currentIndex() == 4:
            self.fitzpatrick_type_4()
        elif self.comboBox_2.currentIndex() == 5:
            self.fitzpatrick_type_5()
        else:
            self.fitzpatrick_type_6()

    def slider_med(self):
        self.MED = self.horizontalSlider.value()
        self.label_20.setText("{} SED".format(self.MED))

    def connect_port(self):
        if not(self.connected):
            try:
                self.ser = serial.Serial(self.comboBox.currentText(), baudrate = 115200, timeout = 1)
            except serial.SerialException:
                self.ser = None
                self.label.setText("Status: Unable to connect. Please ensure you have selected the correct serial port.");
            else:
                self.connected_port = self.comboBox.currentText()
                self.ser.write(b'q23dx7\r\n')
                self.ser.readline()
                self.listWidget_2.addItem("[" + QtCore.QDateTime.currentDateTime().time().toString() + "] " + str(self.ser.readline(), 'utf-8'))
                self.listWidget_2.scrollToBottom()
                self.connected = 1
                self.pushButton.setText("Disconnect")
                self.label.setText("Status: Connected.");
                if self.fitzpatrick_type_set:
                    self.pushButton_3.setEnabled(True)
                self.ser.close()
        else:
            self.ser = None
            self.connected = 0
            self.pushButton.setText("Connect")
            self.label.setText("Status: Not connected. Please select the serial port and click connect.");
            self.listWidget_2.addItem("[" + QtCore.QDateTime.currentDateTime().time().toString() + "] " + "Device disconnected.\n")
            self.listWidget_2.scrollToBottom()
            self.pushButton_3.setEnabled(False)

    def input_terminal(self):
        if self.ser == None:
            self.listWidget_2.addItem("[" + QtCore.QDateTime.currentDateTime().time().toString() + "] " + \
            "Cannot communicate with device. Please check you have connected to the correct serial port.\n")
        else:
            input = list(self.lineEdit.text() + "\r\n")
            self.ser.open()
            for i in range(len(input)):
                self.ser.write(input[i].encode('utf-8'))
            self.ser.readline()
            self.listWidget_2.addItem("[" + QtCore.QDateTime.currentDateTime().time().toString() + "] " + str(self.ser.readline(), 'utf-8'))
            self.ser.close()
        self.listWidget_2.scrollToBottom()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ENGG3800 TEAM 41 PC SOFTWARE"))
        if len(self.available_ports) == 0:
            self.comboBox.setItemText(0, _translate("MainWindow", "No serial port found"))
        else:
            for i in range(len(self.available_ports)):
                self.comboBox.setItemText(i, _translate("MainWindow", self.available_ports[i]))
        self.pushButton.setText(_translate("MainWindow", "Connect"))
        self.label.setText(_translate("MainWindow", "Status: Not connected. Please select the serial port and click connect."))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Fitzpatrick Skin Type [Not Set]"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Fitzpatrick Skin Type I"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "Fitzpatrick Skin Type II"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "Fitzpatrick Skin Type III"))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "Fitzpatrick Skin Type IV"))
        self.comboBox_2.setItemText(5, _translate("MainWindow", "Fitzpatrick Skin Type V"))
        self.comboBox_2.setItemText(6, _translate("MainWindow", "Fitzpatrick Skin Type VI"))
        self.label_12.setText(_translate("MainWindow", "Note: Fitzpatrick skin type currently not set. Please select from the dropdown box or take the quiz below."))
        self.label_4.setText(_translate("MainWindow", "3. What is the colour of your skin (unexposed areas)?"))
        self.comboBox_5.setItemText(0, _translate("MainWindow", "Pink"))
        self.comboBox_5.setItemText(1, _translate("MainWindow", "Very pale"))
        self.comboBox_5.setItemText(2, _translate("MainWindow", "Light brown or olive"))
        self.comboBox_5.setItemText(3, _translate("MainWindow", "Brown"))
        self.comboBox_5.setItemText(4, _translate("MainWindow", "Dark brown"))
        self.comboBox_6.setItemText(0, _translate("MainWindow", "Many"))
        self.comboBox_6.setItemText(1, _translate("MainWindow", "Several"))
        self.comboBox_6.setItemText(2, _translate("MainWindow", "Few"))
        self.comboBox_6.setItemText(3, _translate("MainWindow", "Rare"))
        self.comboBox_6.setItemText(4, _translate("MainWindow", "None"))
        self.label_5.setText(_translate("MainWindow", "4. Do you have freckles on unexposed areas?"))
        self.label_2.setText(_translate("MainWindow", "1. What are the colour of your eyes?"))
        self.label_3.setText(_translate("MainWindow", "2. What is the colour of your hair (naturally and before aging)?"))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "Red"))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "Blonde"))
        self.comboBox_4.setItemText(2, _translate("MainWindow", "Chestnut or dark blonde"))
        self.comboBox_4.setItemText(3, _translate("MainWindow", "Dark brown"))
        self.comboBox_4.setItemText(4, _translate("MainWindow", "Black"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "Light blue or green, grey"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "Blue, green, grey"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "Dark blue or green, light brown (hazel)"))
        self.comboBox_3.setItemText(3, _translate("MainWindow", "Dark brown"))
        self.comboBox_3.setItemText(4, _translate("MainWindow", "Brownish black"))
        self.label_6.setText(_translate("MainWindow", "Genetic"))
        self.label_17.setText(_translate("MainWindow", "[Physical traits]"))
        self.label_7.setText(_translate("MainWindow", "3. How brown do you get?"))
        self.comboBox_7.setItemText(0, _translate("MainWindow", "Hardly or not at all"))
        self.comboBox_7.setItemText(1, _translate("MainWindow", "Light tan"))
        self.comboBox_7.setItemText(2, _translate("MainWindow", "Medium tan"))
        self.comboBox_7.setItemText(3, _translate("MainWindow", "Dark tan"))
        self.comboBox_7.setItemText(4, _translate("MainWindow", "Very dark tan"))
        self.comboBox_8.setItemText(0, _translate("MainWindow", "Very sensitive"))
        self.comboBox_8.setItemText(1, _translate("MainWindow", "Sensitive"))
        self.comboBox_8.setItemText(2, _translate("MainWindow", "Mildly sensitive"))
        self.comboBox_8.setItemText(3, _translate("MainWindow", "Resistant"))
        self.comboBox_8.setItemText(4, _translate("MainWindow", "Very resistant"))
        self.label_8.setText(_translate("MainWindow", "4. Is your face sensitive to the sun?"))
        self.label_9.setText(_translate("MainWindow", "1. What happens to your skin if you stay in the sun for an extended period?"))
        self.label_10.setText(_translate("MainWindow", "2. Do you turn brown after sun exposure?"))
        self.comboBox_9.setItemText(0, _translate("MainWindow", "Never"))
        self.comboBox_9.setItemText(1, _translate("MainWindow", "Rarely"))
        self.comboBox_9.setItemText(2, _translate("MainWindow", "Sometimes"))
        self.comboBox_9.setItemText(3, _translate("MainWindow", "Often"))
        self.comboBox_9.setItemText(4, _translate("MainWindow", "Always"))
        self.comboBox_10.setItemText(0, _translate("MainWindow", "Severe burns, blistering, peeling"))
        self.comboBox_10.setItemText(1, _translate("MainWindow", "Moderate burns, blistering, peeling"))
        self.comboBox_10.setItemText(2, _translate("MainWindow", "Burns sometimes followed by peeling"))
        self.comboBox_10.setItemText(3, _translate("MainWindow", "Rare burns"))
        self.comboBox_10.setItemText(4, _translate("MainWindow", "No burns"))
        self.label_11.setText(_translate("MainWindow", "Sensitivity"))
        self.label_18.setText(_translate("MainWindow", "[Reaction to sun exposure]"))
        self.label_14.setText(_translate("MainWindow", "1. How often do you tan?"))
        self.label_15.setText(_translate("MainWindow", "2. When did you last expose your skin to the sun or artificial tanning sources (tanning beds)?"))
        self.comboBox_13.setItemText(0, _translate("MainWindow", "More than three months ago"))
        self.comboBox_13.setItemText(1, _translate("MainWindow", "In the last 2-3 months"))
        self.comboBox_13.setItemText(2, _translate("MainWindow", "In the last 1-2 months"))
        self.comboBox_13.setItemText(3, _translate("MainWindow", "In the last week"))
        self.comboBox_13.setItemText(4, _translate("MainWindow", "In the last day"))
        self.comboBox_14.setItemText(0, _translate("MainWindow", "Never"))
        self.comboBox_14.setItemText(1, _translate("MainWindow", "Rarely"))
        self.comboBox_14.setItemText(2, _translate("MainWindow", "Sometimes"))
        self.comboBox_14.setItemText(3, _translate("MainWindow", "Often"))
        self.comboBox_14.setItemText(4, _translate("MainWindow", "Always"))
        self.label_16.setText(_translate("MainWindow", "Intentional exposure"))
        self.label_19.setText(_translate("MainWindow", "[Tanning habits]"))
        self.pushButton_2.setText(_translate("MainWindow", "Set Fitzpatrick Skin Type"))
        self.label_13.setText(_translate("MainWindow", "MED:"))
        self.label_20.setText(_translate("MainWindow", "{} SED".format(self.MED)))
        self.pushButton_3.setText(_translate("MainWindow", "Send"))
        self.label_21.setText(_translate("MainWindow", QtCore.QDateTime.currentDateTime().toString()))
        self.pushButton_4.setText(_translate("MainWindow", "Synchronise"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
