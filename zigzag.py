# a simple animation program that creates a back and forth zigzag pattern until user stops it by pressing ctrl+c

import sys, time

indent = 0 # how many white spaces to add
indent_increasing = True # if white spaces are increasing or not

try:
    while True: # main program loop
        print(' ' * indent, end='')
        print('*' * 10)
        time.sleep(0.1)
    
        if indent_increasing:
            indent += 1
            if indent == 20: # change direction
                indent_increasing = False
        else:
            indent -= 1
            if indent == 0: # change direction
                indent_increasing = True
except KeyboardInterrupt:
    sys.exit()