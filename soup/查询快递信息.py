import time
# 从selenium库中调用webdriver模块
from selenium import webdriver
from selenium.webdriver.chrome.options import Options  # 从options模块中调用Options类
import base64
from PIL import Image
import pytesseract

# from 使用IP代理模拟浏览器头 import reptile_header
#
#
# # 快递公司名称（使用拼音全拼）
# courier_services_company = input('请输入快递公司名称（拼音全拼）：')    # shentong
# # 快递单号

courier_number = input('请输入您要查询快递单号：')  # 773075149142325
# # 设置要爬取的网址前半部分
# search_url = 'https://www.kuaidi100.com/query'
# # 网址参数
# params = {
#     'type': courier_services_company,
#     'postid': courier_number,
#     'temp': 0.5413571223018698,
#     'phone': ''
# }

# im = Image.open("test.png")
#
# # 将tesseract安装路径添加到系统变量中
# # 或者使用以下注释代码，路径改成自己的OCR引擎安装路径
# # pytesseract.pytesseract.tesseract_cmd = r"F:\Python\tesseract-ocr\tesseract.exe"
#
# code = pytesseract.image_to_string(im)
#
# print(code)

chrome_options = Options()  # 实例化Option对象
chrome_options.add_argument('--headless')  # 把Chrome浏览器设置为静默模式
driver = webdriver.Chrome(options=chrome_options)  # 设置引擎为Chrome，在后台默默运行

datetime_list = []
content_list = []
query_code_list = []

# 快递公司名称（使用拼音全拼）
# courier_services_company = input('请输入快递公司名称（拼音全拼）：')    # shentong
# 快递单号
# courier_number = input('请输入您要查询快递单号：')  # 773075149142325

# 设置引擎为Chrome，真实地打开一个Chrome浏览器
# driver = webdriver.Chrome()
# 访问页面
search_url = 'https://www.kuaidi100.com/'
driver.get(url=search_url)
# 暂停两秒，等待浏览器缓冲
time.sleep(1)

# 获取完整渲染的网页源代码
pageSource = driver.page_source
# 打印pageSource
# print(pageSource)
# 找到【输入快递单号】的输入框位置，智能识别快递           # 75428736656459
content = driver.find_element_by_id('input')  # 4311611531753
# 输入要查询的快递单号                # YT5168019271225
content.send_keys(courier_number)  # 4311555994270
# 找到【查快递按钮】                 # 557039665309774
button = driver.find_element_by_class_name('button')  # 78168164165920
# 点击【查快递】按钮
button.click()
time.sleep(1)
# 找到【快递信息内容】的位置
datetime = driver.find_elements_by_class_name('datetime')
text = driver.find_elements_by_class_name('text')
# 获取小程序二维码，微信扫一扫 实时跟踪物流更新
query_codes = driver.find_elements_by_css_selector('img')
# 查询错误
error = driver.find_element_by_class_name('error-text').text

