import unittest
from package_virtualenv import ldd
import os


HERE = os.path.abspath(os.path.dirname(__file__))


class TestFindLinks(unittest.TestCase):

    def test(self):
        fixture = os.path.join(HERE, "fixtures/test-env/lib/python2.6/site-packages/lxml/etree.so")

        expected = set([
            "/usr/lib64/libxslt.so.1",
            "/usr/lib64/libexslt.so.0",
            "/usr/lib64/libxml2.so.2",
            "/lib64/libz.so.1",
            "/lib64/libm.so.6",
            "/usr/lib64/libpython2.6.so.1.0",
            "/lib64/libpthread.so.0",
            "/lib64/libc.so.6",
            "/lib64/libgcrypt.so.11",
            "/lib64/libdl.so.2",
            "/lib64/libgpg-error.so.0",
            "/lib64/libutil.so.1",
            ])

        result = ldd.links(fixture)

        self.assertEqual(result, expected)


class TestWalkLinks(unittest.TestCase):
    
    def test(self):
        fixture = os.path.join(HERE, "fixtures/test-env/lib/python2.6/site-packages/lxml/etree.so")

        expected = set([
            "/usr/lib64/libxslt.so.1",
            "/usr/lib64/libexslt.so.0",
            "/usr/lib64/libxml2.so.2",
            "/lib64/libz.so.1",
            "/lib64/libm.so.6",
            "/usr/lib64/libpython2.6.so.1.0",
            "/lib64/libpthread.so.0",
            "/lib64/libc.so.6",
            "/lib64/libgcrypt.so.11",
            "/lib64/libdl.so.2",
            "/lib64/libgpg-error.so.0",
            "/lib64/libutil.so.1",
            ])

        result = ldd.walk_links(set(), fixture)

        self.assertEqual(expected, result)
        
