import random  # 调用random模块

a = random.random()  # 随机从0-1之间抽取一个小数
print(a)

a = random.randint(0, 100)  # 随机从0-100之间抽取一个数字
print(a)

a = random.choice('abcdefg')  # 随机从字符串/列表/字典等对象中抽取一个元素（可能会重复）
print(a)

a = random.sample('abcdefg', 3)  # 随机从字符串/列表/字典等对象中抽取多个不重复的元素
print(a)

items = [1, 2, 3, 4, 5, 6]  # “随机洗牌”，比如打乱列表
random.shuffle(items)
print(items)

print('随机函数random：')
print(dir(random))  # 可以使用dir()函数查看一个模块，看看它里面有什么变量、函数、类、类方法。

# ——————————————————————字符串、列表、字典的模块里面都有什么————————————————————————————
a = ''  # 设置一个字符串
print('字符串：')
print(dir(a))  # 把字符串相关的函数展示出来

a = []  # 设置一个列表
print('列表：')
print(dir(a))  # 把列表相关的函数展示出来

a = {}  # 设置一个字典
print('字典：')
print(dir(a))  # 把字典相关的函数展示出来

# 我们可以搜索到csv模块的官方英文教程：https://docs.python.org/3.6/library/csv.html
# 中文教程：https://yiyibooks.cn/xx/python_352/library/csv.html#module-csv
import csv

print('csv:')
print(dir(csv))
# for i in dir(csv):
#     print(i)
