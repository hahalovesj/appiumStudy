# coding = utf-8

# 定义元素
from appium.webdriver.webdriver import WebDriver

from page.base_page import BasePage
from page.business_del_page import BusinessDelPage


class BusinessListPage(BasePage):
    # 商圈攻略元素
    business_lists = ('id', 'com.lizihang.powerapp:id/constraintLayout')  # 商圈攻略列表ID
    total_project = ('id', 'com.lizihang.powerapp:id/tv_title_num')

    _driver: WebDriver

    # def __init__(self, driver):
    #     self._driver = driver

    # 获得统计字段
    def get_total_house(self) -> str:
        return self.my_find_element(*self.total_project)

    # 获得列表数据第一个
    def get_list_one(self) -> list:
        return self.my_find_elements(*self.business_lists)[0]

    # 进入楼盘攻略详情
    def go_businessdel_page(self):
        self.get_list_one().click()
        return BusinessDelPage(self._driver)
