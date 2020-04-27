#! python3
# bullet_point_adder.py - inserts wikipedia bullet points (*) to the start of each line of text on the clipboard

import pyperclip

text = pyperclip.paste()

#todo - Convert text copied to a wikipedia-style list

pyperclip.copy()