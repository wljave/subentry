import os

list_text = '望帝春心托杜鹃'
with open('poem1.txt', 'r', encoding='utf-8') as f:
    lines = f.read()
# print(lines)
with open('poem_new.txt', 'w', encoding='utf-8') as new:
    for line in lines:
        if line in list_text:
            new.write('__')
        else:
            new.write(line)
os.replace('poem_new.txt', 'poem1.txt')
print('改写完毕！')
path = r'poem1.txt'
file = ''
getcwd = os.getcwd()  # 返回当前工作目录
listdir = os.listdir()  # 返回path指定的文件夹包含的文件或文件夹的名字的列表
# os.mkdir(path)  # 创建文件夹
abspath = os.path.abspath(path)  # 返回绝对路径
basename = os.path.basename(path)  # 返回文件名
isfile = os.path.isfile(path)  # 判断路径是否为文件
isdir = os.path.isdir(path)  # 判断路径是否为目录
print('当前工作目录:' + getcwd)
print('当前工作目录下包含的文件或文件夹的名字的列表：\n'+str(listdir))
print('绝对路径:' + abspath)
print('文件名:' + basename)
print('判断路径是否为文件:' + str(isfile))
print('判断路径是否为目录:' + str(isdir))