try:
    # 如果error为空则正常在快递100中查询，否则进入中通官网查询
    if not error:
        for data in datetime:
            data_time = data.text.replace('\n', ' ')
            datetime_list.append(data_time)
            # print(datetime_list)
        for contents in text:
            content_text = contents.text
            # print(content_text)
            content_list.append(content_text)
            # print(content_list)
        for querycode in query_codes:
            query_code = querycode.get_attribute('src')
            query_code_list.append(query_code)

        for i in range(len(datetime_list)):
            # 打印出快递信息
            print(
                '-----------------------------------------------------------------------------------------------------')
            print('时间：' + datetime_list[i])
            print('地点和跟踪进度：' + content_list[i + 4])

    else:
        zhongtong_url = 'https://www.zto.com/guestservice/bill'
        driver.get(url=zhongtong_url)
        # 暂停两秒，等待浏览器缓冲
        time.sleep(1)

        # 获取完整渲染的网页源代码
        zhongtong_html = driver.page_source
        # print(zhongtong_html)
        # 找到【输入快递单号】的输入框位置
        query_txt = driver.find_element_by_class_name('query_txt')
        # 输入要查询的快递单号
        query_txt.send_keys(courier_number)
        # 找到【查询按钮】
        button = driver.find_element_by_class_name('search_btn')
        # 点击【查快递】按钮
        button.click()
        time.sleep(0.2)
        # 找到【图片验证码】的位置
        verification_img = driver.find_element_by_id('verificationImg')
        # 获取验证码的网址路径
        qr_code_src = verification_img.get_attribute('src')
        # 设置引擎为Chrome，真实地打开一个Chrome浏览器
        drive = webdriver.Chrome()
        drive.get(url=qr_code_src)
        with open('./images/1.png', 'wb') as file:
            print(qr_code_src)
            surl1 = base64.b64decode(qr_code_src[21:])
            file.write(surl1)

        time_list = []
        text_list = []
        # qr_code_src.click()
        auth_code = input('人肉输入验证码：')
        # 找到【验证码输入框】的位置
        verificationTxt = driver.find_element_by_id('verificationTxt')
        # 输入文字
        verificationTxt.send_keys(auth_code)
        # 找到【去定按钮】的位置
        verificationSubmit = driver.find_element_by_id('verificationSubmit')
        # 点击【确定】按钮
        verificationSubmit.click()
        time.sleep(0.3)
        # 找到【快递信息的位置】
        branch = driver.find_elements_by_class_name('branch-item')
        for item in branch:
            times = item.find_element_by_class_name('branch-time')
            texts = item.find_element_by_class_name('branch-text')
            time_list.append(times.text)
            text_list.append(texts.text)
        # print(time_list)
        # print(text_list)
        for j in range(len(time_list)):
            # 打印出快递信息
            print(
                '-----------------------------------------------------------------------------------------------------')
            print('时间：' + time_list[j])
            print('地点和跟踪进度：' + text_list[j])

        # def clear_image(image):
        #     image = image.convert('RGB')
        #     width = image.size[0]
        #     height = image.size[1]
        #     noise_color = get_noise_color(image)
        #
        #     for x in range(width):
        #         for y in range(height):
        #             # 清除边框和干扰色
        #             rgb = image.getpixel((x, y))
        #             if (x == 0 or y == 0 or x == width - 1 or y == height - 1
        #                     or rgb == noise_color or rgb[1] > 100):
        #                 image.putpixel((x, y), (255, 255, 255))
        #     return image
        #
        #
        # def get_noise_color(image):
        #     for y in range(1, image.size[1] - 1):
        #         # 获取第2列非白的颜色
        #         (r, g, b) = image.getpixel((2, y))
        #         if r < 255 and g < 255 and b < 255:
        #             return r, g, b
        #
        #
        # image = Image.open('./images/1.png')
        # # image.save('./images/ocr.png')
        # # image = clear_image(image)
        # # 转化为灰度图
        # imgry = image.convert('L')
        # code = pytesseract.image_to_string(imgry)
        #
        # imgry.save('./images/new.png')
        # with open('./images/code.txt', "w") as f:
        #     print(code)
        #     f.write(str(code))

        drive.close()

    print(
        '*************************************************************************************************************')
    print('微信扫一扫 实时跟踪物流更新图片链接:' + query_code_list[8])
    print(
        '*************************************************************************************************************')
    # 关闭浏览器
    driver.close()


# except IndexError:
#     print('包裹正在等待揽收！')
# except Exception as result:
#     print('捕捉到异常：%s' % result)
except:
    print('您的包裹正在等待揽收，请稍后再进行查询！')
# # 快递查询  1447602156892420526
# express_check_url = reptile_header(url=search_url, params=params)
# # 打印状态码
# print(express_check_url.status_code)
# # 快递信息
# express_information = express_check_url.json()
# print(express_information)
# # 找到快递信息在那一层
# information = express_information['data']
# print(information)
# # 循环遍历取出时间、内容
# for info in information:
#     # 时间
#     time = info['time']
#     print('时间：' + time)
#     # 快递去向内容
#     content = info['context']
#     print('地点和跟踪进度：' + content)
