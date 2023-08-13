# from pathlib import Path

# content = Path("newfile.txt").read_text().replace('\n', ' ')
# print(content)
# import os
def identifyLastLine(route):
    content_variable = open(route, 'r')
#content_variable = open('../newfile.txt', 'r')
    file_lines = content_variable.readlines ()
    content_variable.close ()
    ultima_linea = file_lines [len (file_lines) -1]
    return print(ultima_linea)
# while(True):
#     linea = f.readline()
#     print(linea)
#     if not linea:
#         break
# f.close()