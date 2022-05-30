# coding = utf-8

from time import sleep
from page.base_page import BasePage
from page.theme_house_del_page import ThemeHouseDelPage

'''
10套必卖房详情
'''


class TenHouseDelPage(BasePage):
    # 必卖房名称
    must_sale_name = ('id', 'com.lizihang.powerapp:id/tvHouseName')
    # 特价价格
    special_price = ('id', 'com.lizihang.powerapp:id/tvSpecialPrice')
    # 单价
    unit_price_value = ('id', 'com.lizihang.powerapp:id/tvUnitPriceValue')
    # 产品类型
    product_value = ('id', 'com.lizihang.powerapp:id/tvProductValue')

    # 必卖房名称
    def get_must_sale_name(self):
        return self.my_find_element(*self.must_sale_name)
