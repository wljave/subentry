# # 以读的方式打开文件“abc.txt”
# file1 = open('abc.txt', 'r', encoding='utf-8')
# # 读取“abc.txt”文件的内容，然后保存在变量filecontent里
# filecontent1 = file1.read()
# # 打印变量filecontent里的数据
# print(filecontent1)
# # 关闭file1文件
# file1.close()
#
# # 以追加的方式打开文件“abc.txt”
# file2 = open('abc.txt', 'a', encoding='utf-8')
# # 把字符串写入文件file2中
# file2.write('张无忌\n')
# file2.write('宋青书\n')
# # 关闭file1文件
# file2.close()
#
##########################################################################################################
#Python基础语法-第15关  L15.4读取各科成绩计算总成绩，【L15.5直接读取成绩然后计算总成绩并排序】，L15.6根据总成绩进行排序##
#########################################################################################################
# 以读的方式打开文件“abc.txt”
file3 = open('abc.txt', 'r', encoding='utf-8')
# 读取“abc.txt”文件的内容，然后保存在变量filecontent里
filecontent3 = file3.readlines()
# 打印变量filecontent里的数据
# print(filecontent3)
# 关闭file1文件
file3.close()

dict_scores = {}
list_scores = []
final_scores = []
for i in filecontent3:  # 用for...in...把每一行的数据遍历
    data = i.split()  # 把字符串切分成更细的一个个的字符串
    sum = 0  # 先把总成绩设为0
    for score in data[1:]:  # 遍历列表中第1个数据和之后的数据
        sum = sum + int(score)  # 然后依次加起来，但分数是字符串，所以要转换
    #result = data[0] + str(sum) + '\n'  # 结果就是学生姓名和总分
    #print(data[0])
    #print(sum)
    dict_scores[sum] = data[0]
    list_scores.append(sum)
    #final_scores.append(result)  # 每统计一个学生的总分，就把姓名和总分写入空列表
#print(final_scores)
#print(dict_scores)
#print(list_scores)
list_scores.sort(reverse=True)
#print(list_scores)
for i in list_scores:
    result = dict_scores[i] + str(i) + '\n'
    final_scores.append(result)
print(final_scores)

winner = open('winner_new.txt', 'w', encoding='utf-8')
winner.writelines(final_scores)
winner.close()

# file = open('abc.txt', 'r', encoding='utf-8')
# filecontent = file.readlines()
# i = 1
# for temp in filecontent:
#     # 是把字符串分割的
#     print('{}: {}'.format(i, temp.split()))
#     i += 1
# file.close()
#
# # join()函数，是把字符串合并的
# a = ['c', 'a', 't']
# b = ''
# print(b.join(a))
# c = '-'
# print(c.join(a))
# d = b.join(a)
# print(d.split())

with open('photo1.png', 'rb') as po1:
    r = po1.read()
    with open('photo2.png', 'wb') as po2:
        po2.write(r)
