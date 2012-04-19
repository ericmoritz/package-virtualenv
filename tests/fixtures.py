from itertools import imap
import os


HERE = os.path.abspath(os.path.dirname(__file__))


def load_fixture(filename):
    return set(imap(str.strip,
                    open(os.path.join(HERE, "fixtures", filename))))


LIBRARIES  = load_fixture("librarylist.txt")
PACKAGES   = load_fixture("packagelist.txt")
FILES      = load_fixture("filelist.txt")
VIRTUALENV = os.path.join(HERE,
                          "fixtures/test-env/")
