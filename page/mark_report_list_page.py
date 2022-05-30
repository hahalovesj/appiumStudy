# coding = utf-8
from page.base_page import BasePage

'''
市场报告列表
'''


class MarkReportListPage(BasePage):
    # 城市报告标题
    city_title = ('id', 'com.lizihang.powerapp:id/groupNameTv')
    # 城市报告-查看全部
    city_all_report = ('id', 'com.lizihang.powerapp:id/see_all_tv')
    # 城市报告-lists
    city_report_lists = ('id', 'com.lizihang.powerapp:id/report_item_view')

    # 获取城市报告标题
    def get_city_title(self):
        return self.my_find_element(*self.city_title).text
