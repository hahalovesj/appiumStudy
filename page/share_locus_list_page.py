# coding = utf-8
from time import sleep

from page.base_page import BasePage
from page.dishwashing_del_page import DishWashingdelPage
from page.house_trend_del_page import HouseTrenddelPage
from page.share_locus_del_page import ShareLocusDelPage

'''
分享轨迹列表
'''


class ShareLocusListPage(BasePage):
    # 标题
    page_title = ('id', 'com.lizihang.powerapp:id/tv_title_center')
    # 全司最火-查看次数
    projet_names = ('id', 'com.lizihang.powerapp:id/tv_look_num')
    # 全司最火-查看人数
    projet_statuss = ('id', 'com.lizihang.powerapp:id/tv_look_peo_num')
    # 分享轨迹tap
    share_tap = ('id', 'com.lizihang.powerapp:id/tv_share_locus')
    # 查看明细
    check_del = ('id', 'com.lizihang.powerapp:id/tv_detail')
    # 分享轨迹名称列表
    share_lists = ('id', 'com.lizihang.powerapp:id/tv_property')
    # 分享内容列表
    share_cont_lists = ('id', 'com.lizihang.powerapp:id/tv_share_content')

    # 搜索框
    def get_page_title(self):
        return self.my_find_element(*self.search_et)

    # 获得列表数据第一个
    def get_list_one(self) -> list:
        self.wait_element_located(self.check_del)
        return self.my_find_elements(*self.check_del)[0]

    # 进入详情
    def go_sharelocusdel_page(self):
        self.get_list_one().click()
        return ShareLocusDelPage(self._driver)
