# coding = utf-8
from page.base_page import BasePage

'''
多盘多房转发-房源选择页-待分享清单
'''


class MultiHouseSharePickPage(BasePage):

    # 待分享清单-标题
    share_title = ('id', 'com.lizihang.powerapp:id/tvTitle')
    # 分享历史
    share_history = ('id', 'com.lizihang.powerapp:id/tvHistory')
    # 楼盘排序
    loupan_sort = ('id', 'com.lizihang.powerapp:id/tvRight')
    # 一键清空
    key_to_empty = ('id', 'com.lizihang.powerapp:id/tvLeft')
    # 楼盘list
    loupan_lists = ('id', 'com.lizihang.powerapp:id/rlItem')
    # 新盘标签 多个
    onehand_icons = ('id', 'com.lizihang.powerapp:id/tvTypeNew')
    # 二手标签，多个
    second_icons = ('id', 'com.lizihang.powerapp:id/tvTypeSecond')
    # 项目状态，多个
    loupan_status = ('id', 'com.lizihang.powerapp:id/tvStatuss')
    # 楼盘名称,多个
    loupan_names = ('id', 'com.lizihang.powerapp:id/tvResblockName')
    # 添加新盘
    add_onehand = ('id', 'com.lizihang.powerapp:id/tvAddNewHouse2')
    # 添加二手房
    add_secondhand = ('id', 'com.lizihang.powerapp:id/tvAddSecondHouse2')
    # 分享微信片
    share_wechat_piece = ('id', 'com.lizihang.powerapp:id/tvShare')

    # 获取待分享清单标题
    def get_share_title(self):
        return self.my_find_element(*self.share_title).text
