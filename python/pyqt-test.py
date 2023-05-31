from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

import sys

import serial
import time

ser = serial.Serial('COM3')

ser.baudrate = 9600
ser.bytesize = 8
ser.parity = 'N'
ser.stopbits = 1

time.sleep(3)

print(ser.name)
ser.write(b'hello')


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        
        def buttonPushed(self):
            print("wcq,4,fire")
            ser.write(b'wcq,4,fire')
                            
        self.setWindowTitle("My App")
        
        button = QPushButton("FIRE")
        button.setCheckable(True)
        button.clicked.connect(buttonPushed)
        
        self.setCentralWidget(button)
    


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()

ser.close()
