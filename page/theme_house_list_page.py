# coding = utf-8

from time import sleep
from page.base_page import BasePage
from page.theme_house_del_page import ThemeHouseDelPage

'''
所有主题房列表
'''


class ThemeHouseListPage(BasePage):
    # 页面标题
    page_title = ('id', 'com.lizihang.powerapp:id/tv_title_center')
    # 入口主题名称-多个
    shot_theme_titles = ('id', 'com.lizihang.powerapp:id/tvTitle')
    # 主题名称-多个
    theme_titles = ('id', 'com.lizihang.powerapp:id/tvContent')
    # 上架时间
    page_titles = ('id', 'com.lizihang.powerapp:id/tvTime')

    # 找到列表第一个
    def get_list_one(self) -> list:
        return self.my_find_elements(*self.shot_theme_titles)[0]

    # 进入详情页
    def go_theme_house_del_page(self):
        self.get_list_one().click()
        return ThemeHouseDelPage(self._driver)
