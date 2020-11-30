from crawl import Crawl

class Scrap:
    def __init__(self,url):
        self.crawl = Crawl(url)
        self.soup = self.crawl.crawlPage()
        print(type(self.soup))

    def scrapTitleInfo(self):
        try:
            titleInfo = self.soup.select_one("#title").text
            if titleInfo == "":
                titleInfo = self.soup.select_one("#container > h1 > yt-formatted-string").text
            return titleInfo
        except:
            return "링크를 다시 입력하세요"


    def scrapDetailInfo(self):
        try:
            detailInfo = self.soup.select_one("#description").text
            return detailInfo
        except:
            return ""


    def scrapCommentInfo(self):
        try:
            commentInfo = self.soup.select("yt-formatted-string#content-text")
            commentInfo = str(commentInfo)
            commentInfo = commentInfo.split("</yt-formatted-string>")
            for each in commentInfo:
                lines = each.split("</span>")
                if len(lines) > 15:
                    return lines
            return "댓글 중 가사 댓글이 없습니다"
        except:
            return ""


