# coding = utf-8
from page.base_page import BasePage
from page.dishwashing_del_page import DishWashingdelPage

'''
洗盘列表
'''


class DishWashingListPage(BasePage):
    # 标题
    page_title = ('id', 'com.lizihang.powerapp:id/tv_title_text')
    # 责任盘tap
    zerenpan = ('xpath', '//android.widget.LinearLayout[@content-desc="责任盘"]')
    # 维护盘tap
    weihupan = ('xpath', '//android.widget.LinearLayout[@content-desc="维护盘"]')
    # 范围盘tap
    fanweipan = ('xpath', '//android.widget.LinearLayout[@content-desc="范围盘"]')
    # 已联系统计
    contacted_count = ('id', 'com.lizihang.powerapp:id/count')
    # 洗盘列表-房屋状态
    dishwashing_status = ('id', 'com.lizihang.powerapp:id/state')
    # 洗盘列表-房间号
    dishwashing_rooms = ('id', 'com.lizihang.powerapp:id/title')
    # 洗盘列表-楼盘名
    dishwashing_resbolcks = ('id', 'com.lizihang.powerapp:id/tvContent')
    # 录跟进
    reconrd_lists = ('id', 'com.lizihang.powerapp:id/recordIv')
    # 发短信
    msg_lists = ('id', 'com.lizihang.powerapp:id/iv_msg')
    # 拨打电话
    phone_lists = ('id', 'com.lizihang.powerapp:id/phoneIv')

    def get_page_title(self):
        return self.my_find_element(*self.page_title)

    # 获得列表数据第一个
    def get_list_one(self) -> list:
        return self.my_find_elements(*self.dishwashing_status)[0]

    # 进入详情
    def go_dishwashingdel_page(self):
        self.get_list_one().click()
        return DishWashingdelPage(self._driver)
