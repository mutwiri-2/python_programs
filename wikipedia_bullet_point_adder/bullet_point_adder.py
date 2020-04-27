#! python3
# bullet_point_adder.py - inserts wikipedia bullet points (*) to the start of each line of text on the clipboard

import pyperclip

text = pyperclip.paste() # get text from clipboard

lines = text.split('\n')  # get a list of all lines in the text copied
for i in range(len(lines)):
    lines[i] = '* ' + lines[i] # add bullet point to each line
'\n'.join(lines)  # join the modified lines into a string ready to be copied to the clipboard

pyperclip.copy()