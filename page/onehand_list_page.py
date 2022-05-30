# coding = utf-8

# 定义元素
import time

from appium.webdriver import WebElement
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

from page.base_page import BasePage
from page.onehand_del_page import OneHandDelPage
'''
新房列表页
'''


class OneHandListPage(BasePage):

    # 新房列表元素
    # 搜索输入框
    search_edit = ('id', 'com.lizihang.powerapp:id/edit')
    # 搜索按钮
    search_edit = ('id', 'com.lizihang.powerapp:id/search')

    # 城区
    drop_down_city = ('id', 'com.lizihang.powerapp:id/dropDownMenu0')

    # 报价
    drop_down_price = ('id', 'com.lizihang.powerapp:id/dropDownMenu1')
    # 项目等级
    drop_down_level = ('id', 'com.lizihang.powerapp:id/projectLevel')
    # 更多
    drop_down_more = ('id', 'com.lizihang.powerapp:id/dropDownMenu2')

    # 推广中
    filter_radio1 = ('id', 'com.lizihang.powerapp:id/radio1')
    # 优惠楼盘
    filter_radio2 = ('id', 'com.lizihang.powerapp:id/radio2')
    # 官网展示
    filter_radio3 = ('id', 'com.lizihang.powerapp:id/radio3')
    # 即将开盘
    filter_radio4 = ('id', 'com.lizihang.powerapp:id/radio4')
    # 丽兹专场
    filter_radio5 = ('id', 'com.lizihang.powerapp:id/radio5')

    # 全司必卖-查看更多
    comp_mustsale_more = ('id', 'com.lizihang.powerapp:id/tvMore')
    # 全司必卖推荐房，名称，三个
    comp_mustsale_names = ('id', 'com.lizihang.powerapp:id/tvResblockName')
    # 全司必卖推荐房，地址，三个
    comp_mustsale_adds = ('id', 'com.lizihang.powerapp:id/tvAddress')
    # 全司必卖推荐房，现价，三个
    comp_mustsale_newprices = ('id', 'com.lizihang.powerapp:id/tvNewPrice')
    # 全司必卖推荐房，原价，三个
    comp_mustsale_oldprices = ('id', 'com.lizihang.powerapp:id/tvOldPrice')
    # 更多必卖独家
    mustsale_more = ('id', 'com.lizihang.powerapp:id/tvHeadLook')

    # 项目统计
    total_project = ('id', 'com.lizihang.powerapp:id/tvAllNum')

    # 新房列表，多个
    onehand_lists = ('id', 'com.lizihang.powerapp:id/oneLl')
    # 项目等级
    onehand_level = ('id', 'com.lizihang.powerapp:id/prjLevel')
    # 项目状态
    onehand_status = ('id', 'com.lizihang.powerapp:id/prjStatus')
    # 视频标志icon
    onehand_video_flag = ('id', 'com.lizihang.powerapp:id/flagVideo')
    # 项目名称
    onehand_name = ('id', 'com.lizihang.powerapp:id/resblockName')
    # 产品类型
    onehand_type = ('id', 'com.lizihang.powerapp:id/houseTypeInfo')
    # 城区商圈
    onehand_bizcircle_name = ('id', 'com.lizihang.powerapp:id/bizcircleName')
    # 面积区间
    onehand_area_range = ('id', 'com.lizihang.powerapp:id/areaRange')
    # 报价区间
    onehand_price_range = ('id', 'com.lizihang.powerapp:id/totalPriceRange')
    # 标签，多个
    onehand_labels = ('id', 'com.lizihang.powerapp:id/label')
    # 更新时间
    onehand_update_time = ('id', 'com.lizihang.powerapp:id/updateTime')

    # 分享按钮
    onehand_share_btn = ('id', 'com.lizihang.powerapp:id/shareBtnLl')
    # 删除
    onehand_delete_btn = ('id', 'com.lizihang.powerapp:id/deleteBtnLl')
    # 批量分享按钮
    onehand_multi_share_btn = ('id', 'com.lizihang.powerapp:id/shareRl')


    _driver: WebDriver

    # 获得全司必卖查看更多
    def get_comp_mustsale_more(self):
        return self.my_find_element(*self.comp_mustsale_more)

    # 全司必卖房推荐


    # 全司必卖-查看更多
    def get_more(self):
        return self.my_find_element(*self.must_sale_more)

    # 获得统计字段
    def get_total_project(self) -> WebElement:
        time.sleep(3)
        # return self._driver.find_element(*self.total_project)
        return self.my_find_element(*self.total_project)

    # 获得列表
    def get_list(self):
        return self.my_find_elements(*self.onehand_lists)

    # 获得列表数据第一个
    def get_list_one(self):
        return self.my_find_elements(*self.onehand_lists)[0]

    # 进入新房详情
    def go_onehanddel_page(self):
        self.get_list_one().click()
        return OneHandDelPage(self._driver)
