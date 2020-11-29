import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QGridLayout, QScrollArea
from PyQt5.QtWidgets import QTextEdit, QLineEdit, QToolButton


from search import Search

class YoutubeLyrics(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)

        # Lyrics display window
        self.lyrics = QTextEdit()
        self.lyrics.setReadOnly(True)
        self.lyrics.setAlignment(Qt.AlignCenter)
        self.lyrics.resize(570,720)
        lyricsFont = self.lyrics.font()
        lyricsFont.setPointSize(13)
        self.lyrics.setFont(lyricsFont)

        # Song title display widget
        self.songTitle = QTextEdit()
        self.songTitle.setReadOnly(True)
        self.songTitle.setAlignment(Qt.AlignCenter)
        titleFont = self.songTitle.font()
        titleFont.setPointSize(16)
        titleFont.setBold(True)
        self.songTitle.setFont(titleFont)
        self.songTitle.setMaximumSize(580,80)

        # Artist display widget
        self.artist = QLineEdit()
        self.artist.setReadOnly(True)
        self.artist.setAlignment(Qt.AlignCenter)
        artistFont = self.artist.font()
        artistFont.setPointSize(14)
        self.artist.setFont(artistFont)

        # Input widget for playing video url
        self.urlInput = QLineEdit()

        # Button for submitting a url
        self.submitButton = QToolButton()
        self.submitButton.setText('Submit')
        self.submitButton.clicked.connect(self.submitUrl)

        # Button for reset
        self.resetButton = QToolButton()
        self.resetButton.setText('Reset')
        self.resetButton.clicked.connect(self.reset)

        # Layout placement
        mainLayout = QGridLayout()


        mainLayout.addWidget(self.urlInput, 0, 0, 1, 2)
        mainLayout.addWidget(self.submitButton, 0, 2, 1, 1)
        mainLayout.addWidget(self.songTitle, 1, 0, 2, 3)
        mainLayout.addWidget(self.artist, 3, 0, 1, 3)
        mainLayout.addWidget(self.lyrics, 4, 0, 1, 3)
        mainLayout.addWidget(self.resetButton, 5, 2, 1, 1)

        self.setWindowTitle('Youtube Lyrics Search Program')
        self.setLayout(mainLayout)
        self.setGeometry(1200, 140, 600, 900)


    def searchLyrics(self, url):
        self.search = Search(url)
        self.urlInput.clear()
        songTitle = self.search.searchSong()
        if len(songTitle) > 20:
            if "(" in songTitle:
                songTitle = songTitle.replace("(","\n(")
            else:
                songTitle = songTitle.replace(songTitle[20],songTitle[20]+"\n")
        self.songTitle.setText(songTitle)
        self.artist.setText(self.search.searchArtist())
        self.lyrics.setText(self.search.displayLyrics())

    def submitUrl(self):
        url = self.urlInput.text().strip()
        if "https://www.youtube.com/" in url:
            self.searchLyrics(url)
        else:
            self.urlInput.clear()

    def reset(self):
        self.lyrics.clear()
        self.songTitle.clear()
        self.artist.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    program = YoutubeLyrics()
    program.show()
    sys.exit(app.exec_())

