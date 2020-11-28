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
        self.detail = ""
        self.title = ""
        self.comment = []



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
        # titleInfo = titleInfo
        # pprint(titleInfo)
        return titleInfo

    def scrapDetailInfo(self):
        detailInfo = self.soup.select_one("#description")
        detailInfo = str(detailInfo.text)
        detail = detailInfo.split('\n')[2]

        self.detail = detail

    def scrapCommentInfo(self):
        commentInfo = self.soup.select("yt-formatted-string#content-text")
        commentInfo = str(commentInfo)
        commentInfo = commentInfo.split("</span>")


        for each in commentInfo:
            if "dir=\"auto\">" in each:
                each = each.replace("<span class=\"style-scope yt-formatted-string\" dir=\"auto\">","")
                each = each.replace("\r","")
                each = each.replace("\n","")
                each = each.replace("\xa0","")

                if "<" in each:
                    each = ""
                self.comment.append(each)




    def searchSong(self):
        if '·' in self.detail:
            return self.detail.split('·')[0]
        else:
            return self.title

    def searchArtist(self):
        return self.detail.split('·')[1].strip()

    def searchLyrics(self):
        for each in self.comment:
            if "dir=\"auto\">" not in each:
                self.comment.remove(each)
        return self.comment


if __name__ == '__main__':
    crawl = Scrap("https://www.youtube.com/watch?v=Xp78pd0zkCU&list=RDG4o8Qa6pYz4&index=27")
    crawl.crawlPage()
    crawl.scrapCommentInfo()
    crawl.scrapDetailInfo()
    crawl.scrapTitleInfo()
    print(crawl.searchLyrics())
    print(crawl.searchSong())
    print(crawl.searchArtist())