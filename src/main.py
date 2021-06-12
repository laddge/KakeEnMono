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
    font.generate(os.path.join(PROJECTDIR, 'fonts/Sova_Mono-Regular.ttf'))


if __name__ == '__main__':
    main()
