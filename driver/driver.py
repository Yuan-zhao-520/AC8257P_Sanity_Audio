#coding=utf-8
__author__ = "Yuan_Zhao"
from appium import webdriver

class AppiumTest():
    def __init__(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '9'
        desired_caps['deviceName'] = '0123456789ABCDEF'
        desired_caps['appPackage'] = 'com.android.music'
        desired_caps['appActivity'] = 'com.android.music.MusicBrowserActivity'
        desired_caps['noReset'] = True
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        # 等主页面activity出现
        self.driver.wait_activity("com.android.music.MusicBrowserActivity", 3)

    def get_driver(self):
        return self.driver