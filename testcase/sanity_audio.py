import unittest
import time
import warnings
import os
import sys
sys.path.append('C:\\Program Files\\JetBrains\\PyCharm 2019.1.3\\appiumpython')
from driver.driver import AppiumTest

driver = AppiumTest().get_driver()

# 点击songs列表
time.sleep(1)
element1 = driver.find_element_by_id("com.android.music:id/songtab")
element1.click()
time.sleep(1)
# 进入播放界面
driver.tap([(23, 148), (974, 213)], 100)
time.sleep(1)
# 设置单曲循环
ele = driver.find_element_by_id('com.android.music:id/repeat_menu_item')
ele.click()
time.sleep(1)
ele.click()
path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
class MyTestCase(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)
        print('Start')

    def tearDown(self):
        print('End')

    # 获取歌曲名称
    def music_name(self):
        element1 = driver.find_element_by_id('com.android.music:id/trackname')
        name = element1.text
        return name

    #执行Seek操作
    def Seek(self):
        driver.tap([(296, 577), (310, 582)], 100)
        time.sleep(1)
        driver.tap([(496, 577), (510, 582)], 100)
        time.sleep(1)
        driver.tap([(80, 577), (100, 582)], 100)

    #执行下曲切换
    def Next_music(self):
        # 切换下一曲
        element3 = driver.find_element_by_id('com.android.music:id/next')
        element3.click()
        time.sleep(1)

    #执行上一曲切换
    def Prv_music(self):
        element4 = driver.find_element_by_id('com.android.music:id/prev')
        element4.click()
        time.sleep(1)

     #执行播放暂停操作
    def Play_Pause(self):
        element2 = driver.find_element_by_id('com.android.music:id/pause')
        element2.click()
        time.sleep(1)
        element2.click()

    def test_53_MP3_MPEG1_L3(self):
        #点击Play按钮
        self.Play_Pause()
        #seek操作
        self.Seek()
        # 截图
        driver.get_screenshot_as_file(path +'\\images\\Sanity_Test_053\\' + self.music_name() + '.png')
        #切换下一曲
        self.Next_music()
        #判定切换下一曲是否成功
        try:
            self.assertEqual(self.music_name(), "02_MPEG2_AAC_LC_44.1KHz_2ch_VBR_ADTS", '测试未通过')
            #切换上一曲
            self.Prv_music()
            #判定切换上一曲是否成功
            self.assertEqual(self.music_name(), "MPEG1_L3_44.1KHz_320Kbps_2ch", '测试未通过')
            # 切换下一曲
            self.Next_music()
         except:
            


    def test_55_AAC_MPEG2_AAC_LC(self):
        #点击Play按钮
        self.Play_Pause()
        #seek操作
        self.Seek()
        # 截图
        driver.get_screenshot_as_file(path + '\\images\\Sanity_Test_055\\' + self.music_name() + '.png')
        # 切换下一曲
        self.Next_music()
        # 判定切换下一曲是否成功
        self.assertEqual(self.music_name(), "03_Vorbis_44.1KHz_320Kbps_2ch_CBR_LibVorbis1.0.1", '测试未通过')
        # 切换上一曲
        self.Prv_music()
        # 判定切换上一曲是否成功
        self.assertEqual(self.music_name(), "02_MPEG2_AAC_LC_44.1KHz_2ch_VBR_ADTS", '测试未通过')
        # 切换下一曲
        self.Next_music()

    def test_56_OGG_Vorbis(self):
        # 点击Play按钮
        self.Play_Pause()
        # seek操作
        self.Seek()
        # 截图
        driver.get_screenshot_as_file(path + '\\images\\Sanity_Test_056\\' + self.music_name() + '.png')
        # 切换下一曲
        self.Next_music()
        # 判定切换下一曲是否成功
        self.assertEqual(self.music_name(), "04_APE_44.1KHz_952Kbps_2ch_Fast", '测试未通过')
        # 切换上一曲
        self.Prv_music()
        # 判定切换上一曲是否成功
        self.assertEqual(self.music_name(), "03_Vorbis_44.1KHz_320Kbps_2ch_CBR_LibVorbis1.0.1", '测试未通过')
        # 切换下一曲
        self.Next_music()

    def test_57_APE_APE(self):
        # 点击Play按钮
        self.Play_Pause()
        # seek操作
        # 截图
        driver.get_screenshot_as_file(path + '\\images\\Sanity_Test_057\\' + self.music_name() + '.png')
        self.Seek()
        # 切换下一曲
        self.Next_music()
        # 判定切换下一曲是否成功
        self.assertEqual(self.music_name(), "05_FLAC_44.1KHz_849Kbps_2ch_VBR", '测试未通过')
        # 切换上一曲
        self.Prv_music()
        # 判定切换上一曲是否成功
        self.assertEqual(self.music_name(), "04_APE_44.1KHz_952Kbps_2ch_Fast", '测试未通过')
        # 切换下一曲
        self.Next_music()

    def test_58_FLAC_FLAC(self):
        # 点击Play按钮
        self.Play_Pause()
        # seek操作
        self.Seek()
        # 截图
        driver.get_screenshot_as_file(path + '\\images\\Sanity_Test_058\\' + self.music_name() + '.png')
        # 切换下一曲
        self.Next_music()
        # 判定切换下一曲是否成功
        self.assertEqual(self.music_name(), "06_AMR-NB_8000Hz_13bits_5.2Kbps_1ch_CBR", '测试未通过')
        # 切换上一曲
        self.Prv_music()
        # 判定切换上一曲是否成功
        self.assertEqual(self.music_name(), "05_FLAC_44.1KHz_849Kbps_2ch_VBR", '测试未通过')
        # 切换下一曲
        self.Next_music()

    def test_59_ARM_ARM(self):
        # 点击Play按钮
        self.Play_Pause()
        # seek操作
        self.Seek()
        # 截图
        driver.get_screenshot_as_file(path + '\\images\\Sanity_Test_059\\' + self.music_name() + '.png')
        # 切换下一曲
        self.Next_music()
        # 判定切换下一曲是否成功
        self.assertEqual(self.music_name(), "07_PCM_44.1KHz_10.1Kbps_2ch", '测试未通过')
        # 切换上一曲
        self.Prv_music()
        # 判定切换上一曲是否成功
        self.assertEqual(self.music_name(), "06_AMR-NB_8000Hz_13bits_5.2Kbps_1ch_CBR", '测试未通过')
        # 切换下一曲
        self.Next_music()

    def test_60_WMV_PCM(self):
        # 点击Play按钮
        self.Play_Pause()
        # seek操作
        self.Seek()
        # 截图
        driver.get_screenshot_as_file(path + '\\images\\Sanity_Test_060\\' + self.music_name() + '.png')
        # 切换下一曲
        self.Next_music()
        # 判定切换下一曲是否成功
        self.assertEqual(self.music_name(), "08_AMR_16KHz_14bits (15)", '测试未通过')
        # 切换上一曲
        self.Prv_music()
        # 判定切换上一曲是否成功
        self.assertEqual(self.music_name(), "07_PCM_44.1KHz_10.1Kbps_2ch", '测试未通过')
        # 切换下一曲
        self.Next_music()

    def test_61_AWB_AMR(self):
        # 点击Play按钮
        self.Play_Pause()
        # seek操作
        self.Seek()
        # 截图
        driver.get_screenshot_as_file(path + '\\images\\Sanity_Test_061\\' + self.music_name() + '.png')
        # 切换下一曲
        self.Next_music()
        # 判定切换下一曲是否成功
        self.assertEqual(self.music_name(), "09_天天看到你.和弦", '测试未通过')
        # 切换上一曲
        self.Prv_music()
        # 判定切换上一曲是否成功
        self.assertEqual(self.music_name(), "08_AMR_16KHz_14bits (15)", '测试未通过')
        # 切换下一曲
        self.Next_music()

    def test_62_MIDI(self):
        # 点击Play按钮
        self.Play_Pause()
        # seek操作
        self.Seek()
        # 截图
        driver.get_screenshot_as_file(path + '\\images\\Sanity_Test_062\\' + self.music_name() + '.png')
        # 切换下一曲
        self.Next_music()
        # 判定切换下一曲是否成功
        self.assertEqual(self.music_name(), "10_ADPCM_A-LawProfile_CCITT_48.0KHz_8bits_CNB00011098", '测试未通过')
        # 切换上一曲
        self.Prv_music()
        # 判定切换上一曲是否成功
        self.assertEqual(self.music_name(), "09_天天看到你.和弦", '测试未通过')
        # 切换下一曲
        self.Next_music()

    def test_63_WAV_ALAW(self):
        # 点击Play按钮
        self.Play_Pause()
        # seek操作
        self.Seek()
        # 截图
        driver.get_screenshot_as_file(path + '\\images\\Sanity_Test_063\\' + self.music_name() + '.png')
        # 切换下一曲
        self.Next_music()
        # 判定切换下一曲是否成功
        self.assertEqual(self.music_name(), "MPEG1_L3_44.1KHz_320Kbps_2ch", '测试未通过')
        # 切换上一曲
        self.Prv_music()
        # 判定切换上一曲是否成功
        self.assertEqual(self.music_name(), "10_ADPCM_A-LawProfile_CCITT_48.0KHz_8bits_CNB00011098", '测试未通过')
        # 切换下一曲
        self.Next_music()
