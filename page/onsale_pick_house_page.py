# coding = utf-8
from time import sleep

from page.base_page import BasePage
from page.onsale_edit_table_page import OnsaleEditTablePage

"""
在售房源表-选择在售房源页
"""


class OnsalePickHousePage(BasePage):

    # 房源勾选页
    # 统计房源条数
    total_house = ('id', 'com.lizihang.powerapp:id/all_tv')
    # 全选
    check_all = ('id', 'com.lizihang.powerapp:id/tv_all_select_pic')
    # 单选按钮,可能多个
    radio_buttons = ('id', 'com.lizihang.powerapp:id/selectTv')
    # 制作位置图
    make_location = ('id', 'com.lizihang.powerapp:id/sendMsgTv2')
    # 制作在售表
    make_onsale = ('id', 'com.lizihang.powerapp:id/sendMsgTv')

    # 房源全选
    def chose_radio_btn_all(self):
        self.my_find_element(*self.check_all).click()

    # 房源单选，选择第一个
    def chose_radio_btn_one(self):
        self.my_find_elements(*self.radio_buttons)[0].click()

    # 点击制作位置图
    def make_location(self):
        self.my_find_element(*self.make_location).click()

    # 点击制作在售表
    def click_make_onsale(self):
        self.chose_radio_btn_all()
        sleep(1)
        self.my_find_element(*self.make_onsale).click()
        return OnsaleEditTablePage(self._driver)




