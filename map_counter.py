#!/usr/bin/python
import sys

TAB_CHAR = ’\t’

for line in sys.stdin:
    print('lines' + TAB_CHAR + '1')
    for word in line.strip().split(" "):
        if word: 
            print('words' + TAB_CHAR + '1')
            for letter in word:
                print('chars' + TAB_CHAR + '1')