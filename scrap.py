from pprint import pprint
from bs4 import BeautifulSoup
from selenium import webdriver
import time

class Scrap:
    def __init__(self, url):
        self.driver = webdriver.Chrome(executable_path="/home/sol/다운로드/chromedriver")
        self.url = url
        self.driver.get(url)
        self.soup = ""


    def crawlPage(self):
        lastPageHeight = self.driver.execute_script("return document.documentElement.scrollHeight")
        for i in range(15):
            self.driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
            time.sleep(0.3)
            newPageHeight = self.driver.execute_script("return document.documentElement.scrollHeight")
            lastPageHeight = newPageHeight

        try:
            self.soup = BeautifulSoup(self.driver.page_source, "html.parser")
        except:
            print("e")

        self.driver.close()

    def scrapTitleInfo(self):
        titleInfo = self.soup.select_one("title")
        pprint(titleInfo)
        return titleInfo

    def scrapDetailInfo(self):
        detailInfo = self.soup.select_one("#description")
        pprint(detailInfo)
        return detailInfo

    def scrapCommentInfo(self):
        commentInfo = self.soup.select("yt-formatted-string#content-text")
        pprint(commentInfo)
        return commentInfo


if __name__ == '__main__':
    crawll = Scrap("https://www.youtube.com/watch?v=kGi4CRlJA6w&list=RDG4o8Qa6pYz4&index=3")
    crawll.crawlPage()
    crawll.scrapCommentInfo()
    crawll.scrapDetailInfo()
    crawll.scrapTitleInfo()
