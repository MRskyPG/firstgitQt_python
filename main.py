# pip install requirements.txt
import qt_program_1 as qt1
import sys


app = qt1.QtWidgets.QApplication(sys.argv)
MainWindow = qt1.QtWidgets.QMainWindow()
ui = qt1.Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()


# def on_click():
#     print("click!")

# ui.name_of_Button.clicked.connect(name_of_function)


sys.exit(app.exec())
