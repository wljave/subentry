import random
import time


# 创建一个类，可实例化成具体的游戏角色
class Role(object):
    def __init__(self):  # 把角色名作为默认参数
        self.name = '【普通角色】'
        self.life = random.randint(100, 150)
        self.attack = random.randint(30, 50)


# 创建三个子类，可实例化为3个不同类型的角色
# 战士类（如果战士的对手是刺客则攻击力提升50%）
class Knight(Role):
    def __init__(self):
        super().__init__()  # 超类利用了父类的初始化函数
        self.name = '【圣光骑士】'  # 用子类角色名重写
        self.life = self.life * 5  # 骑士有5份血量
        self.attack = self.attack * 3  # 骑士有3份攻击力

    def fight_buff(self, opponent, str1, str2):  # fight_buff的意思是“战斗强化”，opponent的意思是“对手”
        if opponent.name == '【暗影刺客】':
            self.attack = self.attack * 1.5
            print('『%s』【圣光骑士】对 『%s』【暗影刺客】说：“让无尽光芒制裁你的堕落！”' % (str1, str2))


# 刺客类（如果刺客的对手是射手则攻击力提升50%）
class Assassin(Role):
    def __init__(self):
        super().__init__()
        self.name = '【暗影刺客】'
        self.life = self.life * 3
        self.attack = self.attack * 5

    def fight_buff(self, opponent, str1, str2):  # fight_buff的意思是“战斗强化”，opponent的意思是“对手”
        if opponent.name == '【精灵弩手】':
            self.attack = self.attack * 1.5
            print('『%s』【暗影刺客】对 『%s』【精灵弩手】说：“主动找死，就别怪我心狠手辣。”' % (str1, str2))


# 射手类（如果射手的对手是战士则攻击力提升50%）
class Bowman(Role):
    def __init__(self):
        super().__init__()
        self.name = '【精灵弩手】'
        self.life = self.life * 4
        self.attack = self.attack * 4

    def fight_buff(self, opponent, str1, str2):  # fight_buff的意思是“战斗强化”，opponent的意思是“对手”
        if opponent.name == '【圣光骑士】':
            self.attack = self.attack * 1.5
            print('『%s』【精灵弩手】对 『%s』【圣光骑士】说：“骑着倔驴又如何？你都碰不到我衣服。”' % (str1, str2))


