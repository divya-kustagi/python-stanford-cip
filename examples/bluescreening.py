"""
File: bluescreening.py
--------------------
This program adds the foreground to the background image,
but only copies over the pixels that are not too blue.

Concepts showcased:
Handling images in Python
"""

from simpleimage import SimpleImage
BRIGHTNESS_THRESHOLD = 153


def bluescreen(background, foreground):
    """
    Function to fetch pixels from foreground image that are 'not too blue',
    and replace the corresponding pixels in the background image with them
    """
    for y in range(foreground.height):
        for x in range(foreground.width):
            pixel = foreground.get_pixel(x, y)
            if pixel.blue < BRIGHTNESS_THRESHOLD:
                background.set_pixel(x, y, pixel)


def main():
    """
    Import the foreground and background images, 
    pass them to the bluescreening function, then display the processed output
    """
    background = SimpleImage('images/quad.jpg')
    foreground = SimpleImage('images/tiefighter.jpg')

    background.show()
    foreground.show()

    bluescreen(background, foreground)

    background.show()


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()

