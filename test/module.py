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


print(a)  # 打印变量“a”

hi()  # 调用函数“hi”

print(Go1.a)  # 打印类属性“a”
Go1.do1()  # 调用类方法“Go1”

A = Go2()  # 实例化“Go2”类
print(A.a)  # 打印实例属性“a”
A.do2()  # 调用实例方法“do2”
