""" Utilities to manage medical images and extract a preview """
import argparse

import PIL
import pydicom


def load_dicom(path):
    """Load a Dicom file as Pillow image

    Arguments:
        path {str} -- filename of the dicom file to load

    Returns:
        Image -- a pillow Image
    """
    img_array = pydicom.read_file(path).pixel_array
    img = PIL.Image.fromarray(img_array)
    img = img.convert('I')
    return img

def build_parser():
    """ Builds the argument parser """
    parser = argparse.ArgumentParser()
    parser.add_argument("inp", help="input filename")
    parser.add_argument("out", help="output filename")
    parser.add_argument("size", help="size of the output")
    return parser

if __name__ == "__main__":
    pass
