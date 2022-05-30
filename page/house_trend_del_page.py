# coding = utf-8
from page.base_page import BasePage

'''
一手动态详情
'''


class HouseTrenddelPage(BasePage):
    # 标题
    pro_name = ('id', 'com.lizihang.powerapp:id/resblockNameTv')
    # 报价（万）
    pro_price = ('id', 'com.lizihang.powerapp:id/priceTv')
    # 建面（㎡）
    pro_area = ('id', 'com.lizihang.powerapp:id/areaTv')

    def get_pro_name(self):
        return self.my_find_element(*self.pro_name)


