# coding = utf-8

# 定义元素
from appium.webdriver.webdriver import WebDriver
from page.base_page import BasePage
from page.shyrent_del_page import SiheyuanRentDelPage

'''
四合院租赁列表
'''


class SiheyuanRentListPage(BasePage):
    # 四合院列表元素
    siheyuan_rent_houses = ('id', 'com.lizihang.powerapp:id/ll_root')  # 四合院租赁列表详情ID
    total_house = ('id', 'com.lizihang.powerapp:id/tvAllNum')  # 项目统计

    _driver: WebDriver

    # def __init__(self, driver):
    #     self._driver = driver

    # 获得统计字段
    def get_total_house(self) -> str:
        return self.my_find_element(*self.total_house)

    # 获得列表数据第一个
    def get_list_one(self) -> list:
        return self.my_find_elements(*self.siheyuan_rent_houses)[0]

    # 进入第一个房源的详情
    def go_shyrent_del(self):
        self.get_list_one().click()
        return SiheyuanRentDelPage(self._driver)
