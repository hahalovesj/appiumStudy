# coding = utf-8
from page.base_page import BasePage

'''
地图找房
'''


class MapPage(BasePage):
    # 总数
    total_num = ('id', 'com.lizihang.powerapp:id/tvTotalNum')

    # 获取统计总数
    def get_total_num(self):
        return self.my_find_element(*self.total_num).text
