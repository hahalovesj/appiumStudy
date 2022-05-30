# coding = utf-8

# 定义元素
from time import sleep

from appium.webdriver import WebElement
from appium.webdriver.webdriver import WebDriver

from page.base_page import BasePage
from page.loupan_del_page import LoupanDelPage
'''
成交客源详情
'''


class DealCustBuyDelPage(BasePage):
    # 求购客源元素
    # 客户姓名
    deal_cust_buy_name = ('id', 'com.lizihang.powerapp:id/tv_customername')
    # 客源编码
    deal_cust_buy_code = ('id', 'com.lizihang.powerapp:id/tv_custCode')

    _driver: WebDriver

    # 获得姓名
    def get_cust_name(self) -> WebElement:
        self.wait_element_located(self.deal_cust_buy_name).text
        return self.my_find_element(*self.deal_cust_buy_name)

    # 获得客源编码
    def get_cust_code(self) -> WebElement:
        return self.my_find_element(*self.deal_cust_buy_code).text



