class Fractal:

    def __init__(self, frac):
        """
        Initialize the class. Raise an error if the 'Fractal'
        class is called, not one of the fractal subclasses
        """
        if type(self) is Fractal:
            raise NotImplementedError("Fractal is an abstract class and must be extended")
        self.frac = frac

    def count(self, z):
        """
        If 'count()' from the 'Fractal' class is called, raise an error
        """
        raise NotImplementedError('Concrete subclass of Fractal must implement count()')

    def check_keys(self, frac):
        """
        If 'check_keys()' from the 'Fractal' class is called, raise an error
        """
        raise NotImplementedError('Concrete subclass of Fractal must implement check_keys()')

    def convert_values(self, frac):
        """
        If 'convert_values()' from the 'Fractal' class is called, raise an error
        """
        raise NotImplementedError('Concrete subclass of Fractal must implement convert_values()')

    def min_max(self, cenx, ceny, axln, pixels):
        """
        Calculate the size, minimum x and minimum y. Raise an error
        if any of the calculations fail.
        """
        try:
            minimum = [(cenx - (axln/2.0)), (ceny - (axln/2.0))]
            size = axln/pixels
            return minimum, size
        except:
            raise ValueError("Unable to use type 'str' with type 'int' or 'float'")