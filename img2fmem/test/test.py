import os
import sys
import unittest
import random
from random import randint

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from img2fmem import convert_to_mif

class Test(unittest.TestCase):

    def test_convert_to_mif(self):

        size = 2 * randint(5, 13)
        colour_bits = random.choice([4,6,8])
        image_data = list(range(size))

        for i in range(size):
            image_data[i] = i

        expected_output = ""
        expected_output += "WIDTH = " + str(colour_bits) + ";\n"
        expected_output += "DEPTH = " + str(len(image_data)) + ";\n"
        expected_output += "ADDRESS_RADIX = DEC;\n"
        expected_output += "DATA_RADIX = HEX;\n"
        expected_output += "CONTENT BEGIN\n\n"

        i = 0
        for d in image_data:
            expected_output += str(i) + "  : " + str(d) + ";\n"
            i += 1
        expected_output += "\nEND;"

        self.assertEqual(expected_output, convert_to_mif(colour_bits, image_data))

if __name__ == '__main__':

    unittest.main()