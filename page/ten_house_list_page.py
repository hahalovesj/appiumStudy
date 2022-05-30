# coding = utf-8

from time import sleep
from page.base_page import BasePage
from page.ten_house_del_page import TenHouseDelPage
from page.theme_house_del_page import ThemeHouseDelPage

'''
10套必卖房
'''


class TenHouseListPage(BasePage):
    # 搜索框
    search_et = ('id', 'com.lizihang.powerapp:id/et_search')
    # 去分享
    go_share = ('id', 'com.lizihang.powerapp:id/tvShare')
    # 项目信息
    # 项目名称-多个
    pro_names = ('id', 'com.lizihang.powerapp:id/tvPrjName')
    # 项目等级-多个
    pro_level = ('id', 'com.lizihang.powerapp:id/tvPrjLevel')
    # 共X套-多个
    pro_count = ('id', 'com.lizihang.powerapp:id/tvCount')
    # 房源信息
    # 房源地址-多个
    house_add = ('id', 'com.lizihang.powerapp:id/tvAddress')
    # 全司必卖房标签-多个
    house_must_sale = ('id', 'com.lizihang.powerapp:id/tvMustSale')
    # 特价价格-多个
    house_special_price = ('id', 'com.lizihang.powerapp:id/tvSpecialPrice')

    # 找到列表第一个
    def get_list_one(self) -> list:
        return self.my_find_elements(*self.house_add)[0]

    # 进入详情页
    def go_theme_house_del_page(self):
        self.get_list_one().click()
        return TenHouseDelPage(self._driver)
