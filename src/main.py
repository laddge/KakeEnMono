import os
import fontforge
import ubuntumono
import genjyuu


def main():
    PROJECTDIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../')
    ubuntumono_fn = ubuntumono.main()
    genjyuu_fn = genjyuu.main()
    font = fontforge.open(ubuntumono_fn)
    font.mergeFonts(genjyuu_fn)
    font.selection.none()
    font.selection.select(0x2610)
    font.copy()
    font.selection.select(0x3000)
    font.paste()
    font.selection.select(0x271a)
    font.copy()
    font.selection.select(0x3000)
    font.pasteInto()
    font.intersect()
    font.copyright = '''Copyright (c) 2021 Laddge
[Ubuntu Mono]
Copyright 2011 Canonical Ltd.  Licensed under the Ubuntu Font Licence 1.0

[Source Han Sans]
Copyright (c) 2014, 2015 Adobe Systems Incorporated (http://www.adobe.com/), with Reserved Font Name 'Source'.

[M+ OUTLINE FONTS]
Copyright(c) 2015 M+ FONTS PROJECT'''
    font.familyname = 'KakeEn Mono'
    font.fontname = 'KakeEnMono-Regular'
    font.fullname = 'KakeEn Mono'
    font.version = '1.0.0'
    font.generate(os.path.join(PROJECTDIR, 'fonts/KakeEnMono-Regular.ttf'))


if __name__ == '__main__':
    main()
