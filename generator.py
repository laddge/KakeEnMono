#!/usr/bin/env python2

import sys
import fontforge


def main():
    font = fontforge.font()
    font.mergeFonts(sys.argv[-1])
    font.mergeFonts(sys.argv[-2])
    font.generate('Sova_Mono-Regular.ttf')


if __name__ == '__main__':
    main()
