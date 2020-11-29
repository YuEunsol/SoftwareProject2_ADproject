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
        self.lyrics.resize(408,528)
        lyricsFont = self.lyrics.font()
        lyricsFont.setPointSize(11)
        self.lyrics.setFont(lyricsFont)

        # Scroll Area for Lyrics
        scroll = QScrollArea()
        scroll.setWidget(self.lyrics)

        # Song title display widget
        self.songTitle = QLineEdit()
        self.songTitle.setReadOnly(True)
        self.songTitle.setAlignment(Qt.AlignCenter)
        titleFont = self.songTitle.font()
        titleFont.setPointSize(16)
        titleFont.setBold(True)
        self.songTitle.setFont(titleFont)

        # Artist display widget
        self.artist = QLineEdit()
        self.artist.setReadOnly(True)
        self.artist.setAlignment(Qt.AlignCenter)
        artistFont = self.artist.font()
        artistFont.setPointSize(13)
        self.artist.setFont(artistFont)

        # Input widget for playing video url
        self.urlInput = QLineEdit()

        # Button for submitting a url
        self.submitButton = QToolButton()
        self.submitButton.setText('Submit')
        self.submitButton.clicked.connect(self.submitUrl)

        # # Button for previous Lyrics
        # self.preButton = QToolButton()
        # self.preButton.setText('<')
        # self.preButton.clicked.connect(self.preLyrics)
        #
        # # Button for next Lyrics
        # self.nextButton = QToolButton()
        # self.nextButton.setText('>')
        # self.nextButton.clicked.connect(self.nextLyrics)

        # Button for reset
        self.resetButton = QToolButton()
        self.resetButton.setText('Reset')
        self.resetButton.clicked.connect(self.reset)

        # Layout placement
        mainLayout = QGridLayout()


        mainLayout.addWidget(self.urlInput, 0, 0, 1, 2)
        mainLayout.addWidget(self.submitButton, 0, 2, 1, 1)
        mainLayout.addWidget(self.songTitle, 1, 1, 1, 1)
        mainLayout.addWidget(self.artist, 2, 1, 1, 1)
        mainLayout.addWidget(scroll, 3, 1, 1, 1)
        mainLayout.addWidget(self.resetButton, 4, 1, 1, 1)

        self.setWindowTitle('Youtube Lyrics Search Program')
        self.setLayout(mainLayout)
        self.setGeometry(1200, 240, 500, 700)


    def searchLyrics(self, url):
        self.search = Search(url)
        self.urlInput.clear()
        self.songTitle.setText(self.search.searchSong())
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

