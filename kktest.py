# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class Untitled(unittest.TestCase):
    def setUp(self):
        #self.driver = webdriver.Firefox()

        self.driver = webdriver.Remote(
            command_executor='http://192.168.0.18:7777/wd/hub',
            desired_capabilities={'browserName': 'firefox', 'javascriptEnabled': True},

        )

        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.base_url = "https://play.kkbox.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_untitled(self):
        driver = self.driver
        driver.get(self.base_url + "/explore")
        driver.find_element_by_id("uid").clear()
        driver.find_element_by_id("uid").send_keys("arredeye@hotmail.com")
        driver.find_element_by_id("pwd").clear()
        driver.find_element_by_id("pwd").send_keys("xxxxxxx")
        driver.find_element_by_id("login-btn").click()

        #online classic
        time.sleep(5)
        driver.find_element_by_css_selector("li.active > a > svg.icon-48").click()
        print('online classic OK')

        #play
        time.sleep(5)
        #sharelist = driver.find_element_by_css_selector('.sharelist > ol > li')
        driver.find_element_by_css_selector('.sharelist > ol > li > div > div:nth-of-type(1)').click()
        print('play OK')

        # search
        #time.sleep(5)
        driver.find_element_by_xpath("//input[@type='text']").clear()
        driver.find_element_by_xpath("//input[@type='text']").send_keys(u"田馥甄")
        driver.find_element_by_id("search_btn_cnt").click()
        print('search OK')

    def tearDown(self):
        #self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    #unittest.main()

    suite = unittest.TestSuite()
    suite.addTest(Untitled('test_untitled'))

    unittest.main(verbosity=2)