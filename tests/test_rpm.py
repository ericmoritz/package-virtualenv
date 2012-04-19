import unittest
import sys
from package_virtualenv.backends import rpm
import os
from itertools import imap
import fixtures


class TestGetPackageName(unittest.TestCase):
    def test(self):
        expected = "iptables"
        result = rpm.get_package_name("iptables-1.4.7-3.el6.x86_64")
        self.assertEqual(expected, result)


class TestFindPackages(unittest.TestCase):

    def test(self):
        result = rpm.find_packages(fixtures.LIBRARIES)
        expected = fixtures.PACKAGES

        self.assertEqual(expected, result)


class TestBuildSpec(unittest.TestCase):
    
    def test(self):
        expected = """Name: test-rpm
Summary: A test rpm
Version: 1.0
Release: 1
License: BSD
Requires: required-package, other-required-package

%description
A long description

%build
mkdir -p $RPM_BUILD_ROOT/tmp/test-env
cp -r /tmp/test-env/* $RPM_BUILD_ROOT/tmp/test-env/

%files
/tmp/test-env/foo
"""

        result = rpm.build_spec("/tmp/test-env/",
                                name="test-rpm",
                                summary="A test rpm",
                                description="A long description",
                                version="1.0",
                                release="1",
                                license="BSD",
                                files=["/tmp/test-env/foo"],
                                requires=["required-package",
                                          "other-required-package"])
        print expected
        print
        print result

        self.assertEqual(expected, result)

        
class TestCollectItems(unittest.TestCase):

    def test(self):
        def make_fixture(filename):
            return os.path.join(fixtures.VIRTUALENV, filename)

        expected = {"files": set(imap(make_fixture,
                                 fixtures.FILES)),
                    "packages": fixtures.PACKAGES}

        result = rpm.collect_items(fixtures.VIRTUALENV)

        self.assertEqual(expected, result)
