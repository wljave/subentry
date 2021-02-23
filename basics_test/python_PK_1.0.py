import time 

#展示角色
def show_role(player_life,player_attack,enemy_life,enemy_attack):
    print('【玩家】\n血量：%s\n攻击：%s'%(player_life,player_attack))
    print('------------------------')
    time.sleep(1)
    print('【敌人】\n血量：%s\n攻击：%s'%(enemy_life,enemy_attack))
    print('-----------------------')

#双方PK
def pk_role(player_life,player_attack,enemy_life,enemy_attack):
    while player_life > 0 and enemy_life > 0:
        player_life = player_life - enemy_attack 
        enemy_life = enemy_life - player_attack
        print('你发起了攻击，【敌人】剩余血量%s'%(enemy_life))
        print('敌人向你发起了攻击，【玩家】的剩余血量%s'%(player_life))
        print('-----------------------')
        time.sleep(1)
    victory(player_life,enemy_life) #不在主函数里面调用，在pk里面调用

#保存成绩，胜利得1分、失败-1、平局不得分
player_score = 0    #用来保存玩家成绩
enemy_score = 0    #用来保存敌人成绩

#打印战果
def victory(player_life,enemy_life):
    if player_life > 0 and enemy_life <= 0:
        print('敌人死翘翘了，这局你赢了')
        global enemy_score
        enemy_score += 1
    elif player_life <= 0 and enemy_life > 0:
        print('悲催，这局敌人把你干掉了！')
        global player_score
        player_score -= 1
    else:
        print('哎呀，这局你和敌人同归于尽了！')
    print('-----------------------')
    time.sleep(2)


def score(player_score,enemy_score):
    #打印最终结果
    if player_score > enemy_score :
        print('\n最终获胜方是【你】')
    elif enemy_score > player_score :
        print('\n最终获胜方是【敌人】')
    else:
        print('\n最终两败俱伤')
 
#主函数
def main(player_life,player_attack,enemy_life,enemy_attack):
    show_role(player_life,player_attack,enemy_life,enemy_attack)
    pk_role(player_life,player_attack,enemy_life,enemy_attack)
    #victory(player_life,enemy_life)
    


for i in range(1,4):
    time.sleep(1.5)  # 让局与局之间有较明显的有时间间隔
    print(' \n——————现在是第%s局，ready go!——————'%i)  # 作为局的标记

    main(100,35,105,33)
#score(player_score,enemy_score)
