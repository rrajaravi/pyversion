import unittest
import subprocess
import os

from pyversion import version, get_path, get_dir

class PyversionTester(unittest.TestCase):
    def test_syslib_version(self):
        self.assertIsNone(version('hasattr'))

    def test_thirdparty_version(self):
        self.assertIsNotNone(version('jinja2'))

    def test_getpath(self):
        self.assertTrue(os.path.isfile(get_path('os')))

    def test_getdir(self):
        self.assertTrue(os.path.isdir(get_dir('os')))

if __name__ == '__main__':
    unittest.main()
