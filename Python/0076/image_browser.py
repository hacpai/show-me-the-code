from swampy.Gui import *
from Tkinter import PhotoImage
import Image as PIL
import ImageTk
import os


class ImageBrowser(Gui):
    """An image browser that scans the files in a given directory and
    displays any images that can be read by PIL.
    """

    def __init__(self):
        Gui.__init__(self)
        self.button = self.bu(command=self.quit)

    def image_loop(self, dirname='.'):
        """loop through the files in (dirname), displaying
        images and skipping files PIL can't read.
        """
        for name in os.listdir(dirname):
            try:
                self.show_image(name)
                print name
                self.mainloop()
            except IOError:
                continue
            except:
                break

    def show_image(self, filename):
        """Use PIL to read the file and ImageTk to convert to a PhotoImage,
        which Tk can display.
        """
        image = PIL.open(filename)
        self.photo = ImageTk.PhotoImage(image)
        self.button.config(image=self.photo)


if __name__ == '__main__':
    g = ImageBrowser()
    g.image_loop('.')
