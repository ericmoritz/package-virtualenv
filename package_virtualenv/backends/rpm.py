import os
import re
from .. import utils
from .. import ldd
from subprocess import Popen, PIPE

name_pat = re.compile(r"^Name\s+: ([\w_-]+)")

def get_package_name(package_label):
    p = Popen(["rpm", "-qi", package_label],
              stdout=PIPE, stderr=PIPE)
    returncode = p.wait()

    if returncode:
        raise Exception(p.stderr.read())
    
    content = p.stdout.read()

    match = name_pat.match(content)
    if match:
        return match.group(1)
    else:
        raise Exception("Could not find name in 'rpm -qi %' output " % (package_label, ))
    

def find_packages(file_set):
    p = Popen(["rpm", "-qf"] + list(file_set),
              stdout=PIPE, stderr=PIPE)

    returncode = p.wait()
    
    if returncode:
        raise Exception(p.stderr.read())

    result = set()
    for line in p.stdout:
        line = line.strip()
        if line:
            result.add(get_package_name(line))
    return result


def build_spec(virtualenv_root,
               name="",
               version="",
               release="",
               summary="",
               description="",
               preamble={},
               license="Copyright", files=[], requires=[]):

    if virtualenv_root.endswith("/"):
        virtualenv_root = virtualenv_root[:-1]
    virtualenv_root = os.path.abspath(virtualenv_root)
        
    lines = []

    lines.append("Name: %s"    % (name, ))
    lines.append("Summary: %s" % (summary, ))
    lines.append("Version: %s" % (version, ))
    lines.append("Release: %s" % (release, ))
    lines.append("License: %s" % (license, ))    

    for key, value in sorted(preamble.items()):
        lines.append("%s: %s" % (key, value))
    
    if requires:
        lines.append("Requires: %s" % (", ".join(requires)))

    lines.append("")
    lines.append("%description")
    lines.append(description)


    rel_root = virtualenv_root[1:]
    lines.append("")
    lines.append("""%%build
mkdir -p $RPM_BUILD_ROOT/%(rel_root)s
cp -r %(root)s/* $RPM_BUILD_ROOT/%(rel_root)s/"""\
                     % {"root": virtualenv_root,
                        "rel_root": rel_root})

                 
    lines.append("")
    lines.append("%files")


    for filename in files:
        lines.append(filename)

    lines.append("")

    return "\n".join(lines)


def collect_items(root):
    name = os.path.basename(root)
    root_pat = re.compile("^" + re.escape(root + "/"))

    result = {"files": set(utils.find_files(root)),
              "packages": set()}

    # Collect the RPM package names
    links = set()
    for library in utils.find_libraries(root):
        links = links | ldd.links(library)
    
    result['packages'] = find_packages(links)
    
    return result


def build(virtualenv_root, outfile):
    if virtualenv_root.endswith("/"):
        virtualenv_root = virtualenv_root[:-1]

    items = collect_items(virtualenv_root)
    name = os.path.basename(virtualenv_root)

    # TODO add options for the name, verison, release and summary
    spec = build_spec(virtualenv_root,
                      name=name + "-virtualenv",
                      version="0.1",
                      release="1",
                      summary="The %s virtualenv" % name,
                      description="The %s virtualenv" % name,
                      files=items['files'],
                      requires=items['packages'])

    with open(outfile, "w") as fh:
        fh.write(spec)
