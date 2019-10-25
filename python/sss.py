#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  sss.py


def main(args):
    imie = input('Jak się nazywasz?\n')
    print('witaj', imie, '!')

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
