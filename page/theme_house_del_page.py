# coding = utf-8

from time import sleep

from page.base_page import BasePage


'''
所有主题房详情
'''


class ThemeHouseDelPage(BasePage):
    # 页面标题
    page_title = ('id', 'com.lizihang.powerapp:id/tv_title_text')

    # 标题
    def get_page_title(self):
        return self.my_find_element(*self.page_title)

    # todo 主题内容为内嵌H5

