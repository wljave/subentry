# 出租车计费
class Taxi:
    def __init__(self, kilometers_cost, kilometers_num, kilometers_money):
        # 每公里费用
        self.kilometers_cost = kilometers_cost
        # 起步公里数
        self.kilometers_num = kilometers_num
        # 起步价
        self.kilometers_money = kilometers_money
        # 总公里数
        self.kilometers = float(input('请输入行程公里数：'))
        # 总费用 = 起步价 + (总公里数 - 起步公里数) * 每公里费用
        self.cost = self.kilometers_money + (self.kilometers - self.kilometers_num) * self.kilometers_cost

    # 计费
    def fare(self):
        if 0 < self.kilometers <= self.kilometers_num:
            # 起步价内费用
            print('费用一共是：' + str(self.kilometers_money) + '元')
        elif self.kilometers > self.kilometers_num:
            # 打印总费用
            print('费用一共是：' + str(self.cost) + '元')
        else:
            print('您输入的公里数无效！')


# 参数分别是 每公里费用， 起步公里数， 起步价格
wang_taxi = Taxi(2.5, 3, 15)

wang_taxi.fare()

wang_taxi = Taxi(2.5, 4, 20)

wang_taxi.fare()

wang_taxi = Taxi(2.5, 2, 12)

wang_taxi.fare()

print('---------------把计费函数拆解成计费、记录行程、统计费用、结算信息四个函数--------------')


# 出租车计费
class Taxi1:
    def __init__(self, kilometers_cost, kilometers_num, kilometers_money):
        # 每公里费用
        self.kilometers_cost = kilometers_cost
        # 起步公里数
        self.kilometers_num = kilometers_num
        # 起步价
        self.kilometers_money = kilometers_money
        # 总公里数
        self.kilometers = float(input('请输入行程公里数：'))
        # 总费用 = 起步价 + (总公里数 - 起步公里数) * 每公里费用
        self.cost = self.kilometers_money + (self.kilometers - self.kilometers_num) * self.kilometers_cost

    # 计费
    def blling(self):
        # self.records()
        self.statistical()
        self.settlement()

    # # 记录行程
    # def records(self):
    #     # 总公里数
    #     self.kilometers = float(input('请输入行程公里数：'))

    # 统计费用
    def statistical(self):
        if 0 < self.kilometers <= self.kilometers_num:
            # 起步价内费用
            self.cost = self.kilometers_money
        elif self.kilometers > self.kilometers_num:
            self.cost = self.cost
        else:
            self.cost = 0.0
            print('您输入的公里数无效！')

    # 结算信息
    def settlement(self):
        # 打印总费用
        print('费用一共是：' + str(self.cost) + '元')


class Electric(Taxi1):
    # 结算信息
    def settlement(self):
        # 打印总费用
        print('费用一共是：' + str(self.cost * 0.8) + '元')
    # # 统计费用
    # def statistical(self):
    #     if 0 < self.kilometers <= self.kilometers_num:
    #         # 起步价内费用
    #         self.cost = self.kilometers_money * 0.8
    #     elif self.kilometers > self.kilometers_num:
    #         self.cost = self.cost * 0.8
    #     else:
    #         self.cost = 0.0
    #         print('您输入的公里数无效！')


# 参数分别是 每公里费用， 起步公里数， 起步价格
wang_taxi1 = Taxi1(2.5, 3, 15)

wang_taxi1.blling()

li_electric = Electric(2.5, 3, 15)

li_electric.blling()
