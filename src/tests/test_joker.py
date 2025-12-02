import unittest
from joker import Joker
from lmda import Lambda
from mandelbrot import Mandelbrot
from phoenix import Phoenix
from septagon import Septagon
from parser import parser

class TestJoker(unittest.TestCase):
    def setUp(self):
        self.ld = Lambda(parser('tests/test_files/lambda.frac'))
        self.mb = Mandelbrot(parser('tests/test_files/mandelbrot.frac'))
        self.px = Phoenix(parser('tests/test_files/phoenix.frac'))
        self.sp = Septagon(parser('tests/test_files/septagon.frac'))

    def test_jk_length(self):
        self.assertGreaterEqual(len(Joker(self.ld.iterations).pal), self.ld.iterations)
        self.assertGreaterEqual(len(Joker(self.mb.iterations).pal), self.mb.iterations)
        self.assertGreaterEqual(len(Joker(self.px.iterations).pal), self.px.iterations)
        self.assertGreaterEqual(len(Joker(self.sp.iterations).pal), self.sp.iterations)