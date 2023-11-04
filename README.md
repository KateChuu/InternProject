# InternProject
This repo includes two pyqt practices and one ATE (automatic test equipment) system project I made during the internship in Merry.

## PyQt practices
#### simple_form
This practice allows users to type something, choose some options and submit, then the results will be displayed in the area in the down left corner. LineEdit, button, textBrowser, labels and so on are used here.

#### display_table
This program connects to the database of a material warehouse of the company, printing the stocks and properties in the form of a table. Only the authorised user is allowed to connect to the database. The user can add or delete rows in the table by clicking buttons and entering data in the windows.

## ATE system
An Automatic Test Equipment in Python using the DLL provided by the out-sourced company. The ATE system will be deployed in the oversea factory for checking employee numder, product serial number and which test station the product is at.
The ATE system obtains input from the user interface, passing data to to the Manufacturing execution system (MES), which checks the validity of data and returns the results. Finally, the ATE system displays the results on the windows written by PyQt.
