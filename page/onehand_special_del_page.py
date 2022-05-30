# coding = utf-8

from page.base_page import BasePage

'''
一手好房 列表
'''


class OnehandSpecialDelPage(BasePage):
    # 一手好房楼盘名称
    project_top = ('id', 'com.lizihang.powerapp:id/house_top_video_view')
    # 一手好房楼盘名称
    project_name = ('id', 'com.lizihang.powerapp:id/resblockNameTv')  
    # 新房轮播图
    project_top = ('id', 'com.lizihang.powerapp:id/house_top_vr_thume')
    # 新房名称
    project_name = ('id', 'com.lizihang.powerapp:id/resblockNameTv')
    # 新房报价
    project_price = ('id', 'com.lizihang.powerapp:id/priceTv')
    # 新房建面
    project_area = ('id', 'com.lizihang.powerapp:id/areaTv')
    # 新房单价
    project_unitprice = ('id', 'com.lizihang.powerapp:id/priceSingleTv')
    # 项目资料
    project_data = ('id', 'com.lizihang.powerapp:id/projectLayout')
    # 在售房源
    project_salehouse = ('id', 'com.lizihang.powerapp:id/saleHouseLayout')
    # 项目区位，城区商圈，开发商，产品类型key值,有多个
    project_key_infos = ('id', 'com.lizihang.powerapp:id/keyTv')
    # 项目区位，城区商圈，开发商，产品类型value值,有多个
    project_value_infos = ('id', 'com.lizihang.powerapp:id/valueTv')

    # 上传图片视频
    picture_upload = ('id', 'com.lizihang.powerapp:id/tvUploadVideo')
    # 销控管理
    marketing_control = ('id', 'com.lizihang.powerapp:id/sellControlTv')
    # 优惠管理
    city_discounts = ('id', 'com.lizihang.powerapp:id/discountTv')
    # 带客管理
    bring_cust = ('id', 'com.lizihang.powerapp:id/customTv')
    
    # 一手项目名称
    def get_project_title(self):
        return self.my_find_element(*self.project_name).text

    # 获得报价
    def get_price(self):
        return self.my_find_element(*self.project_price).text

    # 项目区位
    def get_project_position(self):
        return self.my_find_elements(*self.project_key_infos)[0].text + \
               self.my_find_elements(*self.project_value_infos)[0].text



