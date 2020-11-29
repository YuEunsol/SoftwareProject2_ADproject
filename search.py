from scrap import Scrap

class Search:
    def __init__(self, url):
        Scrap(url)
        self.title = Scrap.scrapTitleInfo()
        self.detail = Scrap.scrapDetailInfo()
        self.comment = Scrap.scrapCommentInfo()

    def searchSong(self):
        if '·' in self.detail:
            return self.detail.split('·')[0]
        else:
            return self.title

    def searchArtist(self):
        return self.detail.split('·')[1]

    def searchLyrics(self):
        comment = []
        for each in self.comment:
            if "dir=\"auto\">" in each:
                each = each.replace("<span class=\"style-scope yt-formatted-string\" dir=\"auto\">", "")
                each = each.replace("\r", "")
                each = each.replace("\n", "")
                each = each.replace("\xa0", "")
                if "<" in each:
                    each = ""
                    comment.append(each)
        return comment

    def displayLyrics(self):
        comment = Search.searchLyrics()
        lyrics = ""
        for each in comment:
            if each == "":
                lyrics += "\n"
            else:
                lyrics += each
        return lyrics


