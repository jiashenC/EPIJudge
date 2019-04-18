from test_framework import generic_test


def flip_color(x, y, image):
    color = image[x][y]
    image[x][y] ^= 1
    if x - 1 >= 0 and image[x - 1][y] == color:
        flip_color(x - 1, y, image)
    if x + 1 < len(image) and image[x + 1][y] == color:
        flip_color(x + 1, y, image)
    if y - 1 >= 0 and image[x][y - 1] == color:
        flip_color(x, y - 1, image)
    if y + 1 < len(image[x]) and image[x][y + 1] == color:
        flip_color(x, y + 1, image)


def flip_color_wrapper(x, y, image):
    flip_color(x, y, image)
    return image


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("matrix_connected_regions.py",
                                       'painting.tsv', flip_color_wrapper))
