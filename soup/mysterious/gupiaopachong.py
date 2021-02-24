import requests
import re
import pandas as pd


# 用get方法访问服务器并提取页面数据
def getHtml(cmd, page):
    url = "http://nufm.dfcfw.com/EM_Finance2014NumericApplication/JS.aspx?cb=jQuery112406115645482397511_1542356447436&type=CT&token=4f1862fc3b5e77c150a2b985b12db0fd&sty=FCOIATC&js=(%7Bdata%3A%5B(x)%5D%2CrecordsFiltered%3A(tot)%7D)&cmd=" + cmd + "&st=(ChangePercent)&sr=-1&p=" + str(
        page) + "&ps=20"
    r = requests.get(url)
    pat = "data:\[(.*?)\]"
    data = re.compile(pat, re.S).findall(r.text)
    return data


# 获取单个页面股票数据
def getOnePageStock(cmd, page):
    data = getHtml(cmd, page)
    datas = data[0].split('","')
    stocks = []
    for i in range(len(datas)):
        stock = datas[i].replace('"', "").split(",")
        stocks.append(stock)
    return stocks


def main():
    cmd = {
        "上证指数": "C.1",
        "深圳指数": "C.5",
        "沪深A股": "C._A",
        "上证A股": "C.2",
        "深圳A股": "C._SZAME",
        "新股": "C.BK05011",
        "中小板": "C.13",
        "创业板": "C.80"
    }
    for i in cmd.keys():
        page = 1
        stocks = getOnePageStock(cmd[i], page)
        # 自动爬取多页，并在结束时停止
        while True:
            page += 1
            if getHtml(cmd[i], page) != getHtml(cmd[i], page - 1):
                stocks.extend(getOnePageStock(cmd[i], page))
                # print(i+"已加载第"+str(page)+"页")
            else:
                break

        df = pd.DataFrame(stocks)
        # 提取主要数据/提取全部数据
        # df.drop([0,14,15,16,17,18,19,20,21,22,23,25],axis=1,inplace=True)
        columns = {1: "代码", 2: "名称", 3: "最新价格", 4: "涨跌额", 5: "涨跌幅", 6: "成交量", 7: "成交额", 8: "振幅", 9: "最高", 10: "最低",
                   11: "今开", 12: "昨收", 13: "量比", 24: "时间"}
        df.rename(columns=columns, inplace=True)
        df.to_excel("股票/" + i + ".xls")
        print("已保存" + i + ".xls")


main()
