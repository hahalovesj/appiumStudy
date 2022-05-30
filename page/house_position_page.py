# coding = utf-8
from page.base_page import BasePage

'''
房源位置图
'''


class HousePositionPage(BasePage):
    # 标题
    page_title = ('id', 'com.lizihang.powerapp:id/tv_title_center')

    # 获取标题
    def get_title(self):
        return self.my_find_element(*self.page_title).text
