# coding = utf-8
from time import sleep
from page.base_page import BasePage


'''
报备管理 
'''


class ProjectManagePage(BasePage):
    # 搜索框
    search_et = ('id', 'com.lizihang.powerapp:id/et')
    # 报备时间，项目，报备状态，更多  -- 下拉筛选项
    report_options = ('id', 'com.lizihang.powerapp:id/ll_ev')
    # 待回访，今日未拨打，今日未接通 --快捷筛选
    report_fast_opts = ('id', 'com.lizihang.powerapp:id/tvItem')
    # 统计信息
    report_total = ('id', 'com.lizihang.powerapp:id/tv_statics')
    # 报备编号-可能多个
    report_code = ('id', 'com.lizihang.powerapp:id/tv_reporcode')
    # 预计到访时间
    visit_time = ('id', 'com.lizihang.powerapp:id/tv_createtime')
    # 报备项目
    report_project_name = ('id', 'com.lizihang.powerapp:id/tv_reportproject')
    # 负责按钮
    report_copy = ('id', 'com.lizihang.powerapp:id/tv_copy')
    # 首访复访
    visit_type = ('id', 'com.lizihang.powerapp:id/tv_itemvalue')
    # 确认报备信息-需要判断在不在
    visit_type = ('id', 'com.lizihang.powerapp:id/tv_itemvalue')
    # 录到访-需要判断在不在
    visit_type = ('id', 'com.lizihang.powerapp:id/record_visit')
    # 未到访-需要判断在不在
    visit_type = ('id', 'com.lizihang.powerapp:id/not_visit')
    # 录回访-需要判断在不在
    visit_type = ('id', 'com.lizihang.powerapp:id/return_visit')

    # 搜索框
    def get_search_et(self):
        return self.my_find_element(*self.search_et)

    # 报备名称
    def get_report_project_name(self) -> list:
        return self.my_find_elements(*self.report_project_name)[0]