# 创建一个类，可生成3V3并展示：可分为：欢迎语→随机生成→展示角色
class Game:
    def __init__(self):
        # 初始化各种变量
        self.players = []  # 存玩家顺序
        self.enemies = []  # 存敌人顺序
        self.score = 0  # 比赛积分
        self.i = 0  # 记轮次   注：round表示局数。
        # 执行各种游戏函数
        self.game_start()  # 欢迎语
        self.born_role()  # 随机生成6个角色
        self.show_role()  # 展示角色
        self.order_role()  # 排序并展示
        self.pk_role()  # 让双方 Pk 并展示结果
        self.show_result()  # 展示最终结局

    # 欢迎语
    def game_start(self):
        print('------------ 欢迎来到“炼狱角斗场” ------------')
        print('在昔日的黄昏山脉，奥卢帝国的北境边界上，有传说中的“炼狱角斗场”。')
        print('鲜血与战斗是角斗士的归宿，金钱与荣耀是角斗士的信仰！')
        print('今日，只要你【你的队伍】能取得胜利，你将获得一笔够花500年的财富。')
        time.sleep(2)
        print('将随机生成【你的队伍】和【敌人队伍】！')
        input('\n狭路相逢勇者胜，请按任意键继续。\n')

    # 随机生成6个角色
    def born_role(self):
        # players和enemy列表都要存3个角色
        for i in range(3):
            # 随机抽取可以用random.choice语句：random.choice([Knight(),Assassin(),Bowman()]
            # order = random.choice([Knight(), Assassin(), Bowman()])
            # 然后可以用“列表.append()”把抽到的实例存在列表self.players或者self.enemy中
            # self.players.append(order)
            # self.enemies.append(order)
            self.players.append(random.choice([Knight(), Assassin(), Bowman()]))
            self.enemies.append(random.choice([Knight(), Assassin(), Bowman()]))

    # 展示角色
    def show_role(self):
        print('----------------- 角色信息 -----------------')
        print('你的队伍：')
        for i in range(3):
            print('『我方』%s 血量：%s  攻击：%s' %
                  (self.players[i].name, self.players[i].life, self.players[i].attack))
        print('--------------------------------------------')

        print('敌人队伍：')
        for i in range(3):
            print('『敌方』%s 血量：%s  攻击：%s' %
                  (self.enemies[i].name, self.enemies[i].life, self.enemies[i].attack))
        print('--------------------------------------------')
        input('请按回车键继续。\n')  # 为了让玩家更有控制感，可以插入类似的代码来切分游戏进程。

    # 角色排序，选择出场顺序。
    def order_role(self):
        order_dict = {}
        while self.i < 3:  # 当'i == 3'，循环结束。
            order = int(input('你想将{}放在第几个上场？(输入数字1~3)'.format(self.players[self.i].name)))  # 一个细节：int()
            if order in [1, 2, 3]:  # 先判断输入数字是否是[1,2,3]中的一个，不是的话，执行报错2（行17）.
                if order in order_dict:  # 再判断输入数字是否重复，是的话，执行报错1（下一行）。
                    print('你输入了重复的数字，请重新输入：')  # 报错1
                else:
                    order_dict[order] = self.players[self.i]  # 输入123中不重复的数字，在字典order_dict中创建键值对。
                    self.i += 1  # 有效次数加1
            else:
                print('输入有误，请输入1或2或3：')  # 报错2
        # for i in range(3):
        #     order = int(input('你想将{}放在第几个上场？(输入数字1~3)'.format(self.players[i].name)))
        #     order_dict[order] = self.players[i]

        self.players = []
        for i in range(1, 4):
            self.players.append(order_dict[i])

        # 为了游戏好玩，让电脑也随机出角色
        # random.shuffle(self.enemies)

        print('\n『我方角色』的出场顺序是：%s、%s、%s' % (self.players[0].name, self.players[1].name, self.players[2].name))
        print('『敌方角色』的出场顺序是：%s、%s、%s' % (self.enemies[0].name, self.enemies[1].name, self.enemies[2].name))
        print('\n')
        # time.sleep(0.5)

    # 让双方 Pk 并展示结果
    def pk_role(self):
        for i in range(3):  # # 一共要打三局 i依次为0,1,2
            player_name = self.players[i].name  # 统一将下面会用到的数据先赋值给变量会更清晰更好管理
            # 提取玩家角色名称
            enemy_name = self.enemies[i].name

            # 每一局开战前加buff
            self.players[i].fight_buff(self.enemies[i], '我方', '敌方')
            self.enemies[i].fight_buff(self.players[i], '敌方', '我方')
            # 玩家血量是字典里的值（元组）的第0个元素，以下同理
            player_life = self.players[i].life
            player_attack = self.players[i].attack
            enemy_life = self.enemies[i].life
            enemy_attack = self.enemies[i].attack
            # 每一局开战前展示战斗信息
            print('\n----------------- 【第%s局】 -----------------' % (i + 1))
            print('我方角色：%s vs 敌方角色：%s ' % (player_name, enemy_name))
            print('『我方』%s 血量：%d  攻击：%d' % (player_name, player_life, player_attack))
            print('『敌方』%s 血量：%d  攻击：%d' % (enemy_name, enemy_life, enemy_attack))
            print('--------------------------------------------')
            input('\n 战斗双方准备完毕，请按回车键继续。')
            # 开始判断血量双方血量都大于零，战斗过程会一直然后互扣血量。
            while player_life > 0 and enemy_life > 0:
                enemy_life -= player_attack
                player_life -= enemy_attack
                print('%s发起了攻击，%s剩余血量%d' % (player_name, enemy_name, enemy_life))
                print('%s发起了攻击，%s剩余血量%d' % (enemy_name, player_name, player_life))
                print('--------------------------------------------')
                time.sleep(1)

            if player_life > 0 and enemy_life <= 0:
                print('\n恭喜，我方%s 活下来了。\n' % (self.players[i].name))
                self.score += 1
            elif player_life <= 0 and enemy_life > 0:
                print('\n很遗憾，我方%s 挂掉了！\n' % (self.players[i].name))
                self.score -= 1
            else:
                print('\n我的天，他们俩同归于尽了！\n')
            time.sleep(1)

    # 展示最终结局
    def show_result(self):  # 注意：该函数要设定参数，才能判断单局战果。
        input('\n点击回车，查看比赛的最终结果\n')
        if self.score > 0:
            print('【最终结果：你赢了！】\n最终的财宝都归你了！')
        elif self.score < 0:
            print('【最终结果：你输了！】\n你没有胜利，但也没有失败，在夜色中灰溜溜离开了奥卢帝国。')
        else:
            print('【最终结果：平局！】\n炼狱角斗场又多了几具枯骨。')


game = Game()  # 运行游戏
