# 250605 ~ 07

from lyrics_crawler import create_driver, close_driver, search_songs, get_lyrics
import typing_speed_module as ts
import datetime


driver = create_driver()

while True:
    title = input("노래 제목 또는 가수를 입력해 주세요 > ")
    songs = search_songs(driver, title)

    if songs:
        print("검색 결과 :")
        for i, song in enumerate(songs, 1):
            print(f"{i}. {song['title']} - {song['artist']}")
        break
    else:
        print("곡 정보를 찾을 수 없습니다.")

num = int(input("번호를 선택해 주세요 > "))
lyrics = get_lyrics(driver, songs, num)
close_driver(driver)


start_time = datetime.datetime.now()
user_typing = input(lyrics +'\n')

print("타수 :", ts.speed(start_time, len(user_typing)))
print("점수 :", ts.score(lyrics, user_typing.strip()))
print(f"총 {len(lyrics)} 글자 중 {ts.count_correct_answers(lyrics, user_typing.strip())}개 일치")
