# coding = utf-8

# 定义元素
from appium.webdriver import WebElement
from appium.webdriver.webdriver import WebDriver

from page.base_page import BasePage
from page.business_del_page import BusinessDelPage
from page.onehand_special_del_page import OnehandSpecialDelPage

'''
一手好房 列表
'''


class OnehandSpecialListPage(BasePage):
    # 一手特价房元素
    onehand_spcl_search_edit = ('id', 'com.lizihang.powerapp:id/rvContent')  # 一手好房搜索框
    onehand_spcl_search_button = ('id', 'com.lizihang.powerapp:id/et_search')  # 一手好房列表搜索按钮
    onehand_spcl_companysale = ('xpath', '//android.widget.LinearLayout[@content-desc="全司必卖"]')  # 全司必卖tap
    onehand_spcl_sellwell = ('xpath', '//android.widget.LinearLayout[@content-desc="必卖·独家"]')  # 必卖独家tap
    onehand_spcl_leftover = ('xpath', '//android.widget.LinearLayout[@content-desc="清盘专区"]')  # 清盘专区tap
    onehand_spcl_tips = ('xpath', '//android.widget.TextView[contains(@text, "一键分享")]')  # 提示文案
    share_button = ('id', 'com.lizihang.powerapp:id/tvShare')  # 去分享
    onehand_spcl_names = ('id', 'com.lizihang.powerapp:id/tvPrjName')  # 楼盘名字



    # 获得提示文案
    def get_tips(self) -> WebElement:
        return self.my_find_element(*self.onehand_spcl_tips)

    # 获得去分享
    def get_share(self) -> WebElement:
        return self.my_find_element(*self.share_button)

    # 获得列表数据第一个名称
    def get_list_one(self) -> list:
        return self.my_find_elements(*self.onehand_spcl_names)[0]

    # 进入第一个房源的详情
    def go_onehand_spcl_del(self):
        self.get_list_one().click()
        return OnehandSpecialDelPage(self._driver)
