a = [1, 8, 6, 15, 20, 35, 5, 7]
b = ['a', 'g', 'h', 'f', 'm']
print('{}{}'.format('列表a：', a))  # 输出：[1,8,6,15,20,35,5,7]
# 列表的排序
a.sort()  # 将列表中的元素按照特定的顺序重新排列
print(a)
a.reverse()  # 将列表逆置
print(a)
print('{}{}'.format('列表b：', b))  # 输出：['a','g','h','f','m']
print('{}{}'.format('提取索引为3的单个元素：', a[3]))  # 输出：15
print('{}{}'.format('获取列表所有元素：', a[:]))  # 输出：[1,8,6,15,20,35,5,7]
print('{}{}'.format('从列表索引为2的元素到列表结束的所有元素：', a[2:]))  # 输出：[6,15,20,35,5,7]
print('{}{}'.format('从列表开头第一个元素到列表索引为2的元素：', a[:2]))  # 输出：[1,8]
print('{}{}'.format('从列表索引为2到索引为5的元素：', a[2:5]))  # 输出：[6,15,20]
print('{}{}'.format('提取索引为-2的单个元素（倒数第二个元素）：', a[-2]))  # 输出：5
print('{}{}'.format('列表倒数2个元素：', a[-2:]))  # 输出：[5,7]
print('{}{}'.format('从列表开始至倒数第3个元素：', a[:-2]))  # 输出：[1,8,6,15,20,35]
# 【[a:b]a一定要比b大】
print('{}{}'.format('列表倒数2个至倒数第5个元素：', a[-2:-5]))  # 输出：[]
print('{}{}'.format('列表倒数3个至倒数第5个元素：', a[-5:-2]))  # 输出：[15,20,35]
# 添加列表元素
a.append(3)  # 在列表a的末尾添加元素3
print(a)  # 输出：[1,8,6,15,20,35,5,7，3]
k = a.pop()  # 删除列表a中的最后一个元素，并保存到k中
print(k)  # 输出：3
print(a)  # 输出：[1,8,6,15,20,35,5,7]
a.insert(5, k)  # 在索引值为5的位置将3插入a列表中(在指定位置插入数据)
print(a)  # 输出：[1,8,6,15,20,3，35,5,7]
a.extend(b)  # 将列表b插入至列表a的末尾
print(a)  # 输出：[1, 8, 6, 15, 20, 3, 35, 5, 7, 'a', 'g', 'h', 'f', 'm']

##for i in range(1,10):
##    for j in range(1,10):
##        print('{} * {} = {}\t'.format(i,j,i * j),end = '')
##        if i==j:
##            print('')
##            break

print('\n'.join([' '.join(["%2s ×%2s ＝ %2s" % (j, i, i * j) for j in range(1, i + 1)]) for i in range(1, 10)]))

print('-' * 30 + '1-9乘法表分割线' + '-' * 30)


class Multiplication_Table(object):
    def __init__(self):
        self.cn_num = {1: '一', 2: '二', 3: '三', 4: '四', 5: '五', 6: '六', 7: '七', 8: '八', 9: '九'}
        self.num = int(input('请输入1-9，生成乘法表：'))
        cn_num = self.cn_num[self.num]
        print('{}{}乘法表'.format(cn_num, cn_num))

    def printing(self):
        for i in range(1, self.num + 1):
            for j in range(1, i + 1):
                print('{} * {} = {}'.format(i, j, i * j), end='\t')
            print(' ')


threemt = Multiplication_Table()
threemt.printing()

