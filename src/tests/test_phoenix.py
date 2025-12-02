import unittest
from phoenix import Phoenix
from parser import parser

class TestPhoenix(unittest.TestCase):
    def test_px_keys(self):
        self.assertRaises(RuntimeError, Phoenix, parser('tests/test_files/commented-out-property.frac'))
        self.assertRaises(RuntimeError, Phoenix, parser('tests/test_files/no-centerx.frac'))
        self.assertRaises(RuntimeError, Phoenix, parser('tests/test_files/no-iterations.frac'))

    def test_px_conversion(self):
        px = Phoenix(parser('tests/test_files/phoenix.frac'))
        self.assertIsInstance(px.cimag, float)
        self.assertIsInstance(px.creal, float)
        self.assertIsInstance(px.pimag, float)
        self.assertIsInstance(px.preal, float)
        self.assertIsInstance(px.centerx, float)
        self.assertIsInstance(px.centery, float)
        self.assertIsInstance(px.axislength, float)
        self.assertIsInstance(px.iterations, int)
        self.assertIsInstance(px.pixels, int)
        self.assertRaises(RuntimeError, Phoenix, parser('tests/test_files/bad-int-value.frac'))
        self.assertRaises(RuntimeError, Phoenix, parser('tests/test_files/bad-float-value.frac'))
        self.assertRaises(RuntimeError, Phoenix, parser('tests/test_files/negative-axislen.frac'))
        self.assertRaises(RuntimeError, Phoenix, parser('tests/test_files/zero-axislen.frac'))