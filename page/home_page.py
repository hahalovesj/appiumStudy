# coding = utf-8


import time
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By

from page.accompany_page import AccompanyPage
from page.base_page import BasePage
from page.business_list_page import BusinessListPage
from page.chat_artifact_page import ChatArtifactPage
from page.cust_buy_list_page import CustBuyListPage
from page.cust_oversea_list_page import CustOverseaListPage
from page.cust_rent_list_page import CustRentListPage
from page.deal_cust_buy_list_page import DealCustBuyListPage
from page.dishwashing_list_page import DishWashingListPage
from page.doctor_landz_page import DoctorLandzPage
from page.history_pick_house_page import HistoryPickHousePage
from page.hmall_page import HmallPage
from page.house_compare_page import HouseComparePage
from page.house_position_page import HousePositionPage
from page.multi_house_share_pick_page import MultiHouseSharePickPage
from page.house_trend_list_page import HouseTrendListPage
from page.loupan_list_page import LoupanListPage
from page.map_page import MapPage
from page.mark_report_list_page import MarkReportListPage
from page.market_control_page import MarketControlPage
from page.onehand_list_page import OneHandListPage
from page.onehand_special_list_page import OnehandSpecialListPage
from page.onsale_choose_resblock_page import OnsaleChooseResPage
from page.oversea_list_page import OverseaListPage
from page.resblock_compare_page import ResblockComparePage
from page.renthouse_list_page import RentHouseListPage
from page.secondhand_list_page import SecondHandListPage
from page.share_locus_list_page import ShareLocusListPage
from page.share_pool_list_page import SharePoolListPage
from page.showrecord_page import ShowRecordPage
from page.shyrent_list_page import SiheyuanRentListPage
from page.shysale_list_page import SiheyuanSaleListPage
from page.ten_house_list_page import TenHouseListPage
from page.theme_banner1_page import ThemeBanner1Page
from page.theme_house_list_page import ThemeHouseListPage
from page.wonder_page import WonderPage

"""
首页
"""


