# coding = utf-8
import datetime
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
# 冒号：官方叫做参数的类型建议符
# 箭头：叫做函数返回值的类型建议符


class BasePage:

    def __init__(self, driver: webdriver = None):
        if driver is None:
            capabilities = {
                # CFM7N18A18000471 华为p20pro，夜神模拟器127.0.0.1:62001
                "deviceName": "j7vkoveucu7temkj",  # D5F7N18525004066，CFM7N18A18000471
                "platformName": "Android",
                # "app": "C:\\Users\\shenjing\\Desktop\\PowerApp.apk",
                "appPackage": "com.lizihang.powerapp",
                "appActivity": "com.lizihang.powerapp.activities.SplashActivity",
                "unicodeKeyboard": "True",  # 使用unicode编码方式发送字符串
                "resetKeyboard": "True",  # 将键盘隐藏起来
                "noReset": "True"
            }

            self._driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", capabilities)
            self._driver.implicitly_wait(6)
            # print("新driver创建成功")
        else:
            self._driver = driver
            # print("driver已经存在，直接复用")

    def get_size(self):
        size = self._driver.get_window_size()
        width = size["width"]
        height = size["height"]
        return width, height

    # 向上滑动页面
    def swipe_up(self):
        try:
            width = self.get_size()[0]
            height = self.get_size()[1]
            self._driver.swipe(int(width)/2, int(height)/4, int(width)/2, int(height)/2, 1000)
            print("向上滑动")
        except:
            print("向上滑动失败")
            self.screenshot()

    # 向下滑动页面
    def swipe_down(self):
        try:
            width = self.get_size()[0]
            height = self.get_size()[1]
            # 下滑
            self._driver.swipe(int(width)/2, int(height)/2, int(width)/2, int(height)/5, 1000)
            print("向下滑动")

        except:
            print("向下滑动失败")
            self.screenshot()

    # # 登录app
    # def go_login(self):
    #     self.driver.find_element_by_id('com.lizihang.powerapp:id/et_id').send_keys('BJ30007108')
    #     self.driver.find_element_by_id('com.lizihang.powerapp:id/et_pwd').send_keys('807518')
    #     self.driver.find_element_by_id('com.lizihang.powerapp:id/tv_login').click()

    # 等待元素可见
    def wait_element_located(self, locator):
        try:
            # print("可见元素等到了")
            return WebDriverWait(self._driver, 20, 0.5).until(EC.visibility_of_element_located(locator))

        except:
            self.screenshot()
            print("可见元素没等到!")

    # 等待元素可点击
    def wait_element_clickable(self, locator):
        try:
            # print("可点击元素等到了")
            return WebDriverWait(self._driver, 20, 0.5).until(EC.element_to_be_clickable(locator))

        except:
            self.screenshot()
            print("可点击元素没等到!")

    # 查找元素
    def my_find_element(self, *element):
        try:
            # 这里的*element是为了将element元组拆开，因为find_element要传递两个参数
            # print("元素找到了")
            return self._driver.find_element(*element)
        except Exception as e:
            self.screenshot()  # 截图
            print("my_find_element--元素没找到")

    # 查找多个元素
    def my_find_elements(self, *element):
        try:
            # 这里的*element是为了将element元组拆开，因为find_element要传递两个参数
            # print("元素找到了")
            return self._driver.find_elements(*element)
        except:
            self.screenshot()
            print("my_find_elements--元素列表没找到")

    # 获得元素文本
    def find_ele_text(self, *element):
        try:
            return self.my_find_element(*element).text
        except:
            print("元素文本没找到")

    # 查找并点击元素
    def find_and_click(self, *element):
        try:
            # 这里的*element是为了将element元组拆开，因为find_element要传递两个参数
            self._driver.find_element(*element).click()
            # print("元素点到了")
        except:
            self.screenshot()
            print("元素没点到")

    # 输入信息
    def send_keys(self, loc, value):
        try:
            self.my_find_element(*loc).send_keys(value)
        except:
            self.screenshot()
            print("输入信息失败")

    # 使用键盘的返回
    def go_back(self):
        self._driver.keyevent(4)

    # 切换到h5
    def switch_to_h5(self):
        # 原生切换H5
        contexts = self._driver.contexts
        # print(contexts)
        for cont in contexts:
            if cont == "WEBVIEW_com.lizihang.powerapp":
                self._driver.switch_to.context(cont)
                # print(self._driver.current_context)
                print("切换到H5")

    # 切换到原生
    def switch_to_native(self):
        # 原生切换H5
        contexts = self._driver.contexts
        # print(contexts)
        for cont in contexts:
            if cont == "NATIVE_APP":
                self._driver.switch_to.context(cont)
                # print(self._driver.current_context)
                print("切换到原生")
    # 截图方法
    def screenshot(self):
        try:
            now_time = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')  # 现在
            file_name = str(now_time) + '.png'
            self._driver.get_screenshot_as_file(r'../screenshot/%s' % file_name)
            print("截图啦！")
        except:
            print("截图失败！")

    # 退出driver
    def quite_driver(self):
        self._driver.quit()
        print("退出啦！")
