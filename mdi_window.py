import sys
from PyQt5 import QtWidgets, uic

class MDIWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MDIWindow, self).__init__()
        uic.loadUi('mdi_window.ui', self)

        # Find the "New Window" action by its object name
        self.actionNew_Window = self.findChild(QtWidgets.QAction, 'actionNew_Window')

        # Connect the "New Window" action to the create_new_window slot
        self.actionNew_Window.triggered.connect(self.create_new_window)

    def create_new_window(self):
        sub_window = QtWidgets.QMdiSubWindow()
        self.mdiArea.addSubWindow(sub_window)
        sub_window.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MDIWindow()
    window.show()
    sys.exit(app.exec_())
