# coding = utf-8
from time import sleep

from page.base_page import BasePage
from page.onsale_edit_table_page import OnsaleEditTablePage

"""
历史成交-选择房源
"""


class HistoryPickHousePage(BasePage):

    # 房源勾选页
    # 搜索框-输入框
    search_et = ('id', 'com.lizihang.powerapp:id/et')
    # 搜索按钮
    search_btn = ('id', 'com.lizihang.powerapp:id/iv_search')
    # 排序
    list_sort = ('id', 'com.lizihang.powerapp:id/llSort')
    # 统计房源条数
    total_house = ('id', 'com.lizihang.powerapp:id/tv_statics')
    # 全选
    check_all = ('id', 'com.lizihang.powerapp:id/cb_all')
    # 全选按钮
    radio_buttons = ('id', 'com.lizihang.powerapp:id/cb_all')
    # 单选按钮，可能多个
    radio_buttons = ('id', 'com.lizihang.powerapp:id/ivSingleCheck')
    # 制作成交表
    make_deal = ('id', 'com.lizihang.powerapp:id/tvCompare')

    # 获取统计字段
    def get_total_house(self):
        return self.my_find_element(*self.total_house).text

    # 房源全选
    def chose_radio_btn_all(self):
        self.my_find_element(*self.check_all).click()

    # 房源单选，选择第一个
    def chose_radio_btn_one(self):
        self.my_find_elements(*self.radio_buttons)[0].click()

    # 点击制作成交表
    def make_deal(self):
        self.my_find_element(*self.make_deal).click()






