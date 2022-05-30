# coding = utf-8

# 定义元素
from appium.webdriver import WebElement
from appium.webdriver.webdriver import WebDriver

from page.base_page import BasePage
from page.loupan_del_page import LoupanDelPage


class LoupanListPage(BasePage):
    # 楼盘攻略元素

    loupan_serach_edit = ('id', 'com.lizihang.powerapp:id/et_search')  # 楼盘搜索框

    loupan_serach_btn = ('id', 'com.lizihang.powerapp:id/iv_search')  # 楼盘搜索按钮

    loupan_options = ('id', 'com.lizihang.powerapp:id/ll_ev')  # 楼盘列表筛选4个（区域，产品，报价，更多）

    loupan_lists = ('id', 'com.lizihang.powerapp:id/tvResblockName')  # 楼盘攻略列表ID

    total_project = ('id', 'com.lizihang.powerapp:id/tv_statics')

    _driver: WebDriver

    # def __init__(self, driver):
    #     self._driver = driver

    # 获得统计字段
    def get_total_house(self) -> WebElement:
        return self.my_find_element(*self.total_project)

    # 获得列表数据第一个
    def get_list_one(self) -> list:
        return self.my_find_elements(*self.loupan_lists)[0]

    # 进入楼盘攻略详情
    def go_loupandel_page(self):
        self.get_list_one().click()
        return LoupanDelPage(self._driver)
