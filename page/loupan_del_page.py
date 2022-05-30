# coding = utf-8

# 定义元素
from appium.webdriver import WebElement

from page.base_page import BasePage


class LoupanDelPage(BasePage):
    # 楼盘攻略元素
    # 顶部轮播图
    loupan_top = ('id', 'com.lizihang.powerapp:id/iv')
    # 楼盘名称
    loupan_title = ('id', 'com.lizihang.powerapp:id/tv_resblock_name')


    # 二手报价标题
    second_price_tip = ('id', 'com.lizihang.powerapp:id/tv_second_price_tip')
    # 二手报价
    second_price = ('id', 'com.lizihang.powerapp:id/tv_second_price')
    # 二手均价标题
    second_avg_tip = ('id', 'com.lizihang.powerapp:id/tv_second_avg_tip')
    # 二手均价
    second_avg = ('id', 'com.lizihang.powerapp:id/tv_second_avg')

    # 新房报价标题
    new_price_tip = ('id', 'com.lizihang.powerapp:id/tv_new_price_tip')
    # 新房报价
    new_price = ('id', 'com.lizihang.powerapp:id/tv_new_price')
    # 新房均价标题
    new_avg_tip = ('id', 'com.lizihang.powerapp:id/tv_new_avg_tip')
    # 新房均价
    new_avg = ('id', 'com.lizihang.powerapp:id/tv_new_avg')

    # 优缺点标题栏
    pros_cons_title = ('id', 'com.lizihang.powerapp:id/tv_item_title')

    # 目录
    drawer_open = ('id', 'com.lizihang.powerapp:id/iv_drawer_open')

    # 去拼图
    go_puzzle = ('id', 'com.lizihang.powerapp:id/tvGoPuzzle')
    # 下周图片
    download_pic = ('id', 'com.lizihang.powerapp:id/tvDLPic')
    # 在售房源表
    onsale_table = ('id', 'com.lizihang.powerapp:id/tvOnSaleProperty')
    # 一键制作微信片
    make_wechat_pic = ('id', 'com.lizihang.powerapp:id/tv_make')

    # 获得标题
    def get_loupan_title(self):
        return self.my_find_element(*self.loupan_title)

    # 获得二手报价
    def get_second_price(self):
        return self.my_find_element(*self.second_price).text


