from zipfile import ZipFile
from .. import utils
from .. import ldd
import os
import re


def collect_filenames(root):
    if root.endswith("/"): root = root[:-1]
    name = os.path.basename(root)

    # Collect the virtualenvs
    for filename in utils.find_files(root):
        yield (filename, filename)
    
    # Collect the libraries
    for library in utils.find_libraries(root):
        for link in ldd.links(library):
            yield (link, link)
    

def build(root, outfile):
    zipfile = ZipFile(outfile, "w")
    items = set(collect_filenames(root))

    for localfile, arcfile in items:
        zipfile.write(localfile, arcfile)

    zipfile.close()
