import os
import re


def find_libraries(root):
    for (dirpath, dirnames, filenames) in os.walk(root):
        for filename in filenames:
            if filename.endswith(".so"):
                yield os.path.join(dirpath, filename)


def find_files(root):
    for dirpath, dirnames, filenames in os.walk(root):
        for filename in filenames:
            full_path = os.path.join(dirpath, filename)
            yield os.path.abspath(full_path)

        # check for symlinked directories
        for dirname in dirnames:
            full_path = os.path.abspath(os.path.join(dirpath, dirname))
            if os.path.islink(full_path):
                yield full_path
