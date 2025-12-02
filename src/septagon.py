from fractal import Fractal

class Septagon(Fractal):
    """
    Initialize the required dictionary variables. Call 'check_keys()'
    to verify that all the required keys are present. Call
    'convert_values()' to convert the dictionary values to the correct
    value type.
    """
    def __init__(self, frac_dict):
        super().__init__(frac_dict)
        self.check_keys(self.frac)
        self.convert_values(self.frac)

    def count(self, z):
        """
        Calculate when 'z' is greater than 2. Return that iteration that
        it is greater than 2. If 'z' never is greater than 2, return
        the max iteration count. Check if 'z' is ever 0 to make sure that
        zero division is never attempted and crash the program.
        """
        if z != 0:
            for iteration in range(self.iterations):
                z = (z**7 + (-0.7/5)) / z
                if abs(z) > 2:
                    return iteration
        return self.iterations

    def check_keys(self, frac):
        """
        Check for all the required keys that are required
        in the fractal calculations
        """
        for key in ['iterations', 'pixels', 'centerx', 'centery', 'axislength']:
            if key not in frac:
                raise RuntimeError(f'{key} is a required attribute')

    def convert_values(self, frac):
        """
        Convert all the required values from the dictionary passed
        to the class. If There are any conversion errors, if 'pixels'
        is negative, if iterations is negative, or if 'axislength'
        is negative, raise an error
        """
        try:
            self.axislength = float(frac['axislength'])
            if self.axislength <= 0: raise ValueError('Axislength needs to be greater than 0')
            self.iterations = int(frac['iterations'])
            if self.iterations <= 0: raise ValueError('Iterations needs to be greater than 0')
            self.pixels = int(frac['pixels'])
            if self.pixels <= 0: raise ValueError('Pixels needs to be greater than 0')
            self.centerx = float(frac['centerx'])
            self.centery = float(frac['centery'])
            self.minimum, self.size = self.min_max(self.centerx, self.centery, self.axislength, self.pixels)
        except ValueError as e:
            raise RuntimeError(f'Not a valid number format: {e}')