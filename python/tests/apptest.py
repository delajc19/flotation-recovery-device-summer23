# Joseph de la Viesca
# Luthy Lab
# Wireless Floatation Device Trigger
# UI for shore-side application

from PyQt6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PyQt6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PyQt6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSpinBox,
    QTabWidget, QWidget)

import sys

import serial
import time

ser = serial.Serial('COM5')

ser.baudrate = 9600
ser.bytesize = 8
ser.parity = 'N'
ser.stopbits = 1

time.sleep(3)

isFiring = False

print(ser.name)
ser.write(b'hello')

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        #Main Window
        MainWindow.resize(418, 317)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(418, 317))
        MainWindow.setMaximumSize(QSize(418, 317))
        MainWindow.setAnimated(True)
        MainWindow.setTabShape(QTabWidget.TabShape.Rounded)
        MainWindow.setDockOptions(QMainWindow.DockOption.AllowTabbedDocks|QMainWindow.DockOption.AnimatedDocks)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        
        #Fire button
        self.fireButton = QPushButton(self.centralwidget)
        self.fireButton.setObjectName(u"fireButton")
        self.fireButton.setGeometry(QRect(10, 200, 181, 101))
        self.fireButton.setAutoFillBackground(True)
        self.fireButton.setStyleSheet(u"font: 600 40pt \"Bahnschrift\";")
        self.fireButton.setCheckable(False)
        self.fireButton.clicked.connect(self.buttonPushed)
        
        #Fire time spin box
        self.fireTime = QSpinBox(self.centralwidget)
        self.fireTime.setObjectName(u"fireTime")
        self.fireTime.setGeometry(QRect(280, 240, 61, 61))
        self.fireTime.setAutoFillBackground(True)
        self.fireTime.setMaximum(30)
        self.fireTime.setMinimum(1)
        
        #Fire Time spin box label
        self.fireTimeLabel = QLabel(self.centralwidget)
        self.fireTimeLabel.setObjectName(u"fireTimeLabel")
        self.fireTimeLabel.setGeometry(QRect(220, 200, 181, 41))
        self.fireTimeLabel.setAutoFillBackground(False)
        self.fireTimeLabel.setStyleSheet(u"font: 600 24pt \"Bahnschrift\";")
        MainWindow.setCentralWidget(self.centralwidget)
        
        #Status Frame
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 10, 401, 181))
        self.frame.setAutoFillBackground(True)
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        
        #Initialize grid layout for UI components
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        
        #Status section label
        self.statusLabel = QLabel(self.frame)
        self.statusLabel.setObjectName(u"statusLabel")
        self.statusLabel.setAutoFillBackground(True)
        self.statusLabel.setStyleSheet(u"font: 600 20pt \"Bahnschrift\";")

        self.gridLayout.addWidget(self.statusLabel, 0, 0, 1, 1)
        
        #System status display
        self.statusIndicator = QLabel(self.frame)
        self.statusIndicator.setObjectName(u"statusIndicator")
        self.statusIndicator.setAutoFillBackground(True)
        self.statusIndicator.setStyleSheet(u"font: 600 20pt \"Bahnschrift\";")

        self.gridLayout.addWidget(self.statusIndicator, 0, 1, 1, 2, Qt.AlignmentFlag.AlignHCenter)
        
        #Depth section label
        self.depthLabel = QLabel(self.frame)
        self.depthLabel.setObjectName(u"depthLabel")
        self.depthLabel.setAutoFillBackground(True)
        self.depthLabel.setStyleSheet(u"font: 600 20pt \"Bahnschrift\";")
        
        self.gridLayout.addWidget(self.depthLabel, 1, 0, 1, 1)
        
        #Depth value
        self.depthVal = QLabel(self.frame)
        self.depthVal.setObjectName(u"depthVal")
        self.depthVal.setAutoFillBackground(True)
        self.depthVal.setStyleSheet(u"font: 600 20pt \"Bahnschrift\";")

        self.gridLayout.addWidget(self.depthVal, 1, 1, 1, 1, Qt.AlignmentFlag.AlignRight)
        
        #Unit label for depth
        self.depthUnit = QLabel(self.frame)
        self.depthUnit.setObjectName(u"depthUnit")
        self.depthUnit.setAutoFillBackground(True)
        self.depthUnit.setStyleSheet(u"font: 600 20pt \"Bahnschrift\";")

        self.gridLayout.addWidget(self.depthUnit, 1, 2, 1, 1)
        
        #Distance section label
        self.distLabel = QLabel(self.frame)
        self.distLabel.setObjectName(u"distLabel")
        self.distLabel.setAutoFillBackground(True)
        self.distLabel.setStyleSheet(u"font: 600 20pt \"Bahnschrift\";")

        self.gridLayout.addWidget(self.distLabel, 2, 0, 1, 1)
        
        #Distance value
        self.distVal = QLabel(self.frame)
        self.distVal.setObjectName(u"distVal")
        self.distVal.setAutoFillBackground(True)
        self.distVal.setStyleSheet(u"font: 600 20pt \"Bahnschrift\";")

        self.gridLayout.addWidget(self.distVal, 2, 1, 1, 1, Qt.AlignmentFlag.AlignRight)
        
        #Unit label for distance
        self.distUnit = QLabel(self.frame)
        self.distUnit.setObjectName(u"distUnit")
        self.distUnit.setAutoFillBackground(True)
        self.distUnit.setStyleSheet(u"font: 600 20pt \"Bahnschrift\";")

        self.gridLayout.addWidget(self.distUnit, 2, 2, 1, 1)

        self.retranslateUi(MainWindow)
        
        
        
        QMetaObject.connectSlotsByName(MainWindow)
        
        
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Float Trigger", None))
        self.fireButton.setText(QCoreApplication.translate("MainWindow", u"FIRE", None))
        self.depthLabel.setText(QCoreApplication.translate("MainWindow", u"Depth:", None))
        self.distUnit.setText(QCoreApplication.translate("MainWindow", u"ft", None))
        self.depthUnit.setText(QCoreApplication.translate("MainWindow", u"ft", None))
        self.statusLabel.setText(QCoreApplication.translate("MainWindow", u"Status:", None))
        self.distLabel.setText(QCoreApplication.translate("MainWindow", u"Distance:", None))
        self.depthVal.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.statusIndicator.setText(QCoreApplication.translate("MainWindow", u"Not Fired", None))
        self.distVal.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.fireTimeLabel.setText(QCoreApplication.translate("MainWindow", u"Fire Time (s)", None))
    # retranslateUi
    
    def buttonPushed(self):
        self.fireButton.setEnabled(False)
        self.statusIndicator.setText("Firing")
        buf = 'wcq,4,fire,' + str(self.fireTime.value())
        ser.write(buf.encode('ascii'))
        print(self.statusIndicator.text())
        self.checkFired()
        self.fireButton.setEnabled(True)
        
    def checkFired(self):
        while "Firing" in self.statusIndicator.text():
            msg = str(ser.read(ser.in_waiting))
            print(msg)
            if 'wcq,5,fired' in msg:
                self.statusIndicator.setText("Fired")
        

if __name__ =='__main__':
    app = QApplication(sys.argv)
    app.setStyle("fusion")
    window = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec())