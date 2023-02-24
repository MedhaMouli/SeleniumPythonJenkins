import unittest
from selenium import webdriver
import time

class MyTestCase(unittest.TestCase):
    def test_launch_browser(self):
        filePath = "C:\\Users\\KMEDHASR\\Downloads\\chromedriver_win32\\chromedriver.exe"

        #global driver
        # If you will make driver global then you need to close/quit the browser explicitly

        driver = webdriver.Chrome(filePath)
        time.sleep(2)

        # No need to close/quit the browser as browser will close automatically
        #driver.quit()

    if __name__ == '__main__':
        unittest.main()