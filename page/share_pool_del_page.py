# coding = utf-8

# 定义元素
from appium.webdriver import WebElement
from appium.webdriver.webdriver import WebDriver

from page.base_page import BasePage
from page.loupan_del_page import LoupanDelPage
'''
共享池详情
'''


class SharePoolDelPage(BasePage):
    # 客源编码
    cust_code = ('id', 'com.lizihang.powerapp:id/tv_custCode')
    # 客户姓名
    cust_name = ('id', 'com.lizihang.powerapp:id/tv_name')
    # 来源
    cust_name = ('id', 'com.lizihang.powerapp:id/tv_source')
    # 跟进记录tap
    cust_name = ('id', 'com.lizihang.powerapp:id/rb_trackrecord')
    # 委托记录tap
    cust_name = ('id', 'com.lizihang.powerapp:id/rb_entrust_record')


    _driver: WebDriver

    # 获得姓名
    def get_cust_name(self) -> WebElement:
        return self.my_find_element(*self.cust_name)

    # 获得客源编码
    def get_cust_code(self) -> WebElement:
        return self.my_find_element(*self.cust_code)



