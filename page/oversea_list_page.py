# coding = utf-8

# 定义元素
from appium.webdriver import WebElement
from appium.webdriver.webdriver import WebDriver

from page.base_page import BasePage
from page.oversea_del_page import OverseaDelPage


class OverseaListPage(BasePage):
    # 海外房产元素
    oversea_houses = ('id', 'com.lizihang.powerapp:id/oneLl')  # 海外房产ID

    total_project = ('id', 'com.lizihang.powerapp:id/tv_total')

    _driver: WebDriver

    # def __init__(self, driver):
    #     self._driver = driver

    # 获得统计字段
    def get_total_project(self) -> WebElement:
        return self.my_find_element(*self.total_project)

    # 获得列表数据第一个
    def get_list_one(self) -> list:
        return self.my_find_elements(*self.oversea_houses)[0]

    # 进入第一个房源的详情
    def go_oversea_del(self):
        self.get_list_one().click()
        return OverseaDelPage(self._driver)
