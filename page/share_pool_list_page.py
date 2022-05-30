# coding = utf-8

# 定义元素
from appium.webdriver import WebElement
from appium.webdriver.webdriver import WebDriver
from page.base_page import BasePage
from page.share_pool_del_page import SharePoolDelPage

'''
共享池列表
'''


class SharePoolListPage(BasePage):
    # 共享池元素
    # 搜索框
    share_pool_search_edit = ('id', 'com.lizihang.powerapp:id/et')
    # 组共享池
    share_pool_group = ('id', 'com.lizihang.powerapp:id/rbGroup')
    # 店共享池
    share_pool_store = ('id', 'com.lizihang.powerapp:id/rbStore')
    # 司共享池
    share_pool_company = ('id', 'com.lizihang.powerapp:id/rbCompany')

    # 列表
    share_pool_lists = ('id', 'com.lizihang.powerapp:id/rl_root')
    # 统计记录
    total_cust = ('id', 'com.lizihang.powerapp:id/tv_statics')

    _driver: WebDriver

    # 获得统计字段
    def get_total_house(self) -> WebElement:
        return self.my_find_element(*self.total_cust)

    # 获得组共享池列表数据第一个
    def get_list_one(self) -> list:
        return self.my_find_elements(*self.share_pool_lists)[0]

    # 组共享池第一个详情
    def go_share_pool_group_del(self):
        self.get_list_one().click()
        return SharePoolDelPage(self._driver)

    # 店共享池的第一个详情
    def go_share_pool_store_del(self):
        self.find_and_click(*self.share_pool_store)
        self.wait_element_located(self.share_pool_lists)
        self.get_list_one().click()
        return SharePoolDelPage(self._driver)

    # 司共享池的第一个详情
    def go_share_pool_company_del(self):
        self.find_and_click(*self.share_pool_company)
        self.wait_element_located(self.share_pool_lists)
        self.get_list_one().click()
        return SharePoolDelPage(self._driver)