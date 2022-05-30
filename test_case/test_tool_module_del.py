# coding = utf-8
from time import sleep
import allure
from page.home_page import HomePage

"""
工具模块
"""


@allure.feature("工具模块")
class TestCaseTool:
    # 函数级开始
    def setup(self):
        # 回到首页，防止有些用例报错，未能回到首页
        self.HomePage.go_back_home()
        print("------->setup_method")

    # 函数级结束
    def teardown(self):
        # 回到首页
        self.HomePage.go_back_home()
        print("------->teardown_method")

    # 01进入微聊神器
    @allure.story("微聊神器")
    def test_chat_artifact_del(self):
        title = self.HomePage.go_chat_artifact().get_step1_more().text
        print("微聊神器:" + title)
        assert "查看" in title

    # 02进入兰斯博士 todo 内嵌h5 定位不到
    @allure.story("兰斯博士")
    def test_doctor_landz(self):
        title = self.HomePage.go_doctor_landz().get_landz_title().text
        print("兰斯博士:" + title)
        assert "博士" in title

    # 03多盘多房转发 todo 没做后面分享微信片步骤
    @allure.story("多盘多房转发")
    def test_multi_house_share(self):
        title = self.HomePage.go_multi_house_share().get_share_title()
        print("待分享清单:" + title)
        assert "待分享清单" in title

    # 04进入房源位置图，制作位置图 todo 需要选择楼盘后判断，现在只判断了标题
    @allure.story("房源位置图")
    def test_house_position(self):
        title = self.HomePage.go_house_position().get_title()
        print("房源位置图:" + title)
        assert "选择楼盘" in title

    # 05进入楼盘对比分析
    @allure.story("楼盘对比分析")
    def test_resblock_compare(self):
        total_res = self.HomePage.go_resblock_compare().get_total_res()
        print("楼盘对比分析:" + total_res)
        assert "共搜到" in total_res

    # 06历史成交
    @allure.story("历史成交")
    def test_history_deal(self):
        total_house = self.HomePage.go_history_deal().get_total_house()
        print("历史成交:" + total_house)
        assert "当前共" in total_house

    # 07进入房源对比分析
    @allure.story("房源对比分析")
    def test_house_compare(self):
        total_houses = self.HomePage.go_house_compare().get_total_houses()
        print("房源对比分析:" + total_houses)
        assert "共搜到" in total_houses

    # 08wonder todo
    @allure.story("wonder")
    def test_wonder(self):
        call_today_title = self.HomePage.go_wonder().get_call_today_title()
        print("wonder:" + call_today_title)
        assert "电话量" in call_today_title

    # 09进入市场报告
    @allure.story("市场报告")
    def test_mark_report(self):
        mark_report = self.HomePage.go_mark_report().get_city_title()
        print("市场报告:" + mark_report)
        assert "城市报告" in mark_report

    # 10进入Hmall
    @allure.story("Hmall")
    def test_hamll(self):
        total_res = self.HomePage.go_hmall().get_total_res()
        print("Hmall:" + total_res)
        assert "共搜到" in total_res

    # 11进入地图找房
    @allure.story("地图找房")
    def test_map(self):
        map_total = self.HomePage.go_map().get_total_num()
        print("地图找房:" + map_total)
        assert "当前范围内" in map_total

    # 12进入陪带表 todo 没有带看数据
    @allure.story("陪带表")
    def test_accompany(self):
        cust_buy = self.HomePage.go_accompany().get_cust_buy_tap()
        print("陪带表:" + cust_buy)
        assert "买卖客户" in cust_buy

    # 13进入在售房源表，制作在售表 todo “坚持返回”放到黑名单里
    @allure.story("在售房源表")
    def test_onsale_list(self):
        name = self.HomePage.go_onsale_list().chose_list_one().click_make_onsale().get_resblock_name().text
        print("在售房源表:" + name)
        assert "观湖国际" in name

    # 测试类级开始
    def setup_class(self):
        self.HomePage = HomePage()
        sleep(2)
        self.HomePage.swipe_down()
        print("------->setup_class")

    # 测试类级结束
    def teardown_class(self):
        self.HomePage.quite_driver()
        print("------->teardown_class")

