# coding = utf-8
from time import sleep

from page.base_page import BasePage
from page.onsale_pick_house_page import OnsalePickHousePage

"""
在售房源表-选择楼盘页
"""


class OnsaleChooseResPage(BasePage):
    # top标题
    page_title = ('id', 'com.lizihang.powerapp:id/tv_title_center')
    # 搜索框
    srarch_et = ('id', 'com.lizihang.powerapp:id/et_choose_property')
    # 联想下拉框
    res_names = ('id', 'com.lizihang.powerapp:id/tvHouseName')

    # 获取标题
    def get_title(self):
        return self.my_find_element(*self.page_title)

    # 选择联想下拉框第一个,默认楼盘“观湖国际”
    def chose_list_one(self, content="观湖国际"):
        self.send_keys(self.srarch_et, content)
        sleep(2)
        self.my_find_elements(*self.res_names)[0].click()
        return OnsalePickHousePage(self._driver)







