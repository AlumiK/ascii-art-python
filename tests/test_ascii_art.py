import ascii_art
import unittest


class AsciiArtTestCase(unittest.TestCase):

    @staticmethod
    def test_ascii_art():
        image = ascii_art.to_grayscale('resources/img.png')
        art = ascii_art.make_art(image)
        ascii_art.print_art(art)
