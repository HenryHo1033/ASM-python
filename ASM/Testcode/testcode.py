import os

file_path = os.path.abspath('test2.txt')
with open('C:\\Pycode\\ASM-python\\test2.txt', 'r') as f:
        contents = f.read()

        print(contents)