from .driver_manager import create_driver, close_driver
from .song_search import search_songs
from .lyrics_fetcher import get_lyrics

__all__ = [
    "create_driver",
    "close_driver",
    "search_songs",
    "get_lyrics"
]