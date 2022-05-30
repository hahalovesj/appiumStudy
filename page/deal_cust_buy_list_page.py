# coding = utf-8

from appium import webdriver
from appium.webdriver import WebElement
from page.base_page import BasePage
from page.deal_cust_buy_del_page import DealCustBuyDelPage

'''
成交客-买卖列表
'''


class DealCustBuyListPage(BasePage):
    # 成交客源元素
    # 搜索框
    deal_cust_buy_search_edit = ('id', 'com.lizihang.powerapp:id/et')
    # 成交客列表，多个
    deal_cust_buy_lists = ('id', 'com.lizihang.powerapp:id/rlRoot')
    # 统计记录
    total_cust = ('id', 'com.lizihang.powerapp:id/tv_statics')

    _driver: webdriver

    # 获得统计字段
    def get_total_house(self) -> WebElement:
        return self.my_find_element(*self.total_cust)

    # 获得列表数据第一个
    def get_list_one(self) -> list:
        self.wait_element_located(self.deal_cust_buy_lists)
        return self.my_find_elements(*self.deal_cust_buy_lists)[0]

    # 进入成交客详情
    def go_dealcustbuy_del(self):
        self.get_list_one().click()
        return DealCustBuyDelPage(self._driver)
