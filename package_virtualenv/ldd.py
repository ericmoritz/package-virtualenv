from subprocess import PIPE, Popen
import re

ldd_line_pat = re.compile("^(.+) => (.*) ")


def links(library_filename):
    p = Popen(["ldd", library_filename],
              stdout=PIPE,
              stderr=PIPE)
    returncode = p.wait()
    
    if returncode:
        raise Exception(p.stderr.read())

    result = set()
    for line in p.stdout:
        match = ldd_line_pat.match(line)

        if match:
            linked_lib = match.group(2)
            if linked_lib:
                result.add(linked_lib)

    return result


# This may not be needed, I'm not sure of ld
# links third party libraries.
def walk_links(accum, library_filename):
    for link in links(library_filename):
        if link not in accum:
            accum.add(link)
            walk_links(accum, link)

    return accum
