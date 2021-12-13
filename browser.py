# -*- coding: utf-8
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait as WW
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from datetime import datetime

class Browser():
    def __init__(self, config):
        self.screenshot = config["screenshot"]
        self.timeout = config["timeout"]
        chrome_options=Options()
        chrome_options.add_argument('--headless')
        self.browser = webdriver.Chrome(chrome_options=chrome_options, executable_path="./chromedriver")


    def clickByXPath(self, xpath):
        try:
            locator = (By.XPATH, xpath)
            WW(self.browser, self.timeout).until(EC.visibility_of_element_located(locator))
            self.browser.find_element_by_xpath(xpath).click()
        except Exception as e:
            self.saveScreenshot()
            print(xpath)
            raise e

    def clickByCssSelector(self, cssSelector):
        try:
            locator = (By.CSS_SELECTOR, cssSelector)
            WW(self.browser, self.timeout).until(EC.visibility_of_element_located(locator))
            self.browser.find_element_by_css_selector(cssSelector).click()
        except Exception as e:
            print(cssSelector)
            self.saveScreenshot()
            raise e

    def typeByCssSelector(self, cssSelector, text):
        try:
            locator = (By.CSS_SELECTOR, cssSelector)
            WW(self.browser, self.timeout).until(EC.visibility_of_element_located(locator))
            self.browser.find_element_by_css_selector(cssSelector).clear()
            self.browser.find_element_by_css_selector(cssSelector).send_keys(text)
        except Exception as e:
            self.saveScreenshot()
            print(cssSelector)
            raise e

    def typeByXPath(self, xpath, text):
        try:
            locator = (By.XPATH, xpath)
            WW(self.browser, self.timeout).until(EC.visibility_of_element_located(locator))
            self.browser.find_element_by_xpath(xpath).clear()
            self.browser.find_element_by_xpath(xpath).send_keys(text)
        except Exception as e:
            self.saveScreenshot()
            print(xpath)
            raise e

    def findElementByXPath(self, xpath):
        try:
            locator = (By.XPATH, xpath)
            WW(self.browser, self.timeout).until(EC.visibility_of_element_located(locator))
            element = self.browser.find_element_by_xpath(xpath)
            return element
        except Exception as e:
            self.saveScreenshot()
            print(xpath)
            raise e

    def findElementByCssSelector(self, cssSelector):
        try:
            locator = (By.CSS_SELECTOR, cssSelector)
            WW(self.browser, self.timeout).until(EC.visibility_of_element_located(locator))
            element = self.browser.find_element_by_css_selector(cssSelector)
        except Exception as e:
            self.saveScreenshot()
            print(cssSelector)
            raise e

    def gotoPage(self, url):
        print("goto page %s" % url)
        self.browser.execute_script("window.open(\"%s\")" % url)
        self.browser.switch_to.window(self.browser.window_handles[-1])

    def saveScreenshot(self):
        filename = self.screenshot + '/' + datetime.now().strftime("%Y-%m-%d-%H:%M:%S") + '.png'
        print("saveing screenshot at %s ..."%(filename))
        self.browser.get_screenshot_as_file(filename)

    def close(self):
        try:
            self.browser.quit()
            self.browser.close()
        except:
            pass
