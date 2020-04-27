#! python3
# bullet_point_adder.py - inserts wikipedia bullet points (*) to the start of each line of text on the clipboard

import pyperclip

text = pyperclip.paste() 

lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = '* ' + lines[i]
'\n'.join(lines)

pyperclip.copy()