import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time


class MyDirEventHandler(FileSystemEventHandler):

    def on_moved(self, event):
        pass

    def on_created(self, event):
        print(event)
        # 获得丢进去的文件的后缀
        a = event.src_path.split(".")
        suffix = a[-1]
        # 获取丢进去的文件丢到的目录
        b = event.src_path.split("/")
        new_file_name = b[-1]
        directory = event.src_path.replace(b[-1] , "")
        print("\n获取目录位置:", directory)
        # 获取丢进去之前的最大id（名字编码，空的话给1）
        # 获取所有文件名称
        files = []
        for root, dirs, files in os.walk(directory):
            pass
        # 先去掉自身（以防自身是数字文件名
        files.remove(new_file_name)
        # 去掉非数字
        files2 = []
        for x in files:
            if str.isdigit(x.split(".")[0]):
                files2.append(int(x.split(".")[0]))
        files2.sort()
        files = files2
        # print(files)
        biggest_num = files[-1]
        # print(files)

        # 获取当前最大数字
        filenum = biggest_num + 1
        print("获得可用数字:", filenum)
        # 制作结果位置+名字字符串
        moved = directory + str(filenum) + "." + suffix
        print("文件将重命名为:", moved)
        # 重命名
        os.replace(event.src_path, moved)
        print("文件重命名完成\n")


    def on_deleted(self, event):
        pass

    def on_modified(self, event):
        pass


if __name__ == '__main__':
    DirToWatch = '/Users/kasusa/Desktop/Pic'
    print(f"""
本程序会检测DirToWatch（{DirToWatch}）文件夹，并且按照序号重命名文件。
""")

    # 创建观察者对象
    observer = Observer()
    # 创建事件处理对象
    fileHandler = MyDirEventHandler()

    # 为观察者设置观察对象与处理事件对象
    observer.schedule(fileHandler, DirToWatch, True)
    observer.start()
    print("----开始监控文件夹----")
    try:
        while True:
            time.sleep(2)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
