# coding = utf-8
from page.base_page import BasePage

'''
带看记录
'''


class ShowRecordPage(BasePage):
    # 标题
    page_title = ('id', 'com.lizihang.powerapp:id/tv_title_text')
    # 统计
    total_records = ('id', 'com.lizihang.powerapp:id/tv_statics')
    # 记录
    total_showing = ('id', 'com.lizihang.powerapp:id/tv_statics')

    # 页面标题
    def get_page_title(self):
        self.wait_element_located(self.page_title)
        return self.my_find_element(*self.page_title)

    # 获得统计字段
    def get_total_showing(self):
        self.wait_element_located(self.total_showing)
        return self.my_find_element(*self.total_showing).text
