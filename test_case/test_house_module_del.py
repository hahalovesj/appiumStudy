# coding = utf-8
from time import sleep

import allure

from page.business_list_page import BusinessListPage
from page.home_page import HomePage
from page.loupan_list_page import LoupanListPage
from page.market_control_page import MarketControlPage
from page.onehand_special_list_page import OnehandSpecialListPage

'''
房源模块
'''


@allure.feature("房源模块")
class TestCaseHouse:
    # 函数级开始
    def setup(self):
        # 回到首页
        self.HomePage.go_back_home()
        print("------->setup_method")

    # 函数级结束
    def teardown(self):
        # 回到首页
        self.HomePage.go_back_home()
        print("------->teardown_method")

    # 进入新房项目详情
    @allure.story("新房详情")
    def test_onehand_del(self):
        project_postion = self.HomePage.go_onehand_list().go_onehanddel_page().get_project_position()
        print("新房详情:" + project_postion)
        assert "项目" in project_postion

    # 进入二手房详情
    @allure.story("二手房详情")
    def test_secondhand_del(self):
        house_price = self.HomePage.go_secondhand_list().go_secondhand_del().get_house_price()
        print("二手房:" + house_price)
        assert "万" in house_price

    # 进入租房详情
    @allure.story("租房详情")
    def test_rent_house_del(self):
        house_price = self.HomePage.go_rent_house_list().go_renthouse_del().get_house_price()
        print("租房:" + house_price)
        assert "万/月" in house_price

    # 进入四合院买卖详情
    @allure.story("四合院买卖详情")
    def test_siheyuan_sale_del(self):
        house_price = self.HomePage.go_siheyuan_sale_list().go_shysale_del().get_house_price()
        print("四合院买卖:" + house_price)
        assert "万" in house_price

    # 进入四合院租赁详情
    @allure.story("四合院租赁详情")
    def test_siheyuan_rent_del(self):
        house_price = self.HomePage.go_siheyuan_rent_list().go_shyrent_del().get_house_price()
        print("四合院租赁:" + house_price)
        assert "万/月" in house_price

    # 进入海外房产详情
    @allure.story("海外房产详情")
    def test_oversea_del(self):
        house_price = self.HomePage.go_oversea_list().go_oversea_del().get_oversea_price()
        print("海外:" + house_price)
        assert "万" in house_price
        # 回到原生
        self.HomePage.switch_to_native()

    # 销控
    @allure.story("销控")
    def test_market_control(self):
        total_target = self.HomePage.go_market_control().get_total_target()
        print("销控：" + total_target)
        assert "目标房屋" in total_target

    # 一手好房 todo 还有个房屋详情页的判断
    @allure.story("一手好房")
    def test_onehand_special_del(self):
        project_position = self.HomePage.go_onehand_special_list().go_onehand_spcl_del().get_project_position()
        print("一手好房" + project_position)
        assert "项目区位" in project_position

    # 楼盘攻略 todo 二手报价得先判断一下
    @allure.story("楼盘攻略")
    def test_loupan_del(self):
        second_price = self.HomePage.go_loupan_list().go_loupandel_page().get_second_price()
        print("楼盘攻略：" + second_price)
        assert "万" in second_price

    # 商圈攻略
    @allure.story("商圈攻略")
    def test_business_del(self):
        house_title = self.HomePage.go_business_list().go_businessdel_page().get_house_title()
        print("商圈攻略：" + house_title)
        assert "商圈" in house_title
        self.HomePage.switch_to_native()

    # 测试类级开始
    def setup_class(self):
        self.HomePage = HomePage()
        print("------->setup_class")

    # 测试类级结束
    def teardown_class(self):
        self.HomePage.quite_driver()
        print("------->teardown_class")

