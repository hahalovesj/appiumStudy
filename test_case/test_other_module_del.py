# coding = utf-8
from time import sleep
import allure
from page.home_page import HomePage

'''
其他模块
'''


@allure.feature("其他模块")
class TestCaseOther:
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

    # 进入带看记录
    @allure.story("带看记录")
    def test_go_showrecord(self):
        total_showing = self.HomePage.go_showrecord().get_total_showing()
        print("带看记录:" + total_showing)
        assert "带看记录" in total_showing

    # 进入洗盘
    @allure.story("洗盘")
    def test_go_dishwashing(self):
        title = self.HomePage.go_dishwashing().go_dishwashingdel_page().get_owner_info_modify()
        print("业主信息:" + title)
        assert "修改" in title

    # 进入一手动态
    @allure.story("一手动态")
    def test_go_housetrend(self):
        copy = self.HomePage.go_housetrend().get_copy()
        print("一手动态:" + copy)
        assert "复制" in copy

    # 进入分享轨迹
    @allure.story("分享轨迹")
    def test_go_share_locus(self):
        name = self.HomePage.go_share_locus().go_sharelocusdel_page().get_page_title()
        print("分享轨迹:" + name.text)
        assert "访问明细" in name.text

    # 测试类级开始
    def setup_class(self):
        self.HomePage = HomePage()
        # 不加这个延时 它就不滑动
        sleep(2)
        self.HomePage.swipe_down()
        print("------->setup_class")

    # 测试类级结束
    def teardown_class(self):
        self.HomePage.quite_driver()
        print("------->teardown_class")

