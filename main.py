import random
import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor
from UI import UIClass


class Application(QWidget):
    def __init__(self):
        super().__init__()
        UIClass.init_ui(self)
        self.start = False
        self.qp = QPainter()
        self.pushButton.clicked.connect(self.generate)

    def generate(self):
        self.start = True
        self.update()

    def paintEvent(self, event):
        if self.start:
            self.qp.begin(self)
            for i in range(5):
                self.qp.setBrush(QColor(*[random.randrange(255) for _ in range(3)]))
                d = random.randrange(100)
                self.qp.drawEllipse(random.randrange(100, 598), random.randrange(100, 400), d, d)
            self.qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    appExample = Application()
    appExample.show()
    sys.exit(app.exec())