class HomePage(BasePage):
    # 消息弹框
    totas = (MobileBy.ID, "com.lizihang.powerapp:id/ll")
    # 弹框取消按钮
    totas_cancel = (MobileBy.ID, "com.lizihang.powerapp:id/cancel")

    # 返回按钮
    go_back1_ele = (MobileBy.ID, "com.lizihang.powerapp:id/back")
    go_back2_ele = (MobileBy.ID, "com.lizihang.powerapp:id/iv_title_left")
    go_back3_ele = (MobileBy.ID, "com.lizihang.powerapp:id/iv_title_bar_left_icon")
    go_back4_ele = (MobileBy.ID, "com.lizihang.powerapp:id/iv_left")

    # 主题房，必卖10套房，主题等轮播卡片--获取多个
    carousel_cards = (MobileBy.ID, "com.lizihang.powerapp:id/tv_house_name")
    # ------------房源------------
    # 新房
    onehand = (MobileBy.ID, 'com.lizihang.powerapp:id/tv_onehand')
    # 二手
    secondhand = (MobileBy.ID, 'com.lizihang.powerapp:id/tv_apartmentsale')
    # 租房
    rent_house = (MobileBy.ID, 'com.lizihang.powerapp:id/tv_apartmentlease')
    # 四合院买卖
    siheyuan_sale = (MobileBy.ID, 'com.lizihang.powerapp:id/tv_siheyuansale')
    # 四合院租赁
    siheyuan_rent = (MobileBy.ID, 'com.lizihang.powerapp:id/tv_siheyuanlease')
    # 海外
    oversea = (MobileBy.ID, 'com.lizihang.powerapp:id/tvMapSearchHouse')
    # 销控
    market_control = (MobileBy.ID, 'com.lizihang.powerapp:id/tvMarketControl')
    # 一手好房
    onehand_special = (MobileBy.ID, 'com.lizihang.powerapp:id/tvOneHandSpePrice')
    # 楼盘攻略
    loupan = (MobileBy.ID, 'com.lizihang.powerapp:id/tvSecondPro')
    # 商圈攻略
    business_area = (MobileBy.ID, 'com.lizihang.powerapp:id/tv_trading_strategy')

    # ------------客源------------
    # 求购
    cust_buy = (MobileBy.ID, 'com.lizihang.powerapp:id/tv_buy')
    # 求租
    cust_rent = (MobileBy.ID, 'com.lizihang.powerapp:id/tv_rent')
    # 海外
    oversea_cust = (MobileBy.ID, 'com.lizihang.powerapp:id/tv_oversea')
    # 共享池
    share_pool = (MobileBy.ID, 'com.lizihang.powerapp:id/tv_share_pool')
    # 成交客
    deal_cust = (MobileBy.ID, 'com.lizihang.powerapp:id/tv_deal_customer')
    # TODO 客服来电
    customer_service = ()

    # ------------工具------------
    # 1微聊神器
    chat_artifact = (MobileBy.ID, 'com.lizihang.powerapp:id/tv_chat_artifact')
    # 2兰斯博士
    doctor_landz = (MobileBy.ID, 'com.lizihang.powerapp:id/rl_robot')
    # 3多盘多房转发
    multi_house_share = (MobileBy.ID, 'com.lizihang.powerapp:id/rlHouseShare')
    # 4房源位置图
    house_position = (MobileBy.ID, 'com.lizihang.powerapp:id/tv_house_position')
    # 5楼盘对比分析
    resblock_compare = (MobileBy.ID, 'com.lizihang.powerapp:id/tv_property_pk')
    # 6历史成交
    history_deal = (MobileBy.ID, 'com.lizihang.powerapp:id/rl_tv_dealinginfo')
    # 7房源对比分析
    house_compare = (MobileBy.ID, 'com.lizihang.powerapp:id/tv_house_compare')
    # 8wonder
    wonder = (MobileBy.ID, 'com.lizihang.powerapp:id/server_record_layout')
    # 9市场报告
    mark_report = (MobileBy.ID, 'com.lizihang.powerapp:id/tv_mark_report')
    # 10Hmall
    hmall = (MobileBy.ID, 'com.lizihang.powerapp:id/rl_hmall_chart')
    # 11地图找房
    map = (MobileBy.ID, 'com.lizihang.powerapp:id/rl_map')
    # 12陪带表
    accompany = (MobileBy.ID, 'com.lizihang.powerapp:id/rl_accompany')
    # 13在售房源表
    onsale_list = (MobileBy.ID, 'com.lizihang.powerapp:id/tv_onsale_listing')

    # ------------其他------------
    # 带看记录
    showrecord = (MobileBy.ID, 'com.lizihang.powerapp:id/tv_showrecord')
    # 洗盘
    dishwashing = (MobileBy.ID, 'com.lizihang.powerapp:id/tv_dishwashing')
    # 一手动态
    housetrend = (MobileBy.ID, 'com.lizihang.powerapp:id/tv_housetrend')
    # 分享轨迹
    share_locus = (MobileBy.ID, 'com.lizihang.powerapp:id/tv_share_locus')

    # ------------一手项目管理------------
    # 报备管理
    project_manage = (MobileBy.ID, 'com.lizihang.powerapp:id/tv_onehandprojectmanger')

    # 全司必卖
    company_sale = (MobileBy.ID, 'com.lizihang.powerapp:id/tvCompanySale')

    # 户型管理
    house_type_manage = (MobileBy.ID, 'com.lizihang.powerapp:id/tv_ManageHouseType')

    # 上传单据
    documents_upload = (MobileBy.ID, 'com.lizihang.powerapp:id/tv_upload')

    # -----------------方法-----------------------

    # 返回首页
    def go_back_home(self):
        # 黑名单：在售房源表的坚持返回
        black_list = ['com.lizihang.powerapp:id/tvCancel']
        i = 1
        flag = False
        while i < 5:
            try:
                self._driver.find_element(*self.cust_buy)
                flag = True
                # print("回到首页了")
            except:
                # 遍历黑名单中的元素，进行处理
                for ele_xpath in black_list:
                    # 黑名单元素是否存在
                    eles = self._driver.find_elements(By.ID, ele_xpath)
                    # 黑名单元素出现，进行处理
                    if len(eles) > 0:
                        eles[0].click()
                self.go_back()
                time.sleep(2)
                print("返回")
            # 判断已经回到首页
            if flag:
                break
            i = i + 1

    # 返回1
    def go_home_page(self):
        # 返回
        self.find_and_click(*self.go_back1_ele)
        return self

    # 返回2
    def go_home_page2(self):
        # 返回
        self.find_and_click(*self.go_back2_ele)
        return self

    # 返回3
    def go_home_page3(self):
        # 返回
        self.find_and_click(*self.go_back3_ele)
        return self

    # 返回4
    def go_home_page4(self):
        # 返回
        self.find_and_click(*self.go_back4_ele)
        return self

    '''
    轮播卡片
    '''

    # 进入所有主题房
    def go_theme_house(self):
        self.my_find_elements(*self.carousel_cards)[0].click()
        return ThemeHouseListPage(self._driver)

    # 进入必卖10套房
    def go_10_house(self):
        self.my_find_elements(*self.carousel_cards)[1].click()
        return TenHouseListPage(self._driver)

    # 进入banner1主题
    def go_theme_banner1(self):
        self.my_find_elements(*self.carousel_cards)[2].click()
        return ThemeBanner1Page(self._driver)

    '''
    房源模块
    '''

    # 房源-新房
    def go_onehand_list(self):
        # 点击进入新房列表
        print("点击进入新房列表")
        self.find_and_click(*self.onehand)
        time.sleep(3)
        return OneHandListPage(self._driver)

    # 房源-二手房
    def go_secondhand_list(self):
        # 点击进入二手房列表
        print("点击进入二手房列表")
        self.find_and_click(*self.secondhand)
        return SecondHandListPage(self._driver)

    # 房源-租房
    def go_rent_house_list(self):
        # 点击进入二手房列表
        print("点击进入二手房列表")
        self.find_and_click(*self.rent_house)
        return RentHouseListPage(self._driver)

    # 房源-四合院买卖
    def go_siheyuan_sale_list(self):
        # 点击进入四合院买卖列表
        print("点击进入四合院买卖列表")
        self.find_and_click(*self.siheyuan_sale)
        return SiheyuanSaleListPage(self._driver)

    # 房源-四合院租赁
    def go_siheyuan_rent_list(self):
        # 点击进入四合院租赁列表
        print("点击进入四合院租赁列表")
        self.find_and_click(*self.siheyuan_rent)
        return SiheyuanRentListPage(self._driver)

    # 房源-海外
    def go_oversea_list(self):
        # 点击进入海外列表
        print("点击进入海外列表")
        self.find_and_click(*self.oversea)
        return OverseaListPage(self._driver)

    # 房源-销控
    def go_market_control(self):
        # 点击进入楼盘列表
        print("点击进入销控列表")
        self.find_and_click(*self.market_control)
        return MarketControlPage(self._driver)

    # 房源-一手好房列表
    def go_onehand_special_list(self):
        # 点击进入楼盘列表
        print("点击进入一手好房")
        self.find_and_click(*self.onehand_special)
        return OnehandSpecialListPage(self._driver)

    # 房源-楼盘攻略
    def go_loupan_list(self):
        # 点击进入楼盘列表
        print("点击进入楼盘列表")
        self.find_and_click(*self.loupan)
        return LoupanListPage(self._driver)

    # 房源-商圈攻略
    def go_business_list(self):
        # 点击进入商圈列表
        print("点击进入商圈列表")
        self.find_and_click(*self.business_area)
        return BusinessListPage(self._driver)

    '''
    客源模块
    '''

    # 求购客源
    def go_cust_buy_list(self):
        self.find_and_click(*self.cust_buy)
        print("点击进入求购客列表")
        return CustBuyListPage(self._driver)

    # 求租客源
    def go_cust_rent_list(self):
        self.find_and_click(*self.cust_rent)
        print("点击进入求租客列表")
        return CustRentListPage(self._driver)

    # 海外列表
    def go_cust_oversea_list(self):
        self.find_and_click(*self.oversea_cust)
        print("点击进入海外客列表")
        return CustOverseaListPage(self._driver)

    # 共享池列表
    def go_share_pool_list(self):
        self.find_and_click(*self.share_pool)
        print("点击进入共享池")
        return SharePoolListPage(self._driver)

    # 成交客户
    def go_deal_cust(self):
        self.find_and_click(*self.deal_cust)
        print("找到--成交客户")
        return DealCustBuyListPage(self._driver)

    '''
    工具模块
    '''

    # 微聊神器
    def go_chat_artifact(self):
        self.find_and_click(*self.chat_artifact)
        print("找到--微聊神器")
        return ChatArtifactPage(self._driver)

    # 兰斯博士
    def go_doctor_landz(self):
        self.find_and_click(*self.doctor_landz)
        print("找到--兰斯博士")
        return DoctorLandzPage(self._driver)

    # 多盘多房转发 todo
    def go_multi_house_share(self):
        self.find_and_click(*self.multi_house_share)
        print("找到--多盘多房转发")
        return MultiHouseSharePickPage(self._driver)

    # 在售房源表
    def go_onsale_list(self):
        self.find_and_click(*self.onsale_list)
        print("找到--在售房源表")
        return OnsaleChooseResPage(self._driver)

    # 房源位置图
    def go_house_position(self):
        self.find_and_click(*self.house_position)
        print("找到--房源位置图")
        return HousePositionPage(self._driver)

    # 楼盘对比分析
    def go_resblock_compare(self):
        self.find_and_click(*self.resblock_compare)
        print("找到--楼盘对比分析")
        return ResblockComparePage(self._driver)

    # 历史成交
    def go_history_deal(self):
        self.find_and_click(*self.history_deal)
        return HistoryPickHousePage(self._driver)

    # 房源对比分析
    def go_house_compare(self):
        self.find_and_click(*self.house_compare)
        print("找到--房源对比分析")
        return HouseComparePage(self._driver)

    # wonder
    def go_wonder(self):
        self.find_and_click(*self.wonder)
        print("找到--房源对比分析")
        return WonderPage(self._driver)

    # 市场报告
    def go_mark_report(self):
        self.find_and_click(*self.mark_report)
        print("找到--市场报告")
        return MarkReportListPage(self._driver)

    # Hmall
    def go_hmall(self):
        self.find_and_click(*self.hmall)
        print("找到--hmall")
        return HmallPage(self._driver)

    # 地图找房
    def go_map(self):
        self.find_and_click(*self.map)
        print("找到--地图找房")
        return MapPage(self._driver)

    # 陪带表
    def go_accompany(self):
        self.find_and_click(*self.accompany)
        print("找到--陪带表")
        return AccompanyPage(self._driver)

    # todo 一二手联发

    '''
    其他
    '''

    # 带看记录
    def go_showrecord(self):
        self.find_and_click(*self.showrecord)
        print("找到--带看记录")
        return ShowRecordPage(self._driver)

    # 洗盘列表
    def go_dishwashing(self):
        self.find_and_click(*self.dishwashing)
        print("找到--洗盘")
        return DishWashingListPage(self._driver)

    # 一手动态
    def go_housetrend(self):
        self.find_and_click(*self.housetrend)
        print("找到--一手动态")
        return HouseTrendListPage(self._driver)

    # 分享轨迹
    def go_share_locus(self):
        self.find_and_click(*self.share_locus)
        print("找到--分享轨迹")
        return ShareLocusListPage(self._driver)

    # todo 上传管理

    '''
    一手项目管理
    '''

    # 报备管理 todo return 页面
    def go_project_manage(self):
        self.find_and_click(*self.project_manage)
        print("找到--报备管理")
