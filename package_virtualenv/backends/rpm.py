from subprocess import Popen, PIPE


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
            result.add(line)
    return result


def build_spec(preamble, files=[]):
    lines = []
    for key, value in sorted(preamble.items()):
        lines.append("%s: %s" % (key, value))
    
    lines.append("")
    lines.append("%files")
    for filename in files:
        lines.append(filename)

    lines.append("")

    return "\n".join(lines)
