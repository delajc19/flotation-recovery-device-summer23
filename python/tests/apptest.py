# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'qtdesign-testNEMOMU.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
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
        self.fireButton = QPushButton(self.centralwidget)
        self.fireButton.setObjectName(u"fireButton")
        self.fireButton.setGeometry(QRect(10, 200, 181, 101))
        self.fireButton.setAutoFillBackground(True)
        self.fireButton.setStyleSheet(u"font: 600 40pt \"Bahnschrift\";")
        self.fireButton.setCheckable(True)
        self.fireButton.clicked.connect(self.buttonPushed)
        self.fireTime = QSpinBox(self.centralwidget)
        self.fireTime.setObjectName(u"fireTime")
        self.fireTime.setGeometry(QRect(280, 240, 61, 61))
        self.fireTime.setAutoFillBackground(True)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 10, 401, 181))
        self.frame.setAutoFillBackground(True)
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAutoFillBackground(True)
        self.label_3.setStyleSheet(u"font: 600 20pt \"Bahnschrift\";")

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAutoFillBackground(True)
        self.label_5.setStyleSheet(u"font: 600 20pt \"Bahnschrift\";")

        self.gridLayout.addWidget(self.label_5, 2, 2, 1, 1)

        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAutoFillBackground(True)
        self.label_6.setStyleSheet(u"font: 600 20pt \"Bahnschrift\";")

        self.gridLayout.addWidget(self.label_6, 1, 2, 1, 1)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAutoFillBackground(True)
        self.label_2.setStyleSheet(u"font: 600 20pt \"Bahnschrift\";")

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAutoFillBackground(True)
        self.label_4.setStyleSheet(u"font: 600 20pt \"Bahnschrift\";")

        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)

        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAutoFillBackground(True)
        self.label_8.setStyleSheet(u"font: 600 20pt \"Bahnschrift\";")

        self.gridLayout.addWidget(self.label_8, 1, 1, 1, 1, Qt.AlignmentFlag.AlignRight)

        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAutoFillBackground(True)
        self.label_7.setStyleSheet(u"font: 600 20pt \"Bahnschrift\";")

        self.gridLayout.addWidget(self.label_7, 0, 1, 1, 2, Qt.AlignmentFlag.AlignHCenter)

        self.label_9 = QLabel(self.frame)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAutoFillBackground(True)
        self.label_9.setStyleSheet(u"font: 600 20pt \"Bahnschrift\";")

        self.gridLayout.addWidget(self.label_9, 2, 1, 1, 1, Qt.AlignmentFlag.AlignRight)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(220, 200, 181, 41))
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet(u"font: 600 24pt \"Bahnschrift\";")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
        
        
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Float Trigger", None))
        self.fireButton.setText(QCoreApplication.translate("MainWindow", u"FIRE", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Depth:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"ft", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"ft", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Status:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Distance:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Ready!", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Fire Time (s)", None))
    # retranslateUi
    
    def buttonPushed(self):
        print("wcq,4,fire")
        # ser.write(b'wcq,4,fire')

if __name__ =='__main__':
    import sys
    app = QApplication(sys.argv)
    window = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec())