import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ChromeOptions
from selenium.webdriver import ActionChains


class TaobaoSpider:
    driver = None
    login_url = 'https://login.taobao.com/member/login.jhtml'
    index_url = 'https://taobao.com/'

    def __init__(self, username, password):
        options = ChromeOptions()
        # 不加载图片,加快访问速度
        # options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})
        # 设置为开发者模式，避免被识别
        options.add_experimental_option('excludeSwitches', ['enable-automation'])
        # 使用代理
        options.add_argument('--proxy-server=http://127.0.0.1:9000')
        options.add_argument('disable-infobars')
        self.driver = webdriver.Chrome(executable_path='../chromedriver', options=options)
        self.username = username
        self.password = password

    def run(self):
        self._start_request()

    def _start_request(self):
        self.driver.get(url=self.login_url)
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="fm-login-id"]').send_keys(self.username)
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="fm-login-password"]').send_keys(self.password)
        time.sleep(1)

        # 是否出现滑动验证
        if self._lock_exist():
            self._unlock()

        # 点击登陆
        self.driver.find_element_by_xpath('//*[@id="login-form"]/div[4]/button').click()

        # 等待登陆成功
        WebDriverWait(self.driver, 600).until(EC.presence_of_element_located((By.XPATH, '//*[@id="mtb-nickname"]')))
        # 登陆成功
        self.driver.get(url=self.index_url)

    def _lock_exist(self):
        '''判断是否存在滑动验证'''
        try:
            self.driver.find_element_by_xpath('//*[@id="nocaptcha-password"][@style="display: block;"]')
            return True
        except Exception as err:
            return False

    def _unlock(self):
        bar_element = self.driver.find_element_by_id('nc_1_n1z')
        ActionChains(self.driver).drag_and_drop_by_offset(bar_element, 300, 0).perform()
        time.sleep(1.5)
        # 出现刷新按钮
        try:
            self.driver.find_element_by_xpath('//*[@id="nocaptcha-password"]/div/span/a').click()
            self._unlock()
        except Exception as err:
            print(err)
            raise Exception('滑动验证失败,被监测到了')

    def _parse(self):
        pass


if __name__ == "__main__":
    username = input("请输入你的淘宝用户名:")
    password = input("请输入密码:")

    spider = Taobao(username, password)
    spider.run()