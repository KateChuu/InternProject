# Call UI Configuration .py file
from MES_System import Ui_MES_System

# PyQt is the UI Module
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QTextCursor

from datetime import datetime
import winsound
import time
import sys
import os
import io


# UI Call
class MainWindow(QMainWindow, Ui_MES_System):

    def __init__(self):
        super(MainWindow, self).__init__()
    
        # Initial setting
        self.object = None # initialize the object so we can use the functions in DLL later
        self.setupUi(self)
        self.Console_cursor = QTextCursor(self.Console.document())

        # Disable specific Ui controllers
        self.EmployeeNumber.setEnabled(False)
        self.EnterButton.setEnabled(False)
        self.iCommandSelection.setEnabled(False)
        self.InputData.setEnabled(False)
        self.CheckButton.setEnabled(False)
        self.Remark.setEnabled(False)

        # Variable Assignment
        self.connect_status = 'NG'
        self.disconnect_status = 'NG'
        self.remark = ''
        self.iCommand = ''
        self.pParameter = ''

        # System Shell
        print("System started succesfully.")
        time.sleep(1)
    
        # Initial Function Call
        self.action_event()  

    # This function contains every cases which can be operated through the UI
    def action_event(self):
        self.ConnectButton.clicked.connect(self.connect)
        self.StopButton.clicked.connect(self.disconnect)  # Hit Stop to call disconnect()
        self.EnterButton.clicked.connect(self.check_en)  # Hit Enter to call check_en()
        self.EmployeeNumber.returnPressed.connect(self.check_en) # Hit Enter to submit employee numbers 
        # self.CheckButton.clicked.connect(self.communication) 

    def connect(self):
        self.Console.clear()
        print("===========================")
        
        try:
            print("Connecting to the server...")
            start = time.time()
            self.connect_status = self.object.transStart()
            end = time.time()

        except:
            # Call example.dll, which contains functions provided by the contractor
            import clr 
            clr.FindAssembly("example")
            import example_function

            print("Initializing connection...")
            self.object = example_function.connect()
            start = time.time()
            self.connect_status = self.object.transStart()
            end = time.time()

        if "OK" in self.connect_status:
            console = "Connection succeeded.\n\nAction : Server connection.\nUsage : {} s\nLast Time : {}".format(abs(start - end), datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            self.EnterButton.setEnabled(True)
            self.EmployeeNumber.setEnabled(True)
        else:
            console = "Connection Failed.\n\nAction : Server connection.\nUsage : {} s\nLast Time : {}".format(abs(start - end), datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

        print(console)
        self.Console.insertPlainText(console)

    # Disconnect from the server
    def disconnect(self):
        try:
            self.close()  # Close the window and stop the program.
            self.connect_status = self.object.transClose()
            print()
            print(self.connect_status)
            os._exit(0)

        except Exception as e:
            self.Console_cursor.setPosition(0)
            self.Console.setTextCursor(self.Console_cursor)
            self.Console.insertPlainText("Disconnected from server.\n" + str(e) + '\n')

    # Check availability of employee numbers
    def check_en(self):

        self.Console.clear()

        try:
            en = self.EmployeeNumber.text()
            # If there is no semicolon in the end of employee numbers, add it
            if en[-1] != ";":
                en = en + ";"

            # Get remark
            start = time.time()
            self.remark = self.object.transClose("C001", en)
            end = time.time()
            print("===========================")

            # Show the result and adjust its position
            console = "{}\n\nAction : Employee number check.\nUsage : {} s\nLast Time : {}".format(self.remark, abs(start - end), datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            self.Console.insertPlainText(console)
            print(console)

            # If Employee Number is accepted, we can choose the iCommand
            if self.remark[0:2] == "OK":
                winsound.Beep(1000, 500)
                self.iCommandSelection.setEnabled(True)
                self.InputData.setEnabled(True)
                self.CheckButton.setEnabled(True)
            else:
                winsound.Beep(1000, 1000)
                self.iCommandSelection.setEnabled(False)
                self.InputData.setEnabled(False)
                self.CheckButton.setEnabled(False)

        except Exception as e:
            self.Console_cursor.setPosition(0)
            self.Console.setTextCursor(self.Console_cursor)
            self.Console.insertPlainText(str(e) + '\n') 


if __name__ == '__main__':
    try:
        print("Loading...")
        app = QtWidgets.QApplication(sys.argv)
        window = MainWindow()
        # Window can not be resized and closed
        window.setWindowFlags(Qt.WindowMinimizeButtonHint | Qt.MSWindowsFixedSizeDialogHint)
        window.show()
        sys.exit(app.exec_())

    except Exception as e:
        print(e)
