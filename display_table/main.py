from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from connect import Ui_Form
from table import Ui_MainWindow
from insert import Ui_Form_add_data
import pymssql
import pandas as pd
import numpy as np
import sys

# it should be declared before MainWindow, which then can have inheretance.
class DB_operation():
    def __init__(self):
        pass

    def display_table(self):
        # show the window object
        self.mainwindow.show()
        
        # fetch the table
        self.df = self.select('my_table', self.conn)
        self.table.tableWidget_npi.setRowCount(np.shape(self.df)[0])
        self.table.tableWidget_npi.setColumnCount(np.shape(self.df)[1])
        self.table.tableWidget_npi.setHorizontalHeaderLabels(self.df.columns)
        for row in range(np.shape(self.df)[0]):
            for col in range(np.shape(self.df)[1]):
                try:
                    # TableWidget contains TableWidgetItem
                    self.table.tableWidget_npi.setItem(row, col, QTableWidgetItem( self.df.iloc[row][col]))
                except:
                    continue
    
    # show the window of inputing data
    def select(self, table_name, conn):
        self.sqlstr = 'SELECT * FROM ' + table_name
        self.df = pd.read_sql(self.sqlstr, conn)
        return self.df
    
    # after inputing data, connect to add_data()
    def on_pushButton_add_clicked(self):
        self.widget_insert.show()
        self.form_insert.pushButton_insert.clicked.connect(self.on_pushButton_insert_clicked)

    def on_pushButton_insert_clicked(self):
        # fetch the table
        table_name = 'my_table'
        columns = tuple(self.df.columns)
        values = list()
        self.widget_insert.close() 
        
        # get the data inputed by the user according to the order of the columns
        # hint -- lineEdit: text(), comboBox: currentText(), spinBox: value()
        values.append(self.form_insert.lineEdit_model_name_cht.text())
        values.append(self.form_insert.lineEdit_model_name_eng.text())
        values.append(self.form_insert.lineEdit_parts_no.text())
        values.append(self.form_insert.lineEdit_model_name.text())
        values.append(self.form_insert.lineEdit_project_name.text())
        values.append(self.form_insert.lineEdit_process.text())
        values.append(self.form_insert.spinBox_num.value())
        values.append(self.form_insert.comboBox_mfi.currentText())
        values.append(self.form_insert.comboBox_customer_supply.currentText())
        values.append(self.form_insert.comboBox_track_location.currentText())
        values.append(self.form_insert.lineEdit_location.text())
        values.append(self.form_insert.lineEdit_emp_id.text())
        values.append(self.form_insert.lineEdit_remark.text())
        values.append(self.form_insert.lineEdit_track_in_date.text())
        values.append(self.form_insert.lineEdit_track_in_user.text())

        values = str(tuple(values)) # already include ()
        columns = str(columns).replace("'", "") # already include ()
        self.sqlstr = 'INSERT INTO ' + table_name +  columns + ' VALUES ' +  values  
        print(self.sqlstr)
        cursor = self.conn.cursor()      # create cursor object
        cursor.execute(self.sqlstr)      # execute
        self.conn.commit()               # submit the action
        cursor.close()
        self.display_table()

    def delete_data(self, table_name):
        self.df = self.select(table_name, self.conn)
        index = self.table.tableWidget_npi.currentRow()
        model_name_cht = self.df.iloc[index, 0]
        value = "'" + model_name_cht + "'"
        self.sqlstr = 'DELETE FROM ' + table_name + ' WHERE Model_Name_CHT = ' + value
        cursor = self.conn.cursor()
        cursor.execute(self.sqlstr)
        self.conn.commit()
        cursor.close()
        self.display_table()

class MainWindow(QMainWindow, Ui_Form, Ui_MainWindow, Ui_Form_add_data, DB_operation):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_connect.clicked.connect(self.connect_db)

        # create a new window object for later use
        self.mainwindow = QMainWindow()
        self.widget_insert = QWidget()
        # create a instance of class Ui_MainWindow
        self.table = Ui_MainWindow()
        self.form_insert = Ui_Form_add_data()
        # style the window object with the Ui_MainWindow instance, make sure it is ready to show
        self.table.setupUi(self.mainwindow)
        self.form_insert.setupUi(self.widget_insert)

        self.action_event()
            
    def connect_db(self):
        if self.lineEdit_ip.text() == 'combination_of_digits' and self.lineEdit_username.text() == 'my_username' and \
           self.lineEdit_password.text() == 'my_password' and self.lineEdit_database.text() == 'my_database':
            self.conn = pymssql.connect(server='combination_of_digits',
                                        user='my_username',
                                        password='my_password',
                                        database='my_database')
            print('connected.')
            # close the window, not the connection
            self.close()
            self.display_table()
            
        else:
            self.label_prompt.setText('Connection failed. Please check the information.')

    def action_event(self):
        self.table.pushButton_add.clicked.connect(self.on_pushButton_add_clicked)
        self.table.pushButton_delete.clicked.connect(lambda: self.delete_data('my_table'))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())