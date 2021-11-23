import random
import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor
import UI


class Application(QWidget):
    def __init__(self):
        super().__init__()
        UI.Ui.init_ui(self)
        self.start = False
        self.pushButton.clicked.connect(self.generate)

    def generate(self):
        self.start = True
        self.update()

    def paintEvent(self, event):
        if self.start:
            self.qp = QPainter()
            self.qp.begin(self)
            self.qp.setBrush(QColor(255, 255, 0))
            for i in range(5):
                d = random.randrange(100)
                self.qp.drawEllipse(random.randrange(100, 598), random.randrange(100, 400), d, d)
            self.qp.end()
            self.start = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    appExample = Application()
    appExample.show()
    sys.exit(app.exec())