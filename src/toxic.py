from colour import Color
from palette import Palette

class Toxic(Palette):

    def __init__(self, n):
        """
        Initialize color variables and the 'pal' variable.
        Create the toxic palette with the 'create_pal()' method
        """
        super().__init__(n)
        self.start = Color('#00ff00')
        self.m1 = Color('#000000')
        self.m2 = Color('#0000FF')
        self.end = Color('#FF0000')
        self.pal = []
        self.create_pal(self.num_colors)

    def get_color(self, n):
        """
        Return the color of 'pal' that 'n' corresponds to.
        """
        return self.pal[n]

    def create_pal(self, n):
        """
        Take 'n' (iteration count) and divide it by a number. Use that number to create
        colors in 'pal', thus creating a variety of colors.
        """
        num = int(n / 13)
        for color in self.start.range_to(self.m1, num):
            self.pal.append(color.hex_l)
        for color in self.m1.range_to(self.m2, num):
            self.pal.append(color.hex_l)
        for color in self.m2.range_to(self.m1, num):
            self.pal.append(color.hex_l)
        for color in self.m1.range_to(self.end, num):
            self.pal.append(color.hex_l)
        for color in self.end.range_to(self.start, num):
            self.pal.append(color.hex_l)
        self.pal *= 3