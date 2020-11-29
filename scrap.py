from crawl import Crawl

class Scrap:
    def __init__(self,url):
        self.crawl = Crawl(url)
        self.soup = self.crawl.crawlPage()

    def scrapTitleInfo(self):
        try:
            return self.soup.select_one("#title").text
        except:
            return self.soup.select_one("#container > h1 > yt-formatted-string").text


    def scrapDetailInfo(self):
        try:
            detailInfo = self.soup.select_one("#description")
            detailInfo = str(detailInfo.text)
            detailInfo = detailInfo.split('\n')[2]
        except:
            detailInfo = self.soup.select_one("#container > ytd-expander > ytd-metadata-row-container-renderer")
            detailInfo = str(detailInfo.text)
        return detailInfo

    def scrapCommentInfo(self):
        commentInfo = self.soup.select("yt-formatted-string#content-text")
        commentInfo = str(commentInfo)
        commentInfo = commentInfo.split("</yt-formatted-string>")
        for each in commentInfo:
            lines = each.split("</span>")
            if len(lines) > 15:
                return lines
        return "댓글 중 가사 댓글이 없습니다"


