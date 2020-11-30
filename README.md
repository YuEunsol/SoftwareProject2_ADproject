AD프로젝트 : 유튜브 가사 댓글 찾기 프로그램
====================================

<br><br>

## 개요
유튜브 프리미엄을 쓰는 나는 유튜브로 노래를 자주 듣곤한다.  
   
유튜브 알고리즘이 내가 알지 못했던 좋은 노래로 이끌어주는 경험이 있었기 때문이다.    
   
그런데 유튜브에서의 단점이 하나 있다면 가사를 일일이 댓글에서 찾아야 한다는 것이다.   
  
원래 우리가 쓰던 노래 재생 프로그램(멜론, 벅스, 지니 등..)에선 노래마다 가사가 자동으로 로드되어 굳이 찾을 필요가 없었다.   
  
노래를 듣는 것 만큼이나 노래를 부르는 것을 좋아하는 나는 가사 여부 때문에 최근에 벅스를 다시 구독했다.   
  
하지만 유튜브에만 있는 노래도 많기 때문에 유튜브를 포기할 수는 없었다.   
    
그래서 직접 [유튜브 댓글에서 가사를 찾아주는 프로그램]을 만들어보고자 한다.   

<br><br><br><br><br><br>
<br><br><br><br><br><br>

## 요구사항 명세서

<br>

**1. 기능적 요구사항**

<br>

  - 사용자의 유튜브 url를 받아온다.
  - url에서 동영상 제목, 상세 정보, 댓글란을 텍스트로 불러온다.
  - 동영상 제목, 상세 정보, 댓글란을 탐색하여 알맞은 노래 제목, 아티스트, 가사를 추출한다.
  
<br>

**2. 사용자 인터페이스 요구사항**  
<br>
  - 윈도우 타이틀 바
  - 제목, 가수, 가사
  - 새로고침 버튼
  - 스크롤 창  
  +글씨 크기 키움 버튼  
  +글씨 크기 줄임 버튼
  
 <br><br><br><br><br><br>
 <br><br><br><br><br><br>
 
## 소프트웨어 구조 설계

<br>

**youtubeLyrics.py**
  - YoutubeLyrics  
    -UI component
  - MainWindow  
    -메인 윈도우
    
<br>

**crawl.py**   
  - `url`을 받아 해당 페이지에 있는 `html` 정보를 긁어옴  
  
<br>

**scrap.py**
  - Scrap  
    -긁어온 `html` 정보 중 영상 제목, 상세 정보, 댓글을 추출하여 `String`으로 출력 
    
<br>

**search.py**  
  - Search  
    -찾아낸 영상 정보(영상 제목, 상세 정보, 댓글)에서 노래 제목, 아티스트, 가사를 추출하여 출력  
    
<br><br><br><br><br><br>

| ↓ | 내용 |
|:---|---:|
| **youtubeLyrics** | <br>  user에게 `url`을 입력받음 <br> `url`을 `search`에게 인자로 줌  <br>  |
| **search** |  <br>  `url`을 `scrap`에게 인자로 줌  <br>  |
| **scrap** | <br>  `url`을 `crawl`에게 인자로 줌 |
| **crawl** |  <br>  인자로 받은 `url`에서 `html` 정보를 긁어와 `html` 태그 형식으로 도출 |
| **scrap** |  <br>  받아온 `html` 정보 중 영상 제목에 해당하는 데이터를 추출하여 `String` 형태로 도출 <br> 받아온 `html` 정보 중 상세 정보에 해당하는 데이터를 추출하여 `String` 형태로 도출 <br> 받아온 `html` 정보 중 댓글에 해당하는 데이터를 추출 <br> 추출한 댓글 중 15줄 이상에 해당하는 것만 `String` 형태로 도출 |
| **search** |  <br>  받아온 영상 제목, 상세 정보에서 찾아낸 노래 제목을 도출 <br> 받아온 영상 제목, 상세 정보에서 찾아낸 아티스트를 도출 <br> 받아온 댓글에서 `html`태그를 제거하여 가사를 도출  |
| **youtubeLyrics** |  <br>  받아온 노래 제목, 아티스트, 가사를 창에 띄움 |

<br><br><br><br><br><br>
<br><br><br><br><br><br>

## 구현 상세 설계

<br>

## Crawl

<br>

**1. 자료 구조**

driver  
  - `selenium` 라이브러리 중 크롬 웹 크롤링을 할 수 있는 도구  
  
url  
  - 현재 `url` 주소(`String`)  
      
