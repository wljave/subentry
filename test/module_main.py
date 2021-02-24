# ###############导入模块并起别名#################
import module_test as test

print(test.a)  # 使用“模块.变量”调用模块中的变量

test.hi()  # 使用“模块.函数()”调用模块中的函数

print(test.Go1.a)  # 使用“模块.类.变量”调用模块中的类属性
test.Go1.do1()  # 使用“模块.类.函数()”调用模块中的类方法

A = test.Go2()  # 使用“变量 = 模块.类()”实例化模块中的类
print(A.a)  # 实例化后，不再需要“模块.”
A.do2()  # 实例化后，不再需要“模块.”

# ###############导入指定模块的所有方法，好处是不用加上”模块.“#################
from module_test import *

for i in range(10):
    print(sentence)
    mountain()
    print(Temple.sentence)
    Temple.reading()
    A = Story()
    print(A.sentence)
    A.reading()
    print()
