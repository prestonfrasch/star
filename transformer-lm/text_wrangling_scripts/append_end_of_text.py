import os
directory = './'

for subdirectories, directories, files in os.walk(directory):
    if filename.enswith(".txt"):
        with open("test.txt", "a") as myfile:
            myfile.write("<|endoftext|>")