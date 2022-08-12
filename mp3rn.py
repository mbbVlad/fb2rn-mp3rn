#!/usr/bin/python3
"""Rename Music-files according to Artist and/or Title and/or Track
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
            python3 mp3rn.py P your_file.mp3
"""
import os
import sys
import glob
import mutagen


__AUTHOR__ = 'MBB'
__VERSION__ = 0.02
__all__ = ['get_mp3_tags', 'print_info']


def get_mp3_tags(mp3):
    """From Music-file retrieve artist and title and track tags
    """
    _info = mutagen.File(mp3)
    a = _info.get('TPE1', ('UnknownArtist', ''))[0]     # artist
    t = _info.get('TIT2', ('UnknownTitle', ''))[0]      # title
    r = _info.get('TRCK', ('UnknownTrack', ''))[0]      # track
    y = str(_info.get('TDRC', ('UnknownYear', ''))[0])  # year
    g = _info.get('TCON', ('UnknownGenre', ''))[0]      # genre
    b = _info.get('TALB', ('UnknownAlbum', ''))[0]      # album
    return a, t, r, y, g, b


def print_info(fn, **kwargs):
    """Only print some tags
    """
    print('\n==Common info==')
    print('File:', fn)
    print('Artist:', kwargs['a'])
    print('Title:', kwargs['t'])
    print('Album:', kwargs['b'])
    print('Year:', kwargs['y'])
    print('Genre:', kwargs['g'])
    print('Track №:', kwargs['r'])

    if fn.upper().endswith('MP3'):
        from mutagen.mp3 import MP3
        i = MP3(fn).info
        print('\n==MP3 info==')
        print('Length:', int(i.length//60), 'm', round(i.length % 60), 's')
        print('Channels:', i.channels)
        print(i.bitrate_mode)
        print('Bitrate:', i.bitrate//1000)
        print('Sample rate:', i.sample_rate)
        print('Track gain:', i.track_gain)
        print('Track peak:', i.track_peak)
        print('Album gain:', i.album_gain)
        print('Encoder info:', i.encoder_info)
        print('Encoder settings:', i.encoder_settings)
        print('Version:', i.version)
        print('Layer:', i.layer)
        print('Mode:', i.mode)


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
                d = dict(A=_artist.upper(), a=_artist, T=_title.upper(), t=_title, R=_track, r=_track,
                         Y=_year, y=_year, G=_genre.upper(), g=_genre, B=_album.upper(), b=_album)
                if _1st == 'P':
                    print_info(ar, **d)
                    continue
                newMP3 = ''.join(d.get(c, c) + (' ' if _1st == '+' else '') for c in ar_1st)
                try:
                    os.rename(ar, newMP3.rstrip() + _ext)
                except OSError:
                    print('I can`t to rename', ar)
                    print(sys.exc_info())
            else:
                print("File", ar, "not found!")
