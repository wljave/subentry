# 查看代码和注释，并运行

# 创建一个人事系统类
class HrSystem:
    # 创建存储员工名字的变量 name
    name = ''
    # 创建存储员工工资的变量 salary
    salary = 0
    # 创建存储员工绩效的变量 kpi
    kpi = 0

    # 定义录入员工信息的类方法
    @classmethod
    def record(cls, name, salary, kpi):
        cls.name = name
        cls.salary = salary
        cls.kpi = kpi
        cls.print_record()

    # 定义打印员工信息的类方法
    @classmethod
    def print_record(cls):
        # 以 cls.check_name() 的返回值（0或1）作为判断条件。
        if cls.check_name():
            print('{}的工作信息如下：\n本月工资：{}\n本年绩效：{}'.format(cls.name, cls.salary, cls.kpi))
            cls.kpi_reward()
            print('------------------------------------------------------------')

    # 定义根据 kpi 评奖的类方法
    @classmethod
    def kpi_reward(cls):
        kpi = cls.kpi
        if kpi > 95:
            cls.reward = '明星员工'
            print('恭喜{}拿到{}奖杯'.format(cls.name, cls.reward))
        elif 80 <= kpi <= 95:
            cls.reward = '优秀员工'
            print('恭喜{}拿到{}奖杯'.format(cls.name, cls.reward))
        else:
            cls.reward = '一般员工'
            print('很遗憾{}这次被评为{},没有拿到奖杯，希望来年努力工作，勇创佳绩！'.format(cls.name, cls.reward))

    # 定义一个新的类方法 check_name ，来验证录入的名字是否在公司员工姓名列表里。
    @classmethod
    def check_name(cls):
        # 创建列表保存公司员工姓名
        cls.name_list = ['Kelly', 'Bob', 'Candy', 'Jonny']
        if cls.name in cls.name_list:
            print('录入正确~')
            return 1
        else:
            print('录入错误！%s不是本公司的员工！' % cls.name)
            return 0


HrSystem.record('Kelly', 8000, 89)
HrSystem.record('Bob', 10000, 96)
HrSystem.record('Jonny', 5000, 79)
HrSystem.record('spy', 9000, 85)
