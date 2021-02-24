a = '我是模块中的变量a'


def hi():
    a = '我是函数里的变量a'
    print('函数“hi”已经运行！')


class Go1:  # 如果没有继承的类，class语句中可以省略括号，但定义函数的def语句括号不能省
    a = '我是类1中的变量a'

    @classmethod
    def do1(cls):
        print('函数“do1”已经运行！')


class Go2:
    a = '我是类2中的变量a'

    def do2(self):
        print('函数“do2”已经运行！')


sentence = '从前有座山，'


def mountain():
    print('山里有座庙，')


class Temple:
    sentence = '庙里有个老和尚，'

    @classmethod
    def reading(cls):
        print('在讲故事，')


class Story:
    sentence = '一个长长的故事。'

    def reading(self):
        print('讲的什么故事呢？')
