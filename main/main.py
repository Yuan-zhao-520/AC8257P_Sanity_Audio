import unittest
import HTMLTestRunner_PY3
import time

dir = 'C:/Program Files/JetBrains/PyCharm 2019.1.3/appiumpython/testcase'
suite = unittest.defaultTestLoader.discover(start_dir=dir,pattern='sanity_audio.py')

if __name__ == '__main__':
    # 选择指定时间格式
    timestr = time.strftime('%Y-%m-%d%H%M%S', time.localtime(time.time()))
    html_file = "C:/Program Files/JetBrains/PyCharm 2019.1.3/appiumpython/report/Sanity_Audio_"+ timestr +".html"
    Report = open(html_file, 'wb')
    runner = HTMLTestRunner_PY3.HTMLTestRunner(stream=Report,
                                               verbosity=10,
                                               title='audio_sanity自动化测试报告',
                                               description='执行人：Yuan')
    runner.run(suite)
    Report.close()