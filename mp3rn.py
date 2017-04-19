#!/usr/bin/python3
"""Rename Music-files according to Artisi and/or Title and/or Track
    a or A - Artist (without change) or ARTIST 
    t or T - Title (without change) or TITLE
    r or R - Track
    y or Y - Year
    g or G - Genre (without change) or GENRE
    b or B - Album (without change) or ALBUM
    Example:
             python3 mp3rn.py +At mus.mp3
             >> "ARTIST Title.mp3"

            python3 mp3rn.py -At mus.mp3
             >> "ARTISTTitle.mp3"
             
            python3 mp3rn.py -A_t mus.mp3
             >> "ARTIST_Title.mp3"
             
    P - print tags-info on console ("P" must be without -+)
            python3 P mus.mp3
"""
import os
import sys
import mutagen
import glob


__AUTHOR__ = 'MBB'
__VERSION__ = 0.01
__all__ = ['get_mp3_tags', 'print_info']


def get_mp3_tags(mp3):
    """From Music-file retrieve artist and title and track tags
    """
    _info = mutagen.File(mp3)
    a = _info.get('TPE1', ('UnknownArtist',''))[0]     # artist
    t = _info.get('TIT2', ('UnknownTitle',''))[0]      # title
    r = _info.get('TRCK', ('UnknownTrack',''))[0]      # track
    y = str(_info.get('TDRC', ('UnknownYear',''))[0])  # year
    g = _info.get('TCON', ('UnknownGenre',''))[0]      # genre
    b = _info.get('TALB', ('UnknownTrack',''))[0]      # album
    return a, t, r, y, g, b

def print_info(fn):
    """Onle print some tags
    """
    print('File:', fn)
    print('Artist:', _artist)
    print('Title:', _title)
    print('Album:', _album)
    print('Year:', _year)
    print('Genre:', _genre)
    print('Track №:', _track)

if __name__ == '__main__':
    ar_1st = sys.argv[1][1:]
    _1st = sys.argv[1][0]

    if _1st not in '-+P':
        print('1st argument is bad!')
        exit(1)

    for _c in ar_1st:
        if _c in """!@#$&~%*()[]{}"'\:;><`""":
            print(_c, 'is bad separator!')
            exit(2)

    for ar1 in sys.argv[2:]:
        for ar in glob.glob(ar1):
            if os.path.exists(ar):
                _, _ext = os.path.splitext(ar)
                _artist, _title, _track, _year, _genre, _album = get_mp3_tags(ar)
                d = dict(A=_artist.upper(), a=_artist, T=_title.upper(), t=_title,
                         R=_track, r=_track, Y=_year, y=_year, G=_genre.upper(), g=_genre,
                         B=_album.upper(), b=_album)
                if _1st == 'P':
                    print_info(ar)
                    continue
                newMP3 = ''.join(d.get(c, c) + (' ' if _1st == '+' else '') for c in ar_1st)
                try:
                    os.rename(ar, newMP3.rstrip() + _ext)
                except OSError:
                    print('I can`t to rename', ar)
                    print(sys.exc_info())
            else:
                print("File", ar, "not found!")
