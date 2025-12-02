import sys
from image import ImagePainter
from fractalfactory import FractalFactory
from palettefactory import PaletteFactory

"""
Check for total arguments passed to the command line.
Depending on total arguments, use the default fractal
dictionary and/or default palette.
"""
if len(sys.argv) == 3:
    frac = FractalFactory(sys.argv[1]).make()
    pal = PaletteFactory().make(frac.iterations, sys.argv[2].lower())
    win = ImagePainter(frac, pal)
    win.draw_fractal()
elif len(sys.argv) == 2:
    frac = FractalFactory(sys.argv[1]).make()
    pal = PaletteFactory().make(frac.iterations, '')
    win = ImagePainter(frac, pal)
    win.draw_fractal()
elif len(sys.argv) == 1:
    frac = FractalFactory('default').make()
    pal = PaletteFactory().make(frac.iterations, '')
    win = ImagePainter(frac, pal)
    win.draw_fractal()