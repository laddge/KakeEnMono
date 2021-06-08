import os
import fontforge


def main():
    PROJECTDIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../')
    font_path = os.path.join(PROJECTDIR, 'fonts/togoshi-mono.ttf')
    font = fontforge.open(font_path)
    ascent = 850
    descent = 250
    old_em = 1024
    em = ascent + descent
    font.ascent = float(ascent) / em * old_em
    font.descent = float(descent) / em * old_em
    font.em = em
    save_path = os.path.join(PROJECTDIR, 'fonts/togoshi-mono-edited.ttf')
    font.generate(save_path)
    return save_path
