'''
Created on Apr 18, 2016

@author: ypotluri
'''



import StringIO
import time
import unittest
from teamcity import is_running_under_teamcity
from teamcity.unittestpy import TeamcityTestRunner
from unittest.test import suite

from appium.webdriver.webdriver import webdriver
from selenium.webdriver.support import wait

import HTMLTestRunner
import __main__

class Test(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4729/wd/hub',
            desired_capabilities={
                'app': '/Users/ypotluri/Library/Developer/Xcode/DerivedData/RADialer-dszezfpkvnbrnwcuymmdrubmgqax/Build/Products/Debug-iphoneos/RaDialer.app',
                'appiumVersion': '1.4.13',
                'platformName': 'iOS',
                'platformVersion': '9.3',
                'deviceName': 'iPhone 6' ,
                'udid': '9d0ea19a2bce6b6bbc8b69f4c9fcb3d5bbb90268',
                'deviceOrientation': 'portrait' ,
                'autoDismissAlerts': 'true',
               'autoAcceptAlerts': 'true'
                
            })
        

    def tearDown(self):
        self.driver.quit()


    def testName(self):
       
        server = self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[2]/UIAScrollView[1]/UIATextField[1]");
        server.click();
        time.sleep(2);
        server.send_keys("10.23.223.50");
        username = self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[2]/UIAScrollView[1]/UIATextField[2]");
        username.click();
        username.send_keys("cbal30");
        password = self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[2]/UIAScrollView[1]/UIASecureTextField[1]");
        password.click();
        password.send_keys("123456");
        time.sleep(5);
        next = self.driver.find_element_by_xpath(" //UIAApplication[1]/UIAWindow[2]/UIANavigationBar[1]/UIAButton[3]");
        next.click();
        time.sleep(3);
       # self.driver.find_element_by_name("Simulator").click();
        #self.driver.find_element_by_name("Next").click();
       # mobilenumber = self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[2]/UIAScrollView[1]/UIATextField[2]");
       # mobilenumber.click();
       # mobilenumber.send_keys("123456");
        
        next1 = self.driver.find_element_by_xpath(" //UIAApplication[1]/UIAWindow[2]/UIANavigationBar[1]/UIAButton[3]");
        next1.click();
        time.sleep(4);
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[2]/UIAImage[16]/UIAButton[3]").click();
        
        
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[2]/UIAButton[4]").click();
        time.sleep(2);
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[2]/UIAButton[14]").click();
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[2]/UIAButton[7]").click();
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[2]/UIAButton[10]").click();
        time.sleep(2);

        call = self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[2]/UIAButton[19]");
        time.sleep(2);
        call.click();
        time.sleep(20);
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[2]/UIAButton[24]").click();

        #self.assertTrue(self.driver.find_element_by_name("Mute"), "Call not initiated correctly");
      #  self.assertTrue(self.driver.find_element_by_name("Hold"), "Call not initiated correctly");
       #self.assertTrue(self.driver.find_element_by_name("Transfer"), "Call not initiated correctly");
        '''
        self.driver.find_element_by_name("Mute").click();
        time.sleep(2)
        if(self.driver.find_element_by_name("Hold").is_enabled()):
            self.driver.find_element_by_name("Hold").click();
            time.sleep(2)

        self.driver.find_element_by_name("End Call").click();
        time.sleep(2)
       '''
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    if is_running_under_teamcity():
        runner = TeamcityTestRunner()
    else:
        runner = unittest.TextTestRunner()
    unittest.main(testRunner=runner)
    