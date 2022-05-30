# coding = utf-8
import allure
from page.home_page import HomePage

'''
轮播卡片 测试
'''


@allure.feature("轮播卡片模块")
class TestCaseCards:
    # 函数级开始
    def setup(self):
        # 回到首页
        self.HomePage.go_back_home()
        print("------->setup_method")

    # 函数级结束
    def teardown(self):
        self.HomePage.go_back_home()
        print("------->teardown_method")

    # 进入所有主题房
    @allure.story("所有主题房")
    def test_theme_house_del(self):
        name = self.HomePage.go_theme_house().go_theme_house_del_page().get_page_title()
        print("所有主题房:" + name.text)

    # 进入必卖10套房
    @allure.story("必卖10套房")
    def test_10_house_del(self):
        name = self.HomePage.go_10_house().go_theme_house_del_page().get_must_sale_name()
        print("必卖10套房:" + name.text)

    # 进入banner1主题
    @allure.story("主题1")
    def test_theme_banner1_del(self):
        name = self.HomePage.go_theme_banner1().get_theme_title()
        print("主题1:" + name.text)

    # 测试类级开始
    def setup_class(self):
        self.HomePage = HomePage()
        print("------->setup_class")

    # 测试类级结束
    def teardown_class(self):
        self.HomePage.quite_driver()
        print("------->teardown_class")

