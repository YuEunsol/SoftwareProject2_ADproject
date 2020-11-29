from crawl import Crawl

class Scrap:
    def __init__(self,url):
        self.crawl = Crawl(url)
        self.soup = self.crawl.crawlPage()


    def scrapTitleInfo(self):
        titleInfo = self.soup.select_one("title")
        return titleInfo

    def scrapDetailInfo(self):
        detailInfo = self.soup.select_one("#description")
        detailInfo = str(detailInfo.text)
        detailInfo = detailInfo.split('\n')[2]
        return detailInfo

    def scrapCommentInfo(self):
        commentInfo = self.soup.select("yt-formatted-string#content-text")
        commentInfo = str(commentInfo)
        commentInfo = commentInfo.split("</span>")
        return commentInfo



