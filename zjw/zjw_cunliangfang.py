#!/usr/bin/python3
# -*- coding:utf-8 -*-

"""
住建委存量房网上签约爬虫
"""
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from selenium import webdriver  # 导入webdriver包
import time

driver = webdriver.Chrome()

driver.maximize_window()  # 最大化浏览器

time.sleep(1)  # 暂停1秒钟
flag = 0  # 页面打开标志

lst1 = []  # 存储表格1内容
lst2 = []  # 存储表格2内容
lst3 = []  # 存储表格3内容
# 打开住建委网站
try:
    driver.get('http://zjw.beijing.gov.cn/bjjs/fwgl/fdcjy/index.shtml')
    time.sleep(5)  # 暂停1秒钟
except:
    print("网页打开失败！")
try:
    driver.find_element_by_xpath('//*[@id="newheader-top"]/div[1]/a/img')
    flag = 1
except:
    print("定位表格失败！")

if flag == 1:
    iframe = driver.find_element_by_tag_name("iframe")
    driver.switch_to.frame(iframe)

    # 期房网上签约
    title1 = driver.find_element_by_xpath('//*[@id="8d20a443cc644bf989520d07c0815306"]/div[2]/div/div[1]/h3').text
    # 现房网上签约
    title2 = driver.find_element_by_xpath('//*[@id="8d20a443cc644bf989520d07c0815306"]/div[2]/div/div[2]/h3').text
    # 存量房网上签约
    title3 = driver.find_element_by_xpath('//*[@id="8d20a443cc644bf989520d07c0815306"]/div[2]/div/div[3]/h3').text

    # 期房表
    table1 = driver.find_element_by_xpath('//*[@id="8d20a443cc644bf989520d07c0815306"]/div[2]/div/div[1]/table')
    # 现房表
    table2 = driver.find_element_by_xpath('//*[@id="8d20a443cc644bf989520d07c0815306"]/div[2]/div/div[2]/table')
    # 存量房表
    table3 = driver.find_element_by_xpath('//*[@id="8d20a443cc644bf989520d07c0815306"]/div[2]/div/div[3]/table')

    # 获取表格1各个格内容
    tds1 = table1.find_elements_by_tag_name("td")
    # 获取表格2各个格内容
    tds2 = table2.find_elements_by_tag_name("td")
    # 获取表格3各个格内容
    tds3 = table3.find_elements_by_tag_name("td")

    # 循环表格1内容文本
    for td1 in tds1:
        lst1.append(td1.text)
    print(lst1)
    # 循环表格2内容文本
    for td2 in tds2:
        lst2.append(td2.text)
    print(lst2)
    # 循环表格3内容文本
    for td3 in tds3:
        lst3.append(td3.text)
    print(lst3)

    # 第三方 SMTP 服务
    # mail_host="smtp.XXX.com"  # 设置服务器
    mail_host = "mail.lizihang.com"
    mail_user = "shenjing@lizihang.com"  # 用户名
    mail_pass = "landz@123"  # 口令

    sender = 'shenjing@lizihang.com'  # 发送邮件
    receivers = ['shenjing@lizihang.com']  # 接收邮件，wangyuling@lizihang.com

    mail_msg = """
    <h3>"""+title1+"""</h3>
    <table>
      <tr>
        <td>网上签约套数：</td>
        <td>""" + lst1[1] + """</td>
      </tr>
      <tr>
        <td>网上签约面积：</td>
        <td>""" + lst1[3] + """</td>
      </tr>
      <tr>
        <td>住宅签约套数：</td>
        <td>""" + lst1[5] + """</td>
      </tr>
      <tr>
        <td>住宅签约面积：</td>
        <td>""" + lst1[7] + """</td>
      </tr>
    </table>
    
    <h3>"""+title2+"""</h3>
    <table>
      <tr>
        <td>网上签约套数：</td>
        <td>""" + lst2[1] + """</td>
      </tr>
      <tr>
        <td>网上签约面积：</td>
        <td>""" + lst2[3] + """</td>
      </tr>
      <tr>
        <td>住宅签约套数：</td>
        <td>""" + lst2[5] + """</td>
      </tr>
      <tr>
        <td>住宅签约面积：</td>
        <td>""" + lst2[7] + """</td>
      </tr>
    </table>
    
    <h3>"""+title3+"""</h3>
    <table>
      <tr>
        <td>网上签约套数：</td>
        <td>""" + lst3[1] + """</td>
      </tr>
      <tr>
        <td>网上签约面积：</td>
        <td>""" + lst3[3] + """</td>
      </tr>
      <tr>
        <td>住宅签约套数：</td>
        <td>""" + lst3[5] + """</td>
      </tr>
      <tr>
        <td>住宅签约面积：</td>
        <td>""" + lst3[7] + """</td>
      </tr>
    </table>
       
    <p><a href="http://zjw.beijing.gov.cn/bjjs/fwgl/fdcjy/index.shtml">这是北京市住房和城乡建设委员会网站链接</a></p>"""


    # message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
    message = MIMEText(mail_msg, 'html', 'utf-8')
    message['From'] = Header("邮件自动发送--网上签约数据", 'utf-8')
    message['To'] = Header("王玉玲", 'utf-8')

    subject = '住建委爬取网上签约数据'
    message['Subject'] = Header(subject, 'utf-8')

    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print("邮件发送成功")
    except smtplib.SMTPException:
        print("Error: 无法发送邮件")

driver.quit()
