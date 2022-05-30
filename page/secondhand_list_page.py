# coding = utf-8

# 定义元素
import time

from appium.webdriver import WebElement
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

from page.base_page import BasePage
from page.secondhand_del_page import SecondHandDelPage
'''
二手房列表页
'''


class SecondHandListPage(BasePage):
    # 二手房列表元素
    secondhand_search_edit = (MobileBy.ID, 'com.lizihang.powerapp:id/edit')  # 二手房列表搜索输入框
    secondhand_search_button = (MobileBy.ID, 'com.lizihang.powerapp:id/search')  # 二手房列表搜索按钮
    secondhand_option_city = (MobileBy.ID, 'com.lizihang.powerapp:id/dropDownMenu0')  # 二手房列表-城区筛选
    secondhand_option_price = (MobileBy.ID, 'com.lizihang.powerapp:id/dropDownMenu1')  # 二手房列表-价格筛选
    secondhand_option_room = (MobileBy.ID, 'com.lizihang.powerapp:id/dropDownMenu2')  # 二手房列表-居室筛选
    secondhand_option_more = (MobileBy.ID, 'com.lizihang.powerapp:id/dropDownMenu3')  # 二手房列表-更多筛选
    secondhand_option_order = (MobileBy.ID, 'com.lizihang.powerapp:id/dropDownMenu4')  # 二手房列表-排序

    total_house = (MobileBy.ID, 'com.lizihang.powerapp:id/tvAllNum')  # 项目统计
    secondhand_houses = (MobileBy.ID, 'com.lizihang.powerapp:id/ll_root')  # 二手房列表-房源

    _driver: WebDriver

    # def __init__(self, driver):
    #     self._driver = driver

    # 获得统计字段
    def get_total_project(self) -> WebElement:
        return self.my_find_element(*self.total_house)

    # 获得列表数据第一个
    def get_list_one(self) -> list:
        return self.my_find_elements(*self.secondhand_houses)[0]

    # 进入第一个房源的详情
    def go_secondhand_del(self):
        self.get_list_one().click()
        return SecondHandDelPage(self._driver)


