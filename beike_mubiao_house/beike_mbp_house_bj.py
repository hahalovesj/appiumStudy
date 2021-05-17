#!/usr/bin/python3
# -*- coding:utf-8 -*-
import smtplib
import sys
import io
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from selenium import webdriver  # 导入webdriver包
import time
import xlrd
import xlwt
import datetime

start = time.perf_counter()  # 程序开始时间
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')

# 创建数据存储文件workbook 设置编码
workbookwt = xlwt.Workbook(encoding='utf-8')
# 创建worksheet
worksheet_bj = workbookwt.add_sheet('北京')

# 打开读取文件
workbookrd = xlrd.open_workbook(r'D:\shenjing\pythonWorkplace\beike_mubiao_house\beike_mubiaopan_housebj2021-05-14.xls')
# 根据sheet索引或者名称获取sheet内容
bj_list2 = workbookrd.sheet_by_name('北京')
# 北京sheet的url内容
bj_list = bj_list2.col_values(1)
print(bj_list)

driver = webdriver.Chrome()
driver.maximize_window()  # 最大化浏览器
flag = 1  # 成功标志
for url in bj_list:
    try:
        driver.get(url)
        print(url)
        time.sleep(4)  # 留出加载时间
        flag = 1
    except:
        flag = 0
        print(url + "页面打卡失败或数据错误！")
    if flag:
        try:
            # 获取房源详情数据，总价，均价，房屋户型，所在楼层，建筑面积，小区名称，贝壳编号，套内面积(可能没有)，挂牌时间，
            # 小区
            xiaoqu = driver.find_element_by_xpath('//*[@id="beike"]/div[1]/div[4]/div[1]/div[2]/div[4]/div[1]/a[1]').text
            print(xiaoqu)
            # 总价
            total2 = driver.find_element_by_xpath(
                "//*[@id='beike']/div[1]/div[4]/div[1]/div[2]/div[2]/span[1]").text
            total = "总价" + total2 + "万"  # 组装字段
            print(total)
            # 均价
            unitPrice2 = driver.find_element_by_xpath(
                '//*[@id="beike"]/div[1]/div[4]/div[1]/div[2]/div[2]/div[1]/div[1]/span').text
            unitPrice = "均价" + unitPrice2 + "元/平米"
            print(unitPrice)
            # 房屋户型              //*[@id="beike"]/div[1]/div[4]/div[1]/div[2]/div[3]/div[1]/div[1]
            houseType = driver.find_element_by_xpath(
                '//*[@id="beike"]/div[1]/div[4]/div[1]/div[2]/div[3]/div[1]/div[1]').text
            print(houseType)
            # 所在楼层
            floor = driver.find_element_by_xpath(
                '//*[@id="beike"]/div[1]/div[4]/div[1]/div[2]/div[3]/div[1]/div[2]').text
            print(floor)
            # 建筑面积
            outArea = driver.find_element_by_xpath(
                '//*[@id="beike"]/div[1]/div[4]/div[1]/div[2]/div[3]/div[3]/div[1]').text
            print(outArea)
            # 贝壳编号
            houseRecord2 = driver.find_element_by_xpath(
                '//*[@id="beike"]/div[1]/div[4]/div[1]/div[2]/div[4]/div[4]/span[2]').text
            houseRecord = houseRecord2[:-2]  # 去掉结尾“举报”两个字
            print(houseRecord)
            # 套内面积(可能没有)
            innerArea = driver.find_element_by_xpath('//*[@id="introduction"]/div/div/div[1]/div[2]/ul/li[4]').text
            print(innerArea)
            # 挂牌时间
            onTime = driver.find_element_by_xpath("//*[@id = 'introduction']/div/div/div[2]/div[2]/ul/li[1]").text
            print(onTime)

            # 写入excel ，参数对应 行, 列, 值
            worksheet_bj.write(bj_list.index(url), 0, label=xiaoqu)  # 小区
            worksheet_bj.write(bj_list.index(url), 1, label=total)  # 总价
            worksheet_bj.write(bj_list.index(url), 2, label=unitPrice)  # 均价
            worksheet_bj.write(bj_list.index(url), 3, label=houseRecord)  # 贝壳编号
            worksheet_bj.write(bj_list.index(url), 4, label=houseType)  # 房屋户型
            worksheet_bj.write(bj_list.index(url), 5, label=floor)  # 所在楼层
            worksheet_bj.write(bj_list.index(url), 6, label=outArea)  # 建筑面积
            worksheet_bj.write(bj_list.index(url), 7, label=innerArea)  # 套内面积
            worksheet_bj.write(bj_list.index(url), 8, label=onTime)  # 挂牌时间
        except:
            print(url+"页面数据错误！")

time.sleep(1)  # 暂停1秒钟


# 时间参数
nowTime = datetime.datetime.now().strftime('%Y-%m-%d')  # 现在
# 保存
file_name = 'beike_house_bj' + nowTime + '.xls'
workbookwt.save(file_name)

'''
# 第三方 SMTP 服务
# mail_host="smtp.XXX.com"  #设置服务器
mail_host = "mail.lizihang.com"
mail_user = "shenjing@lizihang.com"  # 用户名
mail_pass = "landz@123"  # 口令

sender = 'shenjing@lizihang.com'  # 发送邮件
receivers = ['shenjing@lizihang.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱，'wangyuling@lizihang.com'，'zhenghaiyan@lizihang.com'

message = MIMEMultipart()

# 文本内容
mail_msg = """
<h2>贝壳责任盘数据</h2>
<p><a href="https://bj.ke.com/">这是贝壳网链接</a></p>"""
textApart = MIMEText(mail_msg, 'html', 'utf-8')
message.attach(textApart)

# 构造附件
exl_file = open(r'D:\shenjing\vsCodeWorkplace\beike\%s' % file_name, 'rb').read()
exl = MIMEText(exl_file, 'base64', 'utf-8')
exl["Content-Type"] = 'application/octet-stream'
# 以下代码可以重命名附件为Excel_test.xls
exl.add_header('Content-Disposition', 'attachment', filename=file_name)
message.attach(exl)

message['From'] = Header("邮件自动发送--贝壳目标盘数据", 'utf-8')
message['To'] = Header("王玉玲", 'utf-8')
message['Subject'] = Header('贝壳目标盘', 'utf-8')

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("邮件发送成功")
except smtplib.SMTPException:
    print("Error: 无法发送邮件")
'''

driver.quit()

end = time.perf_counter()  # 结束时间 单位秒
print("运行耗时", int(end - start)/60)  # 北京楼盘+房屋 运行耗时 23997.9224209

# 北京楼盘运行耗时 939.9924796
# 三地楼盘 运行耗时 1402.1540671999999
