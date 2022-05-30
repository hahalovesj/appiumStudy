# coding = utf-8
from time import sleep

from page.base_page import BasePage
from page.dishwashing_del_page import DishWashingdelPage
from page.house_trend_del_page import HouseTrenddelPage

'''
分享轨迹详情
'''


class ShareLocusDelPage(BasePage):
    # 标题
    page_title = ('id', 'com.lizihang.powerapp:id/tv_title_center')

    # 标题
    def get_page_title(self):
        sleep(3)
        return self.my_find_element(*self.page_title)


