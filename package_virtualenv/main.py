from .backends import zip as zip_backend
from .backends import rpm as rpm_backend
from optparse import OptionParser


BACKENDS = {
    "zip": zip_backend,
    "rpm-spec": rpm_backend,
}


def main():
    parser = OptionParser(usage="usage: %prog [options] virtualenv-root out-filename")
    parser.add_option("-b", "--backend", dest="backend", default="zip",
                      help="backend choices: %s; zip default" % ", ".join(sorted(BACKENDS.keys())),
                      choices=sorted(BACKENDS.keys()))
    
    (options, args) = parser.parse_args()
    if len(args) != 2:
        parser.error("virtualenv-root and out-filename required")
        return

    backend         = BACKENDS[options.backend]
    virtualenv_root = args[0]
    out_filename    = args[1]

    backend.build(virtualenv_root, out_filename)
