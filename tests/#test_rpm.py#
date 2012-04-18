import unittest
import sys
from package_virtualenv.backends import rpm
import os


HERE = os.path.abspath(os.path.dirname(__file__))


class TestFindPackages(unittest.TestCase):

    def test(self):
        lib_set = set([
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


        expected = set([
                'libgpg-error-1.7-4.el6.x86_64',
                'libxml2-2.7.6-4.el6_2.4.x86_64',
                'python-libs-2.6.6-29.el6.x86_64',
                'libgcrypt-1.4.5-9.el6_2.2.x86_64',
                'glibc-2.12-1.47.el6_2.9.x86_64',
                'zlib-1.2.3-27.el6.x86_64',
                'libxslt-1.1.26-2.el6.x86_64'
                ])

        result = rpm.find_packages(lib_set)
    
        self.assertEqual(expected, result)


class TestBuildSpec(unittest.TestCase):
    
    def test(self):
        expected = """Name: test-rpm
Release: 1
Summary: A test rpm
Version: 1.0

%files
/tmp/foo
"""

        result = rpm.build_spec({"Name": "test-rpm",
                                 "Summary": "A test rpm",
                                 "Version": "1.0",
                                 "Release": "1"},
                                files=["/tmp/foo"])
        
        self.assertEqual(expected, result)
        
