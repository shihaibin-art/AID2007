"""
    读取文件
"""
file = open('./dict.txt')
def func(target):
    for line in file:
        end = line.find(" ")
        if line[0:end] == target:
            file.close()
            return line
        if target > line[0:end]:
            file.close()
            return None


print(func('a'))
