#!/usr/bin/python
import sys

TAB_CHAR = ’\t’
number_of_lines = 0
number_of_words = 0 
number_of_characters = 0 
for line in sys.stdin:
	line = line.split()
	number_of_lines +=1
	number_of_words +=len(words)
	number_of_characters += len(line)

print("lines:", number_of_lines, "words:", number_of_words,"characters:" number_of_characters