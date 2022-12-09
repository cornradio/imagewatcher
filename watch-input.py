import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time


class MyDirEventHandler(FileSystemEventHandler):

    def on_moved(self, event):
        pass

    def on_created(self, event):
        print(event)
        # try:
        #         except :
        # print('some thing is wrong!!! try again or restart this Script.')
        # pass
        # 获得丢进去的文件的后缀
        a = event.src_path.split(".")
        suffix = a[-1]
        # 获取丢进去的文件丢到的目录
        b = event.src_path.split("\\")
        new_file_name = b[-1]
        directory = event.src_path.replace(b[-1], "")
        print("\n获取目录位置:", directory)
        # 获取丢进去之前的最大id（名字编码，空的话给1）
        # 获取所有文件名称
        files = []
        for root, dirs, files in os.walk(directory):
            pass
        # print(files)
        # 先去掉自身（以防自身是数字文件名
        files.remove(new_file_name)
        # 去掉非数字
        files2 = files.copy()
        for x in files:
            if str.isdigit(x.split(".")[0]):
                pass
            else:
                files2.remove(x)
        files = files2

        # files.remove(b[1])
        if len(files) > 0:
            nums = []
            for item in files:
                nums.append(int(item.split(".")[0]))
            nums.sort()
            filenum = nums[-1]
            print("获得最大目前数字:", filenum)
            filenum += 1
        else:
            filenum = 1
        print("获得可用数字:", filenum)
        # 制作结果位置+名字字符串
        moved = directory + "\\" + str(filenum) + "." + suffix
        print("文件将重命名为:", moved)
        # 重命名
        os.replace(event.src_path, moved)
        print("文件重命名完成,请手动刷新资源管理器 \n")


    def on_deleted(self, event):
        pass

    def on_modified(self, event):
        pass


"""
使用watchdog 监控文件的变化
"""
if __name__ == '__main__':
    os.system("mode con cols=50 lines=30")
    print(f"""
程序作者 : kasusaland@gmail.com 
时间: 2020-4-28

向c:/test 中丢小马图片吧!
程序会自动根据丢进顺序进行命名排序.
就不用理会windows的 [重名文件] 弹窗了

!!! 注意:
在使用本程序之前赢要确保 [test] 
文件夹中的文件名都是 [数字.xxx]
或者您可以每次使用之前把test中的文件清空,
清空之后会从 [1.xxx] 开始排
2022-5-19 15:16:57
请使用Chrome浏览器，Edge浏览器会导致无法对图片重命名。
""")

    # 创建观察者对象
    observer = Observer()
    # 创建事件处理对象
    fileHandler = MyDirEventHandler()

    # 为观察者设置观察对象与处理事件对象
    x = input("输入要监控的文件夹目录:")
    observer.schedule(fileHandler, x, True)
    observer.start()
    print("----开始监控文件夹----")
    try:
        while True:
            time.sleep(2)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
