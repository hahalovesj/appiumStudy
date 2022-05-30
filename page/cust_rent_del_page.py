# coding = utf-8

# 定义元素
from appium.webdriver import WebElement
from appium.webdriver.webdriver import WebDriver

from page.base_page import BasePage
from page.loupan_del_page import LoupanDelPage
'''
求购客源详情
'''


class CustRentDelPage(BasePage):
    # 求购客源元素
    # 客户姓名
    cust_rent_name = ('id', 'com.lizihang.powerapp:id/tv_customername')
    # 客源编码
    cust_rent_code = ('id', 'com.lizihang.powerapp:id/tv_custCode')

    _driver: WebDriver

    # 获得姓名
    def get_cust_name(self) -> WebElement:
        return self.my_find_element(*self.cust_rent_name)

    # 获得客源编码
    def get_cust_code(self) -> WebElement:
        return self.my_find_element(*self.cust_rent_code)



