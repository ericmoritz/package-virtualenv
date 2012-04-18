import os
import re

def find_libraries(root):
    for (dirpath, dirnames, filenames) in os.walk(root):
        for filename in filenames:
            if filename.endswith(".so"):
                yield os.path.join(dirpath, filename)

