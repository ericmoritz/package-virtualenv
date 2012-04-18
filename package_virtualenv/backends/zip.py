from zipfile import ZipFile
from .. import utils
from .. import ldd
import os
import re


def collect_filenames(root):
    name = os.path.basename(root)
    root_pat = re.compile("^" + re.escape(root + "/"))

    # Collect the virtualenvs
    for dirpath, dirnames, filenames in os.walk(root):
            without_root = root_pat.sub("", dirpath)
            for filename in filenames:
                arcname = os.path.join("/virtualenvs", name, without_root, filename)
                full_path = os.path.join(dirpath, filename)

                yield (full_path, arcname)
    
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
