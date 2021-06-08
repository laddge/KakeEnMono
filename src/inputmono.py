import os
import fontforge


def main():
    PROJECTDIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../')
    font_path = os.path.join(PROJECTDIR, 'fonts/InputMono-Regular.ttf')
    font = fontforge.open(font_path)
    save_path = os.path.join(PROJECTDIR, 'fonts/InputMono-Regular-edited.ttf')
    font.save(save_path)
    return save_path
