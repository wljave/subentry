# 创建一个问卷调查类
class Survey:
    # 收集调查问卷的答案
    def __init__(self, question):
        self.question = question
        # 定义收集问卷问题答案的列表
        self.response = []

    # 显示调查问卷的题目
    def show_question(self):
        print(self.question)

    # 存储问卷搜集的答案
    def store_response(self, new_response):
        # self.response[self.question] = new_response
        self.response.append(new_response)


# 请实例化 Survey() 类，并且显示出这次的调查问卷问题约 2 行代码
food_survey = Survey('你最喜欢的美食是什么？')  # 类的实例化，同时为参数question赋值。
food_survey.show_question()  # 调用类方法打印问题

# 存储问卷调查的答案
while True:
    response = input('请回答问卷问题(什么也不填按回车键退出)：')
    if response == '':
        break
    # 请将答案用问卷系统存储起来,约 1 行代码，变量名见下方。
    food_survey.store_response(response)

# 输出测试
for food in food_survey.response:
    print('美食：' + food)

print('-------------------------------------------收集名字和籍贯地----------------------------------------')


# 创建一个问卷调查类
class Survey:
    # 收集调查问卷的答案
    def __init__(self, question):
        self.question = question
        # 定义收集问卷问题答案的列表
        self.response = []

    # 显示调查问卷的题目
    def show_question(self):
        print(self.question)

    # 存储问卷搜集的答案
    def store_response(self, new_response):
        # self.response[self.question] = new_response
        self.response.append(new_response)


class Inquiry(Survey):
    # 收集调查问卷的答案
    def __init__(self, question):
        # super().__init__(question)
        Survey.__init__(self, question)
        # 定义收集问卷答案的变量，代码量1行
        self.response = {}

    # 存储问卷搜集的答案（覆盖父类的类方法）
    def store_response(self, name, new_response):  # 除了 self，还需要两个参数。
        self.response[name] = new_response  # 键值对的新增


survey = Inquiry('你的籍贯地是哪？')
survey.show_question()
while True:
    response = input('请回答问卷问题，按 q 键退出：')
    if response == 'q':
        break
    name = input('请输入回答者姓名：')
    survey.store_response(name, response)  # 调用类方法，将两次通过 input 的字符串存入字典。

# 输出测试
for name, value in survey.response.items():
    print(name + '：' + value)

print("----------------------------------------------那个男人来了------------------------------------------")


class Person:
    def __init__(self):
        self.name = input('请输入您的姓名：')
        print('大家注意了！')

    def show(self):
        print('一个叫“%s”的人来了。' % self.name)


class Man(Person):
    def __init__(self):
        Person.__init__(self)   # 完全继承父类的方法

    def show(self):
        Person.show(self)   # 完全继承父类的方法

    def leave(self):     # 子类定制新方法
        print('那个叫“%s”的男人留下了他的背影。' % self.name)


author1 = Person()
author1.show()
author2 = Man()
author2.show()
author3 = Man()
author3.leave()
