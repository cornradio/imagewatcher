import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
from console_color_writer import *


def get_id(directory, new_file_name):
    # 获取丢进去之前的最大id（名字编码，空的话给1）
    files = []
    for root, dirs, files in os.walk(directory):
        pass
    # 去掉刚刚加入的文件名
    files.remove(new_file_name)
    files2 = files.copy()
    print_verbose(files)
    # 跳过非数字的文件名 如 .DSstore
    for x in files2:
        if x.split(".")[0].isdigit():
            pass
        else:
            # print_red("toremove",x)
            files.remove(x)
    # 现在所有文件名应都是数字，这一小段返回最大数字，如果没有文件，返回1
    if len(files) > 0:
        nums = []
        for item in files:
            nums.append(int(item.split(".")[0]))
        nums.sort()
        filenum = nums[-1]
        filenum += 1
    else:
        filenum = 1
    print_verbose(f"获得可用数字:{filenum}", )
    return filenum


class MyDirEventHandler(FileSystemEventHandler):
    def on_moved(self, event):
        pass

    def on_created(self, event):
        print(f'文件创建:{event.src_path}')
        "/Users/kasusa/Desktop/电脑壁纸-重命名/图片4.jpg"
        new_file_name = os.path.split(event.src_path)[1]
        directory = os.path.split(event.src_path)[0]
        suffix = new_file_name.split(".")[-1]  # 获得丢进去的文件的后缀
        print_verbose(f'文件全名:{new_file_name}')
        print_verbose(f'文件目录:{directory}')
        print_verbose(f'文件后缀:{suffix}')

        # 制作结果位置+名字字符串
        moved = directory + "/" + str(get_id(directory, new_file_name)) + "." + suffix
        print("重命名为:", moved)
        # 重命名
        os.replace(event.src_path, moved)

    def on_deleted(self, event):
        pass

    def on_modified(self, event):
        pass


"""
使用watchdog 监控文件的变化
"""

def watch_dir(path):
    observer = Observer()
    fileHandler = MyDirEventHandler()
    x = path
    observer.schedule(fileHandler, x, True)
    observer.start()
    print_green("开始监控", f"{x}")
    try:
        while True:
            time.sleep(2)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


if __name__ == '__main__':
    x = input("输入要监控的文件夹目录:")
    watch_dir(x)