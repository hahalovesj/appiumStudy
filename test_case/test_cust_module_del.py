# coding = utf-8
import allure
from page.home_page import HomePage
import time
import xlrd
import xlwt
import datetime
import pytest

'''
客源模块 各个频道测试
'''


@allure.feature("客源模块")
class TestCaseCust:
    # 函数级开始
    def setup(self):
        # 回到首页
        self.HomePage.go_back_home()
        print("------->setup_method")

    # 函数级结束
    def teardown(self):
        self.HomePage.go_back_home()
        print("------->teardown_method")

    # 进入求购客源详情
    @allure.story("求购客源详情")
    def test_cust_buy_del(self):
        name = self.HomePage.go_cust_buy_list().go_custbuydel_page().get_cust_code().text
        print("求购客详情:" + name)
        assert "BJ" in name

    # 进入求租客源详情
    @allure.story("求租客源详情")
    def test_cust_rent_del(self):
        name = self.HomePage.go_cust_rent_list().go_custrentdel_page().get_cust_code().text
        print("求租客详情:" + name)
        assert "BJ" in name

    # 进入海外客源详情
    @allure.story("海外客源详情")
    def test_cust_oversea_del(self):
        name = self.HomePage.go_cust_oversea_list().go_custoverseadel_page().get_cust_code().text
        print("海外客详情:" + name)
        assert "BJ" in name

    # 共享池-店 todo 组共享池没有客源，所以用店的
    @allure.story("共享池-店详情")
    def test_share_pool_buy_del(self):
        name = self.HomePage.go_share_pool_list().go_share_pool_store_del().get_cust_code().text
        print("共享池-店：" + name)
        assert "BJ" in name

    # 成交客户-买卖列表
    @allure.story("成交客户-买卖列表详情")
    def test_deal_custbuy_del(self):
        name = self.HomePage.go_deal_cust().go_dealcustbuy_del().get_cust_code()
        print("成交客-买卖：" + name)
        assert "BJ" in name

    # 测试类级开始
    def setup_class(self):
        self.HomePage = HomePage()
        print("------->setup_class")

    # 测试类级结束
    def teardown_class(self):
        self.HomePage.quite_driver()
        print("------->teardown_class")

