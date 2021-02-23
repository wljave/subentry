# 请根据所学，补全一下代码：

class Calendar:
    # 日程安排的日期
    date = '2020-08-08'
    # 时间清单，以字典形式给出，键位事件，值为安排的时间
    things = {'给父母买礼物': '9:00', '学习': '10:00', '和朋友聚会': '18:30'}

    @classmethod
    def thing_done(cls, thing):
        # for i in cls.things:
        #     print('{}: {}'.format(i, cls.things[i]))
        print('{}: {}'.format(thing, cls.things[thing]))
        del cls.things[thing]

    @classmethod
    def add_thing(cls, thing, time):
        cls.things[thing] = time


Calendar.thing_done('给父母买礼物')
Calendar.add_thing('写日记', '20:00')
print(Calendar.things)
