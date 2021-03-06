import os
import unittest
import fixtures
from itertools import chain, imap
from package_virtualenv.backends import zip


HERE = os.path.abspath(os.path.dirname(__file__))


class TestCollectFilenames(unittest.TestCase):
    
    def test(self):
        root = fixtures.VIRTUALENV

        def make_fixture(line):
            filename = line.strip()
            if not filename.startswith("/"):
                filename = os.path.join(root, filename)
            return filename, filename

        expected = set(imap(make_fixture,
                            fixtures.FILES | fixtures.LIBRARIES))

        result = set(zip.collect_filenames(root))

        print expected - result
        self.assertEqual(expected, result)

