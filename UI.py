from PyQt5.QtWidgets import QPushButton, QMenuBar, QWidget
from PyQt5.QtCore import QRect
from PyQt5.QtGui import QFont


class UIClass:
    @staticmethod
    def init_ui(app):
        app.resize(698, 500)
        app.setWindowTitle('yellow')
        app.centralwidget = QWidget(app)
        app.pushButton = QPushButton(app.centralwidget)
        app.pushButton.setGeometry(QRect(270, 400, 131, 40))
        font = QFont()
        font.setPointSize(12)
        app.pushButton.setFont(font)
        app.menubar = QMenuBar(app)
        app.menubar.setGeometry(QRect(0, 0, 698, 21))
        app.pushButton.setText("Яндекс Шарики")