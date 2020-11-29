from scrap import Scrap

class Search:
    def __init__(self, url):
        self.scrap = Scrap(url)
        self.title = self.scrap.scrapTitleInfo()
        self.detail = self.scrap.scrapDetailInfo()
        self.comment = self.scrap.scrapCommentInfo()

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
                each = each.replace("\">", "")
                if "yt-formatted-string" in each:
                    each = ""
                    comment.append(each)
                else:
                    comment.append(each)
        return comment

    def displayLyrics(self):
        comment = self.searchLyrics()
        lyrics = ""
        for each in comment:
            if each == "":
                lyrics += "\n\n"
            else:
                lyrics += str(each)
        return lyrics


