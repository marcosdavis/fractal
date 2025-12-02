from toxic import Toxic
from moth import Moth
from joker import Joker
from oceanlava import OceanLava

class PaletteFactory:
    def __init__(self):
        """
        Initialize the class
        """
        pass

    def make(self, num_colors, name):
        """
        Check what was the name of the palette passed to
        the method. Call the appropriate palette subclass.
        """
        if name == "":
            print('palette_factory: creating default color palette')
            return Toxic(num_colors)
        elif name == 'toxic':
            return Toxic(num_colors)
        elif name == 'moth':
            return Moth(num_colors)
        elif name == 'joker':
            return Joker(num_colors)
        elif name == 'oceanlava':
            return OceanLava(num_colors)
        else:
            raise NotImplementedError(f'{name} is not a supported palette')