<br><br><br>

**2. crawlPage**  

동적인 웹 크롤링을 위해 해당 웹의 스크롤을 자동으로 내리고 `html` 데이터를 도출하는 모듈  
(가사 댓글은 대체로 상위에 위치하지만, 그렇지 않은 경우도 꽤 있기 때문에 
여러번의 테스트를 통해 25번의 스크롤을 하기로 결정함  
스크롤의 로딩 또한 기다려야 하기 때문에 스크롤당 딜레이 시간을 
0.3초로 잡음)  
    
lastPageHeight  
  - 이전 스크롤 높이  
  
newPageHeight  
  - 새로운 스크롤 높이 
  - `window.scrollTo`를 이용하여 스크롤을 내리고 `newPageHeight`으로 스크롤 높이를 받아옴   
     
result  
  - 최종적으로 스크롤한 페이지에서 받아온 `html` 데이터  
  - `BeautifulSoup` 모듈을 이용하여 `html` 데이터를 받아옴  
<br><br><br>

## Scrap

<br>  

**1. 자료 구조**  
soup  
  - `Crawl`에서 받아온 `html`데이터  
      
url  
  - 현재 url 주소(String)  
      
<br>

**2. scrapTitleInfo**  

titleInfo  
  - `#title` 또는 `#container > h1 > yt-formatted-string` 라는 태그가 붙은 `html` 데이터를 도출  
  - (`#title` > `#container > h1 > yt-formatted-string` 순)  
  - (`.text`를 이용해 필요없는 태그를 제거함)  
  - (값이 하나만 나오기 때문에 `select_one`을 사용)  
  - 위 사항에 해당되지 않을 시 `"링크를 다시 입력하세요"` 도출  
        
<br>

**3. scrapDetailInfo**  

detailInfo  
  - `#description`라는 태그가 붙은 `html` 데이터를 도출  
  - (`.text`를 이용해 필요없는 태그를 제거함)  
  - (값이 하나만 나오기 때문에 `select_one`을 사용)  
  - 위 사항에 해당되지 않을 시 `""` 도출  
        
<br>

**4. scrapCommentInfo**

commentInfo  
  - `yt-formatted-string#content-text`라는 태그가 붙은 `html` 데이터를 추출   
  - (값이 여러 개가 나오기 때문에 `select`를 사용-`List`타입으로 도출)  
  - `String`타입으로 변환 후 `</yt-formatted-string>`으로 `split` (댓글마다 나눔)  
  - `lines` = 인자(`each in commentInfo`)마다 `</span>`으로 `split` (줄 나눔)  
  - `lines`가 15줄 이상이면 가사 댓글로 판정하여 도출   
  - 위 사항에 해당되지 않을 시 `""` 도출  
        
<br><br><br>

## Search

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
  
      <br>  
      
**2. searchSong**  

  - `detail`에 `"·"`가 있으면 `"\n"`과 `"·"`  사이 text 도출  
  - `title`에 `"-"`가 있으면 `"-"` 다음 text 도출  
  - `detail`에 `"-"`가 있으면 `"-"`과 `"\n"` 사이 text 도출  
  - 위 사항에 해당되지 않으면 `title` 도출  
  - 에러 발생시 `"제목을 찾을 수 없습니다"` 도출  
  
      <br>  
      
**3. searchArtist**  

  - `detail`에 `"·"`가 있으면 `"·"`과 `"\n"` 사이 text 도출  
  - `title`에 `"-"`가 있으면 `"-"` 이전 text 도출  
  - `detail`에 `"-"`가 있으면 `"\n"`과 `"-"` 사이 text 도출  
  - 에러 발생시 `"아티스트를 찾을 수 없습니다"` 도출  
  
<br>  

**4. searchLyrics**  


  - `comment`가 `"댓글 중 가사 댓글이 없습니다"`면 그대로 도출   
  - `comment` 중 `"dir=\"auto\">"`가 있는 댓글만 추출하여 `html`태그를 제거하여 `List`타입으로 도출    
  - 에러 발생시 `"가사를 찾을 수 없습니다"` 도출  
  
<br>  

**5. displayLyrics**  

  - `searchLyrics`에서 받아온 가사를 줄바꿈을 넣어 `String`타입으로 도출  
  
      <br><br><br>
      
## YoutubeLyrics  

<br>

**1. MainLayout**  
 
self.lyrics  
  - `QTextEdit` 위젯이며 읽기만 가능  
  - 폰트 사이즈는 13으로 설정  
     
