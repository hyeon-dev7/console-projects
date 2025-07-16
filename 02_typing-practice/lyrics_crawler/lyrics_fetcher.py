from .utils import *
import re # 정규식


def get_lyrics(driver, lst, num) -> str :
    url = lst[num-1]["link"]
    soup = load_parsed_page(driver, url)

    try :
        lyrics_repr = (soup.select_one("#content > div.end_section.section_lyrics > div > p").get_text(strip=True))
        # repr()로 감싸서 print하면 \n \r가 나오는데, 이걸 replace로 없애지 않으면 그냥 print 했을 때 가사가 잘려 나옴
    except :
        raise Exception("가사 정보가 없습니다.")

    lyrics = re.sub(r'\s+', ' ', lyrics_repr) # 줄바꿈 및 공백 정리
    return re.sub(r"^['\"]|['\"]$", '', lyrics) # 가장 앞, 뒤 ' 또는 " 제거
