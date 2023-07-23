from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QTextCursor
from form import Ui_Form
import sys

class MainWindow(QMainWindow, Ui_Form):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        # the document can be treated as one long string.
        self.description_cursor = QTextCursor(self.textbrowser_description.document()) 

        self.setup_events()

    def setup_events(self):
        # press the button or hit ENTER to submit name
        self.button_name.clicked.connect(self.submit_name)
        self.lineedit_name.editingFinished.connect(self.submit_name)

        # press the button to add the selection and question (if there is one)
        self.button_question.clicked.connect(self.submit_question)

    def submit_name(self):
        # get the name
        name = self.lineedit_name.text()

        # show the name in the textBrowser
        self.textbrowser_description.setText(name + '\n')

    def submit_question(self):
        # get the selection and question (if there is one)
        selection = self.selections.currentText()
        question = self.plaintextedit_question.toPlainText()

        # set the cursor to the start point
        self.description_cursor.setPosition(0)
        self.textbrowser_description.setTextCursor(self.description_cursor)

        # insert the selection and question (if there is one)
        self.textbrowser_description.insertPlainText(selection + '\n' + question + '\n')

        # clear the plainTextEdit
        self.plaintextedit_question.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())