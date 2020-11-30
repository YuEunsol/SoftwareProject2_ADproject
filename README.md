AD프로젝트 : 유튜브 가사 댓글 찾기 프로그램
====================================
<br><br>
## 요구사항 명세서
<br>

**1. 기능적 요구사항**  

  - 사용자의 유튜브 url를 받아온다.
  - url에서 동영상 제목, 상세 정보, 댓글란을 텍스트로 불러온다.
  - 동영상 제목, 상세 정보, 댓글란을 탐색하여 알맞은 노래 제목, 아티스트, 가사를 추출한다.
  - 
  
<br>

**2. 사용자 인터페이스 요구사항**  
  - 윈도우 타이틀 바
  - 제목, 가수, 가사
  - 새로고침 버튼
  - 스크롤 창  
  +글씨 크기 키움 버튼  
  +글씨 크기 줄임 버튼
 
 <br><br><br>
 ------------------------------------------------
 <br><br><br>
 
## 소프트웨어 구조 설계
<br>

**youtubeLyrics.py**
  - YoutubeLyrics  
    -UI component
  - MainWindow  
    -메인 윈도우
    
**crawl.py**   
  - `url`을 받아 해당 페이지에 있는 `html` 정보를 긁어옴  
      
**scrap.py**
  - Scrap  
    -긁어온 `html` 정보 중 영상 제목, 상세 정보, 댓글을 추출하여 `String`으로 출력  
   
**search.py**  
  - Search  
    -찾아낸 영상 정보(영상 제목, 상세 정보, 댓글)에서 노래 제목, 아티스트, 가사를 추출하여 출력  
     
    


    


<br>

| ↓ | 내용 |
|:---|---:|
| **youtubeLyrics** | user에게 `url`을 입력받음 <br> `url`을 `search`에게 인자로 줌 |
| **search** |  `url`을 `scrap`에게 인자로 줌 |
| **scrap** |  `url`을 `crawl`에게 인자로 줌 |
| **crawl** | 인자로 받은 `url`에서 `html` 정보를 긁어와 `html` 태그 형식으로 도출 |
| **scrap** | 받아온 `html` 정보 중 영상 제목에 해당하는 데이터를 추출하여 `String` 형태로 도출 <br> 받아온 `html` 정보 중 상세 정보에 해당하는 데이터를 추출하여 `String` 형태로 도출 <br> 받아온 `html` 정보 중 댓글에 해당하는 데이터를 추출 <br> 추출한 댓글 중 15줄 이상에 해당하는 것만 `String` 형태로 도출 |
| **search** | 받아온 영상 제목, 상세 정보에서 찾아낸 노래 제목을 도출 <br> 받아온 영상 제목, 상세 정보에서 찾아낸 아티스트를 도출 <br> 받아온 댓글에서 `html`태그를 제거하여 가사를 도출  |
| **youtubeLyrics** | 받아온 노래 제목, 아티스트, 가사를 창에 띄움 |

<br><br><br>
--------------------------------------------
<br><br><br>

## 구현 상세 설계
<br>

### Crawl
<br>

**1. 자료 구조**

     driver
      - `selenium` 라이브러리 중 크롬 웹 크롤링을 할 수 있는 도구 
     url
      - 현재 `url` 주소(String)
      

**2. crawlPage**  
   - 동적인 웹 크롤링을 위해 해당 웹의 스크롤을 자동으로 내리고 `html` 데이터를 도출하는 모듈  
     (가사 댓글은 대체로 상위에 위치하지만, 그렇지 않은 경우도 꽤 있기 때문에 
     여러번의 테스트를 통해 25번의 스크롤을 하기로 결정함  
     스크롤의 로딩 또한 기다려야 하기 때문에 스크롤당 딜레이 시간을 
     0.3초로 잡음)  
  
     lastPageHeight  
      - 이전 스크롤 높이  
     newPageHeight  
      - 새로운 스크롤 높이  
     `window.scrollTo`를 이용하여 스크롤을 내리고 `newPageHeight`으로 스크롤 높이를 받아옴  
     result  
     - 최종적으로 스크롤한 페이지에서 받아온 `html` 데이터  
     `BeautifulSoup` 모듈을 이용하여 `html` 데이터를 받아옴  
     
      
### Scrap
<br>

**1. 자료 구조**

     soup
      - `Crawl`에서 받아온 `html`데이터  
      url
      - 현재 url 주소(String)  
      
**2. scrapTitleInfo**
      
     titleInfo
      - `#title` 또는 `#container > h1 > yt-formatted-string` 라는 태그가 붙은 `html` 데이터를 도출
      (`#title` > `#container > h1 > yt-formatted-string` 순)
      (`.text`를 이용해 필요없는 태그를 제거함)
      (값이 하나만 나오기 때문에 `select_one`을 사용)
      위 사항에 해당되지 않을 시 `"링크를 다시 입력하세요"` 도출
      
    
 
      
