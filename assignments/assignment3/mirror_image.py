"""
From 'Examples'
File: mirror_image.py
--------------------
Takes an image, and produces one which is twice as wide.
The right side of the new image is the left side of the old image, but mirror reflected.
"""

from simpleimage import SimpleImage


def make_mirrored(filename):
    image = SimpleImage(filename)

    # create new image of width twice the original
    image_mirrored = SimpleImage.blank(2 * image.width, image.height)

    # Get each pixel by co-ordinates, use it set original and reflected pixels of the final image
    for y in range(image.height):
        for x in range(image.width):
            pixel = image.get_pixel(x, y)
            image_mirrored.set_pixel(x, y, pixel)
            image_mirrored.set_pixel(2 * image.width - x - 1, y, pixel)

    return image_mirrored


def main():
    original = SimpleImage('images/burrito.jpg')
    original.show()
    mirrored = make_mirrored('images/burrito.jpg')
    mirrored.show()


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()



