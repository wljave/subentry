import csv

# 调用csv模块
# 调用open()函数打开csv文件，传入参数：文件名“assets.csv”、追加模式“a”、newline=''。
with open('assets.csv', 'a', newline='', encoding='GBK') as csvfile:
    # 用csv.writer()函数创建一个writer对象。
    writer = csv.writer(csvfile, dialect='excel')
    header = ['序号', '小区名称', '地址', '建筑年份', '楼栋', '单元', '户室', '朝向', '面积']
    # 用writerow()函数将表头写进csv文件里
    writer.writerow(header)

    # 序号serial
    serial = 1
    title = input('请输入小区名称：')
    address = input('请输入小区地址：')
    year = input('请输入小区建造年份：')
    block = input('请输入楼栋号：')
    # unit = input('请输入单元号：')

unit_loop = True
while unit_loop:
    unit = input('请输入单元号：')
    # 定义起始楼层数
    start_floor = input('请输入起始楼层：')
    # 定义终止楼层数
    end_floor = input('请输入终止楼层：')

    # 定义户室号
    # floor_last_number = ['01', '02', '03']
    # 开始输入模板数据
    input('接下来请输入起始层每个房间的门牌号、南北朝向及面积，按任意键继续')
    # 户室的尾号
    start_floor_rooms = {}
    floor_last_number = []
    # 收集起始层的房间信息
    # start_floor_rooms = {301: [1, 80], 302: [1, 80], 303: [2, 90]}

    # 定义循环控制量
    room_loop = True
    while room_loop:
        last_number = input('请输入起始楼层户室的尾号:（如01，02）')
        # 将尾号用append()添加列表里，如floor_last_number = ['01','02']
        floor_last_number.append(last_number)
        # 户室号为room_number,由楼层start_floor和尾号last_number组成,如301
        room_number = int(start_floor + last_number)

        direction = int(input('请输入 %d 的朝向(南北朝向输入1，东西朝向输入2)：' % room_number))
        area = int(input('请输入 %d 的面积，单位 ㎡ ：' % room_number))
        # 户室号为键，朝向和面积组成的列表为值，添加到字典里，如start_floor_rooms = {301:[1,70]}
        start_floor_rooms[room_number] = [direction, area]

        # 加入打破循环的条件
        continued = input('是否需要输入下一个尾号？按 n 停止输入，按其他任意键继续：')
        if continued == 'n':
            room_loop = False
        else:
            room_loop = True

    # 新建一个放单元所有户室数据的字典
    unit_rooms = {}
    # 给美楼层创建一个字典
    floor_rooms = {}

    # 外层遍历次数为楼层数之差加1
    floor = int(end_floor) - int(start_floor) + 1
    # a为楼层开始数
    a = int(start_floor)

    for j in range(floor):
        for i in range(len(start_floor_rooms)):
            # 房号
            number = str(a) + floor_last_number[i]
            # [朝向，面积]
            info = start_floor_rooms[int(start_floor + floor_last_number[i])]
            # {房号：[朝向，面积]}
            floor_rooms[int(number)] = info
            # {楼号：{房号：[朝向，面积]}}
            unit_rooms[a] = floor_rooms
            serial += 1
        # 楼层每次循环结束字典清零
        floor_rooms = {}
        a += 1

    print(unit_rooms)

    # 读取字典里的值---方法一
    # for i in range(len(unit_rooms)):
    #     rooms = unit_rooms[i + 3]
    #     print(rooms)

    with open('assets.csv', 'a', newline='')as csvfile:
        writer = csv.writer(csvfile, dialect='excel')
        # 读取字典里的值---方法二
        for sub_dict in unit_rooms.values():
            # print(sub_dist)
            for room, info in sub_dict.items():
                dire = ['', '南北', '东西']
                # print(dire[info[0]])
                writer.writerow([serial, title, address, year, block, unit, room, dire[info[0]], info[1]])
                # print('户室号：%d 朝向：%s 面积：%d' % (room, dire[info[0]], info[1]))

    unit_continue = input('是否需要输入下一个单元？按 n 停止单元输入，按其他任意键继续：')
    if unit_continue == 'n':
        unit_loop = False
    else:
        unit_loop = True

print('恭喜你，资产录入工作完成！')

# for k, v in sub_dict.items():
#     print(k)
#     print(v[0])
# for k, v in unit_rooms.items():
#     for a, b in v.items():
#         print(a)
#         print(b)
