"""
warhol_filter.py
This program generates the Warhol effect based on the original image.

It creates an image which has the patch copied 6 times (in 2 rows and 3 columns) where each
patch gets recolored.
"""
from simpleimage import SimpleImage

import random

N_ROWS = 4
N_COLS = 6
PATCH_SIZE = 222
WIDTH = N_COLS * PATCH_SIZE
HEIGHT = N_ROWS * PATCH_SIZE
PATCH_NAME = 'images/simba-sq.jpg'

def main():
    final_image = SimpleImage.blank(WIDTH, HEIGHT)

    for y in range(0, HEIGHT, PATCH_SIZE):
        for x in range(0, WIDTH, PATCH_SIZE):
            patch = make_recolored_patch(random.uniform(0, 1.5), random.uniform(0, 1.5), random.uniform(0, 1.5))
            final_image = add_patch(final_image, patch, x, y)

    final_image.show()
"""       
    # This is an example which should generate a pinkish patch
    patch00 = make_recolored_patch(1.5, 0, 1.5)
    final_image = add_patch(final_image, patch00, 0, 0)

    patch01 = make_recolored_patch(1.5, 1.5, 0)
    final_image = add_patch(final_image, patch01, PATCH_SIZE, 0)

    patch02 = make_recolored_patch(0, 1.5, 1.5)
    final_image = add_patch(final_image, patch02, 2*PATCH_SIZE, 0)
"""


def add_patch(image, patch, x, y):
    for row in range(PATCH_SIZE):
        for col in range(PATCH_SIZE):
            pixel = patch.get_pixel(row, col)
            image.set_pixel(x+row, y+col, pixel)
    return image


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