import os
from package_virtualenv import utils
import unittest

HERE = os.path.abspath(os.path.dirname(__file__))


class TestFindLibraries(unittest.TestCase):
    
    def test(self):
        root = os.path.join(HERE, "fixtures/test-env/")
        
        expected = set([os.path.join(root, filename)
                    for filename in 
                    ['lib/python2.6/site-packages/lxml/etree.so',
                     'lib/python2.6/site-packages/lxml/objectify.so']
                    ])

        result = set(utils.find_libraries(root))

        self.assertEqual(expected, result)
