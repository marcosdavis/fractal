import unittest
from septagon import Septagon
from parser import parser


class TestSeptagon(unittest.TestCase):
    def test_sg_keys(self):
        self.assertRaises(RuntimeError, Septagon, parser('tests/test_files/commented-out-property.frac'))
        self.assertRaises(RuntimeError, Septagon, parser('tests/test_files/no-centerx.frac'))
        self.assertRaises(RuntimeError, Septagon, parser('tests/test_files/no-iterations.frac'))

    def test_sg_conversion(self):
        sg = Septagon(parser('tests/test_files/septagon.frac'))
        self.assertIsInstance(sg.centerx, float)
        self.assertIsInstance(sg.centery, float)
        self.assertIsInstance(sg.axislength, float)
        self.assertIsInstance(sg.iterations, int)
        self.assertIsInstance(sg.pixels, int)
        self.assertRaises(RuntimeError, Septagon, parser('tests/test_files/bad-int-value.frac'))
        self.assertRaises(RuntimeError, Septagon, parser('tests/test_files/bad-float-value.frac'))
        self.assertRaises(RuntimeError, Septagon, parser('tests/test_files/negative-axislen.frac'))
        self.assertRaises(RuntimeError, Septagon, parser('tests/test_files/zero-axislen.frac'))