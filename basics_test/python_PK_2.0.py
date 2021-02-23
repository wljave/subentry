import random
import time

print('-----------------方法一----------------\n')

player_list =  ['【狂血战士】','【森林箭手】','【光明骑士】','【独行剑客】','【格斗大师】','【枪弹专家】']
players = random.sample(player_list,3)  # 从列表里随机选取三个元素
player_life = {}  # 建立空字典，存放我方角色的血量。
player_attack = {}  # 建立空字典，存放我方角色的攻击。

# 将这个过程封装成函数
def show_role():
    #循环三次
    for i in range(3):
        # 生成角色的属性
        life = random.randint(100,180) 
        attack = random.randint(30,50) 
        player_life[players[i]] = life # 给空字典添加键值对，角色列表players的第0个元素为键，变量life为值
        player_attack[players[i]] = attack # 给空字典添加键值对，角色列表players的第0个元素为键，变量attack为值

    # 展示我方的角色信息
    print('----------------- 角色信息 -----------------')
    print('你的人物：')
    time.sleep(1)
    for i in range(3):
        print('%s  血量：%d  攻击：%d' 
        %(players[i],player_life[players[i]],player_attack[players[i]]))
        
    print('--------------------------------------------')

show_role()


print('-------------方法二------------\n')

player_list =  ['【狂血战士】','【森林箭手】','【光明骑士】','【独行剑客】','【格斗大师】','【枪弹专家】']
players = random.sample(player_list,3)  # 从列表里随机选取三个元素
player_life_attack = {}  # 建立空字典，存放我方角色的血量和攻击。

##for i in range(3):
##    # 将这个过程封装成函数
##    def info():
##        # 生成角色的属性
##        life = random.randint(100,180) 
##        attack = random.randint(30,50)
##        return (life,attack)
##
##    #调用info()函数，将返回的元组(life,attack)赋值给变量data
##    data = info()
##    #往空字典添加键值对，player_list[0]即'狂血战士'为键，data（元组）为值。
##    player_life_attack[players[i]] = data

# 随机生成属性，并用return语句保存属性信息
def born_role2():
    life = random.randint(100,180)
    attack = random.randint(30,50)
    return (life,attack) 
    
# 给角色生成随机属性，并展示角色信息。
def show_role2():
    for i in range(3):
        player_life_attack[players[i]] = born_role2()

    # 展示我方的3个角色信息
    print('----------------- 角色信息 -----------------')
    print('你的人物：')
    time.sleep(1)

    for i in range(3):
        print('%s  血量：%d  攻击：%d' 
        %(players[i],player_life_attack[players[i]][0],player_life_attack[players[i]][1]))
        
    print('--------------------------------------------')

show_role2()



print('-------------添加电脑敌方属性信息------------\n')

player_list =  ['【狂血战士】','【森林箭手】','【光明骑士】','【独行剑客】','【格斗大师】','【枪弹专家】']
enemy_list =  ['【德玛西亚】','【寒冰箭手】','【百里守约】','【东皇太一】','【百里玄策】','【干将莫邪】']
players = random.sample(player_list,3)  # 从列表里随机选取三个元素，保存我方信息
enemies = random.sample(enemy_list,3)  #保存地敌方信息
player_life_attack = {}  # 建立空字典，存放我方角色的血量和攻击。
enemy_life_attack = {}  # 建立空字典，存放我方角色的血量和攻击。


# 随机生成属性，并用return语句保存属性信息
def born_role3():
    life = random.randint(100,180)
    attack = random.randint(30,50)
    return (life,attack) 
    
# 给角色生成随机属性，并展示角色信息。
def show_role3():
    for i in range(3):
        player_life_attack[players[i]] = born_role3()
        # 这里要给敌人角色信息的字典添加键值对
        enemy_life_attack[enemies[i]] = born_role3()

    # 展示我方的3个角色信息
    print('----------------- 角色信息 -----------------')
    print('你的人物：')
    for i in range(3):
        print('%s  血量：%d  攻击：%d' 
        %(players[i],player_life_attack[players[i]][0],player_life_attack[players[i]][1]))
        
    print('--------------------------------------------')
    time.sleep(1)

    print('电脑敌人：')
    # 展示敌方3个角色信息
    for i in range(3):
        print('%s  血量：%d  攻击：%d' 
        %(enemies[i],enemy_life_attack[enemies[i]][0],enemy_life_attack[enemies[i]][1]))
        
    print('--------------------------------------------')

show_role3()
