import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QProgressBar, QVBoxLayout
from PySide6.QtCore import QBasicTimer


class MyClass(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(300, 200)
        # 载入进度条控件
        self.verticalLayout = QVBoxLayout()
        self.pgb = QProgressBar(self)
        self.verticalLayout.addWidget(self.pgb, 0, 0, 1, 1)
        #self.pgb.move(50, 50)
        #self.pgb.resize(250, 20)

        # 配置一个值表示进度条的当前进度
        self.pv = 0

        # 申明一个时钟控件
        self.timer1 = QBasicTimer()

        # 设置进度条的范围
        self.pgb.setMinimum(0)
        self.pgb.setMaximum(100)
        self.pgb.setValue(self.pv)
        # 载入按钮
        self.btn = QPushButton("开始", self)
        self.btn.move(50, 100)
        self.btn.clicked.connect(self.myTimerState)
        self.show()

    def myTimerState(self):
        if self.pv == 100:
            self.close()
        if self.timer1.isActive():
            self.timer1.stop()
            self.btn.setText("开始")
        else:
            self.timer1.start(100, self)
            self.btn.setText("停止")

    def timerEvent(self, e):
        if self.pv == 100:
            self.timer1.stop()
            self.btn.setText("完成")
        else:
            self.pv += 1
            self.pgb.setValue(self.pv)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mc = MyClass()
    app.exec_()


