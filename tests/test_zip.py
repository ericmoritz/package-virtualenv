from pprint import pprint
from package_virtualenv.backends import zip
import unittest
import os

HERE = os.path.abspath(os.path.dirname(__file__))


class TestCollectFilenames(unittest.TestCase):
    
    def test(self):
        root = os.path.join(HERE, "fixtures", "test-env")

        def make_fixture(line):
            filename = line.strip()
            if filename.startswith("/"):
                return filename, filename
            else:
                return (os.path.join(root, filename),
                        os.path.join("/virtualenvs/test-env", filename))

        
        expected = set(map(make_fixture,
                           open(os.path.join(HERE, "fixtures", "filelist.txt"))))

        result = set(zip.collect_filenames(root))

        self.assertEqual(expected, result)
