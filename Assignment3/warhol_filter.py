"""
File: warhol_filter.py
----------------
This program generates the Warhol effect based on the original image.
"""

from simpleimage import SimpleImage
import random

N_ROWS = 2
N_COLS = 3
PATCH_SIZE = 222
WIDTH = N_COLS * PATCH_SIZE
HEIGHT = N_ROWS * PATCH_SIZE
PATCH_NAME = 'images/simba-sq.jpg'

def main():
    final_image = SimpleImage.blank(WIDTH, HEIGHT)

    for j in range(N_ROWS):
        for i in range(N_COLS):
            patch = make_recolored_patch(get_num(), get_num(), get_num())
            for y in range(PATCH_SIZE):
                for x in range(PATCH_SIZE):
                    pixel = patch.get_pixel(x, y)
                    final_image.set_pixel((x + PATCH_SIZE * i), (y + PATCH_SIZE * j), pixel)

    # This is an example which should generate a pinkish patch
    patch = make_recolored_patch(1.5, 0, 1.5)
    final_image.show()

def get_num():
    random_number_generator = random.uniform(0.0, 1.9)
    num = random_number_generator
    return num


def make_recolored_patch(red_scale, green_scale, blue_scale):
    '''
    Implement this function to make a patch for the Warhol Filter. It
    loads the patch image and recolors it.
    :param red_scale: A number to multiply each pixels' red component by
    :param green_scale: A number to multiply each pixels' green component by
    :param blue_scale: A number to multiply each pixels' blue component by
    :return: the newly generated patch
    '''
    patch = SimpleImage(PATCH_NAME)
    for pixel in patch:
        pixel.red *= red_scale
        pixel.green *= green_scale
        pixel.blue *= blue_scale
    return patch

if __name__ == '__main__':
    main()