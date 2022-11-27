# WAP to print lyrics of your favorite song.
# from PyLyrics import *

# print(PyLyrics.getLyrics('Taylor Swift','blank space')) 
# import lyricwikia
# lyrics = lyricwikia.get_lyrics('Led Zeppelin', 'Stairway to heaven')
# print(lyrics)

from lyricsgenius import Genius

genius = Genius()
genius.search_artist('Andy Shauf')
print(genius)