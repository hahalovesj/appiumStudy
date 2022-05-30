# coding = utf-8

# 定义元素
from page.base_page import BasePage
"""
租房详情
"""


class RentHouseDelPage(BasePage):
    # 租房列表元素
    # 二手房详情元素
    renthouse_top_title = ('id', "com.lizihang.powerapp:id/tv_title_text")  # 二手房详情顶部房屋title
    renthouse_map = ('id', 'com.lizihang.powerapp:id/mapRl')  # 二手房详情中地图找房
    renthouse_share = ('id', "com.lizihang.powerapp:id/rl_title_bar_right_icon")  # 分享
    renthouse_top = ('id', "com.lizihang.powerapp:id/iv")  # 二手房详情顶部轮播图

    renthouse_title = ('id', "com.lizihang.powerapp:id/tv_houseTitle")  # 二手房详情标题，页中的标题
    renthouse_price = ('id', "com.lizihang.powerapp:id/tv_price")  # 二手房详情价格
    resblock_click_show = ('id', "com.lizihang.powerapp:id/tvClickShow")  # 楼盘攻略，点击查看

    renthouse_del = ('xpath', '//android.widget.LinearLayout[@content-desc="房源详情"]')  # 房源详情tap
    renthouse_showing = ('xpath', '//android.widget.LinearLayout[@content-desc="带看"]')  # 带看tap
    showing_feedback = ('xpath', '//android.widget.LinearLayout[@content-desc="带看反馈"]')  # 带客反馈tap
    follow_record = ('xpath', '//android.widget.LinearLayout[@content-desc="跟进记录"]')  # 跟进记录tap

    renthouse_more = ('id', 'com.lizihang.powerapp:id/tvRentMore')  # 二手房详情中更多
    renthouse_A = ('id', 'com.lizihang.powerapp:id/tvA')  # 二手房详情中更多之取消A案
    renthouse_close = ('id', 'com.lizihang.powerapp:id/tv_close')  # 二手房详情中更多之关闭ID

    renthouse_follow = ('id', 'com.lizihang.powerapp:id/tvRentFollow')  # 二手房详情中录跟进
    renthouse_upload = ('id', 'com.lizihang.powerapp:id/tvRentUploadVideo')  # 二手房详情中上传图片/视频
    renthouse_contact = ('id', 'com.lizihang.powerapp:id/tvRentContact')  # 二手房详情中联系顾问

    # 获取房源标题
    def get_house_title(self):
        return self.my_find_element(*self.renthouse_title)
        # print("获取二手房标题了")

    # 报价
    def get_house_price(self):
        return self.my_find_element(*self.renthouse_price).text

