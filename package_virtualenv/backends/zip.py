from zipfile import ZipFile
from .. import utils
from .. import ldd
import os
import re


def collect_filenames(root):
    if root.endswith("/"): root = root[:-1]
    name = os.path.basename(root)
    root_pat = re.compile("^" + re.escape(root + "/"))

    # Collect the virtualenvs
    for filename in utils.find_files(root):
        without_root = root_pat.sub("", filename)
        arcname = os.path.join("/virtualenvs", name, without_root)
        yield (filename, arcname)
    
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
