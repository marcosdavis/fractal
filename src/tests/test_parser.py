import unittest
from parser import parser

class TestParser(unittest.TestCase):
    def test_parsed_correctly(self):
        mb = parser('tests/test_files/mandelbrot.frac')
        self.assertIn('centerx', mb)
        self.assertIn('centery', mb)
        self.assertIn('axislength', mb)
        self.assertIn('pixels', mb)
        self.assertIn('iterations', mb)

    def test_parsed_incorrectly(self):
        self.assertRaises(RuntimeError, parser, 'tests/test_files/missing-value.frac')
        self.assertRaises(RuntimeError, parser, 'tests/test_files/no-colons.frac')
        self.assertRaises(RuntimeError, parser, 'tests/test_files/no-property-name.frac')
        self.assertRaises(RuntimeError, parser, 'tests/test_files/too-many-colons.frac')