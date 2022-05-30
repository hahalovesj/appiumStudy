# coding = utf-8
from page.base_page import BasePage

'''
楼盘对比分析
'''


class ResblockComparePage(BasePage):
    # 标题
    total_res = ('id', 'com.lizihang.powerapp:id/tv_statics')

    # 获取标题
    def get_total_res(self):
        return self.my_find_element(*self.total_res).text