self.songTitle  
  - `QTextEdit` 위젯이며 읽기만 가능  
  - 폰트 사이즈는 16으로 설정  
  - 볼드체로 설정  
     
self.artist  
  - `QLineEdit` 위젯이며 읽기만 가능  
  - 폰트 사이즈는 14으로 설정  
     
self.urlInput  
  - `QLineEdit` 위젯  
     
self.submitButton  
  - `QToolButton` 위젯  
  - `self.submitUrl`과 연결되어 있음  
    
self.resetButton  
  - `QToolButton` 위젯   
  - `self.reset`과 연결되어 있음  
  
 <br><br>  
        
**2. searchLyrics**  

<br>  

  - 받아온 `url` 값을 인자로 `Search`모듈을 실행하고 `urlInput`에 입력값을 지움  
  - 노래 제목 뒤에 (Feat. ...)이 붙었을 경우 길어지기 때문에 `"("`앞에서 줄바꿈을 할 수 있도록 함  
  - 혹은 (Feat. ...)이 붙지 않더라도 길어지는 경우를 대비해 20번째 글자에서 줄바꿈을 할 수 있도록 함  
  - `self.songTitle`을 `self.search.searchSong()`에서 받아온 노래 제목 값으로 설정  
  - `self.artist`을 `self.search.searchArtist()`에서 받아온 아티스트 값으로 설정  
  - `self.lyrics`을 `self.search.displayLyrics()`에서 받아온 가사 값으로 설정  
  
<br><br>   
        
**3. submitUrl**  

 <br>  
 
  - `submit` 버튼 클릭 시 `url` 값을 사용자가 입력한 값으로 설정함   
  - 사용자가 입력한 값이 유튜브 링크가 맞는지 확인하고 아닐시 입력값 삭제    

<br><br>  
        
**4. reset**  

<br>  

  - `self.lyrics`, `self.songTitle`, `self.artist` 삭제  
     
      
      
     
    
<br><br><br><br><br><br>
<br><br><br><br><br><br>

## 결과물
<br>


+ 구현하고 싶은 것    
 - 글자 크기 조절  
 - 윈도우 투명도 조절  
 - 윈도우 항상 맨 위에 위치  
     
     
+ 구현하려 했으나 못한 것, 삭제한 것    
 - 자동으로 url 받아오기  
    - 해당 페이지와 연결하는 것이 아니라 크롬 프로그램과 연결해야 하는 것으로 보임    
      실시간으로 url을 받아올 수 있는 모듈을 찾아야 함   
 - 가사 댓글을 여러 개 받아오기  
    - 댓글 html 태그가 다 비슷해서 가사 댓글을 찾기 어려울 줄 알았는데 여러 번 시도 했더니 결국 찾아서 삭제함  
      간혹가다 외국어 버전 가사 댓글도 있기 때문에 다시 추가할 예정  
 - 유튜브 노래 태그 이용해서 데이터 받아오기
    - 유튜브 자체에 노래 정보 태그를 이용해 데이터를 추출하려 했으나 노래태그가 링크 형식으로 되어있어서 text형식으로 추출되지 않음  
      이것을 이용하면 공식 음원이 아니더라도 정확한 정보 추출이 가능하기 때문에 추가할 예정
 - 네이버 검색 후 정보 받아오기  
    - url 자체가 다르기 때문에 웹스크랩을 한 번 거친 뒤 정보를 걸러낸 후 다시 다른 웹스크랩을 해야함(매우매우매우복잡)
      이것을 이용하면 노래 플레이리스트에서도 가사 지원이 가능하기 때문에 추가를 희망함
    
    
<br><br><br>
----------------------------------------
<br><br><br>

## 참고  

<br> 
https://itholic.github.io/linux-path/
https://hyomyo.tistory.com/51
https://yuda.dev/260
https://shinminyong.tistory.com/10
https://m.blog.naver.com/kiddwannabe/221177292446
https://hogni.tistory.com/21
https://beomi.github.io/gb-crawling/posts/2017-01-20-HowToMakeWebCrawler.html
https://tariat.tistory.com/757
https://madplay.github.io/post/python-urllib
https://webisfree.com/2017-11-18/python%EC%97%90%EC%84%9C-%EC%99%B8%EB%B6%80-url%EC%9D%84-%ED%98%B8%EC%B6%9C%ED%95%98%EB%8A%94-%EB%B0%A9%EB%B2%95%EC%9D%80

