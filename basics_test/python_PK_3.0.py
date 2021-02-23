#阅读代码后，点击运行，依次输入3，2，1    
print('------------------------方法一：使用字典-------------------------')
list1 = ['A','B','C']
dict1 = {}

for i in range(3):
    order = int(input('你要把'+list1[i]+'放在第几位？（请输入数字1,2,3)：'))
    dict1[order] = list1[i]

# 清空原本列表list1的元素
list1 = []
for i in range(3):
    list1.append(dict1[i+1])
    
#print(dict1)
print(list1)

print('------------------------方法二：使用列表3、2、1错误-------------------------')
list2 = ['A','B','C']
list3 = []
list4 = []
for i in range (3):
    list3.extend(list2)
    order = int(input('你要把'+list2[i]+'放在第几位？（请输入数字1,2,3):'))
    t = list3.pop(i)
    list4.insert(order-1,t)
    print(list3)
    list3 = []
    print(list4)
##if list4 == ['C', 'A', 'B']:
##    b = list4.pop()
##    list4.insert(1,b)
print(list4)


print('------------------------角色封装-------------------------')

import random

# 将需要的数据和固定变量放在开头
player_list =  ['【狂血战士】','【森林箭手】','【光明骑士】','【独行剑客】','【格斗大师】','【枪弹专家】']
enemy_list = ['【暗黑战士】','【黑暗弩手】','【暗夜骑士】','【嗜血刀客】','【首席刺客】','【陷阱之王】']
players = random.sample(player_list,3)  
enemies = random.sample(enemy_list,3)
player_info = {}
enemy_info = {}

# 随机生成角色的属性
def born_role():
    life = random.randint(100,180)
    attack = random.randint(30,50)
    return life,attack

# 生成和展示角色信息
def show_role():
    for i in range(3):
        player_info[players[i]] = born_role()
        enemy_info[enemies[i]] = born_role()
    
    # 展示我方的3个角色
    print('----------------- 角色信息 -----------------')
    print('你的人物：')
    for i in range(3):
        print('%s  血量：%d  攻击：%d' 
        %(players[i],player_info[players[i]][0],player_info[players[i]][1]))
    print('--------------------------------------------')
    print('电脑敌人：')
    
    # 展示敌方的3个角色
    for i in range(3):
        print('%s  血量：%d  攻击：%d' 
        %(enemies[i],enemy_info[enemies[i]][0],enemy_info[enemies[i]][1]))
    print('--------------------------------------------')
    input('请按回车键继续。\n')  # 为了让玩家更有控制感，可以插入类似的代码来切分游戏进程。

# 角色排序，选择出场顺序。
def order_role(): 
    global players
    order_dict = {}
    for i in range(3):
        order = int(input('你想将 %s 放在第几个上场？(输入数字1~3)'%(players[i])))
        order_dict[order] = players[i]  

    players = []
    for i in range(1,4):
        players.append(order_dict[i])

    #为了游戏好玩，让电脑也随机出角色
    random.shuffle(enemies)
    
    print('\n我方角色的出场顺序是：%s、%s、%s' %(players[0],players[1],players[2]))
    print('敌方角色的出场顺序是：%s、%s、%s' %(enemies[0],enemies[1],enemies[2]))

def main():
    show_role()
    order_role()

main()
