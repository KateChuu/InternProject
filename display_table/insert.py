# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'insert.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form_add_data(object):
    def setupUi(self, Form_add_data):
        Form_add_data.setObjectName("Form_add_data")
        Form_add_data.resize(495, 432)
        self.label_parts_no = QtWidgets.QLabel(Form_add_data)
        self.label_parts_no.setGeometry(QtCore.QRect(240, 70, 61, 16))
        self.label_parts_no.setObjectName("label_parts_no")
        self.label_project_name = QtWidgets.QLabel(Form_add_data)
        self.label_project_name.setGeometry(QtCore.QRect(240, 120, 91, 16))
        self.label_project_name.setObjectName("label_project_name")
        self.label_num = QtWidgets.QLabel(Form_add_data)
        self.label_num.setGeometry(QtCore.QRect(210, 200, 47, 12))
        self.label_num.setObjectName("label_num")
        self.label_customer_supply = QtWidgets.QLabel(Form_add_data)
        self.label_customer_supply.setGeometry(QtCore.QRect(310, 200, 91, 16))
        self.label_customer_supply.setObjectName("label_customer_supply")
        self.label_location = QtWidgets.QLabel(Form_add_data)
        self.label_location.setGeometry(QtCore.QRect(210, 240, 47, 12))
        self.label_location.setObjectName("label_location")
        self.label_track_in_user = QtWidgets.QLabel(Form_add_data)
        self.label_track_in_user.setGeometry(QtCore.QRect(250, 350, 81, 20))
        self.label_track_in_user.setObjectName("label_track_in_user")
        self.lineEdit_model_name_cht = QtWidgets.QLineEdit(Form_add_data)
        self.lineEdit_model_name_cht.setGeometry(QtCore.QRect(130, 30, 331, 20))
        self.lineEdit_model_name_cht.setObjectName("lineEdit_model_name_cht")
        self.lineEdit_model_name_eng = QtWidgets.QLineEdit(Form_add_data)
        self.lineEdit_model_name_eng.setGeometry(QtCore.QRect(130, 70, 91, 20))
        self.lineEdit_model_name_eng.setObjectName("lineEdit_model_name_eng")
        self.lineEdit_parts_no = QtWidgets.QLineEdit(Form_add_data)
        self.lineEdit_parts_no.setGeometry(QtCore.QRect(290, 70, 171, 20))
        self.lineEdit_parts_no.setObjectName("lineEdit_parts_no")
        self.lineEdit_model_name = QtWidgets.QLineEdit(Form_add_data)
        self.lineEdit_model_name.setGeometry(QtCore.QRect(130, 120, 91, 20))
        self.lineEdit_model_name.setObjectName("lineEdit_model_name")
        self.lineEdit_project_name = QtWidgets.QLineEdit(Form_add_data)
        self.lineEdit_project_name.setGeometry(QtCore.QRect(320, 120, 141, 20))
        self.lineEdit_project_name.setObjectName("lineEdit_project_name")
        self.lineEdit_process = QtWidgets.QLineEdit(Form_add_data)
        self.lineEdit_process.setGeometry(QtCore.QRect(130, 160, 331, 20))
        self.lineEdit_process.setObjectName("lineEdit_process")
        self.lineEdit_location = QtWidgets.QLineEdit(Form_add_data)
        self.lineEdit_location.setGeometry(QtCore.QRect(260, 240, 201, 20))
        self.lineEdit_location.setObjectName("lineEdit_location")
        self.lineEdit_emp_id = QtWidgets.QLineEdit(Form_add_data)
        self.lineEdit_emp_id.setGeometry(QtCore.QRect(130, 280, 331, 20))
        self.lineEdit_emp_id.setObjectName("lineEdit_emp_id")
        self.lineEdit_remark = QtWidgets.QLineEdit(Form_add_data)
        self.lineEdit_remark.setGeometry(QtCore.QRect(130, 310, 331, 20))
        self.lineEdit_remark.setObjectName("lineEdit_remark")
        self.lineEdit_track_in_date = QtWidgets.QLineEdit(Form_add_data)
        self.lineEdit_track_in_date.setGeometry(QtCore.QRect(130, 350, 113, 20))
        self.lineEdit_track_in_date.setObjectName("lineEdit_track_in_date")
        self.lineEdit_track_in_user = QtWidgets.QLineEdit(Form_add_data)
        self.lineEdit_track_in_user.setGeometry(QtCore.QRect(330, 350, 131, 20))
        self.lineEdit_track_in_user.setObjectName("lineEdit_track_in_user")
        self.comboBox_mfi = QtWidgets.QComboBox(Form_add_data)
        self.comboBox_mfi.setGeometry(QtCore.QRect(130, 200, 71, 22))
        self.comboBox_mfi.setObjectName("comboBox_mfi")
        self.comboBox_mfi.addItem("")
        self.comboBox_mfi.addItem("")
        self.spinBox_num = QtWidgets.QSpinBox(Form_add_data)
        self.spinBox_num.setGeometry(QtCore.QRect(260, 200, 41, 22))
        self.spinBox_num.setObjectName("spinBox_num")
        self.comboBox_track_location = QtWidgets.QComboBox(Form_add_data)
        self.comboBox_track_location.setGeometry(QtCore.QRect(130, 240, 71, 22))
        self.comboBox_track_location.setObjectName("comboBox_track_location")
        self.comboBox_track_location.addItem("")
        self.comboBox_track_location.addItem("")
        self.comboBox_customer_supply = QtWidgets.QComboBox(Form_add_data)
        self.comboBox_customer_supply.setGeometry(QtCore.QRect(400, 200, 61, 22))
        self.comboBox_customer_supply.setObjectName("comboBox_customer_supply")
        self.comboBox_customer_supply.addItem("")
        self.comboBox_customer_supply.addItem("")
        self.layoutWidget = QtWidgets.QWidget(Form_add_data)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 30, 94, 351))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_model_name_cht = QtWidgets.QLabel(self.layoutWidget)
        self.label_model_name_cht.setObjectName("label_model_name_cht")
        self.verticalLayout.addWidget(self.label_model_name_cht)
        self.label_model_name_eng = QtWidgets.QLabel(self.layoutWidget)
        self.label_model_name_eng.setObjectName("label_model_name_eng")
        self.verticalLayout.addWidget(self.label_model_name_eng)
        self.label_model_name = QtWidgets.QLabel(self.layoutWidget)
        self.label_model_name.setObjectName("label_model_name")
        self.verticalLayout.addWidget(self.label_model_name)
        self.label_process = QtWidgets.QLabel(self.layoutWidget)
        self.label_process.setObjectName("label_process")
        self.verticalLayout.addWidget(self.label_process)
        self.label_mfi = QtWidgets.QLabel(self.layoutWidget)
        self.label_mfi.setObjectName("label_mfi")
        self.verticalLayout.addWidget(self.label_mfi)
        self.label_track_location = QtWidgets.QLabel(self.layoutWidget)
        self.label_track_location.setObjectName("label_track_location")
        self.verticalLayout.addWidget(self.label_track_location)
        self.label_emp_id = QtWidgets.QLabel(self.layoutWidget)
        self.label_emp_id.setObjectName("label_emp_id")
        self.verticalLayout.addWidget(self.label_emp_id)
        self.label_remark = QtWidgets.QLabel(self.layoutWidget)
        self.label_remark.setObjectName("label_remark")
        self.verticalLayout.addWidget(self.label_remark)
        self.label_track_in_date = QtWidgets.QLabel(self.layoutWidget)
        self.label_track_in_date.setObjectName("label_track_in_date")
        self.verticalLayout.addWidget(self.label_track_in_date)
        self.pushButton_insert = QtWidgets.QPushButton(Form_add_data)
        self.pushButton_insert.setGeometry(QtCore.QRect(370, 390, 91, 23))
        self.pushButton_insert.setObjectName("pushButton_insert")

        self.retranslateUi(Form_add_data)
        QtCore.QMetaObject.connectSlotsByName(Form_add_data)

    def retranslateUi(self, Form_add_data):
        _translate = QtCore.QCoreApplication.translate
        Form_add_data.setWindowTitle(_translate("Form_add_data", "Form"))
        self.label_parts_no.setText(_translate("Form_add_data", "Parts_No"))
        self.label_project_name.setText(_translate("Form_add_data", "Project_Name"))
        self.label_num.setText(_translate("Form_add_data", "Num"))
        self.label_customer_supply.setText(_translate("Form_add_data", "Customer_Supply"))
        self.label_location.setText(_translate("Form_add_data", "Location"))
        self.label_track_in_user.setText(_translate("Form_add_data", "Track_In_User"))
        self.comboBox_mfi.setItemText(0, _translate("Form_add_data", "Not_Mfi"))
        self.comboBox_mfi.setItemText(1, _translate("Form_add_data", "Is_Mfi"))
        self.comboBox_track_location.setItemText(0, _translate("Form_add_data", "入庫"))
        self.comboBox_track_location.setItemText(1, _translate("Form_add_data", "退庫"))
        self.comboBox_customer_supply.setItemText(0, _translate("Form_add_data", "非客供"))
        self.comboBox_customer_supply.setItemText(1, _translate("Form_add_data", "客供"))
        self.label_model_name_cht.setText(_translate("Form_add_data", "Model_Name_CHT"))
        self.label_model_name_eng.setText(_translate("Form_add_data", "Model_Name_ENG"))
        self.label_model_name.setText(_translate("Form_add_data", "Model_Name"))
        self.label_process.setText(_translate("Form_add_data", "Process"))
        self.label_mfi.setText(_translate("Form_add_data", "Mfi"))
        self.label_track_location.setText(_translate("Form_add_data", "Track_Location"))
        self.label_emp_id.setText(_translate("Form_add_data", "EMP_ID"))
        self.label_remark.setText(_translate("Form_add_data", "Remark"))
        self.label_track_in_date.setText(_translate("Form_add_data", "Track_In_Date"))
        self.pushButton_insert.setText(_translate("Form_add_data", "Insert"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form_add_data = QtWidgets.QWidget()
    ui = Ui_Form_add_data()
    ui.setupUi(Form_add_data)
    Form_add_data.show()
    sys.exit(app.exec_())