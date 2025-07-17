# 02_typing-practice (VIBE 웹 크롤링 + 타자 연습 프로그램)   

> **제작 기간** : 2025.06.05 ~ 2025.06.07    
> **실행 환경** : Python 콘솔 (Command Line Interface)
          
---

## 프로젝트 소개

네이버 **VIBE 음악 플랫폼에서 노래 가사를 크롤링하여**,   
해당 가사로 **타자 연습을 진행하는 콘솔 기반 프로그램**입니다.

- 웹 크롤링을 통한 데이터 수집
- 모듈 및 패키지 구조 설계 연습
---

## 주요 기능
1. **노래 검색**  
   - 사용자가 입력한 키워드로 VIBE에서 노래 검색  
2. **가사 크롤링**  
   - 선택한 노래의 가사를 VIBE에서 추출  
3. **타자 연습**  
   - 가져온 가사로 타자 연습  
   - 타수 및 정확도 계산 결과 출력   

---

## 폴더 구조
```
02_typing-practice/
├── lyrics_crawler/          # 가사 크롤링 모듈
│   ├── driver_manager.py
│   ├── lyrics_fetcher.py
│   ├── song_search.py
│   └── utils.py
├── main.py                  # 실행 파일
└── typing_speed_module.py   # 타자 측정 기능
```
---

## 외부 라이브러리

**selenium** : 브라우저 자동화 (동적 웹사이트 크롤링용)     
**beautifulsoup4** : HTML 파싱 (정적 웹 데이터 해석)

아래 명령어로 필수 라이브러리를 설치하세요.  
> pip install selenium beautifulsoup4
 
---

## 실행 예시
프로그램 실행 화면입니다.  
노래 검색부터 결과 계산까지의 흐름을 담고 있습니다.
> 흐름 요약 :     
노래 제목 입력 → 노래 선택 → 가사 출력 및 타자 입력 → 결과 출력

![typing_speed](https://github.com/user-attachments/assets/b61de496-4585-4217-a6bf-2fdc123dea4c)