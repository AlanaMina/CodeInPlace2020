"""
File: Section4.py
"""

from simpleimage import SimpleImage

PIXEL_AVERAGE = 153

def main():
    image = SimpleImage("images/simba-sq.jpg")  # 222x222
    width = image.width
    height = image.height
    image.show()

    # narok_filter(image)
    # image.show()

    # image = trim_crop_image(image, 30, width, height)
    # image.show()

    image = border_image(image, 10, width, height)
    image.show()


def border_image(image, border_size, width, height):
    border = SimpleImage.blank(width + border_size * 2, height + border_size * 2, "black")
    for y in range(height):
        for x in range(width):
            pixel = image.get_pixel(x, y)
            if y <= (height + border_size) and x <= (width + border_size):
                border.set_pixel(x + border_size, y + border_size, pixel)
            else:
                pixel.red *= 0
                pixel.green *= 0
                pixel.blue *= 0
    return border


def trim_crop_image(image, trim_size, width, height):
    trim = SimpleImage.blank(width - trim_size * 2, height - trim_size * 2)
    for y in range(trim_size, (height - trim_size)):
        for x in range(trim_size, (width - trim_size)):
            pixel = image.get_pixel(x, y)
            trim.set_pixel(x - trim_size, y - trim_size, pixel)
    return trim


def narok_filter(image):
    for pixel in image:
        if pixel.green > PIXEL_AVERAGE:
            pixel.green = 153
        if pixel.red > PIXEL_AVERAGE:
            pixel.red = 153
        if pixel.blue > PIXEL_AVERAGE:
            pixel.blue = 153

if __name__ == '__main__':
    main()