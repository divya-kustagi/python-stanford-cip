"""
From 'Examples'
File: bluescreening.py
--------------------
This program adds the foreground to the background image,
but only copies over the pixels that are not too blue.
"""

from simpleimage import SimpleImage
BRIGHTNESS_THRESHOLD = 153


def bluescreen(background, foreground):
    for y in range(foreground.height):
        for x in range(foreground.width):
            pixel = foreground.get_pixel(x, y)
            if pixel.blue < BRIGHTNESS_THRESHOLD:
                background.set_pixel(x, y, pixel)


def main():
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

