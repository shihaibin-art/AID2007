import time


def copy(file_path: str):
    file01 = open(file_path, 'rb')  # 打开源文件
    file_name = time.strftime("%Y_%m_%d", time.localtime())+'.jpg'
    file02 = open(file_name, 'wb')  # 创建新文件
    for line in file01:
        file02.write(line)  # 写入新文件
    file01.close()
    file02.close()


copy('/home/tarena/图片/1.jpg')

