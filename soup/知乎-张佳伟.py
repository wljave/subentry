import time
import requests
# ************本地Chrome浏览器的静默默模式设置：**************
from bs4 import BeautifulSoup
from selenium import webdriver  # 从selenium库中调用webdriver模块
from selenium.webdriver.chrome.options import Options  # 从options模块中调用Options类

chrome_options = Options()  # 实例化Option对象
chrome_options.add_argument('--headless')  # 把Chrome浏览器设置为静默模式
driver = webdriver.Chrome(options=chrome_options)  # 设置引擎为Chrome，在后台默默运行


def zhihu(url, params):
    headers = {
        'User-Agent': 'Mozilla/5.0(Windows NT 6.1;Win64;x64) AppleWebKit/537.36(KHTML,like Gecko)Chrome/87.0.4280.88 Safari/537.36 ',
        'referer': 'https://www.zhihu.com/people/zhang-jia-wei/posts',
        'cookie': 'd_c0="APBjRShgnhCPTuXlfXfqQZIM0mbgdKj4E_w=|1578286314";',
        'x-requested-with': 'fetch',
        'x-zse-83': '3_2.0',
        'x-zse-86': '1.0_xy2AUqc_Nx6R2qGLtyk6e0eLSY20xyM7Y0eAUBHqNp',
    }
    # 设置代理IP
    proxy = '171.97.15.9:8080'
    proxies = {
        'http': 'https://' + proxy,
    }
    res = requests.get(url=url, proxies=proxies, headers=headers, params=params)
    return res


def one(params):
    url = 'https://www.zhihu.com/people/zhang-jia-wei/posts'
    # 判断状态码是否正常
    page_one = zhihu(url=url, params=params)
    print(page_one.status_code)
    page_one.encoding = 'utf-8'
    # 1以网页源代码的格式获取数据
    html = page_one.text
    # 2解析数据
    soup = BeautifulSoup(html, 'html.parser')
    # 3提取数据
    zhihu_data = soup.find_all('div', class_='List-item')
    # print(zhihu_data)
    for item in zhihu_data:
        # 文章标题
        title = item.find(class_='ContentItem-title')
        # 头像信息
        head = item.find('a', class_='UserLink-link')
        # 你是谁，你的头像是什么src，你的知乎页面地址是什么href，你是谁alt，
        who = head.find('img')['alt']
        href = head['href']
        image = head.find('img')['src']
        # 点赞人数
        number_peoples = item.find(class_='ArticleItem-extraInfo').text[:-8]
        # 文章内容
        content = item.find('span', itemprop="articleBody").text

        print('作者是：' + who)
        print('知乎链接是：' + 'https:' + href)
        print('头像链接是：' + image)
        print('发表的文章标题：' + title.text)
        print('点赞人数：' + number_peoples)
        print('文章内容：' + content)


for i in range(2):
    params = {'page': i + 1}
    one(params)
    i += 1


def back(param):
    href = 'https://www.zhihu.com/api/v4/members/zhang-jia-wei/articles'
    req = zhihu(url=href, params=param)
    print(req.status_code)
    req.encoding = 'utf-8'
    # 1以网页源代码的格式获取数据
    html = req.text
    # 2解析数据
    soup = BeautifulSoup(html, 'html.parser')  # 使用bs解析网页
    print(soup)
    # 3提取数据
    back_data = soup.find_all('div', class_='ContentItem ArticleItem')
    print(len(back_data))
    # print(back_data)
    for item in back_data:
        # 文章标题
        title = item.find(class_='ContentItem-title')
        # 头像信息
        head = item.find('a', class_='UserLink-link')
        # 你是谁，你的头像是什么src，你的知乎页面地址是什么href，你是谁alt，
        who = head.find('img')['alt']
        href = head['href']
        image = head.find('img')['src']
        # 点赞人数
        number_peoples = item.find(class_='ArticleItem-extraInfo').text[:-8]
        # 文章内容
        content = item.find('span', itemprop="articleBody").text

        print('-----------------------------------------------------------------------------------')
        print('作者是：' + who)
        print('知乎链接是：' + 'https:' + href)
        print('头像链接是：' + image)
        print('发表的文章标题：' + title.text)
        print('点赞人数：' + number_peoples)
        print('文章内容：' + content)


param = {
    'include': 'data[*].comment_count,suggest_edit,is_normal,thumbnail_extra_info,thumbnail,can_comment,comment_permission,admin_closed_comment,content,voteup_count,created,updated,upvoted_followees,voting,review_info,is_labeled,label_info;data[*].author.badge[?(type=best_answerer)].topics',
    'offset': '30',
    'limit': '10',
    'sort_by': 'created',
    # 'sort_by': 'voteups',
}


def article():
    # href = 'https://www.zhihu.com/api/v4/members/zhang-jia-wei/articles'
    # req = zhihu(url=href, params=param)
    # print(req.status_code)
    print('********************************************************')
    href = 'https://www.zhihu.com/people/zhang-jia-wei/posts'
    driver.get(url=href)
    # 反爬虫-比如淘宝
    script = 'Object.defineProperty(navigator,"webdriver",{get:() => false,});'
    # 运行Javascript
    driver.execute_script(script)
    time.sleep(2)
    pageSource = driver.page_source  # 获取Elements中渲染完成的网页源代码
    soup = BeautifulSoup(pageSource, 'html.parser')  # 使用bs解析网页
    # print(soup)
    # 3提取数据
    zhihu_data = soup.find_all('div', class_='ContentItem ArticleItem')
    print(len(zhihu_data))
    # print(zhihu_data)
    for item in zhihu_data:
        # 文章标题
        title = item.find(class_='ContentItem-title')
        # 头像信息
        head = item.find('a', class_='UserLink-link')
        # 你是谁，你的头像是什么src，你的知乎页面地址是什么href，你是谁alt，
        who = head.find('img')['alt']
        href = head['href']
        image = head.find('img')['src']
        # 点赞人数
        number_peoples = item.find(class_='ArticleItem-extraInfo').text[:-8]
        # 文章内容
        content = item.find('span', itemprop="articleBody").text

        print('-----------------------------------------------------------------------------------')
        print('作者是：' + who)
        print('知乎链接是：' + 'https:' + href)
        print('头像链接是：' + image)
        print('发表的文章标题：' + title.text)
        print('点赞人数：' + number_peoples)
        print('文章内容：' + content)


# param = {
#     'include': 'data[*].comment_count,suggest_edit,is_normal,thumbnail_extra_info,thumbnail,can_comment,comment_permission,admin_closed_comment,content,voteup_count,created,updated,upvoted_followees,voting,review_info,is_labeled,label_info;data[*].author.badge[?(type=best_answerer)].topics',
#     'offset': '10',
#     'limit': '10',
#     # 'sort_by': 'created',
#     'sort_by': 'voteups',
# }

article()
back(param)
