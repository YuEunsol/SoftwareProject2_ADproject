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
        elif "-" in self.title:
            return self.title.split("-")[1]
        else:
            return self.title

    def searchArtist(self):
        try:
            return self.detail.split('·')[1]
        except:
            return self.detail

    def searchLyrics(self):
        comment = []
        for each in self.comment:
            if "dir=\"auto\">" in each:
                each = each.replace("<span class=\"style-scope yt-formatted-string\" dir=\"auto\">", "")
                each = each.replace("\r", "")
                each = each.replace("\n", "")
                each = each.replace("\">", "")
                each = each.replace(', <yt-formatted-string class="style-scope ytd-comment-renderer" id="content-text" slot="content" split-lines="',"")
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


