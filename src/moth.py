from colour import Color
from palette import Palette


class  Moth(Palette):

    def __init__(self, n):
        """
        Initialize color variables and the 'pal' variable.
        Create the moth palette with the 'create_pal()' method
        """
        super().__init__(n)
        self.start = Color('#B22234')
        self.white = Color('#FFFFFF')
        self.end = Color('#3C3B6E')
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
        num = int(n / 11)
        for color in self.start.range_to(self.white, num):
            self.pal.append(color.hex_l)
        for color in self.white.range_to(self.end, num):
            self.pal.append(color.hex_l)
        for color in self.end.range_to(self.white, num):
            self.pal.append(color.hex_l)
        for color in self.white.range_to(self.start, num):
            self.pal.append(color.hex_l)
        self.pal *= 3