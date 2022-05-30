# coding = utf-8

# 定义元素
from appium.webdriver.webdriver import WebDriver
from page.renthouse_del_page import RentHouseDelPage
from page.base_page import BasePage

'''
租房-列表
'''


class RentHouseListPage(BasePage):
    # 租房列表元素
    total_house = ('id', 'com.lizihang.powerapp:id/tvAllNum')  # 项目统计
    rent_houses = ('id', 'com.lizihang.powerapp:id/ll_root')  # 二手房列表-房源

    _driver: WebDriver

    # def __init__(self, driver):
    #     self._driver = driver

    # 获得统计字段
    def get_total_project(self) -> str:
        return self.my_find_element(*self.total_house)

    # 获得列表第一个房源
    def get_list_one(self):
        return self.my_find_elements(*self.rent_houses)[0]

    # 进入租房详情
    def go_renthouse_del(self):
        self.get_list_one().click()
        return RentHouseDelPage(self._driver)
