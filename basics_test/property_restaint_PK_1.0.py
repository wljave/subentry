# 版本1.0：类的封装，将类作为函数包，把各种函数打包封装起来
# 版本2.0：类的继承和实例化，让三种不同类型的角色属性也不同
# 版本3.0：为三个角色的类，添加一个让角色之间可以相互克制的类方法
import random
import time


class Game(object):
    # 将需要的数据和固定变量放在开头
    player_list = ['【暗黑战士】', '【黑暗弩手】', '【暗夜骑士】', '【嗜血刀客】', '【首席刺客】', '【陷阱之王】', '【狂血战士】', '【森林箭手】', '【光明骑士】', '【独行剑客】',
                   '【格斗大师】', '【枪弹专家】']
    enemy_list = ['【鲁班七号】', '【宫本武藏】', '【马可波罗】', '【娜可露露】', '【不知火舞】', '【成吉思汗】', '【太乙真人】', '【东皇太一】', '【干将莫邪】', '【百里守约】',
                  '【百里玄策】', '【上官婉儿】', '【鲁班大师】']
    li2 = ['【夏洛特】', '【阿古朵】', '【云中君】', '【猪八戒】', '【沈梦溪】', '【司马懿】', '【米莱狄】', '【裴擒虎】', '【杨玉环】', '【公孙离】', '【明世隐】', '【鬼谷子】',
           '【诸葛亮】', '【蔡文姬】', '【雅典娜】', '【李元芳】', '【孙悟空】', '【橘右京】', '【花木兰】', '【兰陵王】', '【王昭君】', '【姜子牙】', '【程咬金】', '【安琪拉】',
           '【老夫子】', '【武则天】', '【狄仁杰】', '【夏侯淳】', '【钟无艳】', '【高渐离】', '【孙尚香】']
    li3 = ['【蒙恬】', '【蒙犽】', '【西施】', '【马超】', '【盘古】', '【嫦娥】', '【李信】', '【伽罗】', '【盾山】', '【孙策】', '【元歌】', '【狂铁】', '【弈星】',
           '【女娲】',
           '【梦奇】', '【苏烈】', '【大乔】', '【黄忠】', '【哪吒】', '【杨戬】', '【钟馗】', '【虞姬】', '【张飞】', '【刘备】', '【后羿】', '【牛魔】', '【亚瑟】',
           '【张良】',
           '【韩信】', '【刘邦】', '【露娜】', '【貂蝉】', '【关羽】', '【项羽】', '【达摩】', '【李白】', '【典韦】', '【曹操】', '【甄姬】', '【周瑜】', '【吕布】',
           '【芈月】',
           '【白起】', '【扁鹊】', '【孙膑】', '【阿轲】', '【刘禅】', '【庄周】', '【嬴政】', '【妲己】', '【墨子】', '【赵云】', '【小乔】', '【廉颇】']
    li4 = ['【镜】', '【曜】', '【瑶】', '【凯】']
    enemy_list.extend(li2)
    enemy_list.extend(li3)
    enemy_list.extend(li4)
    player_info = {}
    enemy_info = {}

    # 初始化方法
    def __init__(self):
        # 随机抽取3个角色名形成玩家角色列表和敌人角色列表
        self.players = random.sample(self.player_list, 3)
        self.enemies = random.sample(self.enemy_list, 3)
        # 然后执行游戏流程的相关函数展开战斗流程
        self.show_role()
        self.order_role()
        self.pk_role()

    # 随机生成角色的属性
    def born_role(self):
        life = random.randint(100, 180)
        attack = random.randint(30, 50)
        return life, attack

    # 给角色生成随机属性，并展示角色信息。
    def show_role(self):
        for i in range(3):
            # 给我方角色信息的字典添加键值对
            self.player_info[self.players[i]] = self.born_role()
            # 这里要给敌人角色信息的字典添加键值对
            self.enemy_info[self.enemies[i]] = self.born_role()

        # 展示我方的3个角色
        print('----------------- 角色信息 -----------------')
        print('你的人物：')
        for i in range(3):
            print('%s  血量：%d  攻击：%d'
                  % (self.players[i], self.player_info[self.players[i]][0], self.player_info[self.players[i]][1]))
        print('--------------------------------------------')
        print('电脑敌人：')

        # 展示敌方的3个角色
        for i in range(3):
            print('%s  血量：%d  攻击：%d'
                  % (self.enemies[i], self.enemy_info[self.enemies[i]][0], self.enemy_info[self.enemies[i]][1]))
        print('--------------------------------------------')
        input('请按回车键继续。\n')  # 为了让玩家更有控制感，可以插入类似的代码来切分游戏进程。

    # 角色排序，选择出场顺序。
    def order_role(self):
        order_dict = {}
        for i in range(3):
            order = int(input('你想将{}放在第几个上场？(输入数字1~3)'.format(self.players[i])))
            order_dict[order] = self.players[i]

        self.players = []
        for i in range(1, 4):
            self.players.append(order_dict[i])

        # 为了游戏好玩，让电脑也随机出角色
        random.shuffle(self.enemies)

        print('\n我方角色的出场顺序是：%s、%s、%s' % (self.players[0], self.players[1], self.players[2]))
        print('敌方角色的出场顺序是：%s、%s、%s' % (self.enemies[0], self.enemies[1], self.enemies[2]))

    # 角色PK过程
    def pk_role(self):
        round = 1  # 注：round表示局数。
        score = 0
        for i in range(3):  # # 一共要打三局 i依次为0,1,2
            player_name = self.players[i]  # 统一将下面会用到的数据先赋值给变量会更清晰更好管理
            # 提取玩家角色名称
            enemy_name = self.enemies[i]
            # 玩家血量是字典里的值（元组）的第0个元素，以下同理
            player_life = self.player_info[self.players[i]][0]
            player_attack = self.player_info[self.players[i]][1]
            enemy_life = self.enemy_info[self.enemies[i]][0]
            enemy_attack = self.enemy_info[self.enemies[i]][1]
            # 每一局开战前展示战斗信息
            print('\n----------------- 【第%d局】 -----------------' % round)
            print('玩家角色：%s vs 敌方角色：%s ' % (player_name, enemy_name))
            print('%s 血量：%d  攻击：%d' % (player_name, player_life, player_attack))
            print('%s 血量：%d  攻击：%d' % (enemy_name, enemy_life, enemy_attack))
            print('--------------------------------------------')
            input('\n 请按回车键继续。\n')
            # 开始判断血量双方血量都大于零，战斗过程会一直然后互扣血量。
            while player_life > 0 and enemy_life > 0:
                enemy_life = enemy_life - player_attack
                player_life = player_life - enemy_attack
                print('%s发起了攻击，%s剩余血量%d' % (player_name, enemy_name, enemy_life))
                print('%s发起了攻击，%s剩余血量%d' % (enemy_name, player_name, player_life))
                print('--------------------------------------------')
                time.sleep(1)
            else:  # 每局的战果展示，以及分数score和局数round的影响变化。
                print(self.show_result(player_life, enemy_life)[1])
                # 调用show_result()函数，打印返回元组中的第一个元素result。
                score += int(self.show_result(player_life, enemy_life)[0])
                # 调用show_result()函数，完成计分变动。
                round += 1
        ##        print(show_result(player_life,enemy_life))
        ##        print(show_result(player_life,enemy_life)[0])
        ##        print(show_result(player_life,enemy_life)[1])
        input('\n点击回车，查看比赛的最终结果\n')
        if score > 0:
            print('【最终结果：你赢了！】\n')
        elif score < 0:
            print('【最终结果：你输了！】\n')
        else:
            print('【最终结果：平局！】\n')

    # 返回单局战果和计分法所加分数。
    def show_result(self, player_life, enemy_life):  # 注意：该函数要设定参数，才能判断单局战果。
        if player_life > 0 and enemy_life <= 0:
            result = '\n敌人死翘翘了，你赢了！'
            return 1, result  # 返回元组(1,'\n敌人死翘翘了，你赢了！')
        elif player_life <= 0 and enemy_life > 0:
            result = '\n悲催，敌人把你干掉了！'
            return -1, result  # 返回元组(-1,'\n悲催，敌人把你干掉了！')
        else:
            result = '\n哎呀，你和敌人同归于尽了！'
            return 0, result  # 返回元组(0,'\n哎呀，你和敌人同归于尽了！')


# 实例化“游戏类”，从而启动游戏所有相关函数
game = Game()
