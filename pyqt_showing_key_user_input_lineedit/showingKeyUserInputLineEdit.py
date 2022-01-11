from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QLineEdit


class ShowingKeyUserInputLineEdit(QLineEdit):
    keyPressed = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        self.__modifiers_list = (Qt.CTRL | Qt.ALT | Qt.SHIFT | Qt.META)

    def keyPressEvent(self, event):
        keyname = ''
        key = event.key()
        modifiers = int(event.modifiers())
        if modifiers:
            if (modifiers & self.__modifiers_list == modifiers and
                key > 0 and key != Qt.Key_Shift and key != Qt.Key_Alt and
                key != Qt.Key_Control and key != Qt.Key_Meta):
                    keyname = QKeySequence(modifiers + key).toString()
            else:
                keyname = QKeySequence(modifiers).toString()[:-1]
        else:
            keyname = QKeySequence(key).toString()
        self.setText(keyname)
