import random
import time

punches = ['石头', '剪刀', '布']
score = 0

print('*****************石头剪刀布游戏******************')
input('请按下回车键开始游戏')


# 双方亮拳，并展示。
def show_role():
    round = 1  # 注：round表示局数。
    global score
    for i in range(3):
        # 每一局开战前展示战斗信息
        print('\n----------------- 【第%d局】 -----------------' % round)
        # 代表电脑的出拳选择
        computer_choice = random.choice(punches)
        user_choice = input('请你出拳（石头、剪刀、布）：')
        while user_choice not in punches:
            print('输入有误，请重新出拳')
            user_choice = input('请你出拳（石头、剪刀、布）：')

        while user_choice in punches:
            # if user_choice == punches[0] or user_choice == punches[1] or user_choice == punches[2]:
            print('----------------战斗开始------------------')
            print('================电脑VS人==================')
            print('【玩家：{}】VS【电脑：{}】'.format(user_choice, computer_choice))
            break

        show_result(user_choice, computer_choice)
        round += 1

    input('\n点击回车，查看比赛的最终结果\n')
    if score > 0:
        print('【最终结果：你赢了！】\n')
    elif score < 0:
        print('【最终结果：你输了！】\n')

    else:
        print('【最终结果：平局！】\n')
    time.sleep(1)


# 返回单局战果
def show_result(user_choice, computer_choice):
    global score
    if user_choice == computer_choice:
        print('\n结果：平局！')
    # elif (user_choice == punches[0] and computer_choice == punches[1]) or (user_choice == punches[1] and computer_choice == punches[2]) or (user_choice == punches[2] and computer_choice == punches[0]):
    # elif (computer_choice == '剪刀' and user_choice == '石头') or (computer_choice == '布' and user_choice == '剪刀') or (computer_choice == '石头' and user_choice == '布'):
    # 玩家的选择有3种，索引位置分别是：0石头、1剪刀、2布。
    # 假设在电脑索引位置上减1，对应：-1布，0石头，1剪刀，玩家皆胜。
    elif (user_choice == punches[punches.index(computer_choice) - 1]):
        score += 1
        print('\n结果：你赢了！')
    else:
        score -= 1
        print('\n结 果：你输了！')


def again():
    global score
    while True:
        choose = input('你还要和电脑对战吗？(请输入y继续，输入n退出):')
        if (choose == 'y') or (choose == 'Y'):
            score = 0
            show_role()
        elif (choose == 'n') or (choose == 'N'):
            print('再见！欢迎您再来玩猜拳游戏')
            break
        else:
            print('输入有误，请重新选择\n')
            continue


# （主函数）展开战斗流程
def main():
    show_role()
    again()


main()
