"""
File: reflection.py
----------------
Take an image. Generate a new image with twice the height. The top half
of the image is the same as the original. The bottom half is the mirror
reflection of the top half.
"""


# The line below imports SimpleImage for use here
# Its depends on the Pillow package being installed
from simpleimage import SimpleImage


def make_reflected(filename, width, height):
    image = SimpleImage(filename)

    reflected = SimpleImage.blank(width, height * 2)
    for y in range(height):
        for x in range(width):
            pixel = image.get_pixel(x, y)
            reflected.set_pixel(x, y, pixel)
            reflected.set_pixel(x, (height * 2) - (y + 1), pixel)
    return reflected


def main():
    """
    This program tests your highlight_fires function by displaying
    the original image of a fire as well as the resulting image
    from your highlight_fires function.
    """
    original = SimpleImage('images/mt-rainier.jpg')
    width = original.width
    height = original.height
    original.show()

    reflected = make_reflected('images/mt-rainier.jpg', width, height)
    reflected.show()


if __name__ == '__main__':
    main()
