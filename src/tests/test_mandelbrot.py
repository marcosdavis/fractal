import unittest
from mandelbrot import Mandelbrot
from parser import parser

class TestMandelbrot(unittest.TestCase):
    def test_mb_keys(self):
        mb = Mandelbrot(parser('tests/test_files/mandelbrot.frac'))
        self.assertIsInstance(mb.centerx, float)
        self.assertIsInstance(mb.centery, float)
        self.assertIsInstance(mb.axislength, float)
        self.assertIsInstance(mb.iterations, int)
        self.assertIsInstance(mb.pixels, int)
        self.assertRaises(RuntimeError, Mandelbrot, parser('tests/test_files/commented-out-property.frac'))
        self.assertRaises(RuntimeError, Mandelbrot, parser('tests/test_files/no-centerx.frac'))
        self.assertRaises(RuntimeError, Mandelbrot, parser('tests/test_files/no-iterations.frac'))

    def test_mb_conversion(self):
        self.assertRaises(RuntimeError, Mandelbrot, parser('tests/test_files/bad-int-value.frac'))
        self.assertRaises(RuntimeError, Mandelbrot, parser('tests/test_files/bad-float-value.frac'))
        self.assertRaises(RuntimeError, Mandelbrot, parser('tests/test_files/negative-axislen.frac'))
        self.assertRaises(RuntimeError, Mandelbrot, parser('tests/test_files/zero-axislen.frac'))
