import os
import fontforge
import psMat


def main():
    PROJECTDIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../')
    font_path = os.path.join(PROJECTDIR, 'fonts/GenJyuuGothic-Monospace-Regular.ttf')
    font = fontforge.open(font_path)
    ascent = 800
    descent = 200
    old_em = 1024
    em = ascent + descent
    font.ascent = float(ascent) / em * old_em
    font.descent = float(descent) / em * old_em
    font.em = em
    scale = psMat.scale(0.86)
    x = em * (1 - 0.86) / 2
    trans = psMat.translate(x, 0)
    mat = psMat.compose(scale, trans)
    for glyph in font.glyphs():
        if glyph.isWorthOutputting():
            width = glyph.width
            glyph.transform(mat)
            glyph.width = width
    save_path = os.path.join(PROJECTDIR, 'fonts/GenJyuuGothic-Monospace-Regular-edited.ttf')
    font.generate(save_path)
    return save_path
