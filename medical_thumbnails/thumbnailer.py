#!/bin/env python3
""" Utilities to manage medical images and extract a preview """
import argparse

import PIL
import SimpleITK as sitk
from scipy.stats.mstats import mquantiles
import numpy as np

def convert_to_8bit(img_array):
    """Converts to 8 bit, but strething the contrast according to image stats"""
    img_array = img_array.astype('float32')
    int_quant = mquantiles(img_array.ravel(), [0.01, 0.99])

    # if the image is flat return the image or 255
    if int_quant[0] == int_quant[1]:
        flat_field = np.min(img_array.max(), 255)
        return flat_field*np.ones_like(img_array)
    # Remove outliers
    img_array[img_array < int_quant[0]] = int_quant[0]
    img_array[img_array > int_quant[1]] = int_quant[1]

    img_array -= img_array.min()
    img_array /= img_array.max()
    img_array *= 255

    return img_array

def load_image(path):
    """Load a Dicom/nii/nii.gz file as Pillow image

    Arguments:
        path {str} -- filename of the dicom file to load

    Returns:
        Image -- a pillow Image
    """
    img_array = sitk.GetArrayFromImage(sitk.ReadImage(path))
    if img_array.ndim == 3:
        img_array = img_array[:, :, img_array.shape[-1]//2].squeeze()
    img_array = convert_to_8bit(img_array)
    img = PIL.Image.fromarray(img_array).convert('L')
    return img

def save_thumbnail(img, out_fname, size):
    """Resize and save the input image

    Arguments:
        img {Image} -- the Pillow image to process
        out_fname {str} -- the filename of the output file
        size {int} -- the side of the square in which the resized picture will be contained
    """

    img.thumbnail((size, size))
    img.save(out_fname)

def build_parser():
    """ Builds the argument parser """
    parser = argparse.ArgumentParser()
    parser.description = "Generate PNG thumbnails from medical images"
    parser.add_argument("inp", help="input filename")
    parser.add_argument("out", help="output filename")
    parser.add_argument("size", help="size of the output", type=int)
    return parser

if __name__ == '__main__':

    PARSER = build_parser()
    ARGS = PARSER.parse_args()
    IMG = load_image(ARGS.inp)
    save_thumbnail(IMG, ARGS.out, ARGS.size)
