# coding = utf-8

# 定义元素
from time import sleep

from appium import webdriver
from page.base_page import BasePage

'''
兰斯博士
'''


class DoctorLandzPage(BasePage):

    # 标题
    landz_title = ('id', 'com.lizihang.powerapp:id/tv_title_bar_title')
    # 快捷模块入口（新人等级考试，税费计算器，贷款计算器，购房套数查询）
    quick_card = ('xpath', '//*[@id="m-B40EA2E7BF134834B83D33051DAABA94"]/div/div/div[1]')
    # 购房资格
    banner1 = ('xpath', '//*[@id="root"]/div/div[3]/div/div[1]/div/div[2]/ul/li[1]/div')
    # 交易流程
    banner2 = ('xpath', '//*[@id="root"]/div/div[3]/div/div[1]/div/div[2]/ul/li[2]/div')

    _driver: webdriver

    # 获得标题
    def get_landz_title(self):
        return self.my_find_element(*self.landz_title)

    # 获取快捷模块入口（新人等级考试）todo 定位不到
    def go_no1_quick_card(self):
        self.switch_to_h5()
        self.my_find_element(*self.banner1).click()
        sleep(3)




