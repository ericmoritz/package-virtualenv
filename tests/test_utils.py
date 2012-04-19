import os
from package_virtualenv import utils
import unittest
from itertools import imap
import fixtures


HERE = os.path.abspath(os.path.dirname(__file__))


class TestFindLibraries(unittest.TestCase):
    
    def test(self):
        expected = set(imap(lambda fn: os.path.join(fixtures.VIRTUALENV, fn),
                           ['lib/python2.6/site-packages/lxml/etree.so',
                            'lib/python2.6/site-packages/lxml/objectify.so']))

        result = set(utils.find_libraries(fixtures.VIRTUALENV))
        self.assertEqual(expected, result)


class TestFindFiles(unittest.TestCase):
    
    def test(self):
        expected = set(imap(lambda fn: os.path.join(fixtures.VIRTUALENV, fn),
                           fixtures.FILES))

        result = set(utils.find_files(fixtures.VIRTUALENV))

        self.assertEqual(expected, result)

