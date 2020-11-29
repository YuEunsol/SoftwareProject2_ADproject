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
<!---  - TitleScrap  
    -영상 제목을 추출하여 songInfo.py에 저장
  - DetailScrap  
    -상세 정보를 추출하여 songInfo.py에 저장
  - CommentScrap  
    -15줄 이상의 상위 댓글 5개를 추출하여 songInfo.py에 저장
  - Refresh  
    -새로고침하여 모든 정보를 새로 추출--->
  - Scrap  
    -긁어온 `html` 정보 중 영상 제목, 상세 정보, 댓글을 추출하여 `String`으로 출력  
   
**search.py**  
  - Search  
    -찾아낸 영상 정보(영상 제목, 상세 정보, 댓글)에서 노래 제목, 아티스트, 가사를 추출하여 출력  
     
     
<!---  - SearchSong  
    -영상 제목, 상세 정보에서 찾아낸 노래 제목을 도출
  - SearchSinger  
    -영상 제목, 상세 정보에서 찾아낸 아티스트를 도출
  - SearchLyrics  
    -상세 정보, 댓글에서 찾아낸 가사를 도출
  - LyricsSort  
    -가사들 중 (상위 댓글->하위 댓글->상세 정보) 순으로 정렬
  - ResetInfo  
    -노래에 대한 정보를 리셋 --->


    


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
   - 동적인 웹 크롤링을 위해 해당 웹의 스크롤을 자동으로 내리는 모듈  
     (가사 댓글은 대체로 상위에 위치하지만, 그렇지 않은 경우도 꽤 있기 때문에 
     여러번의 테스트를 통해 25번의 스크롤을 하기로 결정함
     스크롤의 로딩 또한 기다려야 하기 때문에 스크롤당 딜레이 시간을 
     0.3초로 잡음)  

     lastPageHeight
      - 
     url
      - 현재 url 주소(String)
      
### Scrap
<br>

**1. 자료 구조**

     titleInfo
      - 영상 제목에 대한 정보(String)  
      
     detailInfo
      - 영상 상세 정보에 대한 정보(String) 
      
     commentInfo
      - 영상 댓글에 대한 정보(List)
      
     url
      - 현재 url 주소(String)
      
### Scrap
<br>

**1. 자료 구조**

     titleInfo
      - 영상 제목에 대한 정보(String)  
      
     detailInfo
      - 영상 상세 정보에 대한 정보(String) 
      
     commentInfo
      - 영상 댓글에 대한 정보(List)
      
     url
      - 현재 url 주소(String)
      
### Scrap
<br>

**1. 자료 구조**

     titleInfo
      - 영상 제목에 대한 정보(String)  
      
     detailInfo
      - 영상 상세 정보에 대한 정보(String) 
      
     commentInfo
      - 영상 댓글에 대한 정보(List)
      
     url
      - 현재 url 주소(String)
      
      
     
    
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
