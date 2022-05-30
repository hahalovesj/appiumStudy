# coding = utf-8

# 定义元素
from appium.webdriver import WebElement
from page.base_page import BasePage

"""
销控
"""


class MarketControlPage(BasePage):
    # 销控元素
    # 销控搜索编辑框
    market_search_edit = ('id', 'com.lizihang.powerapp:id/edit')
    # 销控搜索按钮
    market_search_button = ('id', 'com.lizihang.powerapp:id/search')
    # 销控筛选项（目标房屋，全部楼栋，销控状态）
    market_options = ('id', 'com.lizihang.powerapp:id/title')
    # 楼盘名称
    market_house_name = ('id', 'com.lizihang.powerapp:id/houseName')
    # 总户数
    market_total_num = ('id', 'com.lizihang.powerapp:id/totalNum')

    # 目标户数
    market_target_num = ('id', 'com.lizihang.powerapp:id/targetNum')
    # 统计目标房屋
    market_total_target = ('id', 'com.lizihang.powerapp:id/tvSummary')
    # 提示文案
    tips = ('id', 'com.lizihang.powerapp:id/totalTv')
    # 联想楼盘名称
    market_associate_houses = ('id', 'com.lizihang.powerapp:id/tvHouseName')
    # 楼盘搜索列表输入框
    market_search_et = ('id', 'com.lizihang.powerapp:id/et')

    # 获得提示文案
    def get_tips(self) -> WebElement:
        return self.my_find_element(*self.tips)

    # 点击楼盘名称输入框
    def go_search_edit(self):
        self.find_and_click(*self.market_search_edit)

    # 点击联想楼盘第一个
    def pick_associate_house(self):
        self.go_search_edit()
        self.my_find_elements(*self.market_associate_houses)[0].click()

    # 楼盘名称
    def get_house_name(self):
        self.pick_associate_house()
        return self.my_find_element(*self.market_house_name)

    # 统计目标房屋套数
    def get_total_target(self):
        self.pick_associate_house()
        return self.my_find_element(*self.market_total_target).text


