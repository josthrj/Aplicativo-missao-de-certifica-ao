import sys
from pyside6.qtwidgets import(QApplication, QMainWindow, QWidget)
from Ui_tela_login import Ui_tela_login



class tela_login(QWidget, Ui_tela_login):
    def __init__(self) -> None:
        super(Ui_tela_login).__init__()
        self.setupUi(self)
        self.setWindowTitle("Login Do Sistema")





if __name__ == "_main_":
    app = QApplication(sys.argv)
    window = tela_login()
    window.show()
    app.exec_()







