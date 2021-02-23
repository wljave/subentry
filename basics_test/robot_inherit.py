class Role:
    def __init__(self, name='【角色】'):  # 把角色名作为默认参数
        self.name = name


class RRole:
    def __init__(self, name='【蜘蛛侠】'):
        self.name = name


a = Role()
print('实例a的角色名称是：' + a.name)

b = Role('【钢铁侠】')
print('实例b的角色名称是：' + b.name)

c = RRole()
print('实例c的角色名称是：' + c.name)

print('-' * 30 + '可爱的机器人分割线' + '-' * 30)


# 基础机器人
class Abstract_Robot:
    def __init__(self):
        self.name = input('主人，请给我起个好听的名字：')

    # 自报姓名
    def self_reported(self):
        print('我是%s！' % self.name)
        self.acting_cute()

    # 卖萌
    def acting_cute(self):
        print('主人，%s求抱抱！' % self.name)


# 高级机器人
class Advanced_Robot(Abstract_Robot):
    # 高级卖萌 senior_cute
    def senior_cute(self):
        print('主人，%s每次想到怎么欺负你的时候，就感觉自己全身biubiubiu散发着智慧的光芒！' % self.name)


# 实例化高级机器人
robot = Advanced_Robot()

# 调用自报姓名
robot.self_reported()
# 调用高级卖萌
robot.senior_cute()

print('-' * 30 + '单继承-高级机器人继承基础机器人的方法并重写分割线' + '-' * 30)


# 基础机器人
class Abstract_Robot:
    def __init__(self):
        self.name = input('主人，请给我起个好听的名字：')

    # 自报姓名
    def self_reported(self):
        print('我是%s！' % self.name)
        self.acting_cute()

    # 卖萌
    def acting_cute(self):
        print('主人，%s求抱抱！' % self.name)


# 高级机器人
class Advanced_Robot(Abstract_Robot):
    def __init__(self):
        super().__init__()
        self.iq = input('主人，请给我设定一个智商值：')

    # 自报姓名
    def self_reported(self):
        print('我是高级机器人{}智商高达{}！'.format(self.name, self.iq))
        self.acting_cute()

    # 卖萌 senior_cute
    def acting_cute(self):
        print('主人，%s每次想到怎么欺负你的时候，就感觉自己全身biubiubiu散发着智慧的光芒！' % self.name)


# 实例化高级机器人
robot = Advanced_Robot()

# 调用自报姓名
robot.self_reported()

print('-' * 30 + '多继承-超级机器人继承高级机器人和基础机器人的方法分割线' + '-' * 30)


# 基础机器人
class Abstract_Robot:
    def __init__(self):
        self.name = input('主人，请给我起个好听的名字：')

    # 自报姓名
    def self_reported(self):
        print('我是%s！' % self.name)
        self.acting_cute()

    # 卖萌
    def acting_cute(self):
        print('主人，%s求抱抱！' % self.name)


# 高级机器人
class Advanced_Robot:
    def __init__(self):
        self.name = input('主人，请给我起个好听的名字：')
        self.iq = input('主人，请给我设定一个智商值：')

    # 高级自报姓名
    def senior_self_reported(self):
        print('我是高级机器人{}智商高达{}！'.format(self.name, self.iq))
        self.senior_cute()

    # 高级卖萌 senior_cute
    def senior_cute(self):
        print('主人，%s每次想到怎么欺负你的时候，就感觉自己全身biubiubiu散发着智慧的光芒！' % self.name)


# 超级机器人
class Super_Robot(Advanced_Robot, Abstract_Robot):
    def __init__(self):
        # self.name = input('主人，请给我起个好听的名字：')
        # self.iq = input('主人，请给我设定一个智商值：')
        super().__init__()
        self.magic = input('主人，请给我设定一个绝招：')

    # 超级自报姓名
    def super_self_reported(self):
        print('我是超级机器人{}智商高达{}我的绝招是{}！'.format(self.name, self.iq, self.magic))
        self.super_cute()

    # 超级卖萌
    def super_cute(self):
        print('pika, qiu!%s' % self.name)
        print('''　           　へ　　　　　／|
                      /＼7　　　∠＿/
                     /　│　　／　／
                     │　Z＿,＜　／　　/`ヽ
                     │　　　　　ヽ　　/　　〉
                     Y　　　　　`　/　　/
                     ｲ●　､　●　　⊂⊃〈　　/
                     ()　へ　　　　|　＼〈
                      >ｰ､_　ィ　│／／
                     /へ　　/　ﾉ＜|＼＼
                     ヽ_ﾉ　　(_／　│／／
                      7　　　　　　　|／
                      ＞―r￣￣`ｰ―＿''')


# 实例化基础机器人
# robot = abstract_robot()
# 实例化高级机器人
# robot = advanced_robot()

# 实例化超级机器人
robot = Super_Robot()

# 调用自报姓名
robot.self_reported()  # 调用基础机器人自报姓名
robot.senior_self_reported()  # 调用高级机器人自报姓名
robot.super_self_reported()  # 调用超级机器人自报姓名
