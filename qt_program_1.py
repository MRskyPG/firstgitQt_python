# Form implementation generated from reading ui file 'D:\PycharmProjects\firstgitQt\qt_program_1.ui'
#
# Created by: PyQt6 UI code generator 6.3.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(434, 686)
        MainWindow.setStyleSheet("QWidget {\n"
"  color: white;\n"
"  background-color: #121212;\n"
"  font-family: Rubik;\n"
"  font-size: 16pt;\n"
"  font-weight: 600;\n"
"}\n"
"\n"
"QPushButton {\n"
"background-color: transparent;\n"
"border: none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: #666;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: #888;\n"
"}\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setStyleSheet("color: #888;\n"
"font-size: 16pt;")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.lineEdit.setStyleSheet("font-size: 35pt;\n"
"border: none;")
        self.lineEdit.setMaxLength(10)
        self.lineEdit.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.b7 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.b7.sizePolicy().hasHeightForWidth())
        self.b7.setSizePolicy(sizePolicy)
        self.b7.setObjectName("b7")
        self.gridLayout_3.addWidget(self.b7, 1, 0, 1, 1)
        self.b_clear = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.b_clear.sizePolicy().hasHeightForWidth())
        self.b_clear.setSizePolicy(sizePolicy)
        self.b_clear.setStyleSheet("color: #fc7703;")
        self.b_clear.setObjectName("b_clear")
        self.gridLayout_3.addWidget(self.b_clear, 0, 0, 1, 1)
        self.b4 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.b4.sizePolicy().hasHeightForWidth())
        self.b4.setSizePolicy(sizePolicy)
        self.b4.setObjectName("b4")
        self.gridLayout_3.addWidget(self.b4, 2, 0, 1, 1)
        self.b_percent = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.b_percent.sizePolicy().hasHeightForWidth())
        self.b_percent.setSizePolicy(sizePolicy)
        self.b_percent.setStyleSheet("color: #fc7703;")
        self.b_percent.setObjectName("b_percent")
        self.gridLayout_3.addWidget(self.b_percent, 4, 0, 1, 1)
        self.b2 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.b2.sizePolicy().hasHeightForWidth())
        self.b2.setSizePolicy(sizePolicy)
        self.b2.setObjectName("b2")
        self.gridLayout_3.addWidget(self.b2, 3, 1, 1, 1)
        self.b1 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.b1.sizePolicy().hasHeightForWidth())
        self.b1.setSizePolicy(sizePolicy)
        self.b1.setObjectName("b1")
        self.gridLayout_3.addWidget(self.b1, 3, 0, 1, 1)
        self.b0 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.b0.sizePolicy().hasHeightForWidth())
        self.b0.setSizePolicy(sizePolicy)
        self.b0.setObjectName("b0")
        self.gridLayout_3.addWidget(self.b0, 4, 1, 1, 1)
        self.b5 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.b5.sizePolicy().hasHeightForWidth())
        self.b5.setSizePolicy(sizePolicy)
        self.b5.setObjectName("b5")
        self.gridLayout_3.addWidget(self.b5, 2, 1, 1, 1)
        self.b8 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.b8.sizePolicy().hasHeightForWidth())
        self.b8.setSizePolicy(sizePolicy)
        self.b8.setObjectName("b8")
        self.gridLayout_3.addWidget(self.b8, 1, 1, 1, 1)
        self.b_backspace = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.b_backspace.sizePolicy().hasHeightForWidth())
        self.b_backspace.setSizePolicy(sizePolicy)
        self.b_backspace.setStyleSheet("color: #fc7703;")
        self.b_backspace.setObjectName("b_backspace")
        self.gridLayout_3.addWidget(self.b_backspace, 0, 2, 1, 1)
        self.b_ce = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.b_ce.sizePolicy().hasHeightForWidth())
        self.b_ce.setSizePolicy(sizePolicy)
        self.b_ce.setStyleSheet("color: #fc7703;")
        self.b_ce.setObjectName("b_ce")
        self.gridLayout_3.addWidget(self.b_ce, 0, 1, 1, 1)
        self.b_div = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.b_div.sizePolicy().hasHeightForWidth())
        self.b_div.setSizePolicy(sizePolicy)
        self.b_div.setStyleSheet("color: #fc7703;")
        self.b_div.setObjectName("b_div")
        self.gridLayout_3.addWidget(self.b_div, 0, 3, 1, 1)
        self.b_mul = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.b_mul.sizePolicy().hasHeightForWidth())
        self.b_mul.setSizePolicy(sizePolicy)
        self.b_mul.setStyleSheet("color: #fc7703;")
        self.b_mul.setObjectName("b_mul")
        self.gridLayout_3.addWidget(self.b_mul, 1, 3, 1, 1)
        self.b_minus = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.b_minus.sizePolicy().hasHeightForWidth())
        self.b_minus.setSizePolicy(sizePolicy)
        self.b_minus.setStyleSheet("color: #fc7703;")
        self.b_minus.setObjectName("b_minus")
        self.gridLayout_3.addWidget(self.b_minus, 2, 3, 1, 1)
        self.b_plus = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.b_plus.sizePolicy().hasHeightForWidth())
        self.b_plus.setSizePolicy(sizePolicy)
        self.b_plus.setStyleSheet("color: #fc7703;")
        self.b_plus.setObjectName("b_plus")
        self.gridLayout_3.addWidget(self.b_plus, 3, 3, 1, 1)
        self.b_calc = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.b_calc.sizePolicy().hasHeightForWidth())
        self.b_calc.setSizePolicy(sizePolicy)
        self.b_calc.setStyleSheet("QPushButton{\n"
"background-color: #fc7703;\n"
"border-radius: 25px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #fc9403;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: #fcb23a;\n"
"}")
        self.b_calc.setObjectName("b_calc")
        self.gridLayout_3.addWidget(self.b_calc, 4, 3, 1, 1)
        self.b_point = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.b_point.sizePolicy().hasHeightForWidth())
        self.b_point.setSizePolicy(sizePolicy)
        self.b_point.setObjectName("b_point")
        self.gridLayout_3.addWidget(self.b_point, 4, 2, 1, 1)
        self.b3 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.b3.sizePolicy().hasHeightForWidth())
        self.b3.setSizePolicy(sizePolicy)
        self.b3.setObjectName("b3")
        self.gridLayout_3.addWidget(self.b3, 3, 2, 1, 1)
        self.b6 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.b6.sizePolicy().hasHeightForWidth())
        self.b6.setSizePolicy(sizePolicy)
        self.b6.setObjectName("b6")
        self.gridLayout_3.addWidget(self.b6, 2, 2, 1, 1)
        self.b9 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.b9.sizePolicy().hasHeightForWidth())
        self.b9.setSizePolicy(sizePolicy)
        self.b9.setObjectName("b9")
        self.gridLayout_3.addWidget(self.b9, 1, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator by MR"))
        self.label.setText(_translate("MainWindow", "123"))
        self.lineEdit.setText(_translate("MainWindow", "0"))
        self.b7.setText(_translate("MainWindow", "7"))
        self.b7.setShortcut(_translate("MainWindow", "7"))
        self.b_clear.setText(_translate("MainWindow", "C"))
        self.b4.setText(_translate("MainWindow", "4"))
        self.b4.setShortcut(_translate("MainWindow", "4"))
        self.b_percent.setText(_translate("MainWindow", "%"))
        self.b_percent.setShortcut(_translate("MainWindow", "%"))
        self.b2.setText(_translate("MainWindow", "2"))
        self.b2.setShortcut(_translate("MainWindow", "2"))
        self.b1.setText(_translate("MainWindow", "1"))
        self.b1.setShortcut(_translate("MainWindow", "1"))
        self.b0.setText(_translate("MainWindow", "0"))
        self.b0.setShortcut(_translate("MainWindow", "0"))
        self.b5.setText(_translate("MainWindow", "5"))
        self.b5.setShortcut(_translate("MainWindow", "5"))
        self.b8.setText(_translate("MainWindow", "8"))
        self.b8.setShortcut(_translate("MainWindow", "8"))
        self.b_backspace.setText(_translate("MainWindow", "<-"))
        self.b_backspace.setShortcut(_translate("MainWindow", "Backspace"))
        self.b_ce.setText(_translate("MainWindow", "CE"))
        self.b_ce.setShortcut(_translate("MainWindow", "Del"))
        self.b_div.setText(_translate("MainWindow", "/"))
        self.b_div.setShortcut(_translate("MainWindow", "/"))
        self.b_mul.setText(_translate("MainWindow", "x"))
        self.b_mul.setShortcut(_translate("MainWindow", "*"))
        self.b_minus.setText(_translate("MainWindow", "-"))
        self.b_minus.setShortcut(_translate("MainWindow", "-"))
        self.b_plus.setText(_translate("MainWindow", "+"))
        self.b_plus.setShortcut(_translate("MainWindow", "+"))
        self.b_calc.setText(_translate("MainWindow", "="))
        self.b_calc.setShortcut(_translate("MainWindow", "="))
        self.b_point.setText(_translate("MainWindow", "."))
        self.b_point.setShortcut(_translate("MainWindow", "."))
        self.b3.setText(_translate("MainWindow", "3"))
        self.b3.setShortcut(_translate("MainWindow", "3"))
        self.b6.setText(_translate("MainWindow", "6"))
        self.b6.setShortcut(_translate("MainWindow", "6"))
        self.b9.setText(_translate("MainWindow", "9"))
        self.b9.setShortcut(_translate("MainWindow", "9"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
