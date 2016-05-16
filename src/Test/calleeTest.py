'''
Created on Apr 25, 2016

@author: ypotluri
'''
import time
import unittest

from appium import webdriver


class Test(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Remote(
            command_executor='http://10.57.2.55:8888/wd/hub',
            desired_capabilities={
                'app': '/Users/shoretelqa/Library/Developer/Xcode/DerivedData/RADialer-blhngktwfhshuwfiftcemkjgmgxw/Build/Products/Debug-iphoneos/RaDialer.app',
                'appiumVersion': '1.5.2',
                'platformName': 'iOS',
                'platformVersion': '9.3.1',
                'deviceName': 'iPhone 6 Plus' ,
                'udid': '1fc6ac78555c6132bde540e4e9c1d52e3e863577',
                'deviceOrientation': 'portrait' ,
                'autoDismissAlerts': 'true',
                'autoAcceptAlerts': 'true'

              })


    def tearDown(self):
        self.driver.quit();


    def testName(self):

        '''
        #server = self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[2]/UIAScrollView[1]/UIATextField[1]");
        #server.click();
        time.sleep(2);
        server.send_keys("10.23.223.50");
        username = self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[2]/UIAScrollView[1]/UIATextField[2]");
        username.click();
        username.send_keys("ypotluri1");
        password = self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[2]/UIAScrollView[1]/UIASecureTextField[1]");
        password.send_keys("123456");
        time.sleep(3);
        next = self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[2]/UIANavigationBar[1]/UIAButton[3]");
        next.click();
       # self.driver.find_element_by_name("Simulator").click();
        #self.driver.find_element_by_name("//UIAApplication[1]/UIAWindow[2]/UIANavigationBar[1]/UIAButton[3]").click();
        #mobilenumber = self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[2]/UIAScrollView[1]/UIATextField[2]");
        #mobilenumber.click();
        #mobilenumber.send_keys("123456");
        next1 = self.driver.find_element_by_name("//UIAApplication[1]/UIAWindow[2]/UIANavigationBar[1]/UIAButton[3]");
        next1.click();
        time.sleep(2);
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[2]/UIAImage[16]/UIAButton[3]").click();
        '''
        
        time.sleep(3);



        answer = self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[2]/UIAButton[12]");
        answer.click();
        time.sleep(2);
        audio = self.driver.find_element_by_xpath(" //UIAApplication[1]/UIAWindow[2]/UIAButton[5]");
        audio.click();
        time.sleep(3);

        hold = self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[2]/UIAButton[6]");
        hold.click();
        time.sleep(4);
        hold.click();
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[2]/UIAButton[24]").click();




if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()