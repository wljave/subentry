import requests
from bs4 import BeautifulSoup


def main():
    for i in range(20):
        # 定义要爬取的网页链接
        url = 'http://www.xiachufang.com/explore/?page=%d' % (i + 1)
        # 0.模拟浏览器请求数据
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/87.0.4280.88 Safari/537.36 '
        }
        res = requests.get(url, headers=headers)
        res.encoding = 'utf-8'
        # 检查状态码是否正常
        print('第%d次，状态码：%d' % (i+1, res.status_code) + '\n')
        # 1.以网页源代码的格式获取数据
        html = res.text
        # 2.解析数据
        soup = BeautifulSoup(html, 'html.parser')
        # 3.提取数据
        items = soup.find_all(class_='pure-u-3-4 search-result-list')
        # 定义列表用来保存遍历后的所有的菜名、所有的URL、所有的食材
        menu_pic_list = []  # 展示图片
        menu_name_list = []  # 所有的菜名
        menu_materials_list = []  # 所有的食材
        menu_url_list = []  # 所有的URL
        # 遍历items获取想要的数据
        for item in items:
            # 菜图片
            picture = item.find_all(class_='cover pure-u')
            for pic in picture:
                menu_pic = pic.find('img')['data-src']
                menu_pic_list.append(menu_pic)
            # 标题
            title = item.find(class_='page-title').text
            # 菜名
            menu_name = item.find_all('p', class_='name')
            for name in menu_name:
                menu_name_list.append(name.text.strip())
            # print(menu_name_list)
            # print('菜名：' + name.text.strip())
            # 所需材料
            menu_materials = item.find_all(class_='ing ellipsis')
            for materials in menu_materials:
                menu_materials_list.append(materials.text.strip())
            # print(menu_materials_list)
            # print('所需材料：' + materials.text.strip())
            # 菜名所对应的详情页URL

            for urls in menu_name:
                menu_url = urls.find('a')['href']
                menu_url_list.append(menu_url)
            # print(menu_url_list)
            print('标题：' + title.strip() + '，第%d页' % (i+1) + '\n')
            for j in range(len(menu_name_list)):
                print('图片：' + menu_pic_list[j])
                print('菜名：' + menu_name_list[j])
                print('所需材料：' + menu_materials_list[j])
                print('详情页链接：' + 'https://www.xiachufang.com' + menu_url_list[j] + '\n')
    print('下载完成！')


if __name__ == '__main__':
    main()

# # 引用requests库
# import requests
# # 引用BeautifulSoup库
# from bs4 import BeautifulSoup
#
# url = 'http://www.xiachufang.com/explore/'
# # 0.模拟浏览器请求数据
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
#                   'Chrome/87.0.4280.88 Safari/537.36 '
# }
#
# # 获取数据
# res_foods = requests.get(url, headers=headers)
# # 解析数据
# bs_foods = BeautifulSoup(res_foods.text, 'html.parser')
# # 查找最小父级标签
# list_foods = bs_foods.find_all('div', class_='info pure-u')
#
# foods_list = []
#
# for item in list_foods:
#     foods_name = item.find('p', class_='name').text.strip()
#     food_materials = item.find(class_='ing ellipsis').text.strip()
#     foods_url = item.find('a')['href']
#     # foods_list.append(foods_name)
#     # foods_list.append(food_materials)
#     # foods_list.append('https://www.xiachufang.com' + foods_url)
#     foods_list.append([foods_name, food_materials, 'https://www.xiachufang.com' + foods_url])
# print(foods_list)
# for i in range(len(foods_list)):
#     print('菜名：' + foods_list[i][0])
#     print('所需材料：' + foods_list[i][1])
#     print('详情页链接：' + 'https://www.xiachufang.com' + foods_list[i][2])


# # 引用requests库
# import requests
# # 引用BeautifulSoup库
# from bs4 import BeautifulSoup
# 
# url = 'http://www.xiachufang.com/explore/'
# # 0.模拟浏览器请求数据
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
#                   'Chrome/87.0.4280.88 Safari/537.36 '
# }
#
# # 获取数据
# res_foods = requests.get(url, headers=headers)
# # 解析数据
# bs_foods = BeautifulSoup(res_foods.text, 'html.parser')
# # 查找最小父级标签
# list_foods = bs_foods.find_all('div', class_='info pure-u')
#
# foods_list_all = []
#
# for item in list_foods:
#     foods_name = item.find('p', class_='name').text.strip()
#     food_materials = item.find(class_='ing ellipsis').text.strip()
#     foods_url = item.find('a')['href']
#     foods_list = [foods_name, food_materials, 'https://www.xiachufang.com' + foods_url]
#     foods_list_all.append(foods_list)
# print(foods_list_all)
# for i in range(len(foods_list_all)):
#     print('菜名：' + foods_list_all[i][0])
#     print('所需材料：' + foods_list_all[i][1])
#     print('详情页链接：' + foods_list_all[i][2])

