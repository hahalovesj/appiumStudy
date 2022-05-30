# coding = utf-8
from page.base_page import BasePage

'''
陪带表
'''


class AccompanyPage(BasePage):
    # 买卖客户tap
    cust_buy_tap = ('id', 'android:id/text1')

    # 获取买卖客户tap标题
    def get_cust_buy_tap(self):
        return self.my_find_element(*self.cust_buy_tap).text
