# coding = utf-8
from page.base_page import BasePage

'''
洗盘详情
'''


class DishWashingdelPage(BasePage):
    # 标题-房屋名称
    house_name = ('id', 'com.lizihang.powerapp:id/tv_title_text')
    # 业主信息 修改
    owner_info_modify = ('id', 'com.lizihang.powerapp:id/modifyOwnerInfo')
    # 业主姓名
    owner_name = ('id', 'om.lizihang.powerapp:id/linkmanName')
    # 与业主关系
    owner_relation = ('id', 'com.lizihang.powerapp:id/relationshipCode')
    # 房屋全名
    house_whole_name = ('id', 'com.lizihang.powerapp:id/houseWholeName')

    # 获得项目名称
    def get_house_name(self):
        return self.my_find_element(*self.house_name)

    # 获得业主信息修改
    def get_owner_info_modify(self):
        return self.my_find_element(*self.owner_info_modify).text


