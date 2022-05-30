# coding = utf-8
from page.base_page import BasePage
from page.dishwashing_del_page import DishWashingdelPage
from page.house_trend_del_page import HouseTrenddelPage

'''
一手动态列表
'''


class HouseTrendListPage(BasePage):
    # 搜索框
    search_et = ('id', 'com.lizihang.powerapp:id/et')
    # 一手项目名称
    projet_names = ('id', 'com.lizihang.powerapp:id/tv_resblockName')
    # 状态
    projet_statuss = ('id', 'com.lizihang.powerapp:id/tv_state')
    # 复制
    projet_copies = ('id', 'com.lizihang.powerapp:id/tv_copy')

    # 搜索框
    def get_page_title(self):
        return self.my_find_element(*self.search_et)

    # 获得列表数据第一个
    def get_list_one(self) -> list:
        return self.my_find_elements(*self.projet_names)[0]

    # 获得列表数据第一个复制
    def get_copy_one(self) -> list:
        return self.my_find_elements(*self.projet_copies)[0]

    # 进入详情
    def go_housetrenddel_page(self):
        self.get_list_one().click()
        return HouseTrenddelPage(self._driver)

    def get_copy(self):
        return self.get_copy_one().text
