 #提示：调用模块需在开头写上import 模块名，这里需要用到random模块
import random
import time

def game():

    #保存成绩，胜利得1分、失败-1、平局不得分
    player_score = 0    #用来保存玩家成绩
    enemy_score = 0    #用来保存敌人成绩

    for i in range(1,4):
        time.sleep(1.5)  # 让局与局之间有较明显的有时间间隔
        #print(' \n——————现在是第'+str(i)+'局，ready go!——————')  # 作为局的标记
        print(' \n——————现在是第%s局，ready go!——————'%i)  # 作为局的标记
        #玩家=>player;敌人=>enemy;血量=>HP;攻击力=>ATK 
        player_HP = random.randint(100,150)
        player_ATK = random.randrange(30,51)
        enemy_HP = random.randint(100,150)
        enemy_ATK = random.randrange(30,51)
    ##    for i in range(2):
    ##        HP = random.randint(100,150)
    ##        ATK = random.randrange(30,51)
    ##        if i == 0:
    ##            player_HP = HP
    ##            player_ATK = ATK
    ##        else:
    ##            enemy_HP = HP
    ##            enemy_ATK = ATK
    ##        print(HP,ATK)
    ##    print('\n')

        #显示双方属性
        print('*' * 5 + '这是玩家血量和攻击力' + '*' * 5)
        #print('【玩家】\n'+'血量：'+str(player_HP)+'\n攻击：'+str(player_ATK))
        print('【玩家】\n'+'血量：%s\n攻击：%s'%(player_HP,player_ATK))
        time.sleep(1)
        print('*' * 5 + '这是敌人血量和攻击力' + '*' * 5)
        time.sleep(1)
        print('【敌人】\n'+'血量：%s\n攻击：%s'%(enemy_HP,enemy_ATK))
        print('------------------------')

        #双方对战
        while (player_HP > 0) and (enemy_HP>0):
            #血量计算公式：自身原血量-对方的攻击力=自身剩余血量
            enemy_HP = enemy_HP-player_ATK
            player_HP = player_HP-enemy_ATK
            print('你发起了攻击，【敌人】剩余血量%s'%enemy_HP)
            print('敌人向你发起了攻击，【玩家】剩余血量%s'%player_HP)
            print('------------------------')
            time.sleep(1.5)

        #对战结果
        if (enemy_HP) > 0 and (player_HP <= 0):
            print('恭喜【敌人】获胜')
            enemy_score += 1
        elif (enemy_HP) <= 0 and (player_HP > 0):
            print('恭喜【你】获胜')
            player_score += 1
        else:
            print('@*@平局哦！')
        time.sleep(2)

    #打印最终结果
##    print(player_score,enemy_score)
    if player_score > enemy_score :
        print('\n最终获胜方是【你】')
    elif enemy_score > player_score :
        print('\n最终获胜方是【敌人】')
    else:
        print('\n最终两败俱伤')

game()

while True:
    print('————————————————————————————————————————————————')
    again = input('要再来一局吗?\n请输入y继续，输入n退出：')
    if again == 'y':
        game()
    elif again == 'n':
        break
    else:
        print( '\n输入无效，请输入y或n')
    
