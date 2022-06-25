import ctypes
import sys
from files.symmetry_decomposition import decompose
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow



class mainGUI(QMainWindow):
    
    def __init__(self):
        super().__init__()
        uic.loadUi("files/gui.ui", self)
        self.ok.clicked.connect(self.run)
    
    def run(self):
        input_rep = self.input.text()
        input_group = self.group.currentText()
        try:
            decomposition = decompose(input_rep, input_group)
            self.result.setText(decomposition)
        except ValueError as err_msg:
            self.result.setText(self.red_text(err_msg))
            
    def red_text(self, text):
        return "<span style=\"font-size:10pt; color:#ff0000;\" >{}</span>".format(text)


if sys.platform.startswith("win") or sys.platform.startswith("cygwin"):
    app_id = u"symmetry.decomposer"
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(app_id)


app = QApplication([])
GUI = mainGUI()
GUI.show()
app.exec_()
