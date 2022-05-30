# coding = utf-8

# 定义元素
from page.base_page import BasePage
"""
二手房详情
"""


class SecondHandDelPage(BasePage):
    # 二手房详情元素
    secondhand_top_title = ('id', "com.lizihang.powerapp:id/tv_title_text")  # 二手房详情顶部房屋title
    secondhand_map = ('id', 'com.lizihang.powerapp:id/mapRl')  # 二手房详情中地图找房
    secondhand_share = ('id', "com.lizihang.powerapp:id/rl_title_bar_right_icon")  # 分享
    secondhand_top = ('id', "com.lizihang.powerapp:id/iv")  # 二手房详情顶部轮播图

    secondhand_title = ('id', "com.lizihang.powerapp:id/tv_houseTitle")  # 二手房详情标题，页中的标题
    secondhand_price = ('id', "com.lizihang.powerapp:id/tv_price")  # 二手房详情价格
    resblock_click_show = ('id', "com.lizihang.powerapp:id/tvClickShow")  # 楼盘攻略，点击查看

    house_del = ('xpath', '//android.widget.LinearLayout[@content-desc="房源详情"]')  # 房源详情tap
    showing = ('xpath', '//android.widget.LinearLayout[@content-desc="带看"]')  # 带看tap
    showing_feedback = ('xpath', '//android.widget.LinearLayout[@content-desc="带看反馈"]')  # 带客反馈tap
    follow_record = ('xpath', '//android.widget.LinearLayout[@content-desc="跟进记录"]')  # 跟进记录tap

    secondhand_more = ('id', 'com.lizihang.powerapp:id/tvMore')  # 二手房详情中更多
    secondhand_sale_home = ('id', 'com.lizihang.powerapp:id/tvOnSaleProperty')  # 二手房详情中更多之在售房源表
    secondhand_img = ('id', 'com.lizihang.powerapp:id/tvGoPuzzle')  # 二手房详情中更多之去拼图
    secondhand_download = ('id', 'com.lizihang.powerapp:id/tvDLPic')  # 二手房详情中更多之去下载照片
    secondhand_A = ('id', 'com.lizihang.powerapp:id/tvA')  # 二手房详情中更多之取消A案
    secondhand_focus = ('id', 'com.lizihang.powerapp:id/tvFocus')  # 二手房详情中更多之取消聚焦
    secondhand_close = ('id', 'com.lizihang.powerapp:id/tv_close')  # 二手房详情中更多之关闭ID

    secondhand_follow = ('id', 'com.lizihang.powerapp:id/tvFollow')  # 二手房详情中录跟进
    secondhand_upload = ('id', 'com.lizihang.powerapp:id/tvUploadVideo')  # 二手房详情中上传图片/视频
    secondhand_contact = ('id', 'com.lizihang.powerapp:id/tvContact')  # 二手房详情中联系顾问

    # 获取房源标题
    def get_house_title(self):
        return self.my_find_element(*self.secondhand_title)
        # print("获取二手房标题了")

    # 报价
    def get_house_price(self):
        return self.my_find_element(*self.secondhand_price).text


