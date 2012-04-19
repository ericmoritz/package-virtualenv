import unittest
from package_virtualenv import ldd
import os
import fixtures


class TestFindLinks(unittest.TestCase):

    def test(self):
        fixture = os.path.join(fixtures.VIRTUALENV, "lib/python2.6/site-packages/lxml/etree.so")
        expected = fixtures.LIBRARIES
        result = ldd.links(fixture)
        self.assertEqual(result, expected)


class TestWalkLinks(unittest.TestCase):
    
    def test(self):
        fixture = os.path.join(fixtures.VIRTUALENV, "lib/python2.6/site-packages/lxml/etree.so")
        expected = fixtures.LIBRARIES
        result = ldd.walk_links(set(), fixture)
        self.assertEqual(expected, result)
        
