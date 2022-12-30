# 不要使用，这是未完成的代码。
import sys
# 这里import 你需要用的qt模块
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout, QTextEdit, QLabel
from PyQt6.QtGui import QIcon
import watch_nput


# 这里是你的主窗口类
class myapp(QWidget):
    def __init__(self):
        super().__init__()
        # 设置窗口标题、大小、图标
        self.setWindowTitle("P-watch(or dir watch?)")
        self.setWindowIcon(QIcon("pythonlogo.png"))
        self.resize(500, 400)
        # 设置窗口布局
        layout = QVBoxLayout()
        self.setLayout(layout)
        # 设置输入框、按钮、输出框
        self.lable = QLabel("输入文件夹路径:")
        self.inputField = QLineEdit()

        self.button = QPushButton("开始监听", clicked=self.button_click)  # 这里是按钮名称、点击事件
        self.output = QTextEdit()
        # 将组件添加到布局
        layout.addWidget(self.lable)
        layout.addWidget(self.inputField)
        layout.addWidget(self.button)
        layout.addWidget(self.output)

    # 这里是按钮点击事件 连接到上面的button
    def button_click(self):
        watch_nput.watch_dir(self.inputField.text())


# 这里是主函数
if __name__ == "__main__":
    # 创建一个应用程序对象，允许接受命令行参数
    app = QApplication(sys.argv)
    # 这里设置一下样式，类似css
    app.setStyleSheet('''
    ''')
    window = myapp()  # 创建一个窗口对象
    window.show()  # 显示窗口
    app.exec()  # 这里是进入程序的主循环，并通过exit函数确保主循环安全结束
