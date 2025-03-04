# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Page2.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import os
import pandas as pd

from Page3 import Ui_Form1

# Ui file
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(994, 663)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1056, 731))
        self.widget.setAutoFillBackground(False)
        self.widget.setStyleSheet("background-color:rgb(220, 220, 220)\n"
"")
        self.widget.setObjectName("widget")
        self.listWidget1 = QtWidgets.QListWidget(self.widget)
        self.listWidget1.setGeometry(QtCore.QRect(20, 30, 251, 581))
        self.listWidget1.setObjectName("listWidget1")
        self.InboxButton = QtWidgets.QPushButton(self.widget)
        self.InboxButton.setGeometry(QtCore.QRect(70, 60, 161, 71))
        self.InboxButton.setObjectName("InboxButton")
        self.SpamButton = QtWidgets.QPushButton(self.widget)
        self.SpamButton.setGeometry(QtCore.QRect(70, 330, 161, 71))
        self.SpamButton.setObjectName("SpamButton")
        self.PriorityButton = QtWidgets.QPushButton(self.widget)
        self.PriorityButton.setGeometry(QtCore.QRect(70, 200, 161, 71))
        self.PriorityButton.setObjectName("PriorityButton")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.widget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(280, 30, 701, 581))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.NextPageButton = QtWidgets.QPushButton(self.widget)
        self.NextPageButton.setGeometry(QtCore.QRect(70, 470, 161, 71))
        self.NextPageButton.setObjectName("NextPage")

        # Add QTextEdit to the vertical layout
        self.textEdit = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.verticalLayout.addWidget(self.textEdit)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        # Connect buttons to their respective functions
        self.InboxButton.clicked.connect(self.printInboxText)
        self.SpamButton.clicked.connect(self.printSpamText)
        self.PriorityButton.clicked.connect(self.printPriorityText)
        self.NextPageButton.clicked.connect(self.Page3)

    # Function for the program to connect to Page3
    def Page3(self):
        self.Form = QtWidgets.QWidget()
        self.ui = Ui_Form1()
        self.ui.setupUi(self.Form)
        self.Form.show()

    # Ui function
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.InboxButton.setText(_translate("Form", "Inbox"))
        self.SpamButton.setText(_translate("Form", "Spam"))
        self.PriorityButton.setText(_translate("Form", "Priority"))
        self.NextPageButton.setText(_translate("Form", "Next Page"))

    # Function to read files from folder
    def readFilesFromFolder(self, folder_location, limit=500):
        try:
            # List all .txt files in the folder
            files = [f for f in os.listdir(folder_location) if f.endswith('.txt')]
            content = ""
            for i, file_name in enumerate(files):
                if i >= limit:
                    break
                file_path = os.path.join(folder_location, file_name)
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
                    content += f"----------------------------------------------------------------------------------------------------------------------\n{file.read()}\n\n"
            return content
        except FileNotFoundError:
            return f"The folder '{folder_location}' was not found."
        except Exception as e:
            return f"An error occurred: {e}"
    
    # Function to read csv files 
    def readSingleCSVFile(self, file_location):
        try:
            df = pd.read_csv(file_location)
            top_100 = df.head(100)
            content = ""
            for _, row in top_100.iterrows():
                row_content = "\n".join([f"{col}: {row[col]}" for col in df.columns])
                content += "----------------------------------------------------------------------------------------------------------------------\n" + row_content + "\n\n"
            return content
        except FileNotFoundError:
            return f"The file '{file_location}' was not found."
        except Exception as e:
            return f"An error occurred while reading the file: {e}"
        
    # Methods to print specific text in the QTextEdit
    # Print all emails
    def printInboxText(self):
        folder_location = "ham"  
        content = self.readFilesFromFolder(folder_location)
        self.textEdit.setPlainText(content)

    # Print spam emails
    def printSpamText(self):
        folder_location = "spam"  
        content = self.readFilesFromFolder(folder_location)
        self.textEdit.setPlainText(content)

    # Print priority emails
    def printPriorityText(self):
        file_location = "filtered_df.csv"  
        content = self.readSingleCSVFile(file_location)
        self.textEdit.setPlainText(content)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
