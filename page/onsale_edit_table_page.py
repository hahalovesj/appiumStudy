# coding = utf-8
from page.base_page import BasePage

"""
在售房源表-编辑在售房源表格页
"""


class OnsaleEditTablePage(BasePage):

    # 编辑表格
    # 页面title，编辑表格
    page_title = ('id', 'com.lizihang.powerapp:id/tv_title_center')
    # 表格-序号，多个
    table_num = ('id', 'com.lizihang.powerapp:id/tv_num')
    # 表格-楼盘名称，多个
    table_resblock_name = ('id', 'com.lizihang.powerapp:id/tv_resblockName')
    # 表格-居室，多个
    table_rooms = ('id', 'com.lizihang.powerapp:id/tv_room')
    # 提示信息
    table_rooms = ('id', 'com.lizihang.powerapp:id/tv_change')

    # 获取标题
    def get_title(self):
        return self.my_find_element(*self.page_title)

    # 获取楼盘名称
    def get_resblock_name(self):
        return self.my_find_elements(*self.table_resblock_name)[1]



