import argparse

from PIL import Image

__all__ = ['grayscale_image', 'ascii_art', 'print_art']
default_charset = '$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,"^`\'. '


def get_args():
    parser = argparse.ArgumentParser(
        description='create beautiful ascii arts',
        allow_abbrev=False
    )
    parser.add_argument(
        '-c',
        '--charset',
        type=str,
        default=[default_charset],
        nargs=1,
        help='set the charset used in the output'
    )
    parser.add_argument(
        '-r',
        '--ratio',
        type=float,
        default=[2.25],
        nargs=1,
        help='set image aspect ratio'
    )
    parser.add_argument(
        '-m',
        '--max-size',
        type=int,
        default=[96],
        nargs=1,
        help='set the max size of the output'
    )
    parser.add_argument(
        'infile',
        metavar='IMG',
        type=str,
        nargs=1,
        help='original image'
    )
    return parser.parse_args()


def grayscale_image(infile, max_size, ratio):
    img = Image.open(infile)
    if img.size[0] > max_size:
        t_width = max_size
        t_height = int(img.size[1] * max_size / img.size[0] / ratio)
    else:
        t_height = int(max_size / ratio)
        t_width = int(img.size[0] * max_size / img.size[1])
    return img.resize((t_width, t_height), Image.LANCZOS).convert('L')


def ascii_art(img, charset=default_charset):
    pixels = list(img.getdata())
    step = 256 / len(charset)
    width, height = img.size
    ascii_art = []
    for y in range(0, height):
        line = []
        for x in range(0, width):
            index = int(pixels[x + y * width] / step)
            line.append(charset[index])
        ascii_art.append(line)
    return ascii_art

def print_art(ascii_art):
    for line in ascii_art:
        for char in line:
            print(char, end='')
        print()


if __name__ == '__main__':
    args = get_args()
    image = grayscale_image(args.infile[0], args.max_size[0], args.ratio[0])
    print_art(ascii_art(image, args.charset[0]))
