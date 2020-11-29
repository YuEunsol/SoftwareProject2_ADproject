from bs4 import BeautifulSoup
from selenium import webdriver
import time

class Crawl:
    def __init__(self, url):
        self.driver = webdriver.Chrome(executable_path="/home/sol/다운로드/chromedriver")
        self.url = url
        self.driver.get(url)
        
    def crawlPage(self):
        lastPageHeight = self.driver.execute_script("return document.documentElement.scrollHeight")
        for i in range(15):
            self.driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
            time.sleep(0.3)
            newPageHeight = self.driver.execute_script("return document.documentElement.scrollHeight")
            lastPageHeight = newPageHeight

        try:
            result = BeautifulSoup(self.driver.page_source, "html.parser")
        except:
            print("e")
        self.driver.close()
        return result
