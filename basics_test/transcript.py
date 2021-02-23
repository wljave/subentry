print('--------------------------直接使用类--------------------------------')


# 成绩单
class Transcript:
    @classmethod
    # 录入成绩单
    def input_transcript(cls):
        cls.student_name = input('请输入学生姓名：')
        cls.chinese_scores = int(input('请输入语文成绩：'))
        cls.math_scores = int(input('请输入数学成绩：'))

    @classmethod
    # 打印成绩单
    def print_transcript(cls):
        print(cls.student_name + '的成绩单如下：')
        print('语文成绩：' + str(cls.chinese_scores))
        print('数学成绩：' + str(cls.math_scores))


Transcript.input_transcript()
Transcript.print_transcript()

print('---------------------------------类的实例化后---------------------------')


# 成绩单
class Transcript:

    # 录入成绩单
    def input_transcript(self):  # ①不用再写@classmethod
        self.student_name = input('请输入学生姓名：')  # ③cls.变成self.
        self.chinese_scores = int(input('请输入语文成绩：'))
        self.math_scores = int(input('请输入数学成绩：'))

    # 打印成绩单
    def print_transcript(self):
        print(self.student_name + '的成绩单如下：')
        print('语文成绩：' + str(self.chinese_scores))
        print('数学成绩：' + str(self.math_scores))


# 类的实例化
transcript1 = Transcript()  # ④创建实例对象：成绩单1
transcript2 = Transcript()  # 实例化，得到实例对象“成绩单2”
transcript3 = Transcript()  # 实例化，得到实例对象“成绩单3”

# 实例化后调用
print('现在开始录入三份成绩单：')
transcript1.input_transcript()  # ⑤实例化后使用
transcript2.input_transcript()
transcript3.input_transcript()

print('现在开始打印三份成绩单：')
transcript1.print_transcript()
transcript2.print_transcript()
transcript3.print_transcript()

print('-------------------------类实例化后使用初始化函数__init__------------------------')


# 成绩单
class Transcript:
    # 将录入成绩单的部分公共代码放入初始化函数中，方便调用
    def __init__(self):
        self.student_name = input('请输入学生姓名：')
        self.chinese_scores = int(input('请输入语文成绩：'))
        self.math_scores = int(input('请输入数学成绩：'))

    # 打印成绩单
    def print_transcript(self):
        print(self.student_name + '的成绩单如下：')
        print('语文成绩：' + str(self.chinese_scores))
        print('数学成绩：' + str(self.math_scores))


transcript1 = Transcript()  # 实例化，得到实例对象“成绩单1”
transcript2 = Transcript()  # 实例化，得到实例对象“成绩单2”
transcript3 = Transcript()  # 实例化，得到实例对象“成绩单3”

print('现在开始打印三份成绩单：')
transcript1.print_transcript()
transcript2.print_transcript()
transcript3.print_transcript()

print('-------------------------类实例化后，使用初始化函数__init__，传递参数------------------------')


