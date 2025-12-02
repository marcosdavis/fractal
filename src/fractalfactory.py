from parser import parser
from lmda import Lambda
from septagon import Septagon
from mandelbrot import Mandelbrot
from phoenix import Phoenix

class FractalFactory:
    """
    Initialize the class variables, check if 'default' was passed.
    If not, create a dictionary from the file passed to the class.
    """
    def __init__(self, filename):
        if filename != 'default':
            self.frac_dict = parser(filename)
        else:
            print('fractal_factory: creating default fractal')
            self.frac_dict = {
                'type':'lambda',
                'name':'default',
                'iterations':'256',
                'pixels':'512',
                'axislength':'0.01',
                'centerx':'0.5056',
                'centery':'0.0065'
            }

    def make(self):
        """
        Check the type of fractal passed to the class, if it
        is not compatible, raise an error.
        """
        if self.frac_dict['type'] == 'mandelbrot':
            return Mandelbrot(self.frac_dict)
        elif self.frac_dict['type'] == 'phoenix':
            return Phoenix(self.frac_dict)
        elif self.frac_dict['type'] == 'septagon':
            return Septagon(self.frac_dict)
        elif self.frac_dict['type'] == 'lambda':
            return Lambda(self.frac_dict)
        else:
            raise NotImplementedError(f'{self.frac_dict['type']} is not a supported fractal type')