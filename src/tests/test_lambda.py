import unittest
from lmda import Lambda
from parser import parser

class TestLambda(unittest.TestCase):
    def test_ld_keys(self):
        self.assertRaises(RuntimeError, Lambda, parser('tests/test_files/commented-out-property.frac'))
        self.assertRaises(RuntimeError, Lambda, parser('tests/test_files/no-centerx.frac'))
        self.assertRaises(RuntimeError, Lambda, parser('tests/test_files/no-iterations.frac'))

    def test_ld_conversion(self):
        ld = Lambda(parser('tests/test_files/lambda.frac'))
        self.assertIsInstance(ld.centerx, float)
        self.assertIsInstance(ld.centery, float)
        self.assertIsInstance(ld.axislength, float)
        self.assertIsInstance(ld.iterations, int)
        self.assertIsInstance(ld.pixels, int)
        self.assertRaises(RuntimeError, Lambda, parser('tests/test_files/bad-int-value.frac'))
        self.assertRaises(RuntimeError, Lambda, parser('tests/test_files/bad-float-value.frac'))
        self.assertRaises(RuntimeError, Lambda, parser('tests/test_files/negative-axislen.frac'))
        self.assertRaises(RuntimeError, Lambda, parser('tests/test_files/zero-axislen.frac'))
