# coding = utf-8

# 定义元素
from appium.webdriver import WebElement
from appium.webdriver.webdriver import WebDriver

from page.base_page import BasePage
from page.cust_buy_del_page import CustBuyDelPage
from page.loupan_del_page import LoupanDelPage


class CustBuyListPage(BasePage):
    # 求购客源元素
    # 搜索框
    cust_buy_search_edit = ('id', 'com.lizihang.powerapp:id/et')
    # 求购列表
    cust_buy_lists = ('id', 'com.lizihang.powerapp:id/rl_root')
    # 统计记录
    total_cust = ('id', 'com.lizihang.powerapp:id/tv_statics')

    _driver: WebDriver

    # 获得统计字段
    def get_total_house(self) -> WebElement:
        return self.my_find_element(*self.total_project)

    # 获得列表数据第一个
    def get_list_one(self) -> list:
        self.wait_element_located(self.cust_buy_lists)
        return self.my_find_elements(*self.cust_buy_lists)[0]

    # 进入楼盘攻略详情
    def go_custbuydel_page(self):
        self.get_list_one().click()
        return CustBuyDelPage(self._driver)
