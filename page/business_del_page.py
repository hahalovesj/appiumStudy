# coding = utf-8

from page.base_page import BasePage
"""
商圈攻略详情
"""


class BusinessDelPage(BasePage):
    # 商圈攻略元素
    business_title = ('xpath', '//*[@id="card_0"]/div/h2')  # 商圈攻略标题

    # 商圈攻略标题
    def get_house_title(self) -> str:
        self.switch_to_h5()
        return self.my_find_element(*self.business_title).text
