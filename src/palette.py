class Palette:

    def __init__(self, num_colors):
        """
        Initialize the class. Raise an error if the 'Palette'
        class is called, not one of the palette subclasses
        """
        if type(self) is Palette:
            raise NotImplementedError('Palette is an abstract class and must be extended')
        self.num_colors = num_colors

    def get_color(self, n):
        """
        If the 'get_color()' method on the 'Palette' class is called
        raise an error.
        """
        raise NotImplementedError("Concrete subclass of Palette must implement get_color()")

    def create_pal(self, n):
        """
        If the 'create_pal()' method on the 'Palette' class is called
        raise an error.
        """
        raise NotImplementedError('Concrete subclass of Palette must implement create_pal()')

    def __len__(self):
        return self.num_colors