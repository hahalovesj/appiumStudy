# coding = utf-8

# 定义元素
import time
from page.base_page import BasePage
"""
海外房产详情页
"""


class OverseaDelPage(BasePage):
    # 海外房产top标题
    oversea_top_title = ('id', 'com.lizihang.powerapp:id/tv_title_text2')
    # 顶部轮播
    oversea_top = ('id', 'OverseaHeaderSwiper')
    # 分享
    oversea_share = ('id', 'com.lizihang.powerapp:id/rl_title_bar_right_icon')

    # 海外标题，页中
    oversea_title = ('xpath', '//div[@id="resblockIntroduction"]/div[1]/p[1]')
    # 报价区间
    oversea_price = ('xpath', '//*[@id="resblockIntroduction"]/div[4]/div')
    # 居室区间
    oversea_room = ('xpath', '//*[@id="resblockIntroduction"]/div[5]')
    # 面积区间
    oversea_area = ('xpath', '//*[@id="resblockIntroduction"]/div[6]')

    # 维护人
    holder = ('id', 'com.lizihang.powerapp:id/ll_holder')
    # 维护人经理
    holder_leader = ('id', 'com.lizihang.powerapp:id/ll_holderleader')

    # 获得标题
    def get_oversea_title(self):
        self.switch_to_h5()
        return self.my_find_element(*self.oversea_title)

    # 获得报价
    def get_oversea_price(self):
        self.switch_to_h5()
        return self.my_find_element(*self.oversea_price).text

