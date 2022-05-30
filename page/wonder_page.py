# coding = utf-8
from time import sleep

from page.base_page import BasePage
from page.dishwashing_del_page import DishWashingdelPage
from page.house_trend_del_page import HouseTrenddelPage
from page.share_locus_del_page import ShareLocusDelPage

'''
Wonder页
'''


class WonderPage(BasePage):
    # 公司名称
    page_title = ('id', 'com.lizihang.powerapp:id/tv_group_name')
    # 通话记录
    call_record = ('id', 'com.lizihang.powerapp:id/tong_hua')
    # 短信
    message = ('id', 'com.lizihang.powerapp:id/duan_xin')
    # 微信记录
    wechat_record = ('id', 'com.lizihang.powerapp:id/wei_xin')
    # 敏感词记录
    mingan_record = ('id', 'com.lizihang.powerapp:id/min_gan_ci')
    # 顾问轨迹
    em_track = ('id', 'com.lizihang.powerapp:id/gui_ji')
    # 今日电话量-标题
    call_today_title = ('id', 'com.lizihang.powerapp:id/phone_org_name_tv')
    # 新增电话
    call_new = ('id', 'com.lizihang.powerapp:id/add_phone_ount_tv')
    # 呼出电话
    call_out = ('id', 'com.lizihang.powerapp:id/call_out_count_tv')

    # 今日微信量-标题
    wechat_title = ('id', 'com.lizihang.powerapp:id/wei_xin_org_name_tv')
    # 好友数
    friend_count = ('id', 'com.lizihang.powerapp:id/link_count_tv')

    # 今日私信微信覆盖率
    wechat_coverage_today = ('id', 'com.lizihang.powerapp:id/wei_xin_org_name_tv')
    # 私客微信覆盖率
    wechat_coverage = ('id', 'com.lizihang.powerapp:id/customNumTv')

    # 获得今日电话量标题
    def get_call_today_title(self):
        return self.my_find_element(*self.call_today_title).text


