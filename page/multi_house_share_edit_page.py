# coding = utf-8
from page.base_page import BasePage

'''
多盘多房转发-房源选择页-编辑微信片页
'''


class MultiHouseShareEditPage(BasePage):
    # 总数
    total_houses = ('id', 'com.lizihang.powerapp:id/all_tv')

    # 获取统计总数
    def get_total_houses(self):
        return self.my_find_element(*self.total_houses)
