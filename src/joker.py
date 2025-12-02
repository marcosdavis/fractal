from colour import Color
from palette import Palette

class Joker(Palette):

    def __init__(self, n):
        """
        Initialize color variables and the 'pal' variable.
        Create the joker palette with the 'create_pal()' method
        """
        super().__init__(n)
        self.start = Color('#F4F0EC')
        self.mid = Color('#39FF14')
        self.end = Color('#FF00FF')
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
        num = int(n / 14)
        for color in self.start.range_to(self.mid, num):
            self.pal.append(color.hex_l)
        for color in self.mid.range_to(self.end, num):
            self.pal.append(color.hex_l)
        for color in self.end.range_to(self.mid, num):
            self.pal.append(color.hex_l)
        for color in self.mid.range_to(self.start, num):
            self.pal.append(color.hex_l)
        self.pal *= 4