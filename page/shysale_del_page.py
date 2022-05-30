# coding = utf-8

# 定义元素
from page.base_page import BasePage

"""
四合院买卖详情
"""


class SiheyuanSaleDelPage(BasePage):
    # 四合院详情元素
    siheyuan_title = ('id', "com.lizihang.powerapp:id/tv_houseTitle")  # 四合院详情标题 页中
    siheyuan_top_title = ('id', "com.lizihang.powerapp:id/tv_title_text")  # 二手房详情顶部房屋title
    siheyuan_map = ('id', 'com.lizihang.powerapp:id/mapRl')  # 二手房详情中地图找房
    siheyuan_share = ('id', "com.lizihang.powerapp:id/rl_title_bar_right_icon")  # 分享
    siheyuan_top = ('id', "com.lizihang.powerapp:id/iv")  # 二手房详情顶部轮播图

    siheyuan_title = ('id', "com.lizihang.powerapp:id/tv_houseTitle")  # 二手房详情标题，页中的标题
    siheyuan_price = ('id', "com.lizihang.powerapp:id/tv_price")  # 二手房详情价格

    house_del = ('xpath', '//android.widget.LinearLayout[@content-desc="房源详情"]')  # 房源详情tap
    showing = ('xpath', '//android.widget.LinearLayout[@content-desc="带看"]')  # 带看tap
    showing_feedback = ('xpath', '//android.widget.LinearLayout[@content-desc="带看反馈"]')  # 带客反馈tap
    follow_record = ('xpath', '//android.widget.LinearLayout[@content-desc="跟进记录"]')  # 跟进记录tap

    # 获得标题
    def get_siheyuan_title(self):
        return self.my_find_element(*self.siheyuan_title).text

    # 获取价格
    def get_house_price(self):
        return self.my_find_element(*self.siheyuan_price).text


