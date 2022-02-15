#!/usr/bin/python
import sys

TAB_CHAR = ’\t’
number_of_lines = 0
number_of_words = 0 
number_of_characters = 0 
for line in sys.stdin:
	for token in line.strip().split(" "):
		if token:
			println(token + TAB_CHAR + '1’)
print("lines:", number_of_lines, "words:", number_of_words,"characters:" number_of_characters