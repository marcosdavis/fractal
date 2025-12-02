from tkinter import Tk, Canvas, PhotoImage, mainloop
from time import time
import sys

class ImagePainter:
    """
    Initialize the class and the 'frac' class and the 'pal' class.
    """
    def __init__(self, frac, pal):
        self.frac = frac
        self.pal = pal

    def create_window(self):
        """
        Create the Tkinter window, canvas, and photoimage.
        Return the window and img tkinter objects, as well
        as the start_time variable.
        """
        bg_color = '#000000'
        start_time = time()
        window = Tk()
        canvas = Canvas(window, width=self.frac.pixels, height=self.frac.pixels, background=bg_color)
        canvas.pack()
        img = PhotoImage(width=self.frac.pixels, height=self.frac.pixels)
        canvas.create_image(self.frac.pixels / 2, self.frac.pixels / 2, image=img, state='normal')
        print(f"Rendering {self.frac.frac['name']} fractal", file=sys.stderr)
        return window, img, start_time

    def draw_fractal(self):
        """
        Create a Tkinter window, then calculate the x and y coordinates that
        will be used in the 'frac' 'count()' method. Add the array of colors
        to the 'img' object, then update 'window'
        """
        window, img, st_time = self.create_window()
        for row in range(self.frac.pixels, 0, -1):
            color_array = []
            y = self.frac.minimum[1] + (row * self.frac.size)
            for col in range(self.frac.pixels):
                x = self.frac.minimum[0] + (col * self.frac.size)
                # Based off the type of the fractal, call its count function to get the color index
                # and then retrieve color from the palette
                color_array.append(self.pal.get_color(self.frac.count(complex(x,y))))
            img.put('{' + ' '.join(color_array) + '}', to=(0, self.frac.pixels - row))
            window.update()
            # Call 'status_bar()' to display the status of the fractal image
            self.status_bar(row)
        # When the image is done, call 'time_to_draw()'
        self.time_to_draw(img, st_time)
        # Keep the program running by calling 'mainloop()' until the user exits out of the window
        mainloop()

    def status_bar(self, row):
        """
        Calculate the current percent of the fractal drawn.
        Print the progress to the command line.
        """
        pixels_percent = (self.frac.pixels - row) / self.frac.pixels
        print(f"[{pixels_percent:>4.0%} {'=' * int(34 * pixels_percent):<33}]", end='\r', file=sys.stderr)

    def time_to_draw(self, img, start_time):
        """
        Once the image is finished, save it as a '.png' image, then
        print the total time to draw the fractal and instructions
        on how to exit the program.
        """
        img.write(self.frac.frac['name'] + ".png")
        print(f"\nDone in {time() - start_time:.3f} seconds!", file=sys.stderr)
        print(f"Saved image to file {self.frac.frac['name']}.png", file=sys.stderr)
        print("Close the image window to exit the program", file=sys.stderr)