# coding = utf-8
from page.base_page import BasePage

'''
Hmall
'''


class HmallPage(BasePage):
    # 总数
    total_res = ('id', 'com.lizihang.powerapp:id/tv_statics')
    # 楼盘名称们
    res_names = ('id', 'com.lizihang.powerapp:id/tvResblockName')

    # 获取统计总数
    def get_total_res(self):
        return self.my_find_element(*self.total_res).text
