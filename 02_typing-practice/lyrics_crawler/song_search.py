from .utils import *

def search_songs(driver, title) -> list :
    title = title.strip().replace(' ', '%20')
    url = "https://vibe.naver.com/search?query="+title
    soup = load_parsed_page(driver, url)

    songs = soup.select("div.info_area")
    results = []
    count = 0
    for song in songs:
        title_tag = song.select_one("div.title span.inner a span")
        artist_tag = song.select_one("div.artist a")
        link_tag = song.select_one("div.title span.inner a")

        if not (title_tag and artist_tag and link_tag):
            continue

        results.append({
            "title": title_tag.get_text(),
            "artist": artist_tag.get_text(),
            "link": "https://vibe.naver.com" + link_tag["href"]
        })

        count += 1
        if count >= 3 : break

    return results
