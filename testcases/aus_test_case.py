import unittest
import time
from appium.webdriver.common.mobileby import MobileBy




from appium import webdriver


class Driver:

    def __init__(self):

        desired_caps = {
                "platformName": "Android",
                "platformVersion": "7.0",
                "app": "/home/ors/Downloads/Telegram Desktop/ausweis.apk",
                "deviceName": "be802940",
                "appActivity": "io.ausweis.features.onboarding.OnboardingActivity",
                "appPackage": "eu.tiwlab.ausweis",
                "noReset": "True",
                "automationName": "uiautomator2"
        }

        self.instance = webdriver.Remote("http://0.0.0.0:4723/wd/hub", desired_caps)


class AusTestCases(unittest.TestCase):

    def setUp(self):
        self.driver = Driver()

    def test_calculator_launches(self):
        self.driver.instance.find_element(MobileBy.ID, "eu.tiwlab.ausweis:id/start").click()
        time.sleep(1)
        self.driver.instance.find_element(MobileBy.XPATH,
                                          "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/"
                                          "android.widget.FrameLayout/android.widget.LinearLayout"
                                          "/android.widget.FrameLayout/android.view.ViewGroup/"
                                          "android.widget.LinearLayout[1]/android.widget.FrameLayout/"
                                          "android.widget.EditText").send_keys('i.orsyk+1@ausweis.io')
        self.driver.instance.find_element(MobileBy.XPATH,
                                          "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/"
                                          "android.widget.FrameLayout/android.widget.LinearLayout"
                                          "/android.widget.FrameLayout/android.view.ViewGroup/"
                                          "android.widget.LinearLayout[2]/android.widget.FrameLayout/"
                                          "android.widget.EditText").send_keys('pepsicola')
        self.driver.instance.find_element(MobileBy.XPATH,
                                          "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/"
                                          "android.widget.FrameLayout/android.widget.LinearLayout/"
                                          "android.widget.FrameLayout/android.view.ViewGroup/"
                                          "android.widget.Button[3]").click()

        time.sleep(4)

    def tearDown(self):
        self.driver.instance.quit()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(AusTestCases)
    unittest.TextTestRunner(verbosity=2).run(suite)