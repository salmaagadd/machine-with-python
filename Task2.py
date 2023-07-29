from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from PyQt5 import QtCore, QtGui, QtWidgets
from sklearn.metrics import mean_squared_error
import math
from sklearn.metrics import mean_absolute_error


class Ui_MainWindow2(object):
    X_train = [0]
    X_test = [0]
    y_train = [0]
    y_test = [0]
    y_pred_test = [0]
    y_pred_train = [0]

    def Read_Dataset(self):
        try:
            global X_train, X_test, y_train, y_test
            file_path, _ = QFileDialog.getOpenFileName(None, "Select File", "", "All Files (*)")
            data = pd.read_csv(file_path)

            self.textBrowser_Dataset.setText(data.to_string())
            self.textBrowser_dataDescribe.setText(data.describe().to_string())
            X = data.iloc[:, :-1].values
            y = data.iloc[:, -1].values

            test_size = 30;
            test_size = int(self.Test_SizeScrollBar.value())

            print(test_size)

            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=(test_size / 100), random_state=10)
            regressor = LinearRegression()
            regressor.fit(X_train, y_train)
            print("Regression Done")

        except:
            print("Error In Read DataSet Function")

    def Regularization(self):
        global y_pred_test, y_pred_train
        alpha = float(self.textEdit.toPlainText())
        print("Alpha", alpha)
        ridge = Ridge(alpha=alpha)
        ridge.fit(X_train, y_train)
        y_pred_test = ridge.predict(X_test)
        y_pred_train = ridge.predict(X_train)
        print("Regularization Done")

    def Calculate_MSE(self):

        MSE_train = mean_squared_error(y_train, y_pred_train)
        MSE_test = mean_squared_error(y_test, y_pred_test)
        self.Train_Error_Value.setText(str(round(MSE_train, 5)))
        self.Test_Error_Value.setText(str(round(MSE_test, 5)))

    def Calculate_RMSE(self):
        MSE_train = mean_squared_error(y_train, y_pred_train)
        MSE_test = mean_squared_error(y_test, y_pred_test)

        RMSE_train = math.sqrt(MSE_train)
        RMSE_test = math.sqrt(MSE_test)

        self.Train_Error_Value.setText(str(round(RMSE_train, 5)))
        self.Test_Error_Value.setText(str(round(RMSE_test, 5)))

    def Calculate_MAE(self):
        MAE_train = mean_absolute_error(y_train, y_pred_train)
        MAE_test = mean_absolute_error(y_test, y_pred_test)
        self.Train_Error_Value.setText(str(round(MAE_train, 5)))
        self.Test_Error_Value.setText(str(round(MAE_test, 5)))

    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.MSE_btn = QtWidgets.QPushButton(self.centralwidget)
        self.MSE_btn.setGeometry(QtCore.QRect(680, 450, 151, 61))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.MSE_btn.setFont(font)
        self.MSE_btn.setObjectName("MSE_btn")
        self.RMSE_btn = QtWidgets.QPushButton(self.centralwidget)
        self.RMSE_btn.clicked.connect(self.Calculate_RMSE)
        self.RMSE_btn.setGeometry(QtCore.QRect(370, 450, 141, 61))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.RMSE_btn.setFont(font)
        self.RMSE_btn.setObjectName("RMSE_btn")
        self.MAE_btn = QtWidgets.QPushButton(self.centralwidget)
        self.MAE_btn.setGeometry(QtCore.QRect(40, 450, 151, 61))
        self.MAE_btn.clicked.connect(self.Calculate_MAE)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.MAE_btn.setFont(font)
        self.MAE_btn.setObjectName("MAE_btn")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(150, 540, 220, 31))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(16)
        self.label_7.setFont(font)
        self.label_7.setIndent(5)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(150, 600, 220, 31))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(16)
        self.label_8.setFont(font)
        self.label_8.setIndent(5)
        self.label_8.setObjectName("label_8")
        self.Train_Error_Value = QtWidgets.QLabel(self.centralwidget)
        self.Train_Error_Value.setGeometry(QtCore.QRect(420, 540, 171, 31))
        self.Train_Error_Value.setStyleSheet("border : 3px solid gray")
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(16)
        self.Train_Error_Value.setFont(font)
        self.Train_Error_Value.setIndent(5)
        self.Train_Error_Value.setObjectName("Train_Error_Value")
        self.Test_Error_Value = QtWidgets.QLabel(self.centralwidget)
        self.Test_Error_Value.setGeometry(QtCore.QRect(420, 600, 171, 31))
        self.Test_Error_Value.setStyleSheet("border : 3px solid gray")
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(16)
        self.Test_Error_Value.setFont(font)
        self.Test_Error_Value.setIndent(5)
        self.Test_Error_Value.setObjectName("Test_Error_Value")
        self.textBrowser_Dataset = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_Dataset.setGeometry(QtCore.QRect(10, 70, 560, 310))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(12)
        self.textBrowser_Dataset.setFont(font)
        self.textBrowser_Dataset.setObjectName("textBrowser_Dataset")
        self.textBrowser_dataDescribe = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_dataDescribe.setGeometry(QtCore.QRect(600, 70, 560, 310))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        self.textBrowser_dataDescribe.setFont(font)
        self.textBrowser_dataDescribe.setObjectName("textBrowser_dataDescribe")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(370, 400, 40, 21))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setIndent(5)
        self.label_4.setObjectName("label_4")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(330, 400, 41, 21))
        self.lcdNumber.setObjectName("lcdNumber")
        self.Test_SizeScrollBar = QtWidgets.QScrollBar(self.centralwidget)
        self.Test_SizeScrollBar.setGeometry(QtCore.QRect(130, 400, 191, 21))
        self.Test_SizeScrollBar.setOrientation(QtCore.Qt.Horizontal)
        self.Test_SizeScrollBar.setObjectName("Test_SizeScrollBar")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(600, 395, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(11)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.Regularization_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Regularization_btn.setGeometry(QtCore.QRect(800, 390, 250, 40))
        self.Regularization_btn.clicked.connect(self.Regularization)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Regularization_btn.setFont(font)
        self.Regularization_btn.setObjectName("Regularization_btn")
        self.Browse_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Browse_btn.setGeometry(QtCore.QRect(15, 15, 190, 43))

        self.Browse_btn.clicked.connect(self.Read_Dataset)

        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(16)
        self.Browse_btn.setFont(font)
        self.Browse_btn.setObjectName("Browse_btn")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 400, 120, 21))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setIndent(5)
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(600, 18, 190, 31))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setIndent(10)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.Test_SizeScrollBar.valueChanged['int'].connect(self.lcdNumber.display)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.MSE_btn.setText(_translate("MainWindow", "MSE"))
        self.MSE_btn.clicked.connect(self.Calculate_MSE)
        self.RMSE_btn.setText(_translate("MainWindow", "RMSE"))
        self.MAE_btn.setText(_translate("MainWindow", "MAE"))
        self.label_7.setText(_translate("MainWindow", "Train Error Value : "))
        self.label_8.setText(_translate("MainWindow", "Test Error Value   : "))
        self.Train_Error_Value.setText(_translate("MainWindow", ""))
        self.Test_Error_Value.setText(_translate("MainWindow", ""))
        self.textBrowser_Dataset.setHtml(_translate("MainWindow",
                                                    "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                    "p, li { white-space: pre-wrap; }\n"
                                                    "</style></head><body style=\" font-family:\'Rockwell\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
                                                    "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textBrowser_dataDescribe.setHtml(_translate("MainWindow",
                                                         "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                         "p, li { white-space: pre-wrap; }\n"
                                                         "</style></head><body style=\" font-family:\'Rockwell\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                                         "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "%"))
        self.textEdit.setPlaceholderText(_translate("MainWindow", "Enter Lambda"))
        self.Regularization_btn.setText(_translate("MainWindow", "Perform Regularization"))
        self.Browse_btn.setText(_translate("MainWindow", "Select Dataset"))
        self.label_3.setText(_translate("MainWindow", "Test Size : "))
        self.label_2.setText(_translate("MainWindow", "Data Describe :"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet("""
                      
     QWidget{
      background-color : #323232;
      color : #D1DBCB
                          
     }
     
     QPushButton:hover{
         background-color : #D1DBCB;
         
         }
     QPushButton:checked{
         background-color: #76797C;
         border-color: #6A6969;
         }
     QPushButton:pressed{
          color: black;
          background-color: #D1DBCB;
          padding-top: -15px;
          padding-bottom: -17px;
     }
     
     QPushButton:focus{
          background-color: #D1DBCB;
          color: black;
     }
     QLabel{
        border: 0px solid black;
        margin-left: 2px;
        margin-right: 2px;
       color: #D1DBCB;
     }
     QTextEdit{
      border: 3px solid gray;
       } 
     
     """ )
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow2()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
