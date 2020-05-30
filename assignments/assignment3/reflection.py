"""
File: reflection.py
----------------
This program returns an output image that is twice the height of the original.

The top half of the output image should be identical to the original image. The bottom half,
however, should look like a reflection of the top half.
"""

# The line below imports SimpleImage for use here
# Its depends on the Pillow package being installed
from simpleimage import SimpleImage


def make_reflected(filename):
    image = SimpleImage(filename)

    # create new image of height twice the original
    image_reflected = SimpleImage.blank(image.width, 2 * image.height)

    # Get each pixel by co-ordinates, use it set original and reflected pixels of the final image
    for y in range(image.height):
        for x in range(image.width):
            pixel = image.get_pixel(x, y)
            image_reflected.set_pixel(x, y, pixel)
            image_reflected.set_pixel(x, 2 * image.height - y - 1, pixel)

    return image_reflected


def main():
    """
    This program tests your highlight_fires function by displaying
    the original image of a fire as well as the resulting image
    from your highlight_fires function.
    """
    original = SimpleImage('images/mt-rainier.jpg')
    original.show()
    reflected = make_reflected('images/mt-rainier.jpg')
    reflected.show()


if __name__ == '__main__':
    main()
