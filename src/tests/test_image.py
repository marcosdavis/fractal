import unittest
from fractalfactory import FractalFactory
from palettefactory import PaletteFactory
from image import ImagePainter

class TestImagePainter(unittest.TestCase):
    def setUp(self):
        self.frac = FractalFactory('default').make()
        self.pal = PaletteFactory().make(self.frac.pixels, '')
        self.win = ImagePainter(self.frac, self.pal)
        self.window, self.img, self.start_time = self.win.create_window()

    def test_window(self):
        self.assertIsNotNone(self.window)
        self.assertEqual(self.img.width(), self.frac.pixels)
        self.assertEqual(self.img.height(), self.frac.pixels)