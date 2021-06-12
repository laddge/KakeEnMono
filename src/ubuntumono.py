import os
import psMat
import fontforge


def main():
    PROJECTDIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../')
    font_path = os.path.join(PROJECTDIR, 'fonts/UbuntuMono-Regular.ttf')
    font = fontforge.open(font_path)
    save_path = os.path.join(PROJECTDIR, 'fonts/UbuntuMono-Regular-edited.ttf')
    font.generate(save_path)
    return save_path