**3. scrapDetailInfo**
      
     detailInfo
      - `#description`라는 태그가 붙은 `html` 데이터를 도출
      (`.text`를 이용해 필요없는 태그를 제거함)
      (값이 하나만 나오기 때문에 `select_one`을 사용)
      위 사항에 해당되지 않을 시 `""` 도출
       
      
**4. scrapCommentInfo**
      
     commentInfo
      - `yt-formatted-string#content-text`라는 태그가 붙은 `html` 데이터를 추출  
      (값이 여러 개가 나오기 때문에 `select`를 사용-`List`타입으로 도출)  
      `String`타입으로 변환 후 `</yt-formatted-string>`으로 `split` (댓글마다 나눔)  
      `lines` = 인자(`each in commentInfo`)마다 `</span>`으로 `split` (줄 나눔)
      `lines`가 15줄 이상이면 가사 댓글로 판정하여 도출  
      위 사항에 해당되지 않을 시 `""` 도출
      
### Search
<br>

**1. 자료 구조**

     title
      - `Scrap`에서 받아온 영상 제목에 대한 정보(String)
      
     detail
      - `Scrap`에서 받아온 영상 상세 정보에 대한 정보(String) 
      
     comment
      - `Scrap`에서 받아온 영상 댓글에 대한 정보(List)
      
     url
      - 현재 url 주소(String)
      
**2. searchSong**

     `detail`에 `"·"`가 있으면 `"\n"`과 `"·"`  사이 text 도출  
     `title`에 `"-"`가 있으면 `"-"` 다음 text 도출  
     `detail`에 `"-"`가 있으면 `"-"`과 `"\n"` 사이 text 도출  
     위 사항에 해당되지 않으면 `title` 도출  
     에러 발생시 `"제목을 찾을 수 없습니다"` 도출  
      
**3. searchArtist**

     `detail`에 `"·"`가 있으면 `"·"`과 `"\n"` 사이 text 도출  
     `title`에 `"-"`가 있으면 `"-"` 이전 text 도출  
     `detail`에 `"-"`가 있으면 `"\n"`과 `"-"` 사이 text 도출  
     에러 발생시 `"아티스트를 찾을 수 없습니다"` 도출  
**4. searchLyrics**

     `comment`가 `"댓글 중 가사 댓글이 없습니다"`면 그대로 도출   
     `comment` 중 `"dir=\"auto\">"`가 있는 댓글만 추출하여 `html`태그를 제거하여 `List`타입으로 도출    
     에러 발생시 `"가사를 찾을 수 없습니다"` 도출  
**5. displayLyrics**

     `searchLyrics`에서 받아온 가사를 줄바꿈을 넣어 `String`타입으로 도출  
      
### YoutubeLyrics
<br>

**1. MainLayout**

     self.lyrics
      - `QTextEdit` 위젯이며 읽기만 가능  
        폰트 사이즈는 13으로 설정  
     self.songTitle
      - `QTextEdit` 위젯이며 읽기만 가능  
        폰트 사이즈는 16으로 설정  
        볼드체로 설정  
     self.artist
      - `QLineEdit` 위젯이며 읽기만 가능  
        폰트 사이즈는 14으로 설정  
     self.urlInput
      - `QLineEdit` 위젯  
     self.submitButton
      - `QToolButton` 위젯  
        `self.submitUrl`과 연결되어 있음  
      self.resetButton
      - `QToolButton` 위젯  
        `self.reset`과 연결되어 있음  
        
**2. searchLyrics**

     받아온 `url` 값을 인자로 `Search`모듈을 실행하고 `urlInput`에 입력값을 지움  
     노래 제목 뒤에 (Feat. ...)이 붙었을 경우 길어지기 때문에 `"("`앞에서 줄바꿈을 할 수 있도록 함  
     혹은 (Feat. ...)이 붙지 않더라도 길어지는 경우를 대비해 20번째 글자에서 줄바꿈을 할 수 있도록 함  
     `self.songTitle`을 `self.search.searchSong()`에서 받아온 노래 제목 값으로 설정  
     `self.artist`을 `self.search.searchArtist()`에서 받아온 아티스트 값으로 설정  
     `self.lyrics`을 `self.search.displayLyrics()`에서 받아온 가사 값으로 설정  
        
**3. submitUrl**

     `submit` 버튼 클릭 시 `url` 값을 사용자가 입력한 값으로 설정함  
     사용자가 입력한 값이 유튜브 링크가 맞는지 확인하고 아닐시 입력값 삭제  
     
        
**4. reset**

     `self.lyrics`, `self.songTitle`, `self.artist` 삭제
     
      
      
     
    
<br><br><br>
------------------------------------------
<br><br><br>

## 테스트 보고서  
<br>

| 클래스 | 테스트 | 내용 | 결과 |
|---|:---:|---:|:---:|
| 클래스1 이름 | 테스1트 이름 | 테스트1 내용 | 결과1 |

<br><br><br>
-----------------------------------------
<br><br><br>

## 결과물
<br>


<br><br><br>
----------------------------------------
<br><br><br>

## 참고문헌
<br>
