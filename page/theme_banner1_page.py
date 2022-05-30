# coding = utf-8

from time import sleep
from page.base_page import BasePage
from page.theme_house_del_page import ThemeHouseDelPage

'''
主题banner详情
'''


class ThemeBanner1Page(BasePage):
    # 主题标题
    theme_title = ('id', 'com.lizihang.powerapp:id/tv_title_text')

    # 必卖房名称
    def get_theme_title(self):
        return self.my_find_element(*self.theme_title)
