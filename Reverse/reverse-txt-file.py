# reverse-txt-file.py
# Script that reverses the order of lines in a text file.
# 12.3.2025 (C) DAREKPAGES
# python 3.12.1

from sys import argv
buff = []
met = 0

argv
if len(argv) < 3:
    print('No arguments! Specify source and output text file names, one after another.')
else:
    source_file = argv[1]
    result_file = argv[2]
    with open(source_file, 'r') as f:
        while(True):
            row = f.readline() #read row file
            if row == '': #end of file
                buff.reverse()
                for r in buff:
                    met += 1
                    with open(result_file, 'a') as ft: #save row to file
                        ft.write(r)
                        print('reserved:', met, end='\r')
                break
            if row.find('\n') == -1:
                row = row + '\n'
            buff.append(row)