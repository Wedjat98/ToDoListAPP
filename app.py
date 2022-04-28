from PySide2.QtWidgets import QApplication, QMainWindow
from ui_main import Ui_MainWindow


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.resize(360, 600)
        self.ui.webview.load('http://127.0.0.1:5000')


app = QApplication([])
mainWindow = MainWindow()
mainWindow.show()
app.exec_()
