import os
import fontforge
import ubuntumono
import genjyuu


def main():
    PROJECTDIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../')
    # Ubuntu Monoをいじる
    ubuntumono_fn = ubuntumono.main()
    # 源柔ゴシックをいじる
    genjyuu_fn = genjyuu.main()
    # 改変したUbuntu Monoを開く
    font = fontforge.open(ubuntumono_fn)
    # 改変した源柔ゴシックをマージ
    font.mergeFonts(genjyuu_fn)
    # 全角スペースを可視化
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
    # フォント情報を改変
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
    font.version = '1.0.1'
    # 保存
    font.generate(os.path.join(PROJECTDIR, 'fonts/KakeEnMono-Regular.ttf'))


if __name__ == '__main__':
    main()
