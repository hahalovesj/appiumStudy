# coding = utf-8

# 定义元素
from page.base_page import BasePage

"""
微聊神器
"""


class ChatArtifactPage(BasePage):
    # 微聊神器
    # 二手房tap
    second_left = ('id', 'com.lizihang.powerapp:id/rb_left')
    # 新房tap
    onehand_right = ('id', 'com.lizihang.powerapp:id/rb_right')

    # 第一时间回复：重点提示
    step1_tip = ('id', 'com.lizihang.powerapp:id/tv_tip')
    # 第一时间回复：重点提示内容 及 自我介绍内容
    step1_contents = ('id', 'com.lizihang.powerapp:id/tv_content')
    # 自我介绍模板
    step1_introduce = ('id', 'com.lizihang.powerapp:id/tv_title')
    # 查看更多
    step1_more = ('id', 'com.lizihang.powerapp:id/tv_more')
    # 复制话术
    step1_copy = ('id', 'com.lizihang.powerapp:id/tv_copy')

    # 左侧目录，多个（红宝书20问，step1...step11）
    menu_lists = ('id', 'com.lizihang.powerapp:id/ll_icon')

    # 微聊流程
    chat_flow = ('id', 'com.lizihang.powerapp:id/tv_title_bar_right_text')

    # 获得微聊流程
    def get_chat_flow(self):
        return self.my_find_element(*self.chat_flow).text

    # 获得红宝书20问,i=0;1第一时间回复；2介绍房源；3介绍同盘在售房；4介绍楼盘；5介绍商圈；6Hmall盘；7推荐一手A+；8追求结果；9介绍公司个人
    def get_menu_text(self, i):
        return self.my_find_elements(*self.menu_lists)[i].text

    # 获取查看更多
    def get_step1_more(self):
        return self.my_find_element(*self.step1_more)

    # 获取复制话术
    def get_step1_copy(self):
        return self.my_find_element(*self.step1_copy)



