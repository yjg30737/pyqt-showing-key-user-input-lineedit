# pyqt-showing-key-user-input-lineedit
Detect the key which user input and show it on the lineedit.

## Requirements
PyQt5 >= 5.8

## Setup
```pip3 install git+https://github.com/yjg30737/pyqt-showing-key-user-input-lineedit.git --upgrade```

## Example
Code Sample
```python
from PyQt5.QtWidgets import QWidget, QGridLayout, QApplication
from pyqt_showing_key_user_input_lineedit import ShowingKeyUserInputLineEdit


class LineEditExample(QWidget):
    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        lineedit = ShowingKeyUserInputLineEdit()
        lay = QGridLayout()
        lay.addWidget(lineedit)
        self.setLayout(lay)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    example = LineEditExample()
    example.show()
    app.exec_()
```

Result

https://user-images.githubusercontent.com/55078043/148883096-bc043792-2bcc-4ec3-ad62-350922d5e473.mp4

