import os
import fontforge
import psMat


def main():
    PROJECTDIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../')
    font_path = os.path.join(PROJECTDIR, 'fonts/UbuntuMono-Regular.ttf')
    font = fontforge.open(font_path)
    for glyph in font.glyphs():
        if glyph.unicode in [0x5b, 0x5d]:
            width = glyph.width
            glyph.transform(psMat.scale(1.075))
            glyph.width = width
    save_path = os.path.join(PROJECTDIR, 'fonts/UbuntuMono-Regular-edited.ttf')
    font.generate(save_path)
    return save_path
