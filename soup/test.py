import time
import datetime
# timeStamp = 1603015446
timeStamp = 1603015446
# timeArray = time.localtime(timeStamp)
# otherStyleTime = time.strftime('%Y-%m-%d %H:%M:%S', timeArray)
# # otherStyleTime = time.time()
# print(otherStyleTime)

# 时间戳转化成时间格式
Time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timeStamp))
print(Time[:4] + '年' + Time[5:7] + '月' + Time[8:10] + '日' + Time[10:])
print('┝ 评论：%s' % (Time[:4] + '年' + Time[5:7] + '月' + Time[8:10] + '日' + Time[10:]))
print('昵称：AK47' + '  ━  时间：2020年10月22日 11:33:45' + '  ━  点赞量：500')

print('**********************************************************************************')
print('Python中None,False,0,[],{},(),\'\'都相当于False')
print('可以使用is或is not或 not来准确区分')
a = 'j'
b = 'shenzhen'

# 如果a=0,值=b;如果a!=0,值=a
if a or b:
    print('我是a:' + str(a))
    print('我是b:' + b)
# 如果a=0,值=a;如果a!=0,值=b
if a and b:
    print('我是a:' + str(a))
    print('我是b:' + b)
if not a:
    print('我是not a,' + 'True')
if a is False:
    print('a不为真')
if a is not None:
    print('None 不为空')
if a is not False:
    print('False 不为空')
if a is not 0:
    print('0 不为空')
if a is []:
    print('[] 不为空')
if a is not []:
    print('我是：is not []')
if a is not {}:
    print('{} 不为空')
if a is not ():
    print('() 不为空')
if a is not '':
    print('\'\' 不为空')
print('-------------------------------------------------')
print('in关键字，可用于字符串、列表元素、字典键值判断')

my_lists = list(b)
my_dic = {'a': 1, 'b': 2, 'c': 3}
print(b)
print(my_lists)
if 's' in b:
    print('s在b中')
if 'z' in my_lists:
    print('z在b列表中')
if 'c' in my_dic:
    print('c在字典中')

m = 130
n = 25
k = m // n + 1
# print(k)
# for i in range(k):
#     print(i)
# h = [5, 2, 3, 4, 5, 6, 7]
# for se in h:
#     o = h[se]
#     print(o)
# p = 5
# for i in range(p):
#     print(i)
# print(i)

for t in range(0, 14, 2):
    print('原来的数：' + str(t))
    t += 1
    print('加1之后的数：' + str(t))

# date_time = datetime.datetime.now().strftime("%Y-%m-%d")
date_time = '2020-11-02'
date_time2 = ['2020-12-15', '2021-01-15']
if date_time[5] == '1':
    times = date_time[:4] + '年' + date_time[5:7] + '月' + date_time[8:10] + '日'
else:
    times = date_time[:4] + '年' + date_time[6:7] + '月' + date_time[8:10] + '日'
print(times)
date_time2[:] = []
print(date_time2)
print(type(date_time2))
data_times = time.time()
print(data_times)
