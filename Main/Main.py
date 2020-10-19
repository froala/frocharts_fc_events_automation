from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities 
from Util import Report as report
from Util import chart as chart
from Util import Validate as val
from Events import rendered
from Events import ready
from selenium.webdriver.chrome.options import Options
import time
import os
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from Events import pomFile
from Util import Report as report


class MainClass(object):
    
    def __init__(self):
        report.create_csv()
        
        #Initializing browser and opening URL               `                                                                              
        self.chrome()
        
        self.driver.implicitly_wait(0.2)
        report.browser=self.browser
        report.driver=self.driver
        self.driver.get(chart.url_to_hit())
        
    def chrome(self):
        #Chrome
        self.browser="Chrome"
        pomFile.PageObjectModel.browser=self.browser
        option_new = Options()
        d = DesiredCapabilities.CHROME
        d['loggingPrefs'] = { 'browser':'ALL' }
        self.driver = webdriver.Chrome(executable_path=r'../Drivers/chromedriver.exe', chrome_options=option_new)
        self.driver.maximize_window()
    
    def firefox(self):
        # Firefox 
        self.browser="Firefox"
        pomFile.PageObjectModel.browser=self.browser
        profile = webdriver.FirefoxProfile("/Users/interview/Library/Application Support/Firefox/Profiles/seoqpw8s.default")
        profile.set_preference("print.always_print_silent", True)
        profile.set_preference("browser.download.folderList",2)
        profile.set_preference("browser.download.manager.showWhenStarting",False)
        profile.set_preference("browser.download.dir", os.getcwd())
        profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf")
        d = DesiredCapabilities.FIREFOX
        d['loggingPrefs'] = { 'browser':'ALL' }
        self.driver = webdriver.Firefox(executable_path=r'../Drivers/geckodriver', firefox_profile=profile)
        
        
    
