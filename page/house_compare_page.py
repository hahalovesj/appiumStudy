# coding = utf-8
from page.base_page import BasePage

'''
房源对比分析
'''


class HouseComparePage(BasePage):
    # 总数
    total_houses = ('id', 'com.lizihang.powerapp:id/all_tv')

    # 获取统计总数
    def get_total_houses(self):
        return self.my_find_element(*self.total_houses).text
