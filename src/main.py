import os
import fontforge


def main():
    FONTDIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../fonts')
    font = fontforge.font()
    font.mergeFonts(os.path.join(FONTDIR, 'InputMono-Regular.ttf'))
    font.mergeFonts(os.path.join(FONTDIR, 'togoshi-mono.ttf'))
    font.generate(os.path.join(FONTDIR, 'Sova_Mono-Regular.ttf'))


if __name__ == '__main__':
    main()
