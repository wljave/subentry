import os

# 设置文件夹路径，获取文件夹下的所有文件名
path = '../soup/'
files_list = os.listdir(path)
print(files_list)

# 设置需要查找的关键词
key_word = input("请输入要查找的关键词：")

# 打开结果文件
result_file = open('./result.txt', 'a', encoding='utf-8')

# 循环处理每一个文件
for file_name in files_list:
    # 判断文件类型是否在文件名中
    if '.txt' in file_name:
        # 找到文件时先打印提示
        print("找到了文件：" + file_name)

        # 将文件夹路径和文件名拼接成该文件的相对路径
        target_file = path + file_name

        # 打开文件，读取文件内容，然后关闭文件
        file = open(target_file, 'r', encoding='utf-8')
        content = file.read()
        file.close()

        # 判断关键词是否在文件内容中
        if key_word in content:
            # 匹配到关键词时先打印提示
            print("妙啊，文件【{}】包含了关键词：{}".format(target_file, key_word))

            # 将包含关键词的文档的文件路径，写入结果文件。
            result_file.write(target_file + '\n')

# 关闭结果文件
result_file.close()


# *******方法二*********
# 导入os模块
import os
# 设置文件夹路径为'工作文件夹'，获取文件夹下的所有文件名
file_path = './工作文件夹/'
file_list = os.listdir(file_path)

# 设置需要查找的关键词
key_word = input('请输入您要查找的关键词：')

# 打开结果文件'./result.txt'
with open('./result.txt', 'a', encoding='utf-8')as file1:
    # 循环处理每一个文件
    for file_name in file_list:
        # 判断文件名中是否包含'.txt'
        if '.txt' in file_name:
            # 找到文件时先打印提示
            print("找到了文件：" + file_name)
            # 将文件夹路径和文件名拼接成该文件的相对路径
            target_file = file_path + file_name
            # 打开文件，读取文件内容，然后关闭文件
            with open(target_file, 'r', encoding='utf-8')as file2:
                content = file2.read()
                # 判断关键词是否在文件内容中
                if key_word in content:
                    # 匹配到关键词时先打印提示
                    print("妙啊，文件**{}**包含了关键词：{}".format(target_file, key_word))
                    # 将包含关键词的文档的文件路径，写入结果文件。使用换行符'\n'实现逐行写入的效果。
                    file1.write(target_file + '\n')